import requests
import uuid
import asyncio


class RestAPI(object):
    def __init__(self, url):
        self.url = url

    def create_task(self, payload):
        return requests.put(self.url + "/create-task", json=payload)

    def update_task(self, payload):
        return requests.put(self.url + "/update-task", json=payload)

    def delete_task(self, task_id):
        return requests.delete(self.url + f"/delete-task/{task_id}")

    def get_task(self, task_id):
        return requests.get(self.url + f"/get-task/{task_id}")

    def list_task(self, user_id):
        return requests.get(self.url + f"/list-tasks/{user_id}")

    def new_task_payload(self):
        user_id = f"test_user_{uuid.uuid4().hex}"
        content = f"test_content_{uuid.uuid4().hex}"
        return {
            "content": content,
            "user_id": user_id,
            "is_done": False
        }

    def get_data(self, run_num):
        r = requests.get(self.url)
        print(f"call # {run_num}")
        print(r.status_code)

    async def fetch(self, s, url):
        async with s.get(self.url, url) as r:
            if r.status_code != 200:
                r.raise_for_status()
            return await r.text()

    async def fetch_all(self, s, urls):
        tasks = []
        for url in urls:
            task = asyncio.create_task(self.fetch(s, url))
            tasks.append(task)
        res = await asyncio.gather(*tasks)
        return res
