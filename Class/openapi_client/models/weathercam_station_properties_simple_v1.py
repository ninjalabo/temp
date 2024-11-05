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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.weathercam_preset_simple_v1 import WeathercamPresetSimpleV1
from typing import Optional, Set
from typing_extensions import Self

class WeathercamStationPropertiesSimpleV1(BaseModel):
    """
    Weathercam station properties object with basic information
    """ # noqa: E501
    id: StrictStr = Field(description="Id of the road station")
    name: Optional[StrictStr] = Field(default=None, description="Common name of road station")
    collection_status: Optional[StrictStr] = Field(default=None, description="Data collection status", alias="collectionStatus")
    state: Optional[StrictStr] = Field(default=None, description="Road station state")
    data_updated_time: Optional[datetime] = Field(default=None, description="Data last updated date time", alias="dataUpdatedTime")
    presets: Optional[List[WeathercamPresetSimpleV1]] = Field(default=None, description="Weathercam presets")
    __properties: ClassVar[List[str]] = ["id", "name", "collectionStatus", "state", "dataUpdatedTime", "presets"]

    @field_validator('collection_status')
    def collection_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['GATHERING', 'REMOVED_TEMPORARILY', 'REMOVED_PERMANENTLY']):
            raise ValueError("must be one of enum values ('GATHERING', 'REMOVED_TEMPORARILY', 'REMOVED_PERMANENTLY')")
        return value

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['OK', 'OK_FAULT_DOUBT_CANCELLED', 'FAULT_DOUBT', 'FAULT_CONFIRMED', 'FAULT_CONFIRMED_NOT_FIXED_IN_NEAR_FUTURE', 'REPAIR_REQUEST_POSTED', 'REPAIR_MAINTENANCE_DONE', 'REPAIR_INTERRUPTED']):
            raise ValueError("must be one of enum values ('OK', 'OK_FAULT_DOUBT_CANCELLED', 'FAULT_DOUBT', 'FAULT_CONFIRMED', 'FAULT_CONFIRMED_NOT_FIXED_IN_NEAR_FUTURE', 'REPAIR_REQUEST_POSTED', 'REPAIR_MAINTENANCE_DONE', 'REPAIR_INTERRUPTED')")
        return value

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
        """Create an instance of WeathercamStationPropertiesSimpleV1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in presets (list)
        _items = []
        if self.presets:
            for _item in self.presets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['presets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WeathercamStationPropertiesSimpleV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "collectionStatus": obj.get("collectionStatus"),
            "state": obj.get("state"),
            "dataUpdatedTime": obj.get("dataUpdatedTime"),
            "presets": [WeathercamPresetSimpleV1.from_dict(_item) for _item in obj["presets"]] if obj.get("presets") is not None else None
        })
        return _obj


