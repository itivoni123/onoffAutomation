import requests


class RestAPI(object):
    def __init__(self, url):
        self.url = url

    def create_task(self, payload):
        return requests.put(self.url + "/create-task", json=payload)

    def update_task(self, payload):
        return requests.put(self.url + "/update-task", json=payload)

    def get_task(self, task_id):
        return requests.get(self.url + f"/get-task/{task_id}")

    def new_task_payload(self):
        return {
            "content": "my test content",
            "user_id": "test user",
            "is_done": False
        }
