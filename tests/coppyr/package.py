import os

from tests import here
from tests.base import BaseTestCase

from coppyr import package as pkg


CONFIG_REQUIREMENTS = [
    "PyYAML==6.0"
]

DAEMON_REQUIREMENTS = [
    "python-daemon==2.3.2"
]

DEV_REQUIREMENTS = [
    "build",
    "pytest",
    "pytest-xdist",
    "semver",
    "tox",
    "twine"
]


class PackageTestCase(BaseTestCase):
    def test_parse_requirements(self):
        requirements = pkg.parse_requirements(
            os.path.join(here, "..", "requirements-dev.txt")
        )
        assert requirements == DEV_REQUIREMENTS

    def test_parse_extras(self):
        requirements = pkg.parse_extras(
            config=os.path.join(here, "..", "requirements-config.txt"),
            daemon=os.path.join(here, "..", "requirements-daemon.txt"),
            dev=os.path.join(here, "..", "requirements-dev.txt")
        )

        assert requirements == {
            "config": CONFIG_REQUIREMENTS,
            "daemon": DAEMON_REQUIREMENTS,
            "dev": DEV_REQUIREMENTS,
            "all": CONFIG_REQUIREMENTS + DAEMON_REQUIREMENTS
        }

