from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.add_event_handler('startup')
async def startup_event():
    print('Server On...')

@app.add_event_handler('shutdown')
async def shutdown_event():
    print('Server Off...')

