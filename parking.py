# Description: This script fetches the parking data from the Oulu Traffic API and prints the data to the console.

from imports import *


def parking_start():
    q_address = "https://api.oulunliikenne.fi/proxy/graphql"
    query = "query GetAllCarParks {carParks {carParkId,name,lat,lon,maxCapacity,spacesAvailable}}"
    variables = {}

    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    body = {"query": query, "variables": variables}

    response = requests.post(q_address, json=body, headers=headers)
    with open("parking.json", "w") as f:
        f.write(json.dumps(response.json(), indent=4))

    value_list = []

    with open("parking.json") as f:
        data = json.load(f)
        for carPark in data["data"]["carParks"]:
            values = {
                "name": carPark["name"],
                "maxCapacity": carPark["maxCapacity"],
                "spacesAvailable": carPark["spacesAvailable"],
                "lat": carPark["lat"],
                "lon": carPark["lon"],
            }
            value_list.append(values)

    for i in value_list:
        print(
            f'{i["name"]} - Max capacity: {i["maxCapacity"]} - Spaces available: {i["spacesAvailable"]} - {i["lat"]} - {i["lon"]}'
        )


if __name__ == "__main__":
    parking_start()
