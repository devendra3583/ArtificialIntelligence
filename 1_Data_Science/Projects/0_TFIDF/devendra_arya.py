from flask import Flask
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from flask import request
import pymysql
import json

execfile('tfidf_helper.py')

app = Flask(__name__)
api = Api(app)

class News(Resource):
    def get(self):
        data = json.load(open("news.json"))
        return data
                

api.add_resource(News, '/news') # Route_2

def string2feature(strn):
	s = strn.lower()
	cleaned = clean(s)
	c = cleaned.split() #get in a list
	tokens = remove_stopwords(c)
	features = tokens
	return features

def tfidf():
	#print 'hello'
	list_of_strings = []
	data = json.load(open("news.json"))
	for i in range(10):
		descr =  data['articles'][i]['description']
		list_of_strings.append(descr)
	for s in list_of_strings:
		feature_str = string2feature(s)
		print feature_str





#if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=81)
     

searchAlgorithm()
