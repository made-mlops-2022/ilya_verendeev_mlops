from fastapi import (FastAPI, Request)
from utils import (Pipeline, get_pipe_from_file)
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from schemas import DatasetClass
import pandas as pd
from fastapi_health import health

PIPELINE = Pipeline()

transformer_path = "models/transformer.pkl"
model_path = "models/random_forest_model.pkl"

app = FastAPI(title="Random Forest Model",
              description="Rest API for homework № 2",
              version="1.0")

@app.on_event("startup")
def load_model():
    PIPELINE.transformer = get_pipe_from_file(transformer_path)
    PIPELINE.model = get_pipe_from_file(model_path)

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