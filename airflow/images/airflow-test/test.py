"""train.py"""

import os
import pickle

import pandas as pd
import click
import json
from sklearn.metrics import accuracy_score, f1_score


@click.command('test')
@click.argument("input_dir")
@click.argument("models_dir")
@click.argument("output_dir")
def main(input_dir: str, models_dir: str, output_dir: str)->None:

    os.makedirs(output_dir, exist_ok=True)
    test_x = pd.read_csv(os.path.join(input_dir, "processed_test_data.csv"))
    test_y = pd.read_csv(os.path.join(input_dir, "test_target.csv"))

    with open(os.path.join(models_dir, "model.pkl"), mode='rb') as file:
        model = pickle.load(file)
    predicted_y = model.predict(test_x)

    pd.DataFrame(predicted_y).to_csv(os.path.join(output_dir, "predictions.csv"), index=False)

    accuracy_metrics = accuracy_score(test_y, predicted_y)
    f1_metrics = f1_score(test_y, predicted_y)

    results = {
            "accuracy": accuracy_metrics,
            "f1": f1_metrics,
        }
    with open(os.path.join(output_dir, "metrics.json"), mode='w') as file:
        json.dump(results, file)

if __name__ == '__main__':
    main()
