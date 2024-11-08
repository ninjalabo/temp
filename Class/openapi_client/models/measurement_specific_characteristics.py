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
from openapi_client.models.axle_characteristics import AxleCharacteristics
from openapi_client.models.computation_method_enum import ComputationMethodEnum
from openapi_client.models.direction_enum import DirectionEnum
from openapi_client.models.extension_type import ExtensionType
from openapi_client.models.lane import Lane
from openapi_client.models.measured_or_derived_data_type_enum import MeasuredOrDerivedDataTypeEnum
from openapi_client.models.vehicle_characteristics import VehicleCharacteristics
from typing import Optional, Set
from typing_extensions import Self

class MeasurementSpecificCharacteristics(BaseModel):
    """
    MeasurementSpecificCharacteristics
    """ # noqa: E501
    accuracy: Optional[Union[StrictFloat, StrictInt]] = None
    computation_method: Optional[ComputationMethodEnum] = Field(default=None, alias="computationMethod")
    default_measurement_height: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="defaultMeasurementHeight")
    measurement_side: Optional[DirectionEnum] = Field(default=None, alias="measurementSide")
    period: Optional[Union[StrictFloat, StrictInt]] = None
    smoothing_factor: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="smoothingFactor")
    specific_measurement_value_type: MeasuredOrDerivedDataTypeEnum = Field(alias="specificMeasurementValueType")
    specific_vehicle_characteristics: Optional[VehicleCharacteristics] = Field(default=None, alias="specificVehicleCharacteristics")
    specific_lanes: Optional[List[Lane]] = Field(default=None, alias="specificLanes")
    axle_characteristics: Optional[AxleCharacteristics] = Field(default=None, alias="axleCharacteristics")
    get_measurement_specific_characteristics_extension: Optional[ExtensionType] = Field(default=None, alias="get_MeasurementSpecificCharacteristicsExtension")
    __properties: ClassVar[List[str]] = ["accuracy", "computationMethod", "defaultMeasurementHeight", "measurementSide", "period", "smoothingFactor", "specificMeasurementValueType", "specificVehicleCharacteristics", "specificLanes", "axleCharacteristics", "get_MeasurementSpecificCharacteristicsExtension"]

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
        """Create an instance of MeasurementSpecificCharacteristics from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of computation_method
        if self.computation_method:
            _dict['computationMethod'] = self.computation_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of measurement_side
        if self.measurement_side:
            _dict['measurementSide'] = self.measurement_side.to_dict()
        # override the default output from pydantic by calling `to_dict()` of specific_measurement_value_type
        if self.specific_measurement_value_type:
            _dict['specificMeasurementValueType'] = self.specific_measurement_value_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of specific_vehicle_characteristics
        if self.specific_vehicle_characteristics:
            _dict['specificVehicleCharacteristics'] = self.specific_vehicle_characteristics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in specific_lanes (list)
        _items = []
        if self.specific_lanes:
            for _item in self.specific_lanes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['specificLanes'] = _items
        # override the default output from pydantic by calling `to_dict()` of axle_characteristics
        if self.axle_characteristics:
            _dict['axleCharacteristics'] = self.axle_characteristics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of get_measurement_specific_characteristics_extension
        if self.get_measurement_specific_characteristics_extension:
            _dict['get_MeasurementSpecificCharacteristicsExtension'] = self.get_measurement_specific_characteristics_extension.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MeasurementSpecificCharacteristics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accuracy": obj.get("accuracy"),
            "computationMethod": ComputationMethodEnum.from_dict(obj["computationMethod"]) if obj.get("computationMethod") is not None else None,
            "defaultMeasurementHeight": obj.get("defaultMeasurementHeight"),
            "measurementSide": DirectionEnum.from_dict(obj["measurementSide"]) if obj.get("measurementSide") is not None else None,
            "period": obj.get("period"),
            "smoothingFactor": obj.get("smoothingFactor"),
            "specificMeasurementValueType": MeasuredOrDerivedDataTypeEnum.from_dict(obj["specificMeasurementValueType"]) if obj.get("specificMeasurementValueType") is not None else None,
            "specificVehicleCharacteristics": VehicleCharacteristics.from_dict(obj["specificVehicleCharacteristics"]) if obj.get("specificVehicleCharacteristics") is not None else None,
            "specificLanes": [Lane.from_dict(_item) for _item in obj["specificLanes"]] if obj.get("specificLanes") is not None else None,
            "axleCharacteristics": AxleCharacteristics.from_dict(obj["axleCharacteristics"]) if obj.get("axleCharacteristics") is not None else None,
            "get_MeasurementSpecificCharacteristicsExtension": ExtensionType.from_dict(obj["get_MeasurementSpecificCharacteristicsExtension"]) if obj.get("get_MeasurementSpecificCharacteristicsExtension") is not None else None
        })
        return _obj


