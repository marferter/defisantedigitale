from typing import Union, Optional
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Event(BaseModel):
    app: str
    eventType: str
    timestamp: Optional[str]

all_events = {}

'''
POST /student/12/newEvent
'''
@app.post("/student/{student_id}/newEvent")
async def create_item(event: Event):
    # datetime object containing current date and time
    now = datetime.now()


    if student_id in all_events:
        all_events[student_id].append(event)
    else:
        all_events[student_id] = [event]

    return item


@app.get("/student/{student_id}/events")
def get_all_events(student_id: int):
    return all_events[student_id]

