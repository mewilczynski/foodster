from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='c9cbc2fd5662400e9dd434535d410433')

model = app.models.get('general-v1.3')

def ProcessImage(imagelink):
    predict = model.predict_by_url(url=imagelink)

    list_p = []
    for i in range(0,3):
        list_p.append(predict["outputs"][0]["data"]["concepts"][i]["name"])

    return list_p

def ProcessImageLabels(imagelink):
    predict = model.predict_by_url(url=imagelink)

    list_1 = predict["outputs"][0]["data"]["concepts"][0]["name"]
    list_2 = predict["outputs"][0]["data"]["concepts"][1]["name"]
    list_3 = predict["outputs"][0]["data"]["concepts"][2]["name"]

    return list_1, list_2, list_3
