# -*- coding: utf-8 -*-
import modules.telega as tlg
import modules.webdriver as web_driver
import modules.messages as msg
import modules.func as func, logging
import config.config_yaml
from datetime import datetime

config.config_yaml.init()
cnfg = config.config_yaml.config_global

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

            logger.info(f'{datetime.now()}: Exec check_previous_version()')
            # is_new_value = func.check_previous_version(timetable_dict, f"{info_item['prev_version_file_name']}")
            old_data = func.get_previous_version(f"{info_item['prev_version_file_name']}")

            is_new_value = True if old_data != timetable_dict else False

            if is_new_value:
                func.save_new_version(new_data=timetable_dict, filename = f"{info_item['prev_version_file_name']}")

            logger.info(f'{datetime.now()}: is_new_value = {is_new_value}')

            if len(timetable_dict) > 0 and is_new_value:
                logger.info(f'{datetime.now()}: Send message to telegram')
                tlg.send(msg.timetable_message(timetable_dict),info_item['chat_id'], token=cnfg['TOKEN'])

            if info_item['check_scores'] == True:
                logger.info(f'{datetime.now()}: check_scores = true')
                scores_dict, h3 = web_driver.get_scores_for_user(driver, selector = info_item['period_filter_selector'])
                del old_data
                old_data = func.get_previous_version(f"scores_for_{info_item['name']}.json")

                # is_new_value = func.check_previous_version(scores_array, f"scores_for_{info_item['name']}.json")
                is_new_value = True if old_data != scores_dict else False

                logger.info(f'{datetime.now()}: check_scores = true, is_new_value = {is_new_value}')
                if is_new_value:
                    func.save_new_version(new_data=scores_dict, filename=f"scores_for_{info_item['name']}.json")
                    message_for_parents = msg.scores_to_message(scores_dict, old_data, info_item['name'], h3)
                    for parent in str(info_item['personal_chats_id']).split(','):
                        try:
                            tlg.send(message_for_parents, parent, token=cnfg['TOKEN'])
                        except Exception as e:
                            logger.critical(e, exc_info=True)
            driver.close()
        logger.info(f'{datetime.now()}: End processing {user_code}.')
except BaseException as e:
    logger.critical(e, exc_info=True)
    tlg.send(e.args[0], cnfg['admin_chai_id'], token=cnfg['TOKEN'])
    print(e)

