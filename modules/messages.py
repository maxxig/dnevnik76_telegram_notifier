def timetable_message(timetable_dict):
    msg = ''
    for k, item in timetable_dict.items():
        msg += '🗓 <b>' + k + '</b>'
        for k2, in_item in item.items():
            msg += '\n'
            msg += '\n📚 Предмет: ' + k2
            msg += '\n📖 ДЗ: ' + in_item
        msg += '\n\n'
    return msg