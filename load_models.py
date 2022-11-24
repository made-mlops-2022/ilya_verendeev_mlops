import yadisk
import click

TOKEN = 'y0_AgAAAABXMB9DAAiwqwAAAADUsII21WsLDG_ZQLyy9gb_lrCwVNHJ3Q4'
CLIENT = yadisk.YaDisk(token=TOKEN)

if not CLIENT.check_token():
    raise ValueError("Need to refresh token")

@click.command
@click.argument("transformer_path")
@click.argument("model_path")
def main(transformer_path, model_path):
    CLIENT.download("/made_mlops/transformer.pkl", transformer_path)
    CLIENT.download("/made_mlops/random_forest_model.pkl", model_path)

if __name__ == '__main__':
    main()