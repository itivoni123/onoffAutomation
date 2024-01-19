from automation.restApi.rest_functions import RestAPI


class TestBackEnd(object):

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
        task_func = RestAPI(url)

        # region Prepare\Create a task
        payload = task_func.new_task_payload()
        create_task_id_res = task_func.create_task(payload)
        assert create_task_id_res.status_code == 200
        # endregion Create a task

        # region Action\Update the task
        task_id = create_task_id_res.json()["task"]["task_id"]
        new_payload = {
            "user_id": payload["user_id"],
            "task_id": task_id,
            "content": "my updated content",
            "is_done": True
        }
        update_task_response = task_func.update_task(new_payload)
        assert update_task_response.status_code == 200
        # endregion Action\Update the task

        # region Get and validate the changes
        get_task_response = task_func.get_task(task_id)
        get_task_data = get_task_response.json()
        assert get_task_data["content"] == new_payload["content"]
        assert get_task_data["is_done"] == new_payload["is_done"]
        # region Get and validate the changes

    def test_delete_task(self, url):

        rest = RestAPI(url)

        # region Create a task
        payload = rest.new_task_payload()
        create_task_response = rest.create_task(payload)
        assert create_task_response.status_code == 200
        task_id = create_task_response.json()["tasks"]["task_id"]
        # endregion Create a task

        # region Delete the task
        delete_task_response = rest.delete_task(task_id)
        assert delete_task_response.status_code == 200
        # endregion Delete the task

        # region Validation
        get_task_response = rest.get_task(task_id)
        assert get_task_response.status_code == 404
        # endregion Validation

    def test_list_tasks(self, url):

        rest = RestAPI(url)
        # region Create N tasks
        n = 3
        payload = rest.new_task_payload()
        for _ in range(n):
            create_task_response = rest.create_task(payload)
            assert create_task_response.status_code == 200
        # endregion Create N tasks

        # region List tasks, and check that there are N tasks
        user_id = payload["user_id"]
        list_task_response = rest.list_task(user_id)
        assert list_task_response.status_code == 200
        data = list_task_response.json()
        tasks = data["tasks"]
        assert len(tasks) == n
        # endregion List tasks, and check that there are N tasks
