import json
import requests

class MatrixManager:
    def __init__(self, id):
        self.id = id
        self.api_url = "http://localhost:3001"


    def get_tile(self, dict):
        # Tested, working
        get_tile_url = self.api_url + "/get-tile?x=" + str(dict["x"]) + "&y=" + str(dict["y"])
        response = requests.get(get_tile_url)
        data = response.json()

        return data


    def get_queue(self):
        # Tested, working
        get_queue_url = self.api_url + "/get-queue"
        response = requests.get(get_queue_url)
        data = response.json()

        return data


    def clear_queue(self):
        # Tested, working
        clear_queue_url = self.api_url + "/clear-queue"
        response = requests.delete(clear_queue_url)
        data = response.json()

        return data


    def set_tile(self, dict):
        # Tested, working
        set_tile_url = self.api_url + "/set-tile"
        dict.update({"id": self.id})
        response = requests.post(set_tile_url, data=dict)
        data = response.json()

        return data
