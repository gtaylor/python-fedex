"""
Test module for the Fedex AddressValidationService WSDL.
"""

import unittest

import sys

sys.path.insert(0, '..')
from fedex.services.address_validation_service import FedexAddressValidationRequest

# Common global config object for testing.
from common import get_test_config

CONFIG_OBJ = get_test_config()


class AddressValidationServiceTests(unittest.TestCase):
    """
    These tests verify that the address validation service WSDL is in good shape.
    """

    def test_avs(self):
        avs_request = FedexAddressValidationRequest(CONFIG_OBJ)

        address1 = avs_request.create_wsdl_object_of_type('AddressToValidate')
        address1.Address.StreetLines = ['155 Old Greenville Hwy', 'Suite 103']
        address1.Address.City = 'Clemson'
        address1.Address.StateOrProvinceCode = 'SC'
        address1.Address.PostalCode = 29631
        address1.Address.CountryCode = 'US'
        address1.Address.Residential = False
        avs_request.add_address(address1)

        avs_request.send_request()

        assert avs_request.response


if __name__ == "__main__":
    unittest.main()
