#!/usr/bin/env python
# LICENSE_KEY=SCOTLAND python server.py

import os
import json
from pathlib import Path

import uvicorn
from fastapi import FastAPI

app = FastAPI()

user_db = {
    "0": "lukas",
    "1": "niklas",
    "2": "tobias",
    "3": "mo",
}

FAIL_FLAG = False

@app.get('/user/{user_id}')
async def get_user(user_id: str):
    if FAIL_FLAG: 
        exit()
        
    return user_db[user_id]



def load_product_db(path="./data/products.json"):
    if Path(path).exists():
        with open(path, "rt") as f:
            product_db = json.load(f)
    else:
        product_db = {}

    return product_db


def write_product_db(product_db, path="./data/products.json"):
    Path(path).parent.mkdir(exist_ok=True)
    
    with open(path, "wt") as f:
        json.dump(product_db, f)


@app.get('/product/{product_id}')
async def get_product(product_id: str):
    product_db = load_product_db()
    return product_db[product_id]



@app.post('/product')
async def upsert_product(product_id: str, product_name: str):
    product_db = load_product_db()
    product_db[product_id] = product_name
    print(product_db)
    write_product_db(product_db)


@app.get('/fail')
async def fail():
    global FAIL_FLAG
    FAIL_FLAG = True


if __name__ == "__main__":
    
    if "LICENSE_KEY" not in os.environ or os.environ["LICENSE_KEY"] != "SCOTLAND":
        raise ValueError("Invalid License Key")

    uvicorn.run(app, host="0.0.0.0", port=8000)# test
