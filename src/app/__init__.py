from flask import Flask

app = Flask(__name__.split()[0])

from app import routes
