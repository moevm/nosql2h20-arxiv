from neo4j:latest
WORKDIR /
COPY docker-entrypoint.sh /docker-entrypoint.sh
EXPOSE 7474 7473 7687

ENTRYPOINT ["/sbin/tini", "-g", "--", "/docker-entrypoint.sh"]
COPY . . 
RUN bash ./wget_arxiv.sh
RUN tar xvzf ./arxiv.tar.gz && neo4j-admin import --nodes=Author=./authors.csv --nodes=Article=./articles.csv --relationships=WROTE=./wrote.csv
CMD ["neo4j"]
