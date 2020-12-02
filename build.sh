#!/bin/bash
#sudo docker-compose down --remove-orphans
if [[ -f db/arxiv.tar.gz ]]
then
    echo 'dataset is already downloaded'
#else
#    bash db/wget_arxiv.sh
#    tar -xf arxiv.tar.gz
fi
#if [[ -d /var/lib/neo4j/data/databases/neo4j ]]
#then
#    echo 'AAAAAAAAAAAA'
#    sudo rm -r /var/lib/neo4j/data/databases/neo4j
#fi
#if [[ -d /var/lib/neo4j/data/transactions/neo4j ]]
#then
#    sudo rm -r /var/lib/neo4j/data/transactions/neo4j
#fi

#bash db/importing.sh
#sudo neo4j start

docker-compose build --no-cache
docker-compose up
