from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as C1Image

key_item = 'af65160befb54398b247aa12dd1256e3'

img1 = 'https://prods3.imgix.net/images/articles/2017_04/Feature-restaurant-butcher-bakery-shops2.jpg'

def ProcessImage(imageLink):

    app = ClarifaiApp(api_key = key_item)

    model = app.models.get("general-v1.3")
    image = C1Image(url = imageLink)

    var = model.predict([image])

    for i in range(0, 3):
        #if(var["outputs"][0]["data"]["concepts"][i]["value"] > 0.97):
        print(var["outputs"][0]["data"]["concepts"][i]["name"])

    return

ProcessImage(img1)
