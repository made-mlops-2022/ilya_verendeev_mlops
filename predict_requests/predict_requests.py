import json
import logging
from pathlib import Path
import requests
from utils import generate_dataset

DATASET_SIZE = 20

logging.basicConfig(
    filename="logs.log",
    format="%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.DEBUG,
    filemode="w",
)
logger = logging.getLogger(__name__)

def main():
    logger.debug("Start predict_requests.py script")

    for request in generate_dataset(DATASET_SIZE):
        logger.debug("Generate request - %s", str(request))
        logger.info("Send request")
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json.dumps(request)
        )
        logger.info("Request status code: %s", str(response.status_code))
        logger.debug("Request body: %s", str(response))
    logger.debug("Finish predict_requests.py script")

if __name__ == "__main__":
    main()