# docker push

```sh
# Let's see which images are on the system
docker image ls

# Let's tag the built image properly with the repo url. 
# For Docker Hub repos, the domain can be omitted.
docker tag dbservice docker.io/mokari94/dbservice:latest

# Note the identical image ids
docker image ls

# Push the image
docker push docker.io/mokari94/dbservice:latest

# If "denied: requested access to the resource is denied" appears, first login to the registry 
docker login docker.io

# Push the image
docker push docker.io/mokari94/dbservice:latest
```

# docker pull


```sh
# On a different machine
docker pull mokari94/dbservice
```