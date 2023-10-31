# Name: apiCore.py
# Author: Reacubeth
# Time: 2023/10/31 20:40
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# -- coding: utf-8 --**

import uvicorn
from fastapi import FastAPI, Query, Form, APIRouter, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import time

from dbUtils import db_get_paper


app = FastAPI(
    title="demo",
    docs_url='/api/v1/docs',
    redoc_url='/api/v1/redoc',
    openapi_url='/api/v1/openapi.json'
)

router = APIRouter()


@router.get('/paper')
async def fetch_paper(
    num: int = Query(..., description='returned paper num', example='10')
):
    start = time.time()
    data = db_get_paper(num)
    # print(data)
    return {'time': time.time() - start, 'data': data}


@router.post('/add_paper')
async def add_paper(
        name: str = Form(..., description='paper name', example='Attention is all you need'),
        info: str = Form(..., description='paper info', example='NIPS 2017')
):
    start = time.time()
    print(name, info)
    return {'time': time.time() - start}


@router.put('/update_paper')
async def update_paper(
        p_id: str = Form(..., description='paper id', example='1234'),
):
    start = time.time()
    print(p_id)
    return {'time': time.time() - start}


@router.delete('/delete_paper')
async def delete_paper(
        p_id: str = Query(..., description='paper is', example='1234')
):
    start = time.time()
    print(p_id)
    return {'time': time.time() - start}



app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=8000, workers=1)
