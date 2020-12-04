import pandas as pd
from zipfile import ZipFile, ZIP_BZIP2
from neo4j import GraphDatabase


class DatabaseRequester:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def get_authors_ids(self, reg_name):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Author)"
                              " WHERE a.name =~ $reg_name"
                               " RETURN id(a) LIMIT 50", reg_name='.*'+reg_name+'.*')
            return res.value()

    def get_authors_names(self, ids):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Author)"
                              " WHERE id(a) IN $ids"
                               " RETURN a.name LIMIT 50", ids=ids)
            return res.value()

    def get_colleagues_of_author(self, author_id):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Author)-[:WROTE]-()-[:WROTE]-(b:Author)"
                              " WHERE id(a) = $author_id"
                               " RETURN DISTINCT id(b) LIMIT 50", author_id=author_id)
            return res.value()

    def get_related_to_author(self, author_id):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Author)-[:WROTE*1..5]-(b:Author)"
                              " WHERE id(a) = $author_id"
                               " RETURN DISTINCT id(b) LIMIT 50", author_id=author_id)
            return res.value()


    def get_author_articles_ids(self, author_ids):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Author)-[:WROTE]-(b:Article)"
                              " WHERE id(a) in $author_ids"
                               " RETURN id(a), id(b) LIMIT 50", author_ids=author_ids)
            return res.values()

    def get_article_authors_ids(self, article_ids):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Author)-[:WROTE]-(b:Article)"
                              " WHERE id(b) in $article_ids"
                               " RETURN id(a), a.name", article_ids=article_ids)
            return res.values()

    def get_article_info(self, article_ids):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Article)"
                              " WHERE id(a) in $article_ids"
                               " RETURN a.title, a.doi, a.categories, a.abstract LIMIT 50", article_ids=article_ids)
            return res.values()

    def get_articles_ids(self, reg_title):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Article)"
                              " WHERE a.title =~ $reg_title"
                               " RETURN id(a) LIMIT 50", reg_title='.*'+reg_title+'.*')
            return res.value()

    def get_articles_by_category(self, category):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Article)"
                              " WHERE a.categories =~ $reg_category"
                               " RETURN id(a) LIMIT 50", reg_category='.*'+category+'.*')
            return res.value()

    def get_categories_statistics(self):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Article)"
                               " UNWIND split(a.categories, ' ') AS cat"
                               " RETURN cat, count(a) as count"
                               " ORDER BY count DESC"
                               )
            return res.values()

    def get_authors_statistics(self):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Author)"
                               " RETURN id(a), size((a)--()) as count"
                               " ORDER BY count DESC"
                               " LIMIT 10"
                               )
            return res.values()

    def export_database(self):
        with self.driver.session() as session:
            authors_query = """MATCH (a:Author)
                               RETURN a.name """
            articles_query = """MATCH (a:Article)
                                RETURN id(a), a.title, a.doi, a.categories, a.abstract"""
            wrote_query = """MATCH (a:Author)-[:WROTE]-(b:Article)
                             RETURN a.name, id(b)"""
            res = session.run(authors_query)
            df = pd.DataFrame(res, columns=['name:ID'])
            df.to_csv("authors.csv")

            del res
            del df
            
            res = session.run(articles_query)
            df = pd.DataFrame(res, columns=[':ID', 'title', 'doi', 'categories', 'abstract'])
            df.to_csv("articles.csv")

            del res
            del df

            res = session.run(wrote_query)
            df = pd.DataFrame(res, columns=[':START_ID', ':END_ID'])
            df.to_csv("wrote.csv")
            del res
            del df
        with ZipFile('export.zip', mode='w', compression=ZIP_BZIP2, compresslevel=9) as zf:
            zf.write("authors.csv")
            zf.write("articles.csv")
            zf.write("wrote.csv")
    
    def import_database(self):
        with self.driver.session() as session:
            author_query = """UNWIND $names as name
                              MERGE (a:Author{name:name})"""
            articles_query = """UNWIND $articles as article
                              MERGE (a:Article{title:article[1]})
                              SET a.doi=article[2],
                              a.catergories=article[3], a.abstract=article[4],
                              a.id = article[0]"""
            wrote_query = """UNWIND $wrote as wrote
                             MATCH (a:Author{name:wrote[0]}), (b:Article{id:wrote[1]})
                             MERGE (a)-[:WROTE]-(b)
                             REMOVE b.id"""
            names = pd.read_csv("authors.csv", index_col=False)
            session.run(author_query, names=names['name:ID'].values.tolist())
            articles = pd.read_csv("articles.csv", index_col=False)
            session.run(articles_query, articles=articles.values.tolist())
            wrote = pd.read_csv("wrote.csv", index_col=False)
            session.run(wrote_query, wrote=wrote.values.tolist())


if __name__ == "__main__":
    req = DatabaseRequester("neo4j://localhost:7687", "neo4j", "password")
    #req.export_database()
    req.import_database()
