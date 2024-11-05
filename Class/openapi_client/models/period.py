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
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.day_week_month import DayWeekMonth
from openapi_client.models.extension_type import ExtensionType
from openapi_client.models.multilingual_string import MultilingualString
from openapi_client.models.special_day import SpecialDay
from openapi_client.models.time_period_of_day import TimePeriodOfDay
from typing import Optional, Set
from typing_extensions import Self

class Period(BaseModel):
    """
    Period
    """ # noqa: E501
    start_of_period: Optional[datetime] = Field(default=None, alias="startOfPeriod")
    end_of_period: Optional[datetime] = Field(default=None, alias="endOfPeriod")
    period_name: Optional[MultilingualString] = Field(default=None, alias="periodName")
    recurring_time_period_of_daies: Optional[List[TimePeriodOfDay]] = Field(default=None, alias="recurringTimePeriodOfDaies")
    recurring_day_week_month_periods: Optional[List[DayWeekMonth]] = Field(default=None, alias="recurringDayWeekMonthPeriods")
    recurring_special_daies: Optional[List[SpecialDay]] = Field(default=None, alias="recurringSpecialDaies")
    get_period_extension: Optional[ExtensionType] = Field(default=None, alias="get_PeriodExtension")
    __properties: ClassVar[List[str]] = ["startOfPeriod", "endOfPeriod", "periodName", "recurringTimePeriodOfDaies", "recurringDayWeekMonthPeriods", "recurringSpecialDaies", "get_PeriodExtension"]

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
        """Create an instance of Period from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of period_name
        if self.period_name:
            _dict['periodName'] = self.period_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in recurring_time_period_of_daies (list)
        _items = []
        if self.recurring_time_period_of_daies:
            for _item in self.recurring_time_period_of_daies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recurringTimePeriodOfDaies'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in recurring_day_week_month_periods (list)
        _items = []
        if self.recurring_day_week_month_periods:
            for _item in self.recurring_day_week_month_periods:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recurringDayWeekMonthPeriods'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in recurring_special_daies (list)
        _items = []
        if self.recurring_special_daies:
            for _item in self.recurring_special_daies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recurringSpecialDaies'] = _items
        # override the default output from pydantic by calling `to_dict()` of get_period_extension
        if self.get_period_extension:
            _dict['get_PeriodExtension'] = self.get_period_extension.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Period from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "startOfPeriod": obj.get("startOfPeriod"),
            "endOfPeriod": obj.get("endOfPeriod"),
            "periodName": MultilingualString.from_dict(obj["periodName"]) if obj.get("periodName") is not None else None,
            "recurringTimePeriodOfDaies": [TimePeriodOfDay.from_dict(_item) for _item in obj["recurringTimePeriodOfDaies"]] if obj.get("recurringTimePeriodOfDaies") is not None else None,
            "recurringDayWeekMonthPeriods": [DayWeekMonth.from_dict(_item) for _item in obj["recurringDayWeekMonthPeriods"]] if obj.get("recurringDayWeekMonthPeriods") is not None else None,
            "recurringSpecialDaies": [SpecialDay.from_dict(_item) for _item in obj["recurringSpecialDaies"]] if obj.get("recurringSpecialDaies") is not None else None,
            "get_PeriodExtension": ExtensionType.from_dict(obj["get_PeriodExtension"]) if obj.get("get_PeriodExtension") is not None else None
        })
        return _obj

