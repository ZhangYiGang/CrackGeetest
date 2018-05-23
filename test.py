import numpy as nm
import matplotlib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

conn = flask.MySQLdb.connect("localhost", "root", "123456", "test")
cur = conn.cursor()

