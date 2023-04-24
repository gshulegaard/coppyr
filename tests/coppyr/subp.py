# -*- coding: utf-8 -*-
import os

from coppyr.subp import call, CoppyrSubpError
from coppyr.testing import expect_exception

from tests.base import BaseTestCase, log


here = os.path.abspath(os.path.dirname(__file__))


class SubpTestCase(BaseTestCase):
    def test_subp_basic(self):
        # check a basic successful case
        retcode, out, err = call(f"ls {here}")
        assert retcode == 0
        for fname in ("__init__.py", "subp.py", "lazyproperty.py"):
            assert fname in out
        assert err == [""]

        # test successful case passing log object
        retcode, out, err = call(f"ls {here}", log=log)
        assert retcode == 0
        for fname in ("__init__.py", "subp.py", "lazyproperty.py"):
            assert fname in out
        assert err == [""]
        # since we are a little abstracted away from where the log file is, we
        # are just checking to make sure an exception isn't raised.
        # TODO: Actually check the log file for the log record.

        # check a non-existent directory
        with expect_exception(CoppyrSubpError):
            call(f"ls /foobar/baz")

        # check a non-existent directory without check specified
        retcode, out, err = call(f"ls /foobar/baz", check=False)
        assert retcode == 2
        assert out == [""]
        assert err == [
            "ls: cannot access '/foobar/baz': No such file or directory", ""
        ]
