#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
from spreadsheet import Sheet
from misery import Misery

def test_publish():
    """ Test Misery's publish method.
        """
    sheet = Sheet('test-sheet', 'worksheet-name')
    misery = Misery(sheet)
    publish_value = misery.publish()
    assert publish_value == True
