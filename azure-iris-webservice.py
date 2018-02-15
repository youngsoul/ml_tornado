import requests
import json

"""
https://github.com/Azure-Readiness/hol-azure-machine-learning
"""



url = 'https://ussouthcentral.services.azureml.net/workspaces/953ba34dba104e8eb5513454b24d50f0/services/68cb8a0297b14f9499b45448ea25b7bb/execute?api-version=2.0&details=true'
azure_ml_webservice_api_key = '69+QepDKE9/sLfVfzpJBdE8N12ljqz214+nWVF6odUy/ZsBDtS8KPoCNmYf7CDAbqFK3blxhzi/LPTpWjdV7JA=='
headers = {'Authorization': f"Bearer {azure_ml_webservice_api_key}",
          "Content-Type":"application/json"}


# look at the 'Web Service input' module for Lab008 in AML.
# One of the Web Service Input modules has a name of 'input1' and the other 'input2'.  This is how the
# different data is being mapped to the different inputs.
data =  {
  "Inputs": {
    "input1": {
      "ColumnNames": [
        "Id",
        "SepalLengthCm",
        "SepalWidthCm",
        "PetalLengthCm",
        "PetalWidthCm",
        "Species"
      ],
      "Values": [
        [
        "1","4.9","3.1","1.5","0.1",""
        ]
      ]
    }
  },
  "GlobalParameters": {}
}

r = requests.post(url, data = json.dumps(data), headers=headers)
result = r.content.decode('ascii')
result_json = json.loads(result)
print(f"Prediction: {result_json['Results']['output1']['value']['Values'][0][9]}")
