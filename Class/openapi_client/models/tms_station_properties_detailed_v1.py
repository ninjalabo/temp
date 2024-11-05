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
from openapi_client.models.station_road_address_v1 import StationRoadAddressV1
from typing import Optional, Set
from typing_extensions import Self

class TmsStationPropertiesDetailedV1(BaseModel):
    """
    Tms station properties object with basic information
    """ # noqa: E501
    id: StrictInt = Field(description="Id of the road station")
    tms_number: StrictInt = Field(description="TMS station number", alias="tmsNumber")
    name: Optional[StrictStr] = Field(default=None, description="Common name of road station")
    collection_status: Optional[StrictStr] = Field(default=None, description="Data collection status", alias="collectionStatus")
    state: Optional[StrictStr] = Field(default=None, description="Road station state")
    data_updated_time: Optional[datetime] = Field(default=None, description="Data last updated date time", alias="dataUpdatedTime")
    collection_interval: Optional[StrictInt] = Field(default=None, description="Data collection interval [s]", alias="collectionInterval")
    names: Optional[Dict[str, StrictStr]] = Field(default=None, description="Map of names [fi, sv, en]")
    road_address: Optional[StationRoadAddressV1] = Field(default=None, alias="roadAddress")
    livi_id: Optional[StrictStr] = Field(default=None, description="Id in road registry", alias="liviId")
    country: Optional[StrictStr] = Field(default=None, description="Country where station is located")
    start_time: Optional[datetime] = Field(default=None, description="Station established date time", alias="startTime")
    repair_maintenance_time: Optional[datetime] = Field(default=None, description="Repair maintenance date time", alias="repairMaintenanceTime")
    annual_maintenance_time: Optional[datetime] = Field(default=None, description="Annual maintenance date time", alias="annualMaintenanceTime")
    purpose: Optional[StrictStr] = Field(default=None, description="Purpose of the road station")
    municipality: Optional[StrictStr] = Field(default=None, description="Municipality")
    municipality_code: Optional[StrictInt] = Field(default=None, description="Municipality code", alias="municipalityCode")
    province: Optional[StrictStr] = Field(default=None, description="Province")
    province_code: Optional[StrictInt] = Field(default=None, description="Province code", alias="provinceCode")
    direction1_municipality: StrictStr = Field(description="Direction 1 municipality (1 = According to the road register address increasing direction. I.e. on the road 4 to Lahti, if we are in Korso.)", alias="direction1Municipality")
    direction1_municipality_code: Optional[StrictInt] = Field(default=None, description="Direction 1 municipality code", alias="direction1MunicipalityCode")
    direction2_municipality: StrictStr = Field(description="Direction 2 municipality (2 = According to the road register address decreasing direction. I.e. on the road 4 to Helsinki, if we are in Korso.)", alias="direction2Municipality")
    direction2_municipality_code: Optional[StrictInt] = Field(default=None, description="Direction 2 municipality code", alias="direction2MunicipalityCode")
    station_type: Optional[StrictStr] = Field(default=None, description="TMS station type", alias="stationType")
    calculator_device_type: Optional[StrictStr] = Field(default=None, description="Type of calculation device", alias="calculatorDeviceType")
    sensors: Optional[List[StrictInt]] = Field(default=None, description="Tms Station Sensors ids")
    free_flow_speed1: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Free flow speed to direction 1 [km/h]", alias="freeFlowSpeed1")
    free_flow_speed2: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Free flow speed to direction 2 [km/h]", alias="freeFlowSpeed2")
    __properties: ClassVar[List[str]] = ["id", "tmsNumber", "name", "collectionStatus", "state", "dataUpdatedTime", "collectionInterval", "names", "roadAddress", "liviId", "country", "startTime", "repairMaintenanceTime", "annualMaintenanceTime", "purpose", "municipality", "municipalityCode", "province", "provinceCode", "direction1Municipality", "direction1MunicipalityCode", "direction2Municipality", "direction2MunicipalityCode", "stationType", "calculatorDeviceType", "sensors", "freeFlowSpeed1", "freeFlowSpeed2"]

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

    @field_validator('station_type')
    def station_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DSL_4', 'DSL_6', 'E_18', 'LML_1', 'OLD', 'DSL', 'FINAVIA']):
            raise ValueError("must be one of enum values ('DSL_4', 'DSL_6', 'E_18', 'LML_1', 'OLD', 'DSL', 'FINAVIA')")
        return value

    @field_validator('calculator_device_type')
    def calculator_device_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DSL_3', 'DSL_4_L', 'DSL_4_G', 'DSL_5', 'OTHER']):
            raise ValueError("must be one of enum values ('DSL_3', 'DSL_4_L', 'DSL_4_G', 'DSL_5', 'OTHER')")
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
        """Create an instance of TmsStationPropertiesDetailedV1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of road_address
        if self.road_address:
            _dict['roadAddress'] = self.road_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TmsStationPropertiesDetailedV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "tmsNumber": obj.get("tmsNumber"),
            "name": obj.get("name"),
            "collectionStatus": obj.get("collectionStatus"),
            "state": obj.get("state"),
            "dataUpdatedTime": obj.get("dataUpdatedTime"),
            "collectionInterval": obj.get("collectionInterval"),
            "names": obj.get("names"),
            "roadAddress": StationRoadAddressV1.from_dict(obj["roadAddress"]) if obj.get("roadAddress") is not None else None,
            "liviId": obj.get("liviId"),
            "country": obj.get("country"),
            "startTime": obj.get("startTime"),
            "repairMaintenanceTime": obj.get("repairMaintenanceTime"),
            "annualMaintenanceTime": obj.get("annualMaintenanceTime"),
            "purpose": obj.get("purpose"),
            "municipality": obj.get("municipality"),
            "municipalityCode": obj.get("municipalityCode"),
            "province": obj.get("province"),
            "provinceCode": obj.get("provinceCode"),
            "direction1Municipality": obj.get("direction1Municipality"),
            "direction1MunicipalityCode": obj.get("direction1MunicipalityCode"),
            "direction2Municipality": obj.get("direction2Municipality"),
            "direction2MunicipalityCode": obj.get("direction2MunicipalityCode"),
            "stationType": obj.get("stationType"),
            "calculatorDeviceType": obj.get("calculatorDeviceType"),
            "sensors": obj.get("sensors"),
            "freeFlowSpeed1": obj.get("freeFlowSpeed1"),
            "freeFlowSpeed2": obj.get("freeFlowSpeed2")
        })
        return _obj


