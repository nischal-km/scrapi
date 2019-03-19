from flask import Flask, request
from flask_restful import Resource, Api,reqparse
from json import dumps
import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)
api=Api(app)

# Collection to return
articledata=[]

class Scrap(Resource):
     def post(self):
        req=request.json
        url=req["url"]
        attribute=req["attribute"]
        print("URL to scrap",url)
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        all_links = soup.find_all(attribute)
        for link in all_links:
            articledata.append(link.text.strip())
        return ('').join(articledata)


api.add_resource(Scrap, '/scrap/')
app.run(debug=True)
