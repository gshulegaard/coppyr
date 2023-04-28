# -*- coding: utf-8 -*-
import datetime
import os

import toml

from coppyr.collections import DotDict
from coppyr.config import YAMLConfig, TOMLConfig

from tests import here
from tests.base import BaseTestCase


class YAMLConfigTestCase(BaseTestCase):
    def setup_method(self, method):
        super().setup_method(method)
        self.fpath = os.path.join(here, "fixtures", "test_config.yaml")

    def test_yaml_basic(self):
        config = YAMLConfig(self.fpath)
        assert config is not None
        assert isinstance(config, YAMLConfig)

        assert list(config.keys()) == ["section_1", "section_2", "section_3"]
        assert list(config.items()) == [
            (k, getattr(config, k)) for k in config.keys()
        ]

        # section 1
        assert isinstance(config.section_1, DotDict)
        assert config.section_1.val1 == "foo"
        assert config.section_1.val2 == "bar"
        assert config.section_1.val3 == ["foo", "bar", "baz"]
        assert list(config.section_1.keys()) == ["val1", "val2", "val3"]
        assert list(config.section_1.items()) == [
            (k, getattr(config.section_1, k)) for k in config.section_1.keys()
        ]

        # section 2
        assert config.section_2 == "basic"

        # section 3
        assert config.section_3 == ["baz", "bar", "foo"]

        # test default None
        assert config.section_4 is None


class TOMLConfigTestCase(BaseTestCase):
    def setup_method(self, method):
        super().setup_method(method)
        self.fpath = os.path.join(here, "fixtures", "test_config.toml")

    def test_toml_basic(self):
        config = TOMLConfig(self.fpath)
        assert config is not None
        assert isinstance(config, TOMLConfig)

        assert list(config.keys()) == ["title", "owner", "database", "servers", "clients"]
        assert list(config.items()) == [
            (k, getattr(config, k)) for k in config.keys()
        ]

        # title
        assert config.title == "TOML Example"

        # owner
        assert isinstance(config.owner, DotDict)
        assert config.owner.name == "Tom Preston-Werner"
        assert config.owner.dob == datetime.datetime(
            1979, 5, 27, 7, 32, tzinfo=toml.tz.TomlTz("-08:00")
        )
