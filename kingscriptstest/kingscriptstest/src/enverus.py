"""
Pulling specific data from Enervus API

Developed by: Michael Tanner

"""

import pandas as pd
import os
import requests

'''
Returns a dataframe for a specific API14 of the monthly production data

'''


def getWellProductionData(apiKey, wellApi14):
    print("Begin Getting Well Production Data")
    # Checks if API is 14 digits long
    if len(wellApi14) != 14:
        lengthOfApi = len(wellApi14)
        print("API is not 14 digits long. It is " +
              str(lengthOfApi) + " digits long.")
        return
    # checks to ensure correct class for Enverus API
    if type(apiKey) != str:
        print("API Key is not the correct class")
        return

    def convertDateEnv(dateList):
        length = len(dateList)
        for i in range(0, length):
            if "T" in dateList[i]:
                index = dateList[i].index("T")
                dateList[i] = dateList[i][0:index]

        return dateList

    # POST request to get token
    session = requests.Session()
    url = 'https://api.enverus.com/v3/direct-access/tokens'
    secretKey = apiKey
    headers = {'Content-Type': 'application/json', }
    data = {'secretKey': secretKey}
    response_token = session.post(url, headers=headers, json=data)
    token = response_token.json()['token']

    # GET request to get data
    headers['Authorization'] = "Bearer {}".format(token)

    url = "https://api.enverus.com/v3/direct-access/"
    dataset = 'production'
    query_url = os.path.join(url, dataset)
    headers['Authorization'] = "Bearer {}".format(token)
    params = dict(deleteddate="null",
                  pagesize=100000, API_UWI_14_Unformatted=wellApi14)

    response = session.get(query_url, headers=headers, params=params)
    wellProdData = pd.DataFrame(response.json())

    dataLength = 1

    while dataLength > 0:
        response = session.get(
            url[:-1] + response.links['next']['url'], headers=headers)
        wellProdDataResponse = pd.DataFrame(response.json())
        wellProdData = pd.concat([wellProdData, wellProdDataResponse])
        dataLength = len(wellProdDataResponse)

    dateList = wellProdData['ProducingMonth'].tolist()
    dateListClean = convertDateEnv(dateList)

    return wellProdData
