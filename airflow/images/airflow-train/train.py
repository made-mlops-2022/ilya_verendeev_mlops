"""train.py"""

import os
import pickle

import pandas as pd
import click
from sklearn.linear_model import LogisticRegression


@click.command('train')
@click.option("--input-dir")
@click.option("--models-dir")
def main(input_dir: str, models_dir: str)->None:
    os.makedirs(models_dir, exist_ok=True)
    train_x = pd.read_csv(os.path.join(input_dir, "processed_train_data.csv"))
    train_y = pd.read_csv(os.path.join(input_dir, "train_target.csv"))

    model = LogisticRegression()
    model.fit(train_x, train_y.values.ravel())

    with open(os.path.join(models_dir, "model.pkl"), mode='wb') as file:
        pickle.dump(model, file)

if __name__ == '__main__':
    main()
