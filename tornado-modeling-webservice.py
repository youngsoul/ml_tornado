import requests
import json

"""
https://github.com/Azure-Readiness/hol-azure-machine-learning
"""



url = 'https://ussouthcentral.services.azureml.net/workspaces/953ba34dba104e8eb5513454b24d50f0/services/20f33507a3c442218e9c115b84cadc76/execute?api-version=2.0&details=true'
azure_ml_webservice_api_key = 'mMHzgZHFoAJNSfEXgkhr5W36kOZwJJusTG5ooaLvQfsKkOpVEjqnwdCtRt/kERLBJnKU9cembfoD1l/Rb8sB3w=='
headers = {'Authorization': f"Bearer {azure_ml_webservice_api_key}",
          "Content-Type":"application/json"}


# look at the 'Web Service input' module for Lab008 in AML.
# One of the Web Service Input modules has a name of 'input1' and the other 'input2'.  This is how the
# different data is being mapped to the different inputs.
data =  {
  "Inputs": {
    "input1": {
      "ColumnNames": [
        "State_Num",
        "County_Num",
        "Month",
        "F-Scale_0",
        "F-Scale_1",
        "F-Scale_2",
        "F-Scale_3",
        "F-Scale_4",
        "F-Scale_5",
        "Damage_Bin"
      ],
      "Values": [
        [
          "1",
          "95",
          "7",
          "1",
          "0",
          "0",
          "0",
          "0",
          "0",
          ""
        ]
      ]
    }
  },
  "GlobalParameters": {}
}


r = requests.post(url, data = json.dumps(data), headers=headers)
result = r.content.decode('ascii')
result_json = json.loads(result)
print(f"Prediction: {result_json['Results']['output1']['value']['Values'][0][136]}")
