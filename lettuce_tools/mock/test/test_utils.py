# -*- coding: utf-8 -*-
from lettuce import world
import json
import os


class TestUtils(object):

    def initialize(self):
        """
        Parse the JSON configuration file located in the execution folder and
        store the resulting dictionary in the world.
        """
        with open("mock/test/properties.json") as config_file:
            world.config = json.load(config_file)

        """
        Make sure the logs path exists and create it otherwise.
        """
        if not os.path.exists(world.config["environment"]["logs_path"]):
            os.makedirs(world.config["environment"]["logs_path"])

