import wikipedia
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/{topic}")
def get_top(topic:str):
    return wikipedia.search(topic,results=1)


@app.get("/topic/{topic}")
def get_more_topics(topic: str, num_topics: int):
    return wikipedia.search(topic, num_topics)


class GetTopics(BaseModel):
    topic: str
    num_of_topics: int


class Topic(BaseModel):
    topic: str
    results: str


@app.post("/", response_model=Topic)
def get_topics_post(topic: GetTopics):
    return Topic(topic=topic.topic, results=wikipedia.search(topic.topic, topic.num_of_topics))

