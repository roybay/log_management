Reference: https://hub.docker.com/_/mongo

docker run --name log-db-mongo -d mongo
docker run -it --rm --name log-db-mongo -p 27017:27017 --hostname mongodb.example.com -d mongo 

docker run -it --network log-network --rm mongo mongo --host log-db-mongo logdb


docker-compose -f ./db/stack.yml up