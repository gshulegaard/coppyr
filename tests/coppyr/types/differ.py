# -*- coding: utf-8 -*-
from dataclasses import dataclass, field

from tests.base import BaseTestCase

from coppyr import types

@dataclass
class Animal:
    species: str
    voice: str
    tags: list[str] = field(default_factory=list)


class GetAttrsTestCase(BaseTestCase):
    def test_basic(self):
        dog = Animal("dog", "woof")
        assert types.getattrs(dog) == ["species", "voice", "tags"]


class DiffTestCase(BaseTestCase):
    def test_basic(self):
        dog = Animal("dog", "woof", ["foo", "bar"])
        cat = Animal("cat", "meow", ["foo", "fib", "bar", "baz"])
        diff = types.diff(dog, cat)
        assert diff == {
            "species": ("dog", "cat"),
            "voice": ("woof", "meow"),
            "tags": (["foo", "bar"], ["foo", "fib", "bar", "baz"])
        }

    def test_invert(self):
        dog = Animal("dog", "woof", ["foo", "bar"])
        cat = Animal("cat", "meow", ["foo", "fib", "bar", "baz"])
        assert types.diff(dog, cat) == types.diff(cat, dog, invert=True)

    def test_equivalent(self):
        dog = Animal("dog", "woof", ["foo", "bar"])
        assert types.diff(dog, dog) == {}
