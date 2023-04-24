# -*- coding: utf-8 -*-
import os
import time

from coppyr import Context

from tests.base import BaseTestCase


class ContextTestCase(BaseTestCase):
    def test_basic(self):
        context = Context()

        # check variables
        assert context.app_name == "piston"
        assert context.pid is not None
        assert context.ids is not None
        assert context.action_id == f"{context.pid}_100003"
        assert context.action_stamp is not None
        assert context.logging_keys == [
            "action_id",
            "action_duration",
            "action_duration_str"
        ]
        assert context.cwd == os.getcwd()
        assert context.action_duration is not None
        assert context.action_duration_str is not None
        assert isinstance(context.action_duration_str, str)

        # test increment action id
        time.sleep(1)  # sleep so action_duration is non-zero

        prev_id = context.action_id
        prev_stamp = context.action_stamp
        prev_duration = context.action_duration
        prev_duration_str = context.action_duration_str

        context.inc_action_id()

        assert context.action_id != prev_id
        assert context.action_stamp != prev_stamp
        assert context.action_duration != prev_duration
        assert context.action_duration_str != prev_duration_str

        # test Singleton behavior
        context2 = Context()
        assert context is context2
        assert id(context) == id(context2)
