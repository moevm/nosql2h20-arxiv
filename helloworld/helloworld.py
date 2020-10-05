from neo4j import GraphDatabase

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN '\"' + a.message + '\"' + ' from node ' + id(a)", 
                        message=message)
        #result = tx.run("MATCH (a:Greeting) "
        #                "DELETE a")
        #                "RETURN a.message + ', from node ' + id(a)")
        return result.single()[0]
        #return result.values()


if __name__ == "__main__":
    greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "password")
    greeter.print_greeting("Hello world")
    greeter.close()
