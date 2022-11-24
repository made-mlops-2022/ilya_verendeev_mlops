from fastapi import (FastAPI, Request)
from utils import (Pipeline, get_pipe_from_file)
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from schemas import DatasetClass
import pandas as pd
import os
from fastapi_health import health

PIPELINE = Pipeline()

app = FastAPI(title="Random Forest Model",
              description="Rest API for homework № 2",
              version="1.0")

@app.on_event("startup")
def get_transformer_and_model():
    PIPELINE.transformer = get_pipe_from_file(os.getenv("PATH_TO_TRANSFORMER"))
    PIPELINE.model = get_pipe_from_file(os.getenv("PATH_TO_MODEL"))

@app.post("/predict")
async def predict(data: DatasetClass):
    X = pd.DataFrame([data.dict()])
    y_pred = PIPELINE.predict(X)
    if y_pred[0]:
        result = 'disease'
    else:
        result = 'no disease'
    return {"prediction result": result}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=440,
        content={"details": exc.errors()},
    )

def transformer_ready():
    return PIPELINE.transformer is None

def model_ready():
    return PIPELINE.model is None


async def success_handler():
    return {"status": "ready"}


async def failure_handler():
    results = []
    if not transformer_ready():
        results.append('transformer')
    if not model_ready():
        results.append('model')
    return {"status": ", ".join(results) + " not ready"}


app.add_api_route("/health",
                  health([transformer_ready, model_ready],
                         success_handler=success_handler,
                         failure_handler=failure_handler
                         )
                  )