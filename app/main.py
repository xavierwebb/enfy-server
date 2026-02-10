from fastapi import FastAPI
from app.router.userRouter import router as userRoter
from app.database import init_db

app = FastAPI()

app.include_router(userRoter, prefix='/api')

async def startup_event():
    init_db()
    print('Server On...')

async def shutdown_event():
    print('Server Off...')


app.add_event_handler('startup', startup_event)
app.add_event_handler('shutdown', shutdown_event)