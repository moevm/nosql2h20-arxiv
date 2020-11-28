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

    def get_colleagues_of_author(self, author_id):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Author)-[:WROTE]-()-[:WROTE]-(b:Author)"
                              " WHERE id(a) = $author_id"
                               " RETURN id(b)", author_id=author_id)
            return res.value()

    def get_related_to_author(self, author_id):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Author)-[:WROTE*1..5]-(b:Author)"
                              " WHERE id(a) = $author_id"
                               " RETURN id(b)", author_id=author_id)
            return res.value()

        
    def get_author_articles_ids(self, author_ids):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Author)-[:WROTE]-(b:Article)"
                              " WHERE id(a) in $author_ids"
                               " RETURN id(a),id(b)", author_ids=author_ids)
            return res.values()
    
    def get_article_info(self, article_ids):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Article)"
                              " WHERE id(a) in $article_ids"
                               " RETURN a.title, a.doi, a.categories, a.abstract", article_ids=article_ids)
            return res.values()
    
    def get_articles_ids(self, reg_title):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Article)"
                              " WHERE a.title =~ $reg_title"
                               " RETURN id(a) LIMIT 10", reg_title=reg_title)
            return res.value()

    def get_articles_by_category(self, category):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Article)"
                              " WHERE a.categories =~ $reg_category"
                               " RETURN id(a) LIMIT 10", reg_category='.*'+category+'.*')
            return res.value()

    def get_categories_statistics(self):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Article)"
                               " UNWIND split(a.categories, ' ') AS cat"
                               " RETURN cat, count(a)")
            res = res.values()
            res.sort(key=lambda x: -x[1])
            return res

    def get_authors_statistics(self):
        with self.driver.session() as session:
            res = session.run("MATCH (a:Author)"
                               " RETURN id(a), size((a)--()) as count"
                               " ORDER BY count DESC"
                               " LIMIT 10" 
                               )
            return res.values()



if __name__ == "__main__":
    req = DatabaseRequester("neo4j://localhost:7687", "neo4j", "password")
    ids = req.get_authors_ids("Xu*")
    print(ids)
    res = req.get_authors_names(ids)
    print(res)
    '''names = req.get_authors_names(ids)
    print(names)
    ids = req.get_colleagues_of_author(ids[0])
    print(ids)
    names = req.get_authors_names(ids)
    print(names)
    ids = req.get_related_to_author(ids[0])
    print(ids)


    ids = req.get_author_articles_ids(ids[0])
    print(ids)
    info = req.get_article_info(ids[0])
    print(info)
    '''

    res = req.get_categories_statistics()
    print(res)
    res = req.get_authors_statistics()
    print(res)
    ids = list(map(lambda x: x[0], res))
    print(ids)
    print(req.get_authors_names(ids))

    '''
    ids = req.get_articles_by_category("hep-ph")
    print(ids)
    info = req.get_article_info(ids)
    print(info)
    '''
