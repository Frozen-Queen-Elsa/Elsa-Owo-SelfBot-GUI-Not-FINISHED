from requests import get, post
class CAPI:
	def __init__(self, userID:str):
		self.ID = userID
		self.url = "https://autofarmsupport.tk"
	def solve(self, Json: dict) -> bool:
		Json['id'] = self.ID
		result = post(self.url, json=Json, timeout=300)
		if result.ok:
			return result.json()
		elif result.status_code == 401:
			return False

	def report(self, Json) -> None:
		Json['id'] = self.ID
		post(self.url + "/report", json=Json, timeout=120)
	def status(self):
		result = get(self.url + "/status", timeout=10)
		if result.ok:
			return True
		return False
