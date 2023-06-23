from fastapi import APIRouter
from pydantic import BaseModel

from detail_model import DetailModel

api_router = APIRouter()

class SourceMeasures(BaseModel):
    length: float
    width: float

@api_router.get("/")
async def root():
    return {"message": "Detail validity"}


@api_router.post("/check_validity/")
def check_validity(source: SourceMeasures):
    """Detail validity check by its measurements
    - **length**: detail length
    - **width**: detail width
    """
    model = DetailModel()
    result = model.predict(source.length, source.width)
    return "valid" if result.item() else "invalid"
