from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='c9cbc2fd5662400e9dd434535d410433')

model = app.models.get('general-v1.3')

def ProcessImage(imagelink):

    predict = model.predict_by_url(url=imagelink)

    list_p = []
    for i in range(0,10):
        list_p.append(predict["outputs"][0]["data"]["concepts"][i]["name"])
    
    return list_p
'''
def ProcessImageLabels(imagelink):
    predict = model.predict_by_url(url=imagelink)

    list_1 = predict["outputs"][0]["data"]["concepts"][0]["name"]
    list_2 = predict["outputs"][0]["data"]["concepts"][1]["name"]
    list_3 = predict["outputs"][0]["data"]["concepts"][2]["name"]
    list_4 = predict["outputs"][0]["data"]["concepts"][3]["name"]
    list_5 = predict["outputs"][0]["data"]["concepts"][4]["name"]
    list_6 = predict["outputs"][0]["data"]["concepts"][5]["name"]
    list_7 = predict["outputs"][0]["data"]["concepts"][6]["name"]
    list_8 = predict["outputs"][0]["data"]["concepts"][7]["name"]
    list_9 = predict["outputs"][0]["data"]["concepts"][8]["name"]
    list_10 = predict["outputs"][0]["data"]["concepts"][9]["name"]

    return list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10
'''
