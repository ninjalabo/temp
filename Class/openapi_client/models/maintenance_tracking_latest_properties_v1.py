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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class MaintenanceTrackingLatestPropertiesV1(BaseModel):
    """
    Maintenance tracking properties
    """ # noqa: E501
    id: StrictInt = Field(description="Id for the tracking")
    time: datetime = Field(description="Time of latest tracking")
    created: datetime = Field(description="Creation time of tracking")
    tasks: List[StrictStr] = Field(description="Tasks done during maintenance work")
    direction: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Direction of the last observation")
    domain: Optional[StrictStr] = Field(default=None, description="Domain of the data")
    source: Optional[StrictStr] = Field(default=None, description="Source and owner of the data")
    __properties: ClassVar[List[str]] = ["id", "time", "created", "tasks", "direction", "domain", "source"]

    @field_validator('tasks')
    def tasks_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['BRUSHING', 'BRUSH_CLEARING', 'CLEANSING_OF_BRIDGES', 'CLEANSING_OF_REST_AREAS', 'CLEANSING_OF_TRAFFIC_SIGNS', 'CLIENTS_QUALITY_CONTROL', 'COMPACTION_BY_ROLLING', 'CRACK_FILLING', 'DITCHING', 'DUST_BINDING_OF_GRAVEL_ROAD_SURFACE', 'FILLING_OF_GRAVEL_ROAD_SHOULDERS', 'FILLING_OF_ROAD_SHOULDERS', 'HEATING', 'LEVELLING_GRAVEL_ROAD_SURFACE', 'LEVELLING_OF_ROAD_SHOULDERS', 'LEVELLING_OF_ROAD_SURFACE', 'LINE_SANDING', 'LOWERING_OF_SNOWBANKS', 'MAINTENANCE_OF_GUIDE_SIGNS_AND_REFLECTOR_POSTS', 'MECHANICAL_CUT', 'MIXING_OR_STABILIZATION', 'OTHER', 'PATCHING', 'PAVING', 'PLOUGHING_AND_SLUSH_REMOVAL', 'PREVENTING_MELTING_WATER_PROBLEMS', 'REMOVAL_OF_BULGE_ICE', 'RESHAPING_GRAVEL_ROAD_SURFACE', 'ROAD_INSPECTIONS', 'ROAD_MARKINGS', 'ROAD_STATE_CHECKING', 'SAFETY_EQUIPMENT', 'SALTING', 'SNOW_PLOUGHING_STICKS_AND_SNOW_FENCES', 'SPOT_SANDING', 'SPREADING_OF_CRUSH', 'TRANSFER_OF_SNOW', 'SERVICE_ROUND', 'ENSURING_TRAFFIC_IN_RASPUTITSA', 'OTHER_OPERATIONS_OF_LIGHTING_CONTRACTS', 'LEVELLING_OF_ROAD_SHOULDERS_UNDER_RAILING', 'DUST_BINDING_OF_PAVED_ROAD_SURFACE', 'RENEWAL_OF_EDGE_COLUMNS', 'GARBAGE_OLLECTION', 'GROUP_REPLACEMENT_OF_LAMPS', 'PLOUGHING_OF_SLUSH_DITCH', 'UNKNOWN']):
                raise ValueError("each list item must be one of ('BRUSHING', 'BRUSH_CLEARING', 'CLEANSING_OF_BRIDGES', 'CLEANSING_OF_REST_AREAS', 'CLEANSING_OF_TRAFFIC_SIGNS', 'CLIENTS_QUALITY_CONTROL', 'COMPACTION_BY_ROLLING', 'CRACK_FILLING', 'DITCHING', 'DUST_BINDING_OF_GRAVEL_ROAD_SURFACE', 'FILLING_OF_GRAVEL_ROAD_SHOULDERS', 'FILLING_OF_ROAD_SHOULDERS', 'HEATING', 'LEVELLING_GRAVEL_ROAD_SURFACE', 'LEVELLING_OF_ROAD_SHOULDERS', 'LEVELLING_OF_ROAD_SURFACE', 'LINE_SANDING', 'LOWERING_OF_SNOWBANKS', 'MAINTENANCE_OF_GUIDE_SIGNS_AND_REFLECTOR_POSTS', 'MECHANICAL_CUT', 'MIXING_OR_STABILIZATION', 'OTHER', 'PATCHING', 'PAVING', 'PLOUGHING_AND_SLUSH_REMOVAL', 'PREVENTING_MELTING_WATER_PROBLEMS', 'REMOVAL_OF_BULGE_ICE', 'RESHAPING_GRAVEL_ROAD_SURFACE', 'ROAD_INSPECTIONS', 'ROAD_MARKINGS', 'ROAD_STATE_CHECKING', 'SAFETY_EQUIPMENT', 'SALTING', 'SNOW_PLOUGHING_STICKS_AND_SNOW_FENCES', 'SPOT_SANDING', 'SPREADING_OF_CRUSH', 'TRANSFER_OF_SNOW', 'SERVICE_ROUND', 'ENSURING_TRAFFIC_IN_RASPUTITSA', 'OTHER_OPERATIONS_OF_LIGHTING_CONTRACTS', 'LEVELLING_OF_ROAD_SHOULDERS_UNDER_RAILING', 'DUST_BINDING_OF_PAVED_ROAD_SURFACE', 'RENEWAL_OF_EDGE_COLUMNS', 'GARBAGE_OLLECTION', 'GROUP_REPLACEMENT_OF_LAMPS', 'PLOUGHING_OF_SLUSH_DITCH', 'UNKNOWN')")
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
        """Create an instance of MaintenanceTrackingLatestPropertiesV1 from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MaintenanceTrackingLatestPropertiesV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "time": obj.get("time"),
            "created": obj.get("created"),
            "tasks": obj.get("tasks"),
            "direction": obj.get("direction"),
            "domain": obj.get("domain"),
            "source": obj.get("source")
        })
        return _obj


