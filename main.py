# -*- coding: utf-8 -*-
import modules.telega as tlg
import modules.webdriver as web_driver
import modules.messages as msg
import locale, config.config as config, modules.func as func, logging
from datetime import datetime

#locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
cnfg = config.get_config()

logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)
fileHandler = logging.FileHandler(cnfg['log_file'])
fileHandler.setLevel(logging.DEBUG)
logger.addHandler(fileHandler)


#============
# timetable for Danya
logger.info(f'{datetime.now()}: Start processing.')
driver = web_driver.init_webdrv()
logger.info(f'{datetime.now()}: Exec login_to_dnevnik76()')
driver = web_driver.login_to_dnevnik76(driver, login=cnfg['class_5v_login'], password=cnfg['class_5v_password'])
logger.info(f'{datetime.now()}: Exec get_timetable()')
timetable_dict, driver = web_driver.get_timetable(driver)
driver.close()
logger.info(f'{datetime.now()}: Exec check_previous_version()')
is_new_value = func.check_previous_version(timetable_dict, f"{cnfg['class_5v_prev_version_file']}")
logger.info(f'{datetime.now()}: is_new_value = {is_new_value}')
if len(timetable_dict) > 0 and is_new_value:
    logger.info(f'{datetime.now()}: Send message to telegram')
    tlg.send(msg.timetable_message(timetable_dict),cnfg['class_5v_chat_id'], token=cnfg['TOKEN'])
logger.info(f'{datetime.now()}: End processing.')
#============
