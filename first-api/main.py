from fastapi import FastAPI

from db import database as connection
from db import User

app = FastAPI(
    title='Testing',
    description='Testing my first API',
    version='0.0.1'
)

# events
@app.on_event('startup')
def start_up():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([User])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

# endpoints
@app.get('/')
async def index():
    return {'Name': 'Mario'}

@app.get('/about')
async def about():
    return {'By': 'Mario'}
