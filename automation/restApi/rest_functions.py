import requests


class RestAPI(object):
    def create_task(self, payload, url):
        return requests.put(url + "/create-task", json=payload)

    def update_task(self, payload, url):
        return requests.put(url + "/update-task", json=payload)

    def get_task(self, task_id, url):
        return requests.get(url + f"/get-task/{task_id}")

    def new_task_payload(self):
        return {
            "content": "my test content",
            "user_id": "test user",
            "is_done": False
        }
