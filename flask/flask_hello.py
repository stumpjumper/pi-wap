#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    msg="""
    This is a line of text<br>
    And another line of text<br>
    And one more!<br>
"""
    return msg
    
