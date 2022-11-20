# mlops_made_2022


### Настройка окружение:

1) ```python3 -m venv .venv```
2) ```source .venv/bin/activate```
3) ```pip3 install -r requirements.txt```

### Make directory for logs and results (if there aren't these folders in actual commit):
```mkdir src/logs && mkdir results```
### ML pipeline start with commands:
#### Training:
```python3 -m src.model_pipeline --process-type=train configs/<config's name>```
#### Evaluating:
```python3 -m src.model_pipeline --process-type=predict configs/<config's name>```
### Configs:
1) ```logistic_regression_config.yaml``` - model with logistic regression
2) ```random_forest_config.yaml``` - model with random forest
#### Preprocessing pipeline can be corrected with changing ```preprocessing_params```. There are three different type of preprocessing in configs: ```normalization```, ```polynomial```, ```k-bin```
### Tests:
Tests start with ```python3 -m unittest discover -s ./tests  -p 'test_*.py'```
### Output data:
1) ```results/metrics.json``` - result of predict-process
2) ```src/logs/logs.log``` - logs of all scripts

### Other:
requirements.txt was created with console command:
```pip3 freeze | grep -v hw01 > requirements.txt``` - all libs were saved like this
.gitignore and global .gitignore was created with console command:
1) ```curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore``` - and add -idea
2) ```curl -o $HOME/.gitignore_global https://raw.githubusercontent.com/github/gitignore/master/Global/Linux.gitignore```
