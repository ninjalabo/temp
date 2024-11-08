# coding: utf-8

"""
    Digitraffic Road API

    [OpenAPI document](/swagger/openapi.json)   Digitraffic is a service operated by the [Fintraffic](https://www.fintraffic.fi) offering real time traffic information. Currently the service covers *road, marine and rail* traffic. More information can be found at the [Digitraffic website](https://www.digitraffic.fi/)   The service has a public Google-group [road.digitraffic.fi](https://groups.google.com/forum/#!forum/roaddigitrafficfi) for communication between developers, service administrators and Fintraffic. The discussion in the forum is mostly in Finnish, but you're welcome to communicate in English too.   ### General notes of the API * Many Digitraffic APIs use GeoJSON as data format. Definition of the GeoJSON format can be found at https://tools.ietf.org/html/rfc7946. * For dates and times [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format is used with \"Zulu\" zero offset from UTC unless otherwise specified (i.e., \"yyyy-mm-ddThh:mm:ss[.mmm]Z\"). E.g. 2019-11-01T06:30:00Z.

    The version of the OpenAPI document: Branch: master, tag: 2024.10.28-1 #ef5bdf3 @ 2024-10-29T08:05:03+0000
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.traffic_message_v1_api import TrafficMessageV1Api


class TestTrafficMessageV1Api(unittest.TestCase):
    """TrafficMessageV1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = TrafficMessageV1Api()

    def tearDown(self) -> None:
        pass

    def test_area_location_regions(self) -> None:
        """Test case for area_location_regions

        Traffic messages geometries for regions
        """
        pass

    def test_area_location_regions1(self) -> None:
        """Test case for area_location_regions1

        Traffic messages geometries for regions
        """
        pass

    def test_location_by_id(self) -> None:
        """Test case for location_by_id

        The static information of one location
        """
        pass

    def test_location_types(self) -> None:
        """Test case for location_types

        The static information of location types and locationsubtypes
        """
        pass

    def test_location_versions(self) -> None:
        """Test case for location_versions

        List available location versions
        """
        pass

    def test_locations(self) -> None:
        """Test case for locations

        The static information of locations
        """
        pass

    def test_traffic_message_datex2(self) -> None:
        """Test case for traffic_message_datex2

        Active traffic messages as Datex2
        """
        pass

    def test_traffic_message_datex2_by_situation_id(self) -> None:
        """Test case for traffic_message_datex2_by_situation_id

        Traffic messages by situationId as Datex2
        """
        pass

    def test_traffic_message_simple(self) -> None:
        """Test case for traffic_message_simple

        Active traffic messages as simple JSON
        """
        pass

    def test_traffic_message_simple_by_situation_id(self) -> None:
        """Test case for traffic_message_simple_by_situation_id

        Traffic messages history by situation id as simple JSON
        """
        pass


if __name__ == '__main__':
    unittest.main()
