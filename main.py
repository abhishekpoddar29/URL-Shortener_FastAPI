from fastapi import FastAPI,HTTPException
from fastapi.responses import RedirectResponse


from models import URLRequest
from utils import gen_short_url
from storage import add_url_mapping, get_orignal_url,load_data



app=FastAPI()

@app.get("/{short_url}")
def redirect_to_orignal(short_url: str):
    orignal_url=get_orignal_url(short_url)

    if not orignal_url:
        raise HTTPException(status_code=404,detail="URL not found")
    return RedirectResponse(url=orignal_url)


@app.post("/shorten")
def create_short_url(request:URLRequest):
    if not request.url.startswith(("http://","https://")):
        raise HTTPException(status_code=400,detail="Invalid URL format")
    
    data=load_data()
    short_url=gen_short_url()

    while short_url in data:
        short_url=gen_short_url()
    
    add_url_mapping(short_url,request.url)

    return {
        "short_url":f"http://127.0.0.1:8000/{short_url}"
    }
