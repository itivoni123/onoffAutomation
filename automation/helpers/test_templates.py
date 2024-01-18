import pytest


@pytest.mark.usefixtures("init_driver")
class TestCaseSeleniumGrid(object):
    pass


@pytest.mark.usefixtures("browser")
class TestCaseSelenium(object):
    pass

    def teardown_method(self):
        pass
