import json
import requests

class MatrixManager:
	def __init__(self):
		self.api_url = "http://localhost:3001"


	def get_tile(self, dic):
		# Tested, working
		get_tile_url = self.api_url + "/get-tile?x=" + str(dic["x"]) + "&y=" + str(dic["y"])
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


	def set_tile(self, dic):
		# Tested, working
		set_tile_url = self.api_url + "/set-tile"
		response = requests.post(set_tile_url, data=dic)
		data = response.json()

		return data
