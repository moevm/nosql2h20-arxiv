from neo4j import GraphDatabase

class DatabaseRequester:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def get_authors_id(self, reg_name):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Authors) where a.name =~ $reg_name"
                              " RETURN id(a)", reg_name=reg_name)
            return res.value()

    def get_author_articles_id(self, author_id):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Authors)-[:WROTE]-(b:Article)"
                              " WHERE id(a) = $author_id"
                              " RETURN id(b)", author_id=author_id)
            return res.value()

if __name__ == "__main__":
    req = DatabaseRequester("neo4j://localhost:7687", "neo4j", "password")
    ids = req.get_authors_id("X.*")
    ids = req.get_author_articles_id(ids[0])
    print(ids)

