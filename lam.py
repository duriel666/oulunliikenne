# Description: This script is used to get the traffic data from the Oulu city's traffic API.

from imports import *


# LAM = Liikenteen Automaattinen Mittaus - Automatic Traffic Measurement


def lam_start():
    q_address: str = "https://api.oulunliikenne.fi/proxy/graphql"
    query: str = (
        "query {tmsStations {tmsStationId,name,lat,lon,collectionStatus,measuredTime,sensorValues {roadStationId,name,sensorValue,sensorUnit}}}"
    )
    variables: dict = {}

    headers: dict = {"Content-Type": "application/json", "Accept": "application/json"}

    body: dict = {"query": query, "variables": variables}

    response: Any = requests.post(q_address, json=body, headers=headers)
    with open("lam.json", "w") as f:
        f.write(json.dumps(response.json(), indent=4))

    value_list: list = []

    with open("lam.json") as f:
        data = json.load(f)
        for tmsStation in data["data"]["tmsStations"]:
            for sensorValues in tmsStation["sensorValues"]:
                values = {
                    "roadStationId": sensorValues["roadStationId"],
                    "name": sensorValues["name"],
                    "sensorValue": sensorValues["sensorValue"],
                    "lat": tmsStation["lat"],
                    "lon": tmsStation["lon"],
                }
                value_list.append(values)

    for i in value_list:
        print(f'{i["roadStationId"]} - {i["name"]} - Value: {i["sensorValue"]}')


if __name__ == "__main__":
    lam_start()
