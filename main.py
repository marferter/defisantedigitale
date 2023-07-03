from typing import Union

from fastapi import FastAPI

app = FastAPI()

class Event(BaseModel):
    timestamp: str
    app: str
    eventType: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

all_events = {}

'''
POST /student/12/newEvent
'''
@app.post("/student/{student_id}/newEvent")
async def create_item(event: Event):
    if student_id in all_events:
        all_events[student_id].append(event)
    else:
        all_events[student_id] = [event]

    return item


@app.get("/student/{student_id}/events")
def get_all_events(student_id: int):
    return all_events[student_id]

