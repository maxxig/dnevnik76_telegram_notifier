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

def scores_to_message(scores_array, name, h3):
    msg = f'{name}\n{h3}\n'
    for sc in scores_array:
        msg += '📚 <b>' + sc.split(':')[0] + '</b>'
        msg += f"\n📊 {sc.split(':')[1].lstrip()}"
        msg += '\n'
    return msg