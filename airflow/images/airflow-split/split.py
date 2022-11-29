"""split.py"""

import os
import click
import pandas as pd
from sklearn.model_selection import train_test_split


@click.command('split')
@click.option("--input-dir")
@click.option("--output-dir")
def main(input_dir: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    processed_data_df = pd.read_csv(os.path.join(input_dir, "processed.csv"))
    target_df = pd.read_csv(os.path.join(input_dir, "target.csv"))
    train_x_df, test_x_df, train_y_df, test_y_df = train_test_split(processed_data_df, target_df, test_size=0.3)

    train_x_df.to_csv(os.path.join(output_dir, "processed_train_data.csv"), index=False)
    test_x_df.to_csv(os.path.join(output_dir, "processed_test_data.csv"), index=False)
    train_y_df.to_csv(os.path.join(output_dir, "train_target.csv"), index=False)
    test_y_df.to_csv(os.path.join(output_dir, "test_target.csv"), index=False)

if __name__ == '__main__':
    main()
