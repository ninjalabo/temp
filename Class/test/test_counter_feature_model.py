# coding: utf-8

"""
    Digitraffic Road API

    [OpenAPI document](/swagger/openapi.json)   Digitraffic is a service operated by the [Fintraffic](https://www.fintraffic.fi) offering real time traffic information. Currently the service covers *road, marine and rail* traffic. More information can be found at the [Digitraffic website](https://www.digitraffic.fi/)   The service has a public Google-group [road.digitraffic.fi](https://groups.google.com/forum/#!forum/roaddigitrafficfi) for communication between developers, service administrators and Fintraffic. The discussion in the forum is mostly in Finnish, but you're welcome to communicate in English too.   ### General notes of the API * Many Digitraffic APIs use GeoJSON as data format. Definition of the GeoJSON format can be found at https://tools.ietf.org/html/rfc7946. * For dates and times [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format is used with \"Zulu\" zero offset from UTC unless otherwise specified (i.e., \"yyyy-mm-ddThh:mm:ss[.mmm]Z\"). E.g. 2019-11-01T06:30:00Z.

    The version of the OpenAPI document: Branch: master, tag: 2024.10.28-1 #ef5bdf3 @ 2024-10-29T08:05:03+0000
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.counter_feature_model import CounterFeatureModel

class TestCounterFeatureModel(unittest.TestCase):
    """CounterFeatureModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CounterFeatureModel:
        """Test CounterFeatureModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CounterFeatureModel`
        """
        model = CounterFeatureModel()
        if include_optional:
            return CounterFeatureModel(
                geometry = openapi_client.models.geometry.geometry(),
                type = 'Feature',
                properties = openapi_client.models.counter_model.CounterModel(
                    domain = '', 
                    name = '', 
                    interval = 56, 
                    last_data_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    removed_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = 56, 
                    user_type = 56, 
                    data_updated_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    direction = 56, )
            )
        else:
            return CounterFeatureModel(
                geometry = openapi_client.models.geometry.geometry(),
                type = 'Feature',
                properties = openapi_client.models.counter_model.CounterModel(
                    domain = '', 
                    name = '', 
                    interval = 56, 
                    last_data_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    removed_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = 56, 
                    user_type = 56, 
                    data_updated_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    direction = 56, ),
        )
        """

    def testCounterFeatureModel(self):
        """Test CounterFeatureModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
