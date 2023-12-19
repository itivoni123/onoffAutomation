from time import sleep
from logging import info
from datetime import datetime
from automation.configurations.shared_consts import MINUTE
from automation.helpers.common_helper import convert_variable_to, run_method_in_while, run_method_until
from automation.helpers.wrappers_helper import ElementFallback
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# region Members

DEFAULT_MAX_WAIT_TIME = 30
TIME_TO_WAIT = 1
PULL_INTERVALS = 0.1
DEFAULT_DEBUG_STATE = False
wait_msg = "[[ %s - Wait ]] for Element: %s->%s to be %s"


# endregion Members
class WaitToElement(object):
    def __init__(self, browser, time_to_wait=TIME_TO_WAIT, pull_intervals=PULL_INTERVALS):
        self.wait = WebDriverWait(browser, time_to_wait, pull_intervals)
        self.browser = browser

    def wait_until_present(self, by, elements, wait_time_secs=DEFAULT_MAX_WAIT_TIME, wait_for_attribute="",
                           debug=DEFAULT_DEBUG_STATE, check_for_visibility=True):
        elements = convert_variable_to(elements)
        starting_to_wait = datetime.now()
        if debug:
            info(wait_msg % ("STARTED", by, elements, "present"))
        while self.get_time_passed(starting_to_wait) < wait_time_secs:
            elements_status = []
            for element in elements:

                try:
                    self.wait.until(expected_conditions.presence_of_element_located((by, element)))
                    sleep(0.15)
                    if wait_for_attribute:
                        assert self.browser.find_element(by, element).get_attribute(wait_for_attribute)

                    if check_for_visibility:
                        assert self.wait_until_visible(by, element, wait_time_secs, debug)

                    elements_status.append(True)
                except (NoSuchElementException, TimeoutException, StaleElementReferenceException, AssertionError):
                    elements_status.append(False)

            if False not in elements_status:
                if debug:
                    info(wait_msg % ("FINISHED", by, elements, "present"))
                return True
        if debug:
            info("'wait_until_present' has timed out!, waited %s for: %s!!" %
                 (self.get_time_passed(starting_to_wait), elements))
        return False

    def wait_until_not_present(self, by, elements, wait_time_secs=DEFAULT_MAX_WAIT_TIME, debug=DEFAULT_DEBUG_STATE):
        elements = convert_variable_to(elements)
        starting_to_wait = datetime.now()
        while self.get_time_passed(starting_to_wait) < wait_time_secs:
            elements_status = []
            for element in elements:
                try:
                    if debug:
                        print("wait_until_not_present: ", element, "waited for:",
                              (datetime.now() - starting_to_wait).seconds)
                    self.wait.until(expected_conditions.presence_of_element_located((by, element)))
                    assert not self.browser.find_element(by, element).is_displayed()
                    sleep(0.1)
                    elements_status.append(False)
                except (TimeoutException, StaleElementReferenceException, AssertionError, NoSuchElementException):
                    elements_status.append(True)
            if False not in elements_status:
                return True
        if debug:
            info("'wait_until_not_present' has timed out!, waited %s for: %s!!" %
                 (self.get_time_passed(starting_to_wait), elements))
        return False

    def wait_until_enabled(self, by, elements, wait_time_secs=DEFAULT_MAX_WAIT_TIME, debug=DEFAULT_DEBUG_STATE,
                           check_for_visibility=True):
        elements = convert_variable_to(elements)
        starting_to_wait = datetime.now()
        while self.get_time_passed(starting_to_wait) < wait_time_secs:
            elements_status = []
            for element in elements:
                try:
                    if debug:
                        print("wait_until_enabled: ", element, "waited for:",
                              (datetime.now() - starting_to_wait).seconds)
                    assert self.wait.until(expected_conditions.element_to_be_clickable((by, element)))
                    if check_for_visibility:
                        assert self.browser.find_element(by, element).is_displayed()
                    assert "disabled" not in self.browser.find_element(by, element).get_attribute("class")
                    sleep(0.25)
                    elements_status.append(True)
                except (TimeoutException, StaleElementReferenceException, AssertionError):
                    elements_status.append(False)
            if False not in elements_status:
                return True

        if debug:
            info("'wait_until_enabled' has timed out!, waited %s for: %s!!" %
                 (self.get_time_passed(starting_to_wait), elements))
        return False

    def wait_until_not_enabled(self, by, elements, wait_time_secs=DEFAULT_MAX_WAIT_TIME, debug=DEFAULT_DEBUG_STATE):
        elements = convert_variable_to(elements)
        starting_to_wait = datetime.now()
        while self.get_time_passed(starting_to_wait) < wait_time_secs:
            elements_status = []
            for element in elements:
                try:
                    if debug:
                        print("wait_until_not_enabled: ", element, "waited for:",
                              (datetime.now() - starting_to_wait).seconds)

                    assert ("disabled" in self.browser.find_element(by, element).get_attribute("class")) or (
                        self.wait.until_not(expected_conditions.element_to_be_clickable((by, element)))) or not (
                        self.browser.find_element(by, element).is_enabled())
                    assert not self.browser.find_element(by, element).is_displayed()

                    sleep(0.25)
                    elements_status.append(True)
                except (TimeoutException, StaleElementReferenceException, AssertionError):
                    elements_status.append(False)
            if False not in elements_status:
                return True
        if debug:
            info("'wait_until_not_enabled' has timed out!, waited %s for: %s!!" %
                 (self.get_time_passed(starting_to_wait), elements))
        return False

    def wait_until_visible(self, by, element, wait_time_secs=DEFAULT_MAX_WAIT_TIME, debug=DEFAULT_DEBUG_STATE):
        starting_to_wait = datetime.now()
        if debug:
            info(wait_msg % ("STARTED", by, element, "visible"))
        while self.get_time_passed(starting_to_wait) < wait_time_secs:
            try:
                self.wait.until(expected_conditions.visibility_of_element_located((by, element)))
                if not self.browser.find_element(by, element).is_displayed():
                    self.assert_element_visibility(by, element)

                if debug:
                    info(wait_msg % ("FINISHED", by, element, "visible"))
                return True
            except (TimeoutException, StaleElementReferenceException, AssertionError):
                pass
        return False

    def switch_to_alert_window(self):
        """

        :return:
        """

        alert = self.browser.switch_to_alert()
        alert.accept()
        return True

    def is_feedback_not_exist(self, feedback_id, wait_time_secs=5):
        """

        :param wait_time_secs: default time wait
        :param feedback_id:
        """
        starting_to_wait = datetime.now()
        while (datetime.now() - starting_to_wait).seconds < wait_time_secs:
            try:
                self.wait.until(lambda browser: len(browser.find_elements_by_id(feedback_id)) == 0)
            except TimeoutException:
                pass

    @staticmethod
    def get_time_passed(from_datetime, to_datetime=None):
        return (datetime.now() - from_datetime).seconds if to_datetime is None else (
                to_datetime - from_datetime).seconds

    @ElementFallback()
    def wait_for_element_visibility(self, by, element, timeout=MINUTE, is_visible=True, check_for_visibility=True,
                                    print_logs=True, **kwargs):
        visible_text = "visible" if is_visible else "not visible"
        print_logs = kwargs.pop("print_logs", print_logs)

        if print_logs:
            info(wait_msg % ("STARTED", by, element, visible_text))
        run_method_in_while(max_wait_time=timeout,
                            method=self.is_element_visibility_equals_to, by=by, element=element,
                            element_wait_intervals=int(MINUTE / 10),
                            should_be_visible=is_visible, check_for_visibility=check_for_visibility,
                            print_logs=print_logs)
        if print_logs:
            info(wait_msg % ("FINISHED", by, element, visible_text))

    def is_element_visibility_equals_to(self, by, element, element_wait_intervals=30, should_be_visible=True,
                                        check_for_visibility=True):
        return should_be_visible == self.wait_until_present(by, element, wait_time_secs=element_wait_intervals,
                                                            check_for_visibility=check_for_visibility)

    @ElementFallback()
    def timer_wait_element(self, by, element, timeout=MINUTE, is_visible=True, check_for_visibility=True,
                           consistency_timeout=1, **kwargs):
        visible_text = "visible" if is_visible else "not visible"
        log_msg = f"[[ %s - Element Timer Wait ]] (element) {element} -> (by){by} to be {visible_text}"
        info(log_msg % "STARTED")
        kwargs.update(dict(by=by, element=element, element_wait_intervals=consistency_timeout * 2, timeout=timeout,
                           method=self.is_element_visibility_equals_to, should_be_visible=is_visible,
                           check_for_visibility=check_for_visibility, print_logs=False,
                           consistency_timeout=consistency_timeout))
        result = self.timer_wait(**kwargs)
        info(log_msg % "FINISHED")
        return result

    @ElementFallback()
    def timer_wait(self, method, timeout=MINUTE, consistency_timeout=10, **kwargs):

        old_result = run_method_until(max_wait_time=timeout, method=method, **kwargs)
        starting_to_wait = datetime.now()
        method_consistency = datetime.now()

        while self.get_time_passed(starting_to_wait) < timeout:
            curr_result = run_method_until(max_wait_time=timeout, method=method, **kwargs)
            if self.get_time_passed(method_consistency) > consistency_timeout:
                return old_result

            if curr_result != old_result:
                method_consistency = datetime.now()
                old_result = curr_result

        assert False, "Method results are not consistence"

    def assert_element_visibility(self, by, element):
        assert self.browser.find_element(by, element).value_of_css_property("visibility")
        assert self.browser.find_element(by, element).value_of_css_property("display")
        element_size = self.browser.find_element(by, element).size
        assert element_size['width'] > 0
        assert element_size['height'] > 0

    def wait_until_page_is_still(self, timeout=3):
        starting_to_wait = datetime.now()

        while self.get_time_passed(starting_to_wait) < timeout:
            self.timer_wait(self.__get_page_source, timeout=timeout, print_logs=False)

    def __get_page_source(self):
        return self.browser.page_source

    def page_has_loaded(self):
        print("Checking if {} page is loaded.".format(self.browser.current_url))
        page_state = self.browser.execute_script('return document.readyState;')
        return page_state == 'complete'
