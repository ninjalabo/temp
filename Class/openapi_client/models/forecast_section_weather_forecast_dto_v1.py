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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.forecast_condition_reason_dto_v1 import ForecastConditionReasonDtoV1
from typing import Optional, Set
from typing_extensions import Self

class ForecastSectionWeatherForecastDtoV1(BaseModel):
    """
    Forecast section's weather forecast
    """ # noqa: E501
    time: Optional[datetime] = Field(default=None, description="Observation or forecast time depending on type")
    type: Optional[StrictStr] = Field(default=None, description="Tells if object is an observation or a forecast. (OBSERVATION, FORECAST)")
    forecast_name: Optional[StrictStr] = Field(default=None, description="Name of the forecast", alias="forecastName")
    daylight: Optional[StrictBool] = Field(default=None, description="Tells if there is daylight: true/false")
    road_temperature: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Road temperature at given time. If not available value is not set", alias="roadTemperature")
    temperature: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Air temperature")
    wind_speed: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Wind speed in m/s", alias="windSpeed")
    wind_direction: Optional[StrictInt] = Field(default=None, description="Wind direction in degrees. 0 when there is no wind or the direction is variable. 90 degrees is arrow to the east (count clockwise)", alias="windDirection")
    overall_road_condition: Optional[StrictStr] = Field(default=None, description="Overall road condition", alias="overallRoadCondition")
    weather_symbol: Optional[StrictStr] = Field(default=None, description="Weather symbol code. See corresponding symbols at https://www.vaisala.com/en/vaisala-weather-symbols. Symbols are allowed to be used in user's applications but any further modification and redistribution is denied.", alias="weatherSymbol")
    reliability: Optional[StrictStr] = Field(default=None, description="Forecast reliability")
    forecast_condition_reason: Optional[ForecastConditionReasonDtoV1] = Field(default=None, alias="forecastConditionReason")
    data_updated_time: datetime = Field(description="Data last updated time", alias="dataUpdatedTime")
    __properties: ClassVar[List[str]] = ["time", "type", "forecastName", "daylight", "roadTemperature", "temperature", "windSpeed", "windDirection", "overallRoadCondition", "weatherSymbol", "reliability", "forecastConditionReason", "dataUpdatedTime"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['OBSERVATION', 'FORECAST']):
            raise ValueError("must be one of enum values ('OBSERVATION', 'FORECAST')")
        return value

    @field_validator('overall_road_condition')
    def overall_road_condition_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NORMAL_CONDITION', 'POOR_CONDITION', 'EXTREMELY_POOR_CONDITION', 'CONDITION_COULD_NOT_BE_RESOLVED']):
            raise ValueError("must be one of enum values ('NORMAL_CONDITION', 'POOR_CONDITION', 'EXTREMELY_POOR_CONDITION', 'CONDITION_COULD_NOT_BE_RESOLVED')")
        return value

    @field_validator('reliability')
    def reliability_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SUCCESSFUL', 'NO_DATA_FROM_ROADSTATION', 'FAILED']):
            raise ValueError("must be one of enum values ('SUCCESSFUL', 'NO_DATA_FROM_ROADSTATION', 'FAILED')")
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
        """Create an instance of ForecastSectionWeatherForecastDtoV1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of forecast_condition_reason
        if self.forecast_condition_reason:
            _dict['forecastConditionReason'] = self.forecast_condition_reason.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ForecastSectionWeatherForecastDtoV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "time": obj.get("time"),
            "type": obj.get("type"),
            "forecastName": obj.get("forecastName"),
            "daylight": obj.get("daylight"),
            "roadTemperature": obj.get("roadTemperature"),
            "temperature": obj.get("temperature"),
            "windSpeed": obj.get("windSpeed"),
            "windDirection": obj.get("windDirection"),
            "overallRoadCondition": obj.get("overallRoadCondition"),
            "weatherSymbol": obj.get("weatherSymbol"),
            "reliability": obj.get("reliability"),
            "forecastConditionReason": ForecastConditionReasonDtoV1.from_dict(obj["forecastConditionReason"]) if obj.get("forecastConditionReason") is not None else None,
            "dataUpdatedTime": obj.get("dataUpdatedTime")
        })
        return _obj

