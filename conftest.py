from datetime import datetime
from os import path, environ, makedirs
import pytest
from selenium.common.exceptions import TimeoutException, WebDriverException
from seleniumwire import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', dest='browser', action='store', default='chrome')
    parser.addoption('--user', dest='user', action='store', default='')
    parser.addoption('--password', dest='password', action='store', default='')
    parser.addoption('--login_page', dest='login_page', action='store', default='https://facebook.com')
    parser.addoption('--url', dest='url', action='store', default="https://reqres.in")
    parser.addoption('--wiki_url', dest='wiki_url', action='store', default="https://en.wikipedia.org/wiki/")
    parser.addoption('--file_path', dest='file_path', action='store',
                     default="/Users/itaytivony/Desktop/Duality/page_source.html")


@pytest.fixture
def browser(request):
    # browser_type = request.config.getoption('browser')
    driver = webdriver.Chrome()
    return driver


@pytest.fixture
def url(request):
    url = request.config.getoption('url')
    return url


@pytest.fixture
def wiki_url(request):
    url = request.config.getoption('wiki_url')
    return url

@pytest.fixture
def file_path(request):
    url = request.config.getoption('file_path')
    return url


@pytest.fixture
def user(request):
    user_name = request.config.getoption('user')
    return user_name


@pytest.fixture
def password(request):
    password = request.config.getoption('password')
    return password


@pytest.fixture
def login_page(request):
    login_page = request.config.getoption('login_page')
    return login_page


@pytest.fixture
def mark_type(request):
    mark_type = request.config.getoption('mark_type')
    return mark_type


def _get_marker_details(item, marker):
    for marker_found in item.iter_markers(marker):
        return [arg for arg in marker_found.args]


def get_random_storage():
    return environ.get("RANDOM_STORAGE")


def check_for_parametrize(item):
    format_params_marker = _get_marker(item, 'params_format')
    if not format_params_marker:
        return


def _get_marker(item, marker):
    return item.keywords._markers.get(marker, False)


def check_to_exclude_we(item):
    # storage_name = get_random_storage()
    # storage_details = get_we_details(storage_name)
    exclude_marker = _get_marker_details(item, 'not_run')
    test_name = item.originalname or item.name
    print(test_name, exclude_marker, "yofi")

    # if exclude_marker is None or not storage_details:
    #     return

    # exclude_marker = exclude_marker[0].split(",")
    # if storage_name in exclude_marker:
    #     other_available_we = get_other_available_we(exclude_marker)

        # if not other_available_we:
    #TODO - handle this line
    # if exclude_marker in "not_run":
    #     item.add_marker(pytest.mark.skip(reason="%s Are excluded from running on this test" % exclude_marker))
    #         return True
    #     storage_name = random.choice(other_available_we)
    #
    # environ[f"{test_name}_specific_we"] = storage_name


# def check_run_only_provider(item):
#     running_provider = Provider.get()
#     is_test_mark_aws = _get_marker_details(item, Provider.FaceBook)
#     is_test_mark_azure = _get_marker_details(item, Provider.Azure)
#     expected_provider = []
#     if is_test_mark_aws is not None:
#         expected_provider.append(Provider.AWS)
#     if is_test_mark_azure is not None:
#         expected_provider.append(Provider.Azure)
#
#     if not expected_provider:
#         return
#     if running_provider not in expected_provider:
#         item.add_marker(pytest.mark.skip(reason=f"Test Should not run on the "
#                                                 f"current Provider(current: {running_provider}) | "
#                                                 f"expected Provider: {expected_provider}"))


def get_screenshots_folder():
    screenshots_dir = "/screenshots"
    screenshots_dir = screenshots_dir if path.exists(screenshots_dir) else "/tmp" + screenshots_dir
    screenshots_dir += "/" + environ.get("BUILD_NUMBER", "0")
    return screenshots_dir


#TODO: delete from S3 bucket
# def delete_old_screenshots_s3():
#     pass
    # screenshots = get_objects_in_s3_path(TEST_BUCKET, "builds_screenshots")
    # old_screenshots = [{"Key": old_file['Key']} for old_file in screenshots
    #                    if (datetime.now().date() - old_file['LastModified'].date()).days > 7]
    # delete_files_from_s3(TEST_BUCKET, old_screenshots)


# def send_msg_to_slack(screenshots_path):
#     """
#     Send a message to #automation_alerts channel
#     """
#     steps_results = {}
#     build_number = environ.get("BUILD_NUMBER", "0")
#     build_name, build_data = get_steps_data_by_build_num(build_number)
#     if isinstance(build_data, str):
#         steps_results = build_data
#     else:
#         for url in build_data:
#             step_result = get_step_status(url['url'])
#             if step_result:
#                 steps_results.update(step_result)
#     if steps_results:
#         steps_results = minimize_log(steps_results)
#         msg = {
#             "blocks": [{
#                 "type": "section",
#                 "text": {
#                     "type": "mrkdwn",
#                     "text": "<%s|Failures on Build: `%s`  `#%s`>\nFailures in the following steps: %s" % (
#                         (build_url % build_number), build_name, build_number, steps_results)}
#             }]}
#         if build_number != "0":
#             post_api(slack_url, json=msg)


# def pytest_sessionfinish(session, exitstatus):
#     """ whole test run finishes. """
#
#     screenshots_path = get_screenshots_folder()
#
#     try:
#         if 'test_check_build_status' in str(session.items):
#             send_msg_to_slack(screenshots_path)
#     except AttributeError:
#         pass
#     # delete_old_screenshots_s3()


def pytest_collection_modifyitems(session, config, items):
    # cleanup_dp_volumes(config.getoption("second_we"))
    # on_prem = var_to_bool(config.getoption("on_prem"))

    for item in items:
        # if on_prem and item.get_closest_marker("NotForOnPrem") is not None:
        #     item.add_marker(pytest.mark.skip(reason="Test cannot run on OnPrem"))
        #     continue
        #check_run_only_provider(item)
        check_to_exclude_we(item)
        # check_run_only_for_we(item)

        if _get_marker(item, 'parametrize'):
            check_for_parametrize(item)
