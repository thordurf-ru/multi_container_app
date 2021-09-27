from typing import Optional

import psycopg2
import uvicorn
from fastapi import FastAPI
from datetime import datetime

from pydantic import BaseModel

app = FastAPI()

conn = psycopg2.connect(
    host='best-number-db',
    database='best_number',
    user='postgres',
    password='password',
    port='5432'
)


class BestNumber(BaseModel):
    bestNumber: Optional[int]


@app.get("/bestnumber")
def get_best_number():
    cursor = conn.cursor()

    cursor.execute('''
    select * 
    from best_number 
    order by created desc
    fetch first row only''')

    rows = cursor.fetchall()
    return rows[0][0] if len(rows) > 0 else None


@app.post("/bestnumber")
def save_best_number(body: BestNumber):
    cursor = conn.cursor()
    cursor.execute('insert into best_number (number, created) '
                   'values (%s, %s)', (body.bestNumber, datetime.now()))
    conn.commit()


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
