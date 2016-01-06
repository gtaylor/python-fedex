"""
Test module for the Fedex ShipService WSDL.
"""

import unittest

import sys

sys.path.insert(0, '..')
from fedex.services.availability_commitment_service import FedexAvailabilityCommitmentRequest

# Common global config object for testing.
from common import get_test_config

CONFIG_OBJ = get_test_config()


class AvailabilityCommitmentServiceTests(unittest.TestCase):
    """
    These tests verify that the shipping service WSDL is in good shape.
    """

    def test_track(self):
        # Test shipment tracking. Query for a tracking number and make sure the
        # first (and hopefully only) result matches up.

        avc_request = FedexAvailabilityCommitmentRequest(CONFIG_OBJ)

        avc_request.Origin.PostalCode = 'M5V 3A4'
        avc_request.Origin.CountryCode = 'CA'

        avc_request.Origin.PostalCode = '27577'  # 29631
        avc_request.Origin.CountryCode = 'US'

        avc_request.send_request()
        assert avc_request.response


if __name__ == "__main__":
    unittest.main()
