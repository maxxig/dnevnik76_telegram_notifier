# -*- coding: utf-8 -*-
import json, os.path
import config.config_yaml

from datetime import datetime

def mark_changed_score_list(old_data, new_data):
    '''Marked class if scores changed or class added'''
    for item in new_data:
        if item in old_data:
            if old_data[item] != new_data[item]:
                new_data[item] += ' :bangbang:'
        else:
            new_data[item] += ' :bangbang:'
    return new_data

def get_previous_version(filename):
    if config.config_yaml.config_global['path_for_files'] is not None and len(config.config_yaml.config_global['path_for_files']) > 3:
        filename = config.config_yaml.config_global['path_for_files'] + '/' + filename
    data = {}
    if os.path.exists(filename):
        with open(filename,'r', encoding='utf-8') as file:
            data = json.load(file)
    return data

def save_new_version (new_data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(new_data, file, ensure_ascii=False)

def can_start(hours):
    hours_now = datetime.now().hour
    split_hours = [h.rstrip().lstrip() for h in hours.split(',')]
    for item in split_hours:
        item_split = item.split('-')
        if int(item_split[0]) <= hours_now and int(item_split[1]) >= hours_now:
            return True
    return False