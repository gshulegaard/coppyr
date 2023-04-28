# -*- coding: utf-8 -*-
import abc
from typing import Dict

from coppyr.collections import DotDict
from coppyr.error import CoppyrError


# errors


class CoppyrConfigIOError(CoppyrError):
    description = "Error opening the config file."


class CoppyrConfigYAMLError(CoppyrError):
    description = "Couldn't load YAML."


# objects


class AbstractConfig(DotDict):
    def __init__(self, file_path: str=None):
        """
        :param file_path: String
            Path to the YAML file to load.  This can be absolute or relative.
        """
        if file_path is None:
            raise CoppyrConfigIOError(
                "File path not specified."
            )

        self.__file_path__ = file_path

        # Load KV arguments into DotDict
        super().__init__(**self.load(file_path))

    @abc.abstractstaticmethod
    def load(file_path: str) -> Dict:
        return {}


class YAMLConfig(AbstractConfig):
    @staticmethod
    def load(file_path: str):
        import yaml

        try:
            with open(file_path, "r") as f:
                raw = yaml.load(f, Loader=yaml.CLoader)
        except IOError as e:
            raise CoppyrConfigIOError(
                f"Failed to load file path \"{file_path}\".",
                caught=e
            )
        except Exception as e:
            raise CoppyrConfigYAMLError(caught=e)

        return raw


class TOMLConfig(AbstractConfig):
    @staticmethod
    def load(file_path: str):
        import toml

        try:
            raw = toml.load(file_path)
        except IOError as e:
            raise CoppyrConfigIOError(
                f"Failed to load file path \"{file_path}\".",
                caught=e
            )
        except Exception as e:
            raise CoppyrConfigYAMLError(caught=e)

        return raw


# TODO: Add an environment lookup for the configuration bit.
