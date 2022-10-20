# -*- coding: utf-8 -*-
import json, os.path
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