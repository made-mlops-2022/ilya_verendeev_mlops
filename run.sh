if [[ -z $PATH_TO_TRANSFORMER ]]; then
  export PATH_TO_TRANSFORMER="transformer.pkl"
fi

if [[ -z $PATH_TO_MODEL ]]; then
  export PATH_TO_MODEL="random_forest_model.pkl"
fi

if [ ! -f "$PATH_TO_TRANSFORMER" ] && [ ! -f "$PATH_TO_MODEL" ]; then
    python3 -m load_models $PATH_TO_TRANSFORMER $PATH_TO_MODEL
else
    echo "Pipelines are already exist"
fi

uvicorn app:app --reload --host 0.0.0.0 --port 8000
