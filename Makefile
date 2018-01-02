.PHONY: all test override deps publish
SHELL := /bin/bash

all: deps test

deps:
	pip install -r requirements.txt

test:
	python -m unittest discover test

override:
	./override/override.sh

publish:
	./publish.sh
