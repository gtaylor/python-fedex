"""
Test module for the Fedex PackageMovementInformationService WSDL.
"""

import unittest

import sys
sys.path.insert(0, '..')
from fedex.services.package_movement import PostalCodeInquiryRequest

# Common global config object for testing.
from common import get_test_config
CONFIG_OBJ = get_test_config()


class PackageMovementServiceTests(unittest.TestCase):
    """
    These tests verify that the package movement service WSDL is in good shape.
    """
    def test_postal_inquiry(self):

        inquiry = PostalCodeInquiryRequest(CONFIG_OBJ)
        inquiry.PostalCode = '29631'
        inquiry.CountryCode = 'US'

        inquiry.send_request()

        assert inquiry.response
        assert inquiry.response.HighestSeverity == 'SUCCESS'



if __name__ == "__main__":

    unittest.main()
