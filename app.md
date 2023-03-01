##### Install dependencies
pip install -r requirements.txt

##### Serve on localhost:5500
##### First, activate the python environment for this app
##### Then, run app using selected Conda environment
##### --no-capture-output is required to see logs
source activate <my_environment>
conda run --no-capture-output python run.py

##### To automatically update the requirements.txt file (Caution: not app specific will list everything available in the pip install directory, even for other apps)
python -m pip freeze > requirements.txt

##### Include Procfile before deploying to Heroku
##### 'run' refers to 'run.py' file
(e.g.,: web: gunicorn module_name_where_app_instance_exists:name_of_the_app_instance)
web: gunicorn run:my_app