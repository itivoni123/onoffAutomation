import requests
from automation.restApi.rest_functions import RestAPI


class TestBackEnd(RestAPI):

    def test_numbers(self):

        a = 1
        b = 3
        assert a + b == 4

    def test_status_code(self, url):

        res = requests.get(url)
        assert res.status_code == 200

    def test_create_task(self, url):

        payload = self.new_task_payload()
        create_task_id_res = self.create_task(payload)
        assert create_task_id_res.status_code == 200
        data = create_task_id_res.json()

        task_id = data["task"]["task_id"]
        get_task_id_res = self.get_task(task_id)
        assert get_task_id_res.status_code == 200
        get_task_data = get_task_id_res.json()

        assert get_task_data["content"] == payload["content"]
        assert get_task_data["user_id"] == payload["user_id"]

    def test_update_task(self, url):

        #Create a task
        payload = self.new_task_payload()
        create_task_id_res = self.create_task(payload, url)
        assert create_task_id_res.status_code == 200
        task_id = create_task_id_res.json()["task"]["task_id"]
        #Update the task
        new_payload = {
            "user_id": payload["user_id"],
            "task_id": task_id,
            "content": "my updated content",
            "is_done": True
        }
        update_task_response = self.update_task(new_payload, url)
        assert update_task_response.status_code == 200
        #Get and validate the changes
        get_task_response = self.get_task(task_id, url)
        get_task_data = get_task_response.json()
        print(get_task_data)
        assert get_task_data["content"] == new_payload["content"]
        assert get_task_data["is_done"] == new_payload["is_done"]
