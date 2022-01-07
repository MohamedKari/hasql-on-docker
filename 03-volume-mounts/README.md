# `docker run` with a volume mount


```sh
mkdir ./data
# Shell 1 
docker run -e LICENSE_KEY=SCOTLAND -p 10000:8000 -v /Users/mo/code/hasql-on-docker/3-volume-mounts/data:/app/data dbservice

# Shell 2
docker run -e LICENSE_KEY=SCOTLAND -p 10001:8000 -v /Users/mo/code/hasql-on-docker/3-volume-mounts/data:/app/data dbservice

# Shell 3
curl -X POST "http://localhost:10000/product?product_id=0&product_name=tablet"
curl "http://localhost:10001/product/0" 
# Yields 'tablet' from 10001, orginally written to 10000
curl -X POST "http://localhost:10001/product?product_id=0&product_name=smartphone"
curl "http://localhost:10000/product/0" 
# Yields 'smartphone'
```