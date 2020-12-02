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
            authors_query = """WITH \"MATCH (a:Author)
             RETURN a.name as `name:ID` \" AS query"""
            articles_query = """WITH \"MATCH (a:Article)
             RETURN id(a) as `:ID`, a.title as title, a.doi as doi, 
             a.categories as categories, a.abstract as abstract \" AS query"""
            wrote_query = """WITH \"MATCH (a:Author)-[:WROTE]-(b:Article)
             RETURN a.name as `:START_ID`, id(b) as `:END_ID` \" AS query"""
            end_of_query = """ CALL apoc.export.csv.query(query, $file, {})
             YIELD file, source, format, nodes
             RETURN file, source, format, nodes"""
            session.run(authors_query + end_of_query, file="authors.csv")
            session.run(articles_query + end_of_query, file="articles.csv")
            session.run(wrote_query + end_of_query, file="wrote.csv")


if __name__ == "__main__":
    req = DatabaseRequester("neo4j://localhost:7687", "neo4j", "password")
