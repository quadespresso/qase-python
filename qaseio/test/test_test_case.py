"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qaseio
from qaseio.model.attachment import Attachment
from qaseio.model.custom_field_value import CustomFieldValue
from qaseio.model.tag_value import TagValue
from qaseio.model.test_step import TestStep
globals()['Attachment'] = Attachment
globals()['CustomFieldValue'] = CustomFieldValue
globals()['TagValue'] = TagValue
globals()['TestStep'] = TestStep
from qaseio.model.test_case import TestCase


class TestTestCase(unittest.TestCase):
    """TestCase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTestCase(self):
        """Test TestCase"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TestCase()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
