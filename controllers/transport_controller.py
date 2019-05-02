import json

import requests
from config import TRANSPORT_ADDRESS


def __get_city_by_name(name):
    request_city_by_id = requests.post("".join([TRANSPORT_ADDRESS, "/api/cityitem"]),
                                       json={"Name": name}).content
    request_city_by_id = json.loads(request_city_by_id).replace('\'', '"')
    city_id = json.loads(request_city_by_id)[0]['cityId']
    return city_id


def __get_city_by_id(id):
    request_city_by_id = requests.get("".join([TRANSPORT_ADDRESS, "/api/cities/", id])).content
    request_city_by_id = json.loads(request_city_by_id).replace('\'', '"')
    city_name = json.loads(request_city_by_id)["CityName"]
    return city_name
