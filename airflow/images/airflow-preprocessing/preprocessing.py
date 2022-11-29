"""preprocessing.py"""

import os

import pandas as pd
import click
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


@click.command('preprocessing')
@click.option("--input-dir")
@click.option("--output-dir")
def main(input_dir: str, output_dir: str)->None:
    os.makedirs(output_dir, exist_ok=True)
    data_df = pd.read_csv(os.path.join(input_dir, "data.csv"))
    target_df = pd.read_csv(os.path.join(input_dir, "target.csv"))

    preprocessing_pipe = Pipeline([('impute', SimpleImputer(strategy='mean')),
                                   ('scaler', StandardScaler())])
    processed_data_df = pd.DataFrame(preprocessing_pipe.fit_transform(data_df),
                                     columns=data_df.columns)
    processed_data_df.to_csv(os.path.join(output_dir, "processed.csv"), index=False)
    target_df.to_csv(os.path.join(output_dir, "target.csv"), index=False)


if __name__ == '__main__':
    main()
