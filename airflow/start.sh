export FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
cd images/airflow-ml-base && docker build -t airflow-ml-base:latest .
cd ../.. && docker compose up --build
docker-compose logs test_dags