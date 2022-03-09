"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import qaseio
from qaseio.api.plans_api import PlansApi  # noqa: E501


class TestPlansApi(unittest.TestCase):
    """PlansApi unit test stubs"""

    def setUp(self):
        self.api = PlansApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_plan(self):
        """Test case for create_plan

        Create a new plan.  # noqa: E501
        """
        pass

    def test_delete_plan(self):
        """Test case for delete_plan

        Delete plan.  # noqa: E501
        """
        pass

    def test_get_plan(self):
        """Test case for get_plan

        Get a specific plan.  # noqa: E501
        """
        pass

    def test_get_plans(self):
        """Test case for get_plans

        Get all plans.  # noqa: E501
        """
        pass

    def test_update_plan(self):
        """Test case for update_plan

        Update plan.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
