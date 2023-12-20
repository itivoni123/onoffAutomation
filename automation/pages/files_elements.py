from enum import Enum

"""
    Order of Elements should be like this:
    1. Classes
    2. IDs
    3. CSS
    4. XPATH
"""
# region Members
CSS_STARTS_WITH_ID = "[id^='%s']"
CSS_DIV_BY_NAME = '[name="%s"]'
CSS_BUTTON_BY_TYPE = 'button[type="%s"]'


# endregion Members

class ElementsSuffix(object):
    header = "-header"
    dropdown = "-dropdown"
    select = "-select"
    checkbox = "-checkbox"
    radio = "-radio"
    input = "-input"
    search_input = "-search" + input
    search_feedback = "-search-feedback"
    search_button = "-search-button"
    search_input_icon = "-search-input-search-icon"
    search_input_delete = "-search-input-x-icon"
    search_container = "-search-container"


class ElementInfix(object):
    table = "-table"
    modal = "-modal"


class SharedElements(object):
    # region ID
    ID_SERVER_GENERIC_ID = "root"
    ID_SERVER_LOADER = "main-loader"
    ID_CLOSE_MODAL_BTN = "modal-action-complete"
    ID_POP_UP_MODAL_YES = "modal-action-yes"
    ID_POP_UP_MODAL_NO = "modal-action-no"
    ID_VOLUME_DETAILS_BACK_BTN = "settings-page-link"
    ID_TABLE_HEADER = "%s-table-header-cell-%s"
    ID_LOGGED_USER_SETTINGS = "User"
    ID_BLOCKED_COMPONENT = "block"
    ID_WE_TAB = "working-environments-tab"
    ID_LOADING = "loading"
    ID_CONTINUE_ENABLED_BTN = "continue-btn-ok2go"
    ID_CONFIGURATION_TAB = "configuration-link"
    ID_BACK_TO_DASHBOARD = "dashboard-page-link"
    # endregion ID

    # region CSS SELECTOR
    CSS_ACTIVE_MENU_IN_IFRAME_BY_ID = '[id="%s"][class$="active"]'
    CSS_ACTIVE_TAB = '[class$="active"]'
    CSS_ACTIVE_TAB_BY_ID = '[id=%s]' + CSS_ACTIVE_TAB
    CSS_VIEW_ALL_MODAL_ROW_BY_TITLE = 'div[title="%s"]'
    CSS_WE_SCAN_STATUS_LOADING = '[class="ui active loader"]'
    CSS_TOOLTIP_MSG = ".tooltip-arrow"
    CSS_NOTIFICATIONS = '[class="notifications"]'
    CSS_VIEW_ALL_ROWS_NAMES = f'[id="dashboard-bars-chart-%s"] [class="pattern-name"] > div'
    # endregion CSS SELECTOR

    # region XPATH
    XPATH_OPEN_TOP_MENU_BY_TEXT = "//div[text()='%s']/ancestor::button"
    XPATH_LINK_BY_TEXT = '//a[text()="%s"]'
    XPATH_SPAN_BY_TEXT = '//span[text()="%s"]'
    XPATH_EXPANDED_SERVICES = '//div[@id="row"]/../descendant::div[text()="%s"]'
    XPATH_SHOW_ALL_SERVICES = '//div[@id="row"]/*[contains(text(), "All Services")]'
    XPATH_SAAS_LINK = XPATH_LINK_BY_TEXT % "Lets go to Cloud Manager SaaS"
    XPATH_CUSTOM_CHECKBOX_BY_ID = "//*[@id='%s']/preceding-sibling::input"
    # endregion XPATH


class LoginElements(object):
    # region ID
    ID_LOGIN = "login"
    ID_LOGIN_BTN = "login-btn"
    # endregion ID

    # region CSS
    CSS_EMAIL_INPUT = CSS_DIV_BY_NAME % "email"
    CSS_PASSWORD_INPUT = CSS_DIV_BY_NAME % "pass"
    CSS_SUBMIT_BUTTON = CSS_BUTTON_BY_TYPE % "submit"
    # endregion CSS


class AlbumsElements(object):
    ID_ALBUMS_RELEASED_TITLE = "albums"


class FBProfileElements(object):
    # region CLASS
    IMG_COVER = "profileCoverPhoto"
    CLASS_NUM_OF_FRIENDS = "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o " \
                           "kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr " \
                           "f1sip0of lzcic4wl gpro0wi8 m9osqain lrazzd5p"
    # endregion CLASS


class TimeFrames(Enum):
    last_hour = "quick-filter-last-hour"
    last_day = "quick-filter-last-24-hours"
    last_week = "quick-filter-last-week"
    last_month = "quick-filter-last-month"
    last_year = "quick-filter-last-year"
    before = "range-date-picker-tab-before"
    after = "range-date-picker-tab-after"
    between = "range-date-picker-tab-between"


CONTEXTUAL_PATTERNS = ["Contextual - Sexual", "Contextual - Religion", "Contextual - Philosophy",
                       "Contextual - Ethnicity", "Contextual - Criminal", "Contextual - Health"]
