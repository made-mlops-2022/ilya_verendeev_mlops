FROM python:3.9-slim

COPY requirements.txt app.py load_models.py schemas.py utils.py run.sh ./app/
RUN python3 -m pip install --upgrade pip && pip install -r ./app/requirements.txt

WORKDIR /app

ENV PATH_TO_TRANSFORMER="transformer.pkl"
ENV PATH_TO_MODEL="random_forest_model.pkl"

CMD ["bash", "run.sh"]
