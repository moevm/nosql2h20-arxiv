sudo neo4j-admin import --database neo4j --nodes=Author=./authors.csv --nodes=Article=./articles.csv --relationships=WROTE=./wrote.csv
