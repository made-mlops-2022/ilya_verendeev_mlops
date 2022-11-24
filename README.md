## Homework №2
### Docker:
To build docker image with API:
```
docker build -t ilyaverendeev/homework_mlops:v1 .
```
To pull it from [DockerHub](https://hub.docker.com/r/ilyaverendeev/homework_mlops):
```
docker pull ilyaverendeev/homework_mlops:v1
```
To run container with API:
```
docker run --name homework_mlops -p 8000:8000 ilyaverendeev/homework_mlops:v1
```
### Fast API:
All information about endpoints and data-validators in API is shows in ```http://0.0.0.0:8000/docs``` <br />
Bash-script ```run.sh``` starts in docker.
To test custom requests use script ```predict_requests.py``` from parent system:
```
python3 -m predict_requests.predict_requests
```
**P.S.** 
This script generate data using generator ```utils.generate_dataset``` <br />
**P.P.S.**
Before using ```predict_requests.predict_requests``` start container
### Tests:
To run test from parent system:
```
bash run_tests.sh
```
### Docker optimization:
1. Add .dockerignore
2. Many run-operations in one
3. Try to use ```docker build``` from stdin, but it hasn't got some results
4. Drop from requirements.txt packages, which are used only in ```predict_requests.predict_requests``` and ```test_app```
