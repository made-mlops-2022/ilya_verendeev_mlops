"""train.py"""

import os
import pickle

import pandas as pd
import click
import mlflow
from mlflow.tracking import MlflowClient
import json
from sklearn.metrics import accuracy_score, f1_score

URL = "http://localhost:5000"
@click.command('test')
@click.option("--input-dir")
@click.option("--models-dir")
@click.option("--output-dir")
@click.option("--operation")
def main(input_dir: str, models_dir: str, output_dir: str, operation: str)->None:
    mlflow.set_tracking_uri(URL)
    if operation == 'validate':
        mlflow.set_experiment("validate")
    else:
        mlflow.set_experiment("predict")

    mlflow_client = MlflowClient()

    os.makedirs(output_dir, exist_ok=True)
    test_x = pd.read_csv(os.path.join(input_dir, "processed_test_data.csv"))
    test_y = pd.read_csv(os.path.join(input_dir, "test_target.csv"))

    mv = mlflow_client.search_model_versions("name='LogReg'")
    version = max([dict(v)['version'] for v in mv])
    model = mlflow.sklearn.load_model(f"models:/LogReg/{version}")

    predicted_y = model.predict(test_x)

    pd.DataFrame(predicted_y).to_csv(os.path.join(output_dir, "predictions.csv"), index=False)

    accuracy_metrics = accuracy_score(test_y, predicted_y)
    f1_metrics = f1_score(test_y, predicted_y)

    results = {
            "accuracy": accuracy_metrics,
            "f1": f1_metrics,
        }
    with mlflow.start_run():
        mlflow.log_metrics(results)

    with open(os.path.join(output_dir, "metrics.json"), mode='w') as file:
        json.dump(results, file)

if __name__ == '__main__':
    main()
