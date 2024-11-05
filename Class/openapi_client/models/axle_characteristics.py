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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.extension_type import ExtensionType
from typing import Optional, Set
from typing_extensions import Self

class AxleCharacteristics(BaseModel):
    """
    AxleCharacteristics
    """ # noqa: E501
    maximum_weight: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maximumWeight")
    minimum_weight: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="minimumWeight")
    get_axle_characteristics_extension: Optional[ExtensionType] = Field(default=None, alias="get_AxleCharacteristicsExtension")
    __properties: ClassVar[List[str]] = ["maximumWeight", "minimumWeight", "get_AxleCharacteristicsExtension"]

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
        """Create an instance of AxleCharacteristics from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of get_axle_characteristics_extension
        if self.get_axle_characteristics_extension:
            _dict['get_AxleCharacteristicsExtension'] = self.get_axle_characteristics_extension.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AxleCharacteristics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maximumWeight": obj.get("maximumWeight"),
            "minimumWeight": obj.get("minimumWeight"),
            "get_AxleCharacteristicsExtension": ExtensionType.from_dict(obj["get_AxleCharacteristicsExtension"]) if obj.get("get_AxleCharacteristicsExtension") is not None else None
        })
        return _obj


