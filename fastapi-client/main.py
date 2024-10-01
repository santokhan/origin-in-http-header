from fastapi import FastAPI
import requests

app = FastAPI()


def fetch():
    response = requests.get(
        "http://localhost:8080",
        headers={
            "Origin": "http://localhost:8040",
            "Referer": "http://localhost:8040/",
        },
    )
    data = {
        "url": response.json(),  # Assuming the response is JSON
    }
    print(data)


fetch()
