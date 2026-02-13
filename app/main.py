from fastapi import FastAPI
from app.router.userRouter import router as userRouter
from app.router.eventRouter import router as eventRouter
from app.router.searchRouter import router as searchRouter
from app.database import init_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(userRouter, prefix='/api')
app.include_router(eventRouter, prefix='/api')
app.include_router(searchRouter, prefix='/api')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

async def startup_event():
    init_db()
    print('Server On...')

async def shutdown_event():
    print('Server Off...')


app.add_event_handler('startup', startup_event)
app.add_event_handler('shutdown', shutdown_event)