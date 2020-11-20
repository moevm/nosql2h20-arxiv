from neo4j import GraphDatabase

import_query = '''USING PERIODIC COMMIT
               LOAD CSV WITH HEADERS FROM "file:///arxiv.csv" AS row
               WITH row LIMIT 1000
               MERGE (article:Article {title: row.title})
               ON CREATE SET article.doi = row.doi,
                             article.abstract = row.abstract,
                             article.categories = row.categories
               FOREACH (name in split(row.authors, ";") |
                             MERGE (author:Author{name:name})
                             MERGE (author)-[:WROTE]-(article))'''

def importing(uri, user, password):
    driver = GraphDatabase.driver(uri, auth=(user, password))
    with driver.session() as session:
        greeting = session.run(import_query)
    driver.close()


if __name__ == "__main__":
    importing("bolt://localhost:7687", "neo4j", "password")
