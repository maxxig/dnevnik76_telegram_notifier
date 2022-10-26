# -*- coding: utf-8 -*-
import json, os.path
import config.config_yaml

from datetime import datetime
def check_previous_version(new_data, filename):

    old_data = {}
    if os.path.exists(filename):
        with open(filename,'r', encoding='utf-8') as file:
            old_data = json.load(file)
    if new_data != old_data:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, ensure_ascii=False)
        return True
    return False

def can_start(hours):
    hours_now = datetime.now().hour
    split_hours = [h.rstrip().lstrip() for h in hours.split(',')]
    for item in split_hours:
        item_split = item.split('-')
        if int(item_split[0]) <= hours_now and int(item_split[1]) >= hours_now:
            return True
    return False