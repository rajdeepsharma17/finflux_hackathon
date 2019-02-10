#!/usr/bin/python
# # -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask import request, redirect, jsonify
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from databaseSetup import Base, Members
from flask_cors import CORS
from flask import session as login_session
import random
import string
import json
import requests


app = Flask(__name__)
CORS(app)


# Connect to Database and create database session
engine = create_engine('sqlite:///finflux.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Finflux"


@app.route('/')
def showLogin():
    return redirect('/login')


@app.route('/api/json')
def showJson():
    member = session.query(Members)
    return jsonify(Members=[r.serialize for r in member])



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=5000)
