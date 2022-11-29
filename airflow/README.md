
```Bash-script``` для запуска родительского докера ```airflow-ml-base``` и ```docker-compose```:
```
bash start.sh
```
To check data into container use:
```
docker exec -it scheduler bash
```
Test - start in separate container - ```unittests```. To see logs use command:
```
docker-compose logs unittests
```
MlFlow here:
```
http://localhost:5000/
```
https://github.com/mrts/docker-postgresql-multiple-databases/blob/master/create-multiple-postgresql-databases.sh