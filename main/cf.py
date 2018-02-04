from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='c9cbc2fd5662400e9dd434535d410433')

model = app.models.get('general-v1.3')

def ProcessImage(imagelink):
    predict = model.predict_by_url(url=imagelink)

    list_p = []
    for i in range(0,7):
        list_p.append(predict["outputs"][0]["data"]["concepts"][i]["name"])

    return list_p
