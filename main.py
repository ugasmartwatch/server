from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import sqlite3

app = FastAPI()

@app.get("/")
async def root():
    return {"server_status":":)"}

@app.get("/devices")
async def get_device_ids():
    with dbConnection() as con:
       return pd.read_sql("select device_id from profiles", con)['device_id'].to_list() 
    return {"message": "UGASmartwatch Database unavailable contact Kyle Johnsen"}

class Profile(BaseModel):
    device_id: str
    config_json: str

@app.put("/profiles")
async def put_profile(p: Profile):
    with dbConnection() as con:
        con.execute("INSERT INTO profiles (device_id, config) values (?,?)", (p.device_id, p.config_json));
        return {"success": "True"}
    return {"success": "False", "message": "UGASmartwatch Database unavailable contact Kyle Johnsen"}

@app.get("/profiles")
async def get_profile(device_id):
    with dbConnection() as con:
       return pd.read_sql("select * from profiles where device_id = ?", con, params=(device_id,)).iloc[0].to_json()
    return {"success": "False", "message": "UGASmartwatch Database unavailable contact Kyle Johnsen"}

class Sync(BaseModel):
    device_id: str
    sync_data: str

@app.put("/syncs")
async def put_sync(s: Sync):
    with dbConnection() as con:
        con.execute("INSERT INTO syncs (device_id, data) values (?,?)", (s.device_id, s.sync_data));
        return {"success": "True"}
    return {"success": "False", "message": "UGASmartwatch Database unavailable contact Kyle Johnsen"}

def dbConnection():
    return sqlite3.connect("db.db")
