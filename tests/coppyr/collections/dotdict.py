# -*- coding: utf-8 -*-
from tests.base import BaseTestCase

from coppyr.config import DotDict


class DotDictTestCase(BaseTestCase):
    def setup_method(self, method):
        super().setup_method(method)
        self.raw = {
            "section_1": {
                "val1": "foo",
                "val2": "bar",
                "val3": ["foo", "bar", "baz"]
            },
            "section_2": "basic",
            "section_3": ["baz", "bar", "foo"]
        }

    def test_basic(self):
        config = DotDict(**self.raw)
        assert config is not None
        assert isinstance(config, DotDict)

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
