import json
current_lang = "en"


class Local:
    def __init__(self, file):
        self.lang_file = file

    def get(self, tag):
        with open(self.lang_file, "r", encoding="UTF-8") as file:
            return json.load(file)[tag]
