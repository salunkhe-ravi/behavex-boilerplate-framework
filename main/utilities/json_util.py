import json


class JsonUtils():
    
    def get_value(key, json_file_path):
        json_obj = json.load(open(json_file_path))
        return json_obj[key]
