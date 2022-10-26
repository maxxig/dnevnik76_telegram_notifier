import yaml
def init():
    global config_global
    with open('config/config.yaml') as f:
        config_global = yaml.safe_load(f)