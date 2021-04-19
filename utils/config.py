# coding: utf-8 
import os.path
import yaml

class Config:
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def load(env):
        with open(os.path.join("config",env + ".yaml"), "rb") as f:
            config_str = f.read()
        config_str = yaml.load(config_str)
        print(config_str)

        return config_str