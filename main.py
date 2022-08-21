import string
from tokenize import Name
from typing import Optional, Union
from urllib import response
from fastapi import FastAPI, status, Response
from pydantic import BaseModel

app = FastAPI()

# Create Your Response Object
class MatchDataObj(BaseModel):
    Name: str
    Tagline: Union[str, None] = None

@app.get("/matches-data", response_model = MatchDataObj)
async def getMatchesData(*, name: Optional[str] = None,  tagline: Optional[str] = None, response : Response):
    # Call Your File And Get Data From It Here 
    item : MatchDataObj = MatchDataObj(Name = name, Tagline = tagline)
    response.status_code = status.HTTP_200_OK
    # Return Data in JSON Formate From Here
    return item
