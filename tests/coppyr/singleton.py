# -*- coding: utf-8 -*-
from coppyr.singleton import Singleton, Namespace

from tests.base import BaseTestCase


class SingletonTestCase(BaseTestCase):
    def test_init(self):
        single = Singleton()
        single2 = Singleton()
        assert single is single2
        assert id(single) == id(single2)


class NamespaceTestCase(BaseTestCase):
    def teardown_method(self, method):
        # reset class Namespace attributes
        Namespace._instance = None
        Namespace._init = True

        super().teardown_method(method)

    def test_init(self):
        ns = Namespace()
        ns2 = Namespace()
        assert ns is ns2
        assert id(ns) == id(ns2)

    def test_basic(self):
        ns = Namespace()

        # get None
        assert ns.key1 is None

        # set key
        ns.key1 = "foo"
        assert ns.key1 == "foo"

        # same key access
        ns2 = Namespace()
        assert ns2.key1 == "foo"
