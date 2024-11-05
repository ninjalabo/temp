# coding: utf-8

"""
    Digitraffic Road API

    [OpenAPI document](/swagger/openapi.json)   Digitraffic is a service operated by the [Fintraffic](https://www.fintraffic.fi) offering real time traffic information. Currently the service covers *road, marine and rail* traffic. More information can be found at the [Digitraffic website](https://www.digitraffic.fi/)   The service has a public Google-group [road.digitraffic.fi](https://groups.google.com/forum/#!forum/roaddigitrafficfi) for communication between developers, service administrators and Fintraffic. The discussion in the forum is mostly in Finnish, but you're welcome to communicate in English too.   ### General notes of the API * Many Digitraffic APIs use GeoJSON as data format. Definition of the GeoJSON format can be found at https://tools.ietf.org/html/rfc7946. * For dates and times [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format is used with \"Zulu\" zero offset from UTC unless otherwise specified (i.e., \"yyyy-mm-ddThh:mm:ss[.mmm]Z\"). E.g. 2019-11-01T06:30:00Z.

    The version of the OpenAPI document: Branch: master, tag: 2024.10.28-1 #ef5bdf3 @ 2024-10-29T08:05:03+0000
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.traffic_announcement_feature_v1 import TrafficAnnouncementFeatureV1

class TestTrafficAnnouncementFeatureV1(unittest.TestCase):
    """TrafficAnnouncementFeatureV1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrafficAnnouncementFeatureV1:
        """Test TrafficAnnouncementFeatureV1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrafficAnnouncementFeatureV1`
        """
        model = TrafficAnnouncementFeatureV1()
        if include_optional:
            return TrafficAnnouncementFeatureV1(
                type = '',
                geometry = None,
                properties = openapi_client.models.traffic_announcement_properties_v1.TrafficAnnouncementPropertiesV1(
                    situation_id = '', 
                    situation_type = 'TRAFFIC_ANNOUNCEMENT', 
                    traffic_announcement_type = 'GENERAL', 
                    version = 56, 
                    release_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    version_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    announcements = [
                        openapi_client.models.traffic_announcement_v1.TrafficAnnouncementV1(
                            language = 'FI', 
                            title = '', 
                            location = openapi_client.models.location_v1.LocationV1(
                                country_code = 56, 
                                location_table_number = 56, 
                                location_table_version = '', 
                                description = '', ), 
                            location_details = openapi_client.models.location_details_v1.LocationDetailsV1(
                                area_location = openapi_client.models.area_location_v1.AreaLocationV1(
                                    areas = [
                                        openapi_client.models.area_v1.AreaV1(
                                            name = '', 
                                            location_code = 56, 
                                            type = 'MUNICIPALITY', )
                                        ], ), 
                                road_address_location = openapi_client.models.road_address_location_v1.RoadAddressLocationV1(
                                    primary_point = openapi_client.models.road_point_v1.RoadPointV1(
                                        municipality = '', 
                                        province = '', 
                                        country = '', 
                                        road_address = openapi_client.models.traffic_message_road_address_v1.TrafficMessageRoadAddressV1(
                                            road = 56, 
                                            road_section = 56, 
                                            distance = 56, ), 
                                        road_name = '', 
                                        alert_c_location = openapi_client.models.alert_c_location_v1.AlertCLocationV1(
                                            location_code = 56, 
                                            name = '', 
                                            distance = 56, ), ), 
                                    secondary_point = openapi_client.models.road_point_v1.RoadPointV1(
                                        municipality = '', 
                                        province = '', 
                                        country = '', 
                                        road_address = openapi_client.models.traffic_message_road_address_v1.TrafficMessageRoadAddressV1(
                                            road = 56, 
                                            road_section = 56, 
                                            distance = 56, ), 
                                        road_name = '', 
                                        alert_c_location = openapi_client.models.alert_c_location_v1.AlertCLocationV1(
                                            location_code = 56, 
                                            name = '', 
                                            distance = 56, ), ), 
                                    direction = 'UNKNOWN', 
                                    direction_description = '', ), ), 
                            features = [
                                openapi_client.models.feature_v1.FeatureV1(
                                    name = 'speed limit', 
                                    quantity = 30, 
                                    unit = 'km/h', 
                                    description = 'The road is narrow and winding', 
                                    time_and_duration = openapi_client.models.time_and_duration_v1.TimeAndDurationV1(
                                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        estimated_duration = openapi_client.models.estimated_duration_v1.EstimatedDurationV1(
                                            minimum = 'PT6H', 
                                            maximum = 'PT8H', 
                                            informal = '', ), ), )
                                ], 
                            road_work_phases = [
                                openapi_client.models.road_work_phase_v1.RoadWorkPhaseV1(
                                    id = '', 
                                    working_hours = [
                                        openapi_client.models.weekday_time_period_v1.WeekdayTimePeriodV1(
                                            weekday = 'MONDAY', 
                                            start_time = 15:30:00, 
                                            end_time = 15:30:00, )
                                        ], 
                                    comment = '', 
                                    time_and_duration = openapi_client.models.time_and_duration_v1.TimeAndDurationV1(
                                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                    work_types = [
                                        openapi_client.models.work_type_v1.WorkTypeV1(
                                            type = 'BRIDGE', 
                                            description = '', )
                                        ], 
                                    restrictions = [
                                        openapi_client.models.restriction_v1.RestrictionV1(
                                            restriction = openapi_client.models.feature_v1.FeatureV1(
                                                name = 'speed limit', 
                                                quantity = 30, 
                                                unit = 'km/h', 
                                                description = 'The road is narrow and winding', ), )
                                        ], 
                                    restrictions_liftable = True, 
                                    severity = 'LOW', 
                                    slow_traffic_times = [
                                        openapi_client.models.weekday_time_period_v1.WeekdayTimePeriodV1(
                                            weekday = 'MONDAY', 
                                            start_time = 15:30:00, 
                                            end_time = 15:30:00, )
                                        ], 
                                    queuing_traffic_times = [
                                        
                                        ], )
                                ], 
                            early_closing = 'CLOSED', 
                            comment = '', 
                            time_and_duration = , 
                            additional_information = '', 
                            sender = '', 
                            last_active_itinerary_segment = openapi_client.models.last_active_itinerary_segment_v1.LastActiveItinerarySegmentV1(
                                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                legs = [
                                    openapi_client.models.itinerary_leg_v1.ItineraryLegV1(
                                        road_leg = openapi_client.models.itinerary_road_leg_v1.ItineraryRoadLegV1(
                                            road_number = 56, 
                                            road_name = '', 
                                            start_area = '', 
                                            end_area = '', ), 
                                        street_name = '', )
                                    ], ), )
                        ], 
                    contact = openapi_client.models.contact_v1.ContactV1(
                        phone = '', 
                        email = '', ), 
                    data_updated_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return TrafficAnnouncementFeatureV1(
                type = '',
                geometry = None,
                properties = openapi_client.models.traffic_announcement_properties_v1.TrafficAnnouncementPropertiesV1(
                    situation_id = '', 
                    situation_type = 'TRAFFIC_ANNOUNCEMENT', 
                    traffic_announcement_type = 'GENERAL', 
                    version = 56, 
                    release_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    version_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    announcements = [
                        openapi_client.models.traffic_announcement_v1.TrafficAnnouncementV1(
                            language = 'FI', 
                            title = '', 
                            location = openapi_client.models.location_v1.LocationV1(
                                country_code = 56, 
                                location_table_number = 56, 
                                location_table_version = '', 
                                description = '', ), 
                            location_details = openapi_client.models.location_details_v1.LocationDetailsV1(
                                area_location = openapi_client.models.area_location_v1.AreaLocationV1(
                                    areas = [
                                        openapi_client.models.area_v1.AreaV1(
                                            name = '', 
                                            location_code = 56, 
                                            type = 'MUNICIPALITY', )
                                        ], ), 
                                road_address_location = openapi_client.models.road_address_location_v1.RoadAddressLocationV1(
                                    primary_point = openapi_client.models.road_point_v1.RoadPointV1(
                                        municipality = '', 
                                        province = '', 
                                        country = '', 
                                        road_address = openapi_client.models.traffic_message_road_address_v1.TrafficMessageRoadAddressV1(
                                            road = 56, 
                                            road_section = 56, 
                                            distance = 56, ), 
                                        road_name = '', 
                                        alert_c_location = openapi_client.models.alert_c_location_v1.AlertCLocationV1(
                                            location_code = 56, 
                                            name = '', 
                                            distance = 56, ), ), 
                                    secondary_point = openapi_client.models.road_point_v1.RoadPointV1(
                                        municipality = '', 
                                        province = '', 
                                        country = '', 
                                        road_address = openapi_client.models.traffic_message_road_address_v1.TrafficMessageRoadAddressV1(
                                            road = 56, 
                                            road_section = 56, 
                                            distance = 56, ), 
                                        road_name = '', 
                                        alert_c_location = openapi_client.models.alert_c_location_v1.AlertCLocationV1(
                                            location_code = 56, 
                                            name = '', 
                                            distance = 56, ), ), 
                                    direction = 'UNKNOWN', 
                                    direction_description = '', ), ), 
                            features = [
                                openapi_client.models.feature_v1.FeatureV1(
                                    name = 'speed limit', 
                                    quantity = 30, 
                                    unit = 'km/h', 
                                    description = 'The road is narrow and winding', 
                                    time_and_duration = openapi_client.models.time_and_duration_v1.TimeAndDurationV1(
                                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        estimated_duration = openapi_client.models.estimated_duration_v1.EstimatedDurationV1(
                                            minimum = 'PT6H', 
                                            maximum = 'PT8H', 
                                            informal = '', ), ), )
                                ], 
                            road_work_phases = [
                                openapi_client.models.road_work_phase_v1.RoadWorkPhaseV1(
                                    id = '', 
                                    working_hours = [
                                        openapi_client.models.weekday_time_period_v1.WeekdayTimePeriodV1(
                                            weekday = 'MONDAY', 
                                            start_time = 15:30:00, 
                                            end_time = 15:30:00, )
                                        ], 
                                    comment = '', 
                                    time_and_duration = openapi_client.models.time_and_duration_v1.TimeAndDurationV1(
                                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                    work_types = [
                                        openapi_client.models.work_type_v1.WorkTypeV1(
                                            type = 'BRIDGE', 
                                            description = '', )
                                        ], 
                                    restrictions = [
                                        openapi_client.models.restriction_v1.RestrictionV1(
                                            restriction = openapi_client.models.feature_v1.FeatureV1(
                                                name = 'speed limit', 
                                                quantity = 30, 
                                                unit = 'km/h', 
                                                description = 'The road is narrow and winding', ), )
                                        ], 
                                    restrictions_liftable = True, 
                                    severity = 'LOW', 
                                    slow_traffic_times = [
                                        openapi_client.models.weekday_time_period_v1.WeekdayTimePeriodV1(
                                            weekday = 'MONDAY', 
                                            start_time = 15:30:00, 
                                            end_time = 15:30:00, )
                                        ], 
                                    queuing_traffic_times = [
                                        
                                        ], )
                                ], 
                            early_closing = 'CLOSED', 
                            comment = '', 
                            time_and_duration = , 
                            additional_information = '', 
                            sender = '', 
                            last_active_itinerary_segment = openapi_client.models.last_active_itinerary_segment_v1.LastActiveItinerarySegmentV1(
                                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                legs = [
                                    openapi_client.models.itinerary_leg_v1.ItineraryLegV1(
                                        road_leg = openapi_client.models.itinerary_road_leg_v1.ItineraryRoadLegV1(
                                            road_number = 56, 
                                            road_name = '', 
                                            start_area = '', 
                                            end_area = '', ), 
                                        street_name = '', )
                                    ], ), )
                        ], 
                    contact = openapi_client.models.contact_v1.ContactV1(
                        phone = '', 
                        email = '', ), 
                    data_updated_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
        )
        """

    def testTrafficAnnouncementFeatureV1(self):
        """Test TrafficAnnouncementFeatureV1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
