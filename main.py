from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
async def root():
    return {"server_status":":)"}

@app.get("/devices")
async def get_device_ids():
    with dbConnection() as con:
       return pd.read_sql("select device_id from profiles", con)['device_id'].to_list() 
    return {"message": "UGASmartwatch Database unavailable contact Kyle Johnsen"}

@app.put("/profile")
async def put_profile(device_id, profile):
    with dbConnection() as con:
        con.execute("INSERT INTO profiles (device_id, config) values (?,?)", (device_id, profile));
        return {"success": "True"}
    return {"success": "False", "message": "UGASmartwatch Database unavailable contact Kyle Johnsen"}

@app.get("/profile")
async def get_profile(device_id):
    with dbConnection() as con:
       return pd.read_sql("select * from profiles where devicie_id = ?", con, (device_id,))['device_id'].to_list() 
    return {"success": "False", "message": "UGASmartwatch Database unavailable contact Kyle Johnsen"}

@app.put("/sync")
async def put_sync(device_id, sync_data):
    with dbConnection() as con:
        con.execute("INSERT INTO syncs (device_id, data) values (?,?)", (device_id, sync_data));
        return {"success": "True"}
    return {"success": "False", "message": "UGASmartwatch Database unavailable contact Kyle Johnsen"}

def dbConnection():
    return sqlite3.connect("db.db")
