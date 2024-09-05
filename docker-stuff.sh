cd appbasicapi
docker build -t appbasicapi .
cd ../apptimerapi
docker build -t apptimerapi .
cd ../apppubsub
docker build -t apppubsub .

docker stop appbasicapi
docker rm appbasicapi
docker stop apptimerapi
docker rm apptimerapi
docker stop apppubsub
docker rm apppubsub

docker run -d -p 5080:80 --name appbasicapi appbasicapi
docker run -d -p 5088:80 --name apptimerapi apptimerapi
docker run -d -p 5089:80 --name apppubsub apppubsub