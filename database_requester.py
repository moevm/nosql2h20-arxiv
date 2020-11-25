from neo4j import GraphDatabase

class DatabaseRequester:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def get_authors_ids(self, reg_name):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Author)"
                              " WHERE a.name =~ $reg_name"
                               " RETURN id(a)", reg_name=reg_name)
            return res.value()

    def get_authors_names(self, ids):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Author)"
                              " WHERE id(a) IN $ids"
                               " RETURN a.name", ids=ids)
            return res.value()

        
    def get_author_articles_ids(self, author_id):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Author)-[:WROTE]-(b:Article)"
                              " WHERE id(a) = $author_id"
                               " RETURN id(b)", author_id=author_id)
            return res.value()
    
    def get_article_info(self, article_id):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Article)"
                              " WHERE id(a) = $article_id"
                               " RETURN a.title, a.doi, a.categories, a.abstract", article_id=article_id)
            return res.values()

if __name__ == "__main__":
    req = DatabaseRequester("neo4j://localhost:7687", "neo4j", "password")
    ids = req.get_authors_ids("Xu*")
    names = req.get_authors_names(ids)
    print(names)

    ids = req.get_author_articles_ids(ids[0])
    print(ids)
    info = req.get_article_info(ids[0])
    print(info)

