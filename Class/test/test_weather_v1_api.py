# coding: utf-8

"""
    Digitraffic Road API

    [OpenAPI document](/swagger/openapi.json)   Digitraffic is a service operated by the [Fintraffic](https://www.fintraffic.fi) offering real time traffic information. Currently the service covers *road, marine and rail* traffic. More information can be found at the [Digitraffic website](https://www.digitraffic.fi/)   The service has a public Google-group [road.digitraffic.fi](https://groups.google.com/forum/#!forum/roaddigitrafficfi) for communication between developers, service administrators and Fintraffic. The discussion in the forum is mostly in Finnish, but you're welcome to communicate in English too.   ### General notes of the API * Many Digitraffic APIs use GeoJSON as data format. Definition of the GeoJSON format can be found at https://tools.ietf.org/html/rfc7946. * For dates and times [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format is used with \"Zulu\" zero offset from UTC unless otherwise specified (i.e., \"yyyy-mm-ddThh:mm:ss[.mmm]Z\"). E.g. 2019-11-01T06:30:00Z.

    The version of the OpenAPI document: Branch: master, tag: 2024.10.28-1 #ef5bdf3 @ 2024-10-29T08:05:03+0000
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.weather_v1_api import WeatherV1Api


class TestWeatherV1Api(unittest.TestCase):
    """WeatherV1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = WeatherV1Api()

    def tearDown(self) -> None:
        pass

    def test_forecast_section_by_id(self) -> None:
        """Test case for forecast_section_by_id

        The static information of weather forecast sections
        """
        pass

    def test_forecast_section_forecasts_by_id(self) -> None:
        """Test case for forecast_section_forecasts_by_id

        Current data of weather forecast sections
        """
        pass

    def test_forecast_section_simple_by_id(self) -> None:
        """Test case for forecast_section_simple_by_id

        The static information of simple weather forecast sections
        """
        pass

    def test_forecast_section_simple_forecasts_by_id(self) -> None:
        """Test case for forecast_section_simple_forecasts_by_id

        Current data of simple weather forecast sections
        """
        pass

    def test_forecast_sections(self) -> None:
        """Test case for forecast_sections

        The static information of weather forecast sections
        """
        pass

    def test_forecast_sections_forecasts(self) -> None:
        """Test case for forecast_sections_forecasts

        Current data of detailed weather forecast sections
        """
        pass

    def test_forecast_sections_simple(self) -> None:
        """Test case for forecast_sections_simple

        The static information of simple weather forecast sections
        """
        pass

    def test_forecast_sections_simple_forecasts(self) -> None:
        """Test case for forecast_sections_simple_forecasts

        Current data of simple weather forecast sections
        """
        pass

    def test_weather_data(self) -> None:
        """Test case for weather_data

        Current data of weather stations
        """
        pass

    def test_weather_data_by_id(self) -> None:
        """Test case for weather_data_by_id

        Current data of one weather station
        """
        pass

    def test_weather_sensors(self) -> None:
        """Test case for weather_sensors

        The static information of available sensors of weather stations
        """
        pass

    def test_weather_station_by_road_station_id(self) -> None:
        """Test case for weather_station_by_road_station_id

        The static information of one weather station
        """
        pass

    def test_weather_stations(self) -> None:
        """Test case for weather_stations

        The static information of weather stations
        """
        pass


if __name__ == '__main__':
    unittest.main()
