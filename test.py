#
# old_data = {'Биология': '5.0, 5', 'Иностранный язык (английский)': '5.0, Н, 5, 5, 5, 5, 5', 'История': '4.0, 5, <b>3</b>, 4', 'Литература': '<b>3.6</b>, Н, Н, Н, 5, <b>3</b>, <b>3</b>, <b>3</b>, 4', 'Математика': '4.7, Н, Н, Н, Н, 5, 4, 4, 5, 4, 5, 4, 5, 5, 5, 5, 5', 'Музыка': '5.0, Н, 5, 5', 'Основы духовно нравственной культуры народов России': '4.0, 4', 'Русский язык': '4.0, 4, 4, 4, 4, 4, 4', 'Технология': '5.0, 5', 'Физическая культура': '4.7, Н, Н, 5, 4, 5'}
# new_data = {'Биология': '5.0, 5', 'География': '4.0, 4, 4, 4', 'Изобразительное искусство': '5.0, 5', 'Иностранный язык (английский)': '5.0, Н, 5, 5, 5, 5, 5, 4', 'История': '4.0, 5, <b>3</b>, 4', 'Литература': '<b>3.6</b>, Н, Н, Н, 5, <b>3</b>, <b>3</b>, <b>3</b>, 4', 'Математика': '4.7, Н, Н, Н, Н, 5, 4, 4, 5, 4, 5, 4, 5, 5, 5, 5, 5', 'Музыка': '5.0, Н, 5, 5', 'Основы духовно нравственной культуры народов России': '4.0, 4', 'Русский язык': '4.0, 4, 4, 4, 4, 4, 4', 'Технология': '5.0, 5', 'Физическая культура': '4.7, Н, Н, 5, 4, 5'}
# def mark_changed_score_list(old_data, new_data):
#     '''Marked class if scores changed or class added'''
#     for item in new_data:
#         if item in old_data:
#             if old_data[item] != new_data[item]:
#                 new_data[item] += ' :bangbang:'
#         else:
#             new_data[item] += ' :bangbang:'
#     return new_data
#
# print(mark_changed_score_list(old_data, new_data))
from datetime import datetime

test = {datetime(2022, 11, 11, 0, 0): {'Физическая культура': 'передвижение в упоре лежа на полу ', 'Русский язык': 'уч № 132 '}, datetime(2022, 11, 10, 0, 0): {'Физическая культура': 'упражнения для формирования правильной осанки ', 'Русский язык': 'уч № 128 ', 'Английский': 'Учебник: с. 37 текст читать на оценку '}, datetime(2022, 11, 9, 0, 0): {'Русский язык': 'рт '}}


d = {datetime.strftime(k, '%d.%m.%Y'): v for k,v in test.items()}
print(d)
