.PHONY: help venv clean docker-rm docker-build docker test test-rebuild test-env build upload

TESTS = "tests/"
N = 1

help:
	@echo "Please use \"make <target>\" where <target> is one of:"
	@echo "  clean               to remove build artifacts."
	@echo "  test                to run tests with every python interpreter"
	@echo "                      available."
	@echo "  test-rebuild        remove and recreate all tox virtual"
	@echo "                      environments."
	@echo "  ENV=\"\$$env\" test-env to run tests with a single interpreter"
	@echo "                      where \$$env is one of: py36, py37"
	@echo ""
	@echo "All test recipes can specify a subset of tests using the "
	@echo "\"TESTS\" macro with a py.test target form.  E.G:"
	@echo ""
	@echo "  \$$ make TESTS=\"tests/<file>.py[::test]\" test"
	@echo ""
	@echo "Additionally, you can parallelize tests with pytest-xdist using"
	@echo "the \"N\" macro.  E.G:"
	@echo ""
	@echo "  \$$ make N=4 test"
	@echo ""

venv:
	@rm -rf venv
	@python3 -m venv venv/coppyr

clean:
	@rm -rf dist/*
	@rm -rf build/*
	@find . -path '*/.*' -prune -o -name '__pycache__' -exec rm -fr {} +
	@find . -path '*/.*' -prune -o -name '*.egg-info' -exec rm -fr {} +
	@find . -path '*/.*' -prune -o -name '*.py[co]' -exec rm -fr {} +
	@find . -path '*/.*' -prune -o -name '*.build' -exec rm -fr {} +
	@find . -path '*/.*' -prune -o -name '*.so' -exec rm -fr {} +
	@find . -path '*/.*' -prune -o -name '*.c' -exec rm -fr {} +
	@find . -path '*/.*' -prune -o -name '*~' -exec rm -fr {} +

docker-rm:
	@cd docker && docker-compose -f dev.compose.yaml rm -s -v -f;

docker-build: docker-rm
	@cd docker && docker-compose -f dev.compose.yaml build --no-cache;

docker:
	@cd docker && docker-compose -f dev.compose.yaml run coppyr-dev;

test: clean
	python3 -m tox --skip-missing-interpreters -- ${TESTS} -n ${N}
	@make clean

test-rebuild: clean
	rm -rf .tox
	python3 -m tox --skip-missing-interpreters --recreate --notest
	@make clean

test-env: clean
	python3 -m tox -e ${ENV} -- ${TESTS} -n ${N}

build: clean
	@python3 -m build

upload: build
	@twine upload dist/*
