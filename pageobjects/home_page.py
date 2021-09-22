
from utils.util import get_profiles_value


class HomePageObject():

    def navigate_to_app(context):
        context.wrapper.open(get_profiles_value(context, 'app_url'))
