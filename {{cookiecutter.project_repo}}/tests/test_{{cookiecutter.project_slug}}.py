#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{ cookiecutter.project_slug }}` package."""

# To be tested with : python3 -m pytest -vs tests/test_{{ cookiecutter.project_slug }}.py

import pytest
import os
from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}

# Get useful environment variables
VAR = os.environ.get('VAR', None)


def test_class_MyClass():
    myclass_object = MyClass(param1=1, param2="abc")
    assert myclass_object.attribute == 1
    assert str(myclass_object) == "1 abc"


def test_class_MyClass_errors():
    with pytest.raises(KeyError):
        MyClass(param1=1, param2="UNKNOWN")

    with pytest.raises(TypeError):
        MyClass(param1="abc", param2="abc")

    with pytest.raises(ValueError):
        MyClass(param2="abc")
