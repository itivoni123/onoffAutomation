import pytest


@pytest.mark.usefixtures("init_driver")
class TestCaseCC(object):
    pass

    def teardown_method(self):
        pass
