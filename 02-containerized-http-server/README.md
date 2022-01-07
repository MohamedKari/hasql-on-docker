#  docker build

```sh
# Let's write the Dockerfile first
code Dockerfile

# look at the images on your computer BEFORE the build
docker image ls
docker build .

# look at the images on your computer AFTER the build
docker image ls

# Let's build the tag the image
# Notice that this time the build finishes immediately as all layers cached
docker build --tag dbservice .

# Let's modify the server.py file and rebuild the image
# Notice that all layers are reused up to the one for which the hash changed are reused
echo "# test" >> app/server.py

# The image is nothing else but a set of layers, each of the layers being a set of files
# docker image save  -o 324d00e9ca41.tar
```

# docker run

## Environment Variables
```sh
docker run dbservice
# DOESN'T WORK because the license was not set

docker run -e LICENSE_KEY=SCOTLAND dbservice
curl http://localhost:8000/user/3
# DOESN'T WORK because the port is not exposed
```

## Port Bindings
```sh
docker run -e LICENSE_KEY=SCOTLAND -p 8000:8000 dbservice
curl http://localhost:8000/user/3
# WORKS

docker run -e LICENSE_KEY=SCOTLAND -p 9000:8000 dbservice
curl http://localhost:9000/user/3
# WORKS
```


# docker ps

```sh
docker ps
```

```txt
CONTAINER ID   IMAGE       COMMAND              CREATED          STATUS          PORTS                                       NAMES
d5406e6533db   dbservice   "python server.py"   16 seconds ago   Up 15 seconds   0.0.0.0:9000->8000/tcp, :::9000->8000/tcp   unruffled_gagarin
```

# docker stop

```sh
docker stop $CONTAINER_ID
docker ps
```

# docker exec
```sh
docker run -e LICENSE_KEY=SCOTLAND -p 8000:8000 dbservice
docker ps
docker exec -it $CONTAINER_ID bash

# In the container shell:
ll /
top

cd /app
ll

# On a client machine
curl -X POST "http://localhost:8000/product?product_id=0&product_name=smartphone"

# In the container shell
ll /app
cat products.json

# On a client machine
curl -X POST "http://localhost:8000/product?product_id=1&product_name=tablet" 

# In the container shell
cat products.json

# On a client machine
curl "http://localhost:8000/product/0"
```

> How do we keep data persistent if a container dies or is simply restarted? 
> How can different containers access the same data files?