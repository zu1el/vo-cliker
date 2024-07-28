import json
from loger import logger, logger_read


def data_load(file):
    with open(file, "r", encoding="UTF-8") as data:
        logger.info("data load sucefulled")
        return json.load(data)


def user_data_load(file, _id):
    with open(file, "r", encoding="UTF-8") as data:
        data = json.load(data)
    for user in data["users"]:
        if user["_id"] == _id:
            return user
    logger.critical("No user in data")
    return False


def data_dump(file, data):
    with open(file, "w", encoding="UTF-8") as file:
        json.dump(file, data, indent=4)


def user_data_dump(file, new_user):
    with open(file, "r") as data:
        data = json.load(data)
    list_id = 0
    ststus = False
    for user in data["users"]:
        if user["_id"] == new_user["_id"]:
            data["users"][list_id] = new_user
            with open(file, "w") as file_:
                json.dump(data, file_, indent=4)
            ststus = True
        else:
            list_id += 1
    if not ststus:
        data["users"].append(new_user)
        with open(file, "w") as file_:
            json.dump(data, file_, indent=4)
    else:
        return False
