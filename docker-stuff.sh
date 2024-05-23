cd appbasicapi
docker build -t appbasicapi .
cd ../apptimerapi
docker build -t apptimerapi .

docker stop appbasicapi
docker rm appbasicapi
docker stop apptimerapi
docker rm apptimerapi

docker run -d -p 5080:80 --name appbasicapi appbasicapi
docker run -d -p 5088:80 --name apptimerapi apptimerapi
