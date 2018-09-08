import json
import requests

class MatrixManager:
	def __init__(self):
		self.api_url = "http://localhost:3001"


    def get_tile(self, x, y):
        response = requests.get(f"{self.api_url}/get-tile?x={x}&y={y}")
        data = response.json()

		return data


    def get_queue(self):
        response = requests.get(f"{self.api_url}/get-queue")
        data = response.json()

		return data


    def clear_queue(self):
        response = requests.delete(f"{self.api_url}/clear-queue")
        data = response.json()

		return data


    def set_tile(self, x, y, c):
        dic = {"x": x, "y": y, "c": c, "id": self.id}
        response = requests.post(f"{self.api_url}/set-tile", data=dic)
        data = response.json()

		return data
