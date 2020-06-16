#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: kayfindo
"""
from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('medform.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form

      with open('file.json', 'w') as f:
        json.dump(request.form, f)

      response = requests.post('http://localhost:4000/', json=json.dumps(result))

      return render_template("result.html",result = result, message=response.content)

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = True)