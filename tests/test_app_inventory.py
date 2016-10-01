#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_app_inventory
----------------------------------

Tests for `app_inventory` module.
"""
import pytest

from app_inventory import app_inventory


pytest.fixture(params=[1,2])
def sample_fixture(request):
    return request.param

def test_sample(sample_fixture):
    assert sample_fixture in [1,2,3,4,5]


