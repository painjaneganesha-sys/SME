from fastapi import APIRouter
from pydantic import BaseModel


fetchdatarouter = APIRouter(prefix = "/fetch")

class DataModel(BaseModel):
    ContractName : str
    ContractPrice : float



@fetchdatarouter.get("/")
async def get_data():
    """ This returns all the methods of fetch data. """
    result = ["ContractName", "ContractPrice"]
    return result

