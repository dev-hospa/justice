#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 09:38:19 2021

@author: sveter
"""

# app.py
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///justice_db.db'
app.config["SQLALCHEMY_ECHO"] = True
app.secret_key = "123456"
app.debug = True
toolbar = DebugToolbarExtension(app)
db = SQLAlchemy(app)