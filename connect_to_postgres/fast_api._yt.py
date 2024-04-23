from fastapi import FastAPI
import random

#create the app, so you can query infromation form the api

app = FastAPI()

#endpoint
@app.get('/')

#path to use to get to infromation  #root of application, 
# first response user gets when user loads api

async def root():
    return {
        'example': 'This is an example',
            'data': 0
            }  # basic API response
    
#random number
@app.get('/random')
async def get_random():
    rn: int = random.randint(0,100)
    return {'number': rn, 'limit': 100}

#random number with limit 
@app.get('/random/{limit}')
async def get_random(limit: int):
    rn: int = random.randint(0, limit)
    return {'number': rn, 'limit': limit}