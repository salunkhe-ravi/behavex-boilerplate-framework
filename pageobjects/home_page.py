
from utils.util import get_profiles_value


class HomePage():

    _search_box = "searchInput"
    _search_button = "//i[@class='sprite svg-search-icon']"

    def __init__(self):
        pass

    def navigate_to_app(self, context):
        context.driver.open(get_profiles_value(context, 'app_url'))

    def enter_text_to_search(self, context, data):
        context.driver.enter_text_by_id(self._search_box, data)

    def click_search_button(self, context):
        context.driver.click_element_by_xpath(self._search_button)
