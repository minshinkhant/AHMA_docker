from typing import Optional
from fastapi import FastAPI, Response, Cookie
# import requests

# session = requests.Session()
# response = session.get("")

app = FastAPI()

#main page endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

#item id testing
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

#cookies testing 
@app.get("/cookies/")
def create_cookie(response: Response):
    response.set_cookie(key="fakesession", value="1")
    return {"message": "got the cookies"}

#cookies delete
@app.get("/cookies/delete")
def delete_cookie(response: Response):
	response.delete_cookie("fakesession")
	return {"cookies deleted"}

#get request to vend an item
@app.get("/items/{item_id}/vend")
async def vend(response: Response, fakesession:Optional[str] = Cookie(None)):
 	if (fakesession):
 		return {"a user can only vend once"}
 	else:
 		#setting a cookie
 		response.set_cookie(key="fakesession", value="cookies_value")
 		return {"message": "vending the simple product"}

