import json
from typing import Optional, Union
from fastapi import FastAPI, status, Response, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

# app intialization
app = FastAPI()

# template configuration
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# cors origin configuration
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Create Your Response Object
class MatchDataObj(BaseModel):
    Name: str
    Tagline: Union[str, None] = None

@app.get("/matches-data", response_model = MatchDataObj)
async def getMatchesData(*, name: Optional[str] = None,  tagline: Optional[str] = None, response : Response):
    # Call Your File And Get Data From It Here 
    # res = YourMethodName()
    # comment below  lines
    item : MatchDataObj = MatchDataObj(Name = name, Tagline = tagline)
    response.status_code = status.HTTP_200_OK
    # Return Data in JSON Formate From Here
    # uncomment below line
    # return json.dump(res)
    # comment below line
    return item


# html view
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})