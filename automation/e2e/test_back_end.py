import requests


class TestBackEnd(object):

    def test_numbers(self):

        a = 1
        b = 3
        assert a + b == 4

    def test_status_code(self, url):

        res = requests.get(url)
        assert res.status_code == 200
