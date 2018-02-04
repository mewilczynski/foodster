from flask import Flask, request, render_template

from yelp import *
from cf import *

##from PyDictionary import PyDictionary
##dictionary = PyDictionary

import json

food_img1 = 'https://recipes.heart.org/-/media/aha/recipe/recipe-images/mediterranean-salad.jpg'
food_img2 = 'https://media1.s-nbcnews.com/j/newscms/2017_20/1215661/baked-chicken-today-170519-tease_15b214baba5431d761c7a46cf08e062c.today-inline-large.jpg'
food_img3 = 'https://recipes.heart.org/recipes/1128/mediterranean-salad'
food_img = 'http://www.ruchiskitchen.com/wp-content/uploads/2016/12/spicy-peanut-noodles-recipe-14.jpg'

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/swipe', methods=['GET'])
def swipe():
    cf_list = ProcessImage(food_img)
    list_1, list_2, list_3 = ProcessImageLabels(food_img)
    print(list_1)
    print(list_2)
    print(list_3)
    name, name1, name2 = query_api("food", ', '.join(cf_list), "Tampa, FL", True)
    print(name)
    print(name1)
    print(name2)
    return render_template('swipe.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']

    return


if __name__ == "__main__":
    app.run()
