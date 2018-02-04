##testing from python shell, NO flask

from PIL import Image

import urllib.request

from yelp import *
from cf import *

##from PyDictionary import PyDictionary
##dictionary = PyDictionary

import json

food_img = ['https://recipes.heart.org/-/media/aha/recipe/recipe-images/mediterranean-salad.jpg',
'https://budgetbytes.com/wp-content/uploads/2016/07/Pasta-with-Butter-Tomato-Sauce-and-Toasted-Bread-Crumbs-utensils.jpg',
'https://media.timeout.com/images/103902673/image.jpg','https://upload.wikimedia.org/wikipedia/commons/e/e6/BLT_sandwich_on_toast.jpg'
'http://alyssasarfity.com/wp-content/uploads/2014/04/Screen-Shot-2014-04-03-at-6.34.25-PM-940x529.png']

def main():

    top_list = []

    for i in range(len(food_img)):
        link = urllib.request.urlopen(food_img[i])
        img = Image.open(link)
        size = 256 , 256
        img.thumbnail(size)
        img.show()
        response = input("Left or right? ")
        if response is 'r':
            cf_list = ProcessImage(link)
            top_list.append(cf_list)
            img.close()
        if response is 'l':
            img.close()
        print(top_list)
        print("\n")



    #print("\n")
    #query_api("food", ', '.join(cf_list), "Tampa, FL", True)



if __name__ == "__main__":
    main()
