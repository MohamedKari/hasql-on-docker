# Prepare the environment
```sh
python -m venv .env
source .env/bin/activate
pip install --upgrade pip
pip install fastapi==0.68.0
pip install uvicorn==0.14.0
```

# Run the server
```sh
export LICENSE_KEY=SCOTLAND
python server.py
```

# Make a request
```sh
# Use the browser
open http://localhost:8000/user/1

# or curl / POSTMAN
curl http://localhost:8000/user/1
```