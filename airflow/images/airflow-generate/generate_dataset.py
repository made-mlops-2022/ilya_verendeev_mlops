"""generate_dataset.py"""

import os
import pandas as pd
from sklearn.datasets import make_classification
import click

DATASET_SIZE = 200

@click.command("generate")
@click.argument("output_dir")
def main(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    data, target = make_classification(n_samples=500,
                                             n_features=20,
                                             n_classes=2)
    pd.DataFrame(data).to_csv(os.path.join(output_dir, "data.csv"), index=False)
    pd.DataFrame(target).to_csv(os.path.join(output_dir, "target.csv"), index=False)

if __name__ == '__main__':
    main()
