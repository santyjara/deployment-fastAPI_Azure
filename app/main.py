from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("app/model.joblib")


class Item(BaseModel):
    feature_1: float
    feature_2: float
    feature_3: float
    feature_4: float


@app.post("/predict")
async def generate_prediction(item: Item):

    pred = model.predict([[item.feature_1, item.feature_2, item.feature_3, item.feature_4]])[0]

    return {"prediction": int(pred)}
