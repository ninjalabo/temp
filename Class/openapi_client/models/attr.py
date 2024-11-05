# coding: utf-8

"""
    Digitraffic Road API

    [OpenAPI document](/swagger/openapi.json)   Digitraffic is a service operated by the [Fintraffic](https://www.fintraffic.fi) offering real time traffic information. Currently the service covers *road, marine and rail* traffic. More information can be found at the [Digitraffic website](https://www.digitraffic.fi/)   The service has a public Google-group [road.digitraffic.fi](https://groups.google.com/forum/#!forum/roaddigitrafficfi) for communication between developers, service administrators and Fintraffic. The discussion in the forum is mostly in Finnish, but you're welcome to communicate in English too.   ### General notes of the API * Many Digitraffic APIs use GeoJSON as data format. Definition of the GeoJSON format can be found at https://tools.ietf.org/html/rfc7946. * For dates and times [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format is used with \"Zulu\" zero offset from UTC unless otherwise specified (i.e., \"yyyy-mm-ddThh:mm:ss[.mmm]Z\"). E.g. 2019-11-01T06:30:00Z.

    The version of the OpenAPI document: Branch: master, tag: 2024.10.28-1 #ef5bdf3 @ 2024-10-29T08:05:03+0000
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.node_list import NodeList
from openapi_client.models.type_info import TypeInfo
from typing import Optional, Set
from typing_extensions import Self

class Attr(BaseModel):
    """
    Attr
    """ # noqa: E501
    name: Optional[StrictStr] = None
    value: Optional[StrictStr] = None
    specified: Optional[StrictBool] = None
    owner_element: Optional[Element] = Field(default=None, alias="ownerElement")
    schema_type_info: Optional[TypeInfo] = Field(default=None, alias="schemaTypeInfo")
    id: Optional[StrictBool] = None
    attributes: Optional[NamedNodeMap] = None
    local_name: Optional[StrictStr] = Field(default=None, alias="localName")
    node_name: Optional[StrictStr] = Field(default=None, alias="nodeName")
    node_value: Optional[StrictStr] = Field(default=None, alias="nodeValue")
    parent_node: Optional[Node] = Field(default=None, alias="parentNode")
    child_nodes: Optional[NodeList] = Field(default=None, alias="childNodes")
    first_child: Optional[Node] = Field(default=None, alias="firstChild")
    last_child: Optional[Node] = Field(default=None, alias="lastChild")
    previous_sibling: Optional[Node] = Field(default=None, alias="previousSibling")
    next_sibling: Optional[Node] = Field(default=None, alias="nextSibling")
    owner_document: Optional[Document] = Field(default=None, alias="ownerDocument")
    namespace_uri: Optional[StrictStr] = Field(default=None, alias="namespaceURI")
    base_uri: Optional[StrictStr] = Field(default=None, alias="baseURI")
    text_content: Optional[StrictStr] = Field(default=None, alias="textContent")
    prefix: Optional[StrictStr] = None
    node_type: Optional[StrictInt] = Field(default=None, alias="nodeType")
    __properties: ClassVar[List[str]] = ["name", "value", "specified", "ownerElement", "schemaTypeInfo", "id", "attributes", "localName", "nodeName", "nodeValue", "parentNode", "childNodes", "firstChild", "lastChild", "previousSibling", "nextSibling", "ownerDocument", "namespaceURI", "baseURI", "textContent", "prefix", "nodeType"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Attr from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of owner_element
        if self.owner_element:
            _dict['ownerElement'] = self.owner_element.to_dict()
        # override the default output from pydantic by calling `to_dict()` of schema_type_info
        if self.schema_type_info:
            _dict['schemaTypeInfo'] = self.schema_type_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parent_node
        if self.parent_node:
            _dict['parentNode'] = self.parent_node.to_dict()
        # override the default output from pydantic by calling `to_dict()` of child_nodes
        if self.child_nodes:
            _dict['childNodes'] = self.child_nodes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of first_child
        if self.first_child:
            _dict['firstChild'] = self.first_child.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_child
        if self.last_child:
            _dict['lastChild'] = self.last_child.to_dict()
        # override the default output from pydantic by calling `to_dict()` of previous_sibling
        if self.previous_sibling:
            _dict['previousSibling'] = self.previous_sibling.to_dict()
        # override the default output from pydantic by calling `to_dict()` of next_sibling
        if self.next_sibling:
            _dict['nextSibling'] = self.next_sibling.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner_document
        if self.owner_document:
            _dict['ownerDocument'] = self.owner_document.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Attr from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "value": obj.get("value"),
            "specified": obj.get("specified"),
            "ownerElement": Element.from_dict(obj["ownerElement"]) if obj.get("ownerElement") is not None else None,
            "schemaTypeInfo": TypeInfo.from_dict(obj["schemaTypeInfo"]) if obj.get("schemaTypeInfo") is not None else None,
            "id": obj.get("id"),
            "attributes": NamedNodeMap.from_dict(obj["attributes"]) if obj.get("attributes") is not None else None,
            "localName": obj.get("localName"),
            "nodeName": obj.get("nodeName"),
            "nodeValue": obj.get("nodeValue"),
            "parentNode": Node.from_dict(obj["parentNode"]) if obj.get("parentNode") is not None else None,
            "childNodes": NodeList.from_dict(obj["childNodes"]) if obj.get("childNodes") is not None else None,
            "firstChild": Node.from_dict(obj["firstChild"]) if obj.get("firstChild") is not None else None,
            "lastChild": Node.from_dict(obj["lastChild"]) if obj.get("lastChild") is not None else None,
            "previousSibling": Node.from_dict(obj["previousSibling"]) if obj.get("previousSibling") is not None else None,
            "nextSibling": Node.from_dict(obj["nextSibling"]) if obj.get("nextSibling") is not None else None,
            "ownerDocument": Document.from_dict(obj["ownerDocument"]) if obj.get("ownerDocument") is not None else None,
            "namespaceURI": obj.get("namespaceURI"),
            "baseURI": obj.get("baseURI"),
            "textContent": obj.get("textContent"),
            "prefix": obj.get("prefix"),
            "nodeType": obj.get("nodeType")
        })
        return _obj

from openapi_client.models.document import Document
from openapi_client.models.element import Element
from openapi_client.models.named_node_map import NamedNodeMap
from openapi_client.models.node import Node
# TODO: Rewrite to not use raise_errors
Attr.model_rebuild(raise_errors=False)

