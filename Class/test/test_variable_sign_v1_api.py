# coding: utf-8

"""
    Digitraffic Road API

    [OpenAPI document](/swagger/openapi.json)   Digitraffic is a service operated by the [Fintraffic](https://www.fintraffic.fi) offering real time traffic information. Currently the service covers *road, marine and rail* traffic. More information can be found at the [Digitraffic website](https://www.digitraffic.fi/)   The service has a public Google-group [road.digitraffic.fi](https://groups.google.com/forum/#!forum/roaddigitrafficfi) for communication between developers, service administrators and Fintraffic. The discussion in the forum is mostly in Finnish, but you're welcome to communicate in English too.   ### General notes of the API * Many Digitraffic APIs use GeoJSON as data format. Definition of the GeoJSON format can be found at https://tools.ietf.org/html/rfc7946. * For dates and times [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format is used with \"Zulu\" zero offset from UTC unless otherwise specified (i.e., \"yyyy-mm-ddThh:mm:ss[.mmm]Z\"). E.g. 2019-11-01T06:30:00Z.

    The version of the OpenAPI document: Branch: master, tag: 2024.10.28-1 #ef5bdf3 @ 2024-10-29T08:05:03+0000
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.variable_sign_v1_api import VariableSignV1Api


class TestVariableSignV1Api(unittest.TestCase):
    """VariableSignV1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = VariableSignV1Api()

    def tearDown(self) -> None:
        pass

    def test_api_variable_sign_v1_images_text_get(self) -> None:
        """Test case for api_variable_sign_v1_images_text_get

        Generate svg-image from given text
        """
        pass

    def test_api_variable_sign_v1_signs_datex2_get(self) -> None:
        """Test case for api_variable_sign_v1_signs_datex2_get

        Return all variables signs as datex2
        """
        pass

    def test_get_code_descriptions(self) -> None:
        """Test case for get_code_descriptions

        Return all code descriptions.
        """
        pass

    def test_variable_sign_by_path(self) -> None:
        """Test case for variable_sign_by_path

        Return the latest value of a variable sign
        """
        pass

    def test_variable_sign_history(self) -> None:
        """Test case for variable_sign_history

        Return the history of variable sign data
        """
        pass

    def test_variable_signs(self) -> None:
        """Test case for variable_signs

        Return the latest data of variable signs. If deviceId is given, latest data for that sign will be returned, otherwise return the latest data for each sign from the last 7 days.
        """
        pass


if __name__ == '__main__':
    unittest.main()
