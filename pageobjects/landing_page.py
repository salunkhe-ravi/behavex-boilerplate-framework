

class LandingPage():

    _display_name = "(//td[@class='infobox-data nickname'])[1]"
    _header_name = "//h1[@id='firstHeading']"

    def __init__(self):
        pass

    def verify_display_name(self, context, expected_data):
        display_name = context.driver.get_text_by_xpath(self._display_name)
        context.driver.verify_text_equals(
            display_name, expected_data)

    def verify_header_name(self, context, expected_data):
        display_name = context.driver.get_text_by_xpath(self._header_name)
        context.driver.verify_text_equals(display_name, expected_data)
