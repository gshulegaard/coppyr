# -*- coding: utf-8 -*-
from coppyr.types import lazyproperty

from tests.base import BaseTestCase


class TestClass(object):
    foo = "bar"

    @lazyproperty
    def myprop(self):
        return self.foo


class TestClassWithout(object):
    foo = "bar"

    @property
    def myprop(self):
        return self.foo


class LazyPropertyTestCase(BaseTestCase):
    def setup_method(self, method):
        super().setup_method(method)
        self.test_cls = TestClass
        self.test_cls_without = TestClassWithout

    def test_lazyproperty(self):
        # initialize the object
        obj = self.test_cls()

        # retrieve the property, it should now be cached.
        assert obj.myprop == "bar"

        # change the cls variable
        obj.foo = "baz"
        assert obj.foo == "baz"

        # make sure test property returns the previously retrieved value
        assert obj.myprop == "bar"

        # now check this on a class definition without lazy property
        obj = self.test_cls_without()

        assert obj.myprop == "bar"

        obj.foo = "baz"
        assert obj.foo == "baz"

        assert obj.myprop == "baz"  # changed since it isn't lazy
