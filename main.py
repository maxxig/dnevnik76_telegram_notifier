# -*- coding: utf-8 -*-
import modules.telega as tlg
import modules.webdriver as web_driver
import modules.messages as msg
import modules.func as func, logging
import config.config_yaml as config
from datetime import datetime

cnfg = config.get_config()

logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)
fileHandler = logging.FileHandler(cnfg['log_path'])
fileHandler.setLevel(logging.DEBUG)
logger.addHandler(fileHandler)

users = {key: item for key, item in cnfg['users'].items() if item['active'] == True}
try:
    for user_code, info_item in users.items():
        logger.info(f'{datetime.now()}: Start processing for user {user_code}')
        can_start = func.can_start(info_item['hours'])
        logger.info(f'{datetime.now()}: can_start = {can_start}')
        if can_start:
            driver = web_driver.init_webdrv()
            logger.info(f'{datetime.now()}: Exec login_to_dnevnik76()')
            driver = web_driver.login_to_dnevnik76(driver, login=info_item['login'], password=info_item['password']
                                                   , region=info_item['region'], school=info_item['school'])
            logger.info(f'{datetime.now()}: Exec get_timetable()')
            timetable_dict, driver = web_driver.get_timetable(driver)
            driver.close()
            logger.info(f'{datetime.now()}: Exec check_previous_version()')
            is_new_value = func.check_previous_version(timetable_dict, f"{info_item['prev_version_file_name']}")
            logger.info(f'{datetime.now()}: is_new_value = {is_new_value}')
            if len(timetable_dict) > 0 and is_new_value:
                logger.info(f'{datetime.now()}: Send message to telegram')
                tlg.send(msg.timetable_message(timetable_dict),info_item['chat_id'], token=cnfg['TOKEN'])
        logger.info(f'{datetime.now()}: End processing {user_code}.')
except BaseException as e:
    logger.critical(e, exc_info=True)
    #tlg.send('Что то со мной не так!', cnfg['admin_chai_id'], token=cnfg['TOKEN'])
    tlg.send(e.args[0], cnfg['admin_chai_id'], token=cnfg['TOKEN'])

