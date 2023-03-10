from flask import Flask

app = Flask(__name__, instance_relative_config=True)

from my_app import routes

app.config.from_object('config')