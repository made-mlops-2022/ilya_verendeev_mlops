export PATH_TO_TRANSFORMER="transformer.pkl"
export PATH_TO_MODEL="random_forest_model.pkl"

python3 -m pip install --upgrade pip && pip install -r requirements.txt
python3 -m load_models $PATH_TO_TRANSFORMER $PATH_TO_MODEL

python3 -m unittest test_app.py

rm $PATH_TO_TRANSFORMER $PATH_TO_MODEL
unset PATH_TO_TRANSFORMER
unset PATH_TO_MODEL