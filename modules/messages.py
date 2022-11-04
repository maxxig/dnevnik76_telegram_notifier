def timetable_message(timetable_dict):
    """Conver timetable to telegram text message"""
    msg = ''
    for k, item in timetable_dict.items():
        msg += '🗓 <b>' + k + '</b>'
        for k2, in_item in item.items():
            msg += '\n'
            msg += '\n📚 Предмет: ' + k2
            msg += '\n📖 ДЗ: ' + in_item
        msg += '\n\n'
    return msg

def scores_to_message(new_data, old_data, name, h3):
    """Checked scores for which class changed and mark it !!
       old_data only for this check
    """
    msg = f'{name}\n{h3}\n'
    for class_name, scores in new_data.items():
        msg += '📚 <b>' + class_name + '</b>'
        msg += f"\n📊 {scores}"
        if class_name in old_data:
            if old_data[class_name] != scores:
                msg += ' ‼️'
        else:
            msg += ' ‼️'
        msg += '\n'
    return msg