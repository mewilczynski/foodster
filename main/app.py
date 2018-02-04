from flask import Flask, request, render_template

from yelp import *
from cf import *

##from PyDictionary import PyDictionary
##dictionary = PyDictionary

import json
food_img = 'https://recipes.heart.org/-/media/aha/recipe/recipe-images/mediterranean-salad.jpg'

app = Flask(__name__)

@app.route('/')
def home():
    cf_list = ProcessImage(food_img)
    print(cf_list)
    print("\n")
    query_api("food", ', '.join(cf_list), "Tampa, FL", True)

    return render_template('index.html')


@app.route('/swipe', methods=['GET'])
def swipe():
    return render_template('swipe.html')

if __name__ == "__main__":
    app.run()
