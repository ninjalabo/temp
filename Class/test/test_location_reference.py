# coding: utf-8

"""
    Digitraffic Road API

    [OpenAPI document](/swagger/openapi.json)   Digitraffic is a service operated by the [Fintraffic](https://www.fintraffic.fi) offering real time traffic information. Currently the service covers *road, marine and rail* traffic. More information can be found at the [Digitraffic website](https://www.digitraffic.fi/)   The service has a public Google-group [road.digitraffic.fi](https://groups.google.com/forum/#!forum/roaddigitrafficfi) for communication between developers, service administrators and Fintraffic. The discussion in the forum is mostly in Finnish, but you're welcome to communicate in English too.   ### General notes of the API * Many Digitraffic APIs use GeoJSON as data format. Definition of the GeoJSON format can be found at https://tools.ietf.org/html/rfc7946. * For dates and times [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format is used with \"Zulu\" zero offset from UTC unless otherwise specified (i.e., \"yyyy-mm-ddThh:mm:ss[.mmm]Z\"). E.g. 2019-11-01T06:30:00Z.

    The version of the OpenAPI document: Branch: master, tag: 2024.10.28-1 #ef5bdf3 @ 2024-10-29T08:05:03+0000
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.location_reference import LocationReference

class TestLocationReference(unittest.TestCase):
    """LocationReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LocationReference:
        """Test LocationReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LocationReference`
        """
        model = LocationReference()
        if include_optional:
            return LocationReference(
                get_location_reference_extension = openapi_client.models._location_reference_extension_type._LocationReferenceExtensionType(
                    facility_location = openapi_client.models.facility_location.FacilityLocation(
                        time_zone = '', 
                        address = openapi_client.models.address.Address(
                            postcode = '', 
                            city = openapi_client.models.multilingual_string.MultilingualString(
                                values = openapi_client.models.values.Values(
                                    values = [
                                        openapi_client.models.multilingual_string_value.MultilingualStringValue(
                                            value = '', 
                                            lang = '', )
                                        ], ), ), 
                            country_code = '', 
                            address_lines = [
                                openapi_client.models.address_line.AddressLine(
                                    type = openapi_client.models._address_line_type_enum._AddressLineTypeEnum(
                                        value = 'APARTMENT', 
                                        get_extended_value = '', ), 
                                    text = openapi_client.models.multilingual_string.MultilingualString(
                                        values = openapi_client.models.values.Values(
                                            values = [
                                                openapi_client.models.multilingual_string_value.MultilingualStringValue(
                                                    value = '', 
                                                    lang = '', )
                                                ], ), ), 
                                    get_address_line_extension = openapi_client.models._extension_type._ExtensionType(
                                        anies = [
                                            openapi_client.models.element.Element(
                                                schema_type_info = openapi_client.models.type_info.TypeInfo(
                                                    type_name = '', 
                                                    type_namespace = '', ), 
                                                attribute_node_ns = openapi_client.models.attr.Attr(
                                                    name = '', 
                                                    value = '', 
                                                    specified = True, 
                                                    owner_element = openapi_client.models.element.Element(
                                                        attribute_node = openapi_client.models.attr.Attr(
                                                            name = '', 
                                                            value = '', 
                                                            specified = True, 
                                                            id = True, 
                                                            attributes = openapi_client.models.named_node_map.NamedNodeMap(
                                                                length = 56, 
                                                                named_item = openapi_client.models.node.Node(
                                                                    local_name = '', 
                                                                    node_name = '', 
                                                                    node_value = '', 
                                                                    parent_node = openapi_client.models.node.Node(
                                                                        local_name = '', 
                                                                        node_name = '', 
                                                                        node_value = '', 
                                                                        child_nodes = openapi_client.models.node_list.NodeList(
                                                                            length = 56, ), 
                                                                        first_child = , 
                                                                        last_child = , 
                                                                        previous_sibling = , 
                                                                        next_sibling = , 
                                                                        owner_document = openapi_client.models.document.Document(
                                                                            doctype = openapi_client.models.document_type.DocumentType(
                                                                                name = '', 
                                                                                public_id = '', 
                                                                                system_id = '', 
                                                                                entities = openapi_client.models.named_node_map.NamedNodeMap(
                                                                                    length = 56, 
                                                                                    named_item_ns = , ), 
                                                                                notations = , 
                                                                                internal_subset = '', 
                                                                                local_name = '', 
                                                                                node_name = '', 
                                                                                node_value = '', 
                                                                                namespace_uri = '', 
                                                                                base_uri = '', 
                                                                                text_content = '', 
                                                                                prefix = '', 
                                                                                node_type = 56, ), 
                                                                            document_element = , 
                                                                            input_encoding = '', 
                                                                            xml_encoding = '', 
                                                                            xml_standalone = True, 
                                                                            xml_version = '', 
                                                                            strict_error_checking = True, 
                                                                            document_uri = '', 
                                                                            dom_config = openapi_client.models.dom_configuration.DOMConfiguration(
                                                                                parameter_names = openapi_client.models.dom_string_list.DOMStringList(
                                                                                    length = 56, ), ), 
                                                                            implementation = openapi_client.models.dom_implementation.DOMImplementation(), 
                                                                            local_name = '', 
                                                                            node_name = '', 
                                                                            node_value = '', 
                                                                            namespace_uri = '', 
                                                                            base_uri = '', 
                                                                            text_content = '', 
                                                                            prefix = '', 
                                                                            node_type = 56, ), 
                                                                        namespace_uri = '', 
                                                                        base_uri = '', 
                                                                        text_content = '', 
                                                                        prefix = '', 
                                                                        node_type = 56, ), 
                                                                    child_nodes = openapi_client.models.node_list.NodeList(
                                                                        length = 56, ), 
                                                                    first_child = , 
                                                                    last_child = , 
                                                                    previous_sibling = , 
                                                                    next_sibling = , 
                                                                    owner_document = openapi_client.models.document.Document(
                                                                        input_encoding = '', 
                                                                        xml_encoding = '', 
                                                                        xml_standalone = True, 
                                                                        xml_version = '', 
                                                                        strict_error_checking = True, 
                                                                        document_uri = '', 
                                                                        implementation = openapi_client.models.dom_implementation.DOMImplementation(), 
                                                                        local_name = '', 
                                                                        node_name = '', 
                                                                        node_value = '', 
                                                                        namespace_uri = '', 
                                                                        base_uri = '', 
                                                                        text_content = '', 
                                                                        prefix = '', 
                                                                        node_type = 56, ), 
                                                                    namespace_uri = '', 
                                                                    base_uri = '', 
                                                                    text_content = '', 
                                                                    prefix = '', 
                                                                    node_type = 56, ), 
                                                                named_item_ns = , ), 
                                                            local_name = '', 
                                                            node_name = '', 
                                                            node_value = '', 
                                                            parent_node = , 
                                                            child_nodes = , 
                                                            first_child = , 
                                                            last_child = , 
                                                            previous_sibling = , 
                                                            next_sibling = , 
                                                            owner_document = , 
                                                            namespace_uri = '', 
                                                            base_uri = '', 
                                                            text_content = '', 
                                                            prefix = '', 
                                                            node_type = 56, ), 
                                                        tag_name = '', 
                                                        attributes = , 
                                                        local_name = '', 
                                                        node_name = '', 
                                                        node_value = '', 
                                                        parent_node = , 
                                                        child_nodes = , 
                                                        first_child = , 
                                                        last_child = , 
                                                        previous_sibling = , 
                                                        next_sibling = , 
                                                        owner_document = , 
                                                        namespace_uri = '', 
                                                        base_uri = '', 
                                                        text_content = '', 
                                                        prefix = '', 
                                                        node_type = 56, ), 
                                                    id = True, 
                                                    attributes = , 
                                                    local_name = '', 
                                                    node_name = '', 
                                                    node_value = '', 
                                                    parent_node = , 
                                                    child_nodes = , 
                                                    first_child = , 
                                                    last_child = , 
                                                    previous_sibling = , 
                                                    next_sibling = , 
                                                    owner_document = , 
                                                    namespace_uri = '', 
                                                    base_uri = '', 
                                                    text_content = '', 
                                                    prefix = '', 
                                                    node_type = 56, ), 
                                                attribute_node = , 
                                                tag_name = '', 
                                                attributes = , 
                                                local_name = '', 
                                                node_name = '', 
                                                node_value = '', 
                                                parent_node = , 
                                                child_nodes = , 
                                                first_child = , 
                                                last_child = , 
                                                previous_sibling = , 
                                                next_sibling = , 
                                                owner_document = , 
                                                namespace_uri = '', 
                                                base_uri = '', 
                                                text_content = '', 
                                                prefix = '', 
                                                node_type = 56, )
                                            ], ), 
                                    order = 56, )
                                ], 
                            get_address_extension = openapi_client.models._extension_type._ExtensionType(), ), ), 
                    anies = [
                        
                        ], )
            )
        else:
            return LocationReference(
        )
        """

    def testLocationReference(self):
        """Test LocationReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
