import json


def get_profiles_value(context, key):
    """Retrieve value from resources/profiles.json

    Args:
        key ([type]): Provide the key to retrieve the value of
    """
    j = json.load(open('./resources/profiles.json'))
    return j[context.config.userdata['profile']][key]
