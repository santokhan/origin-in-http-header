from fastapi import FastAPI, HTTPException, Request

app = FastAPI()


def reset_url(request: Request):
    """
    Will work on the production environment only < Santo
    """
    origin = request.headers.get("origin")
    if origin:
        if not origin.endswith('/'):
            origin += '/'
        return f"{origin}zurücksetzen"
    raise ValueError("The 'origin' header is missing.")


@app.get("/")
async def root(request: Request):
    try:
        url = reset_url(request)
        print(f"url: {url}")
        return {"url": url} 
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
