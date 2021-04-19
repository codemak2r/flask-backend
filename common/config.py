# coding: utf-8 
import os.path
import yaml

class Config:
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def load(filename):
        with open(os.path.join("config",filename + ".yaml"), "rb") as f:
            config_str = f.read()
        config_str = yaml.load(config_str, Loader=yaml.FullLoader)

        return config_str