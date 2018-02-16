import requests
import json

"""
https://github.com/Azure-Readiness/hol-azure-machine-learning
"""

url = 'https://ussouthcentral.services.azureml.net/workspaces/953ba34dba104e8eb5513454b24d50f0/services/20f33507a3c442218e9c115b84cadc76/execute?api-version=2.0&details=true'
azure_ml_webservice_api_key = 'mMHzgZHFoAJNSfEXgkhr5W36kOZwJJusTG5ooaLvQfsKkOpVEjqnwdCtRt/kERLBJnKU9cembfoD1l/Rb8sB3w=='
headers = {'Authorization': f"Bearer {azure_ml_webservice_api_key}",
           "Content-Type": "application/json"}

# look at the 'Web Service input' module for Lab008 in AML.
# One of the Web Service Input modules has a name of 'input1' and the other 'input2'.  This is how the
# different data is being mapped to the different inputs.
data = {
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
                    "9",
                    "11",
                    "4",
                    "0",
                    "0",
                    "0",
                    "0",
                    "1",
                    "0",
                    ""
                ]
            ]
        }
    },
    "GlobalParameters": {}
}

# r = requests.post(url, data=json.dumps(data), headers=headers)
# result = r.content.decode('ascii')
# result_json = json.loads(result)
# print(f"Prediction: {result_json['Results']['output1']['value']['Values'][0][136]}")


# danny flesh head of portfolio, tom zale- head of real estate
def summarize(statenum, county_num):
    for month in range(0, 12):
        for f in range(1, 6):
            if f == 0:
                f0 = 1
                f1 = 0
                f2 = 0
                f3 = 0
                f4 = 0
                f5 = 0
            elif f == 1:
                f0 = 0
                f1 = 1
                f2 = 0
                f3 = 0
                f4 = 0
                f5 = 0
            elif f == 2:
                f0 = 0
                f1 = 0
                f2 = 1
                f3 = 0
                f4 = 0
                f5 = 0
            elif f == 3:
                f0 = 0
                f1 = 0
                f2 = 0
                f3 = 1
                f4 = 0
                f5 = 0
            elif f == 4:
                f0 = 0
                f1 = 0
                f2 = 0
                f3 = 0
                f4 = 1
                f5 = 0
            else:
                f0 = 0
                f1 = 0
                f2 = 0
                f3 = 0
                f4 = 0
                f5 = 1

            values = []
            values.append(f"{statenum}")
            values.append(f"{county_num}")
            values.append(f"{month}")

            values.append(f"{f0}")
            values.append(f"{f1}")
            values.append(f"{f2}")
            values.append(f"{f3}")
            values.append(f"{f4}")
            values.append(f"{f5}")
            values.append("")

            # d1 = data.format(values[0],values[1],values[2], values[3], values[4], values[5], values[6], values[7],values[8], values[9] )

            data['Inputs']['input1']['Values'] = [
                [values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8],
                 values[9]]]

            r = requests.post(url, data=json.dumps(data), headers=headers)
            result = r.content.decode('ascii')
            result_json = json.loads(result)
            predicton = result_json['Results']['output1']['value']['Values'][0][136]
            output = f"State: {statenum}, County: {county_num}, Month: {month}: F: {f} = Prediction: {result_json['Results']['output1']['value']['Values'][0][136]}"
            print(output)

if __name__ == '__main__':
    summarize(12, 95)