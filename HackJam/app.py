from flask import Flask, request, render_template

from yelp import *
from cf import *

##from PyDictionary import PyDictionary
##dictionary = PyDictionary

import json

food_img = ['https://recipes.heart.org/-/media/aha/recipe/recipe-images/mediterranean-salad.jpg',
            'https://media1.s-nbcnews.com/j/newscms/2017_20/1215661/baked-chicken-today-170519-tease_15b214baba5431d761c7a46cf08e062c.today-inline-large.jpg',
            'https://recipes.heart.org/recipes/1128/mediterranean-salad',
            'http://www.ruchiskitchen.com/wp-content/uploads/2016/12/spicy-peanut-noodles-recipe-14.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/001_Tacos_de_carnitas%2C_carne_asada_y_al_pastor.jpg/1200px-001_Tacos_de_carnitas%2C_carne_asada_y_al_pastor.jpg',
            'http://cdn1.bostonmagazine.com/wp-content/uploads/sites/2/2017/07/ice-cream-boston.jpg',
            'https://www.firehousesubs.com/media/1740/large-tbr.jpg',
            'https://images-gmi-pmc.edge-generalmills.com/2031a382-71dc-4fd0-9ef7-72d011a9eebd.jpg',
            'http://www.saturdayeveningpost.com/wp-content/uploads/satevepost/seafood.jpg',
            'https://assets.epicurious.com/photos/57bdeab384c001120f6164fc/master/pass/barba-yiannis-grilled-lamb.jpg',
            'https://img.leafcdn.tv/640/photos.demandstudios.com/getty/article/181/28/186485589.jpg',
            'https://d9hyo6bif16lx.cloudfront.net/live/img/production/detail/menu/breakfast_breakfast-classics_big-two-do-breakfast.jpg',
            'http://www.hot-dog.org/sites/default/files/pictures/hot-dogs-on-the-grill-sm.jpg',
            'http://food.fnr.sndimg.com/content/dam/images/food/fullset/2011/2/2/0/BXSP01H_soft-hard-boiled-eggs-02_s4x3.jpg.rend.hgtvcom.616.462.suffix/1371595523837.jpeg'
            ]
global j
j = 0

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/swipe', methods=['GET'])

def swipe():
    cf_list = ProcessImage(food_img[j])

    print(cf_list)

    global j
    j += 1

    '''
    list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10 = ProcessImageLabels(food_img[10])
    print(list_1)
    print(list_2)
    print(list_3)
    print(list_4)
    print(list_5)
    print(list_6)
    print(list_7)
    print(list_8)
    print(list_9)
    print(list_10)
    '''

    name, name1, name2, location, location1, location2 = query_api("food", ', '.join(cf_list), "4202 E Fowler Ave, Tampa, FL", True, 40000)
    print(name + "\t\t" + location)
    print(name1 + "\t\t" + location1)
    print(name2 + "\t\t" + location2)

    return render_template('swipe.html', Pic=food_img[j], Name1=name,Loc1=location,Name2=name1,Loc2=location1,Name3=name2,Loc3=location2)
    #<p>Here is my variable: {{ variable }}</p>

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']

    return


if __name__ == "__main__":
    app.run()
