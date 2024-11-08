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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.emissions import Emissions
from openapi_client.models.extension_type import ExtensionType
from openapi_client.models.fuel_type_enum import FuelTypeEnum
from openapi_client.models.gross_weight_characteristic import GrossWeightCharacteristic
from openapi_client.models.heaviest_axle_weight_characteristic import HeaviestAxleWeightCharacteristic
from openapi_client.models.height_characteristic import HeightCharacteristic
from openapi_client.models.length_characteristic import LengthCharacteristic
from openapi_client.models.load_type_enum import LoadTypeEnum
from openapi_client.models.number_of_axles_characteristic import NumberOfAxlesCharacteristic
from openapi_client.models.vehicle_equipment_enum import VehicleEquipmentEnum
from openapi_client.models.vehicle_type_enum import VehicleTypeEnum
from openapi_client.models.vehicle_usage_enum import VehicleUsageEnum
from openapi_client.models.width_characteristic import WidthCharacteristic
from typing import Optional, Set
from typing_extensions import Self

class VehicleCharacteristics(BaseModel):
    """
    VehicleCharacteristics
    """ # noqa: E501
    fuel_types: Optional[List[FuelTypeEnum]] = Field(default=None, alias="fuelTypes")
    load_type: Optional[LoadTypeEnum] = Field(default=None, alias="loadType")
    vehicle_equipment: Optional[VehicleEquipmentEnum] = Field(default=None, alias="vehicleEquipment")
    vehicle_types: Optional[List[VehicleTypeEnum]] = Field(default=None, alias="vehicleTypes")
    vehicle_usage: Optional[VehicleUsageEnum] = Field(default=None, alias="vehicleUsage")
    year_of_first_registration: Optional[StrictInt] = Field(default=None, alias="yearOfFirstRegistration")
    gross_weight_characteristics: Optional[List[GrossWeightCharacteristic]] = Field(default=None, alias="grossWeightCharacteristics")
    height_characteristics: Optional[List[HeightCharacteristic]] = Field(default=None, alias="heightCharacteristics")
    length_characteristics: Optional[List[LengthCharacteristic]] = Field(default=None, alias="lengthCharacteristics")
    width_characteristics: Optional[List[WidthCharacteristic]] = Field(default=None, alias="widthCharacteristics")
    heaviest_axle_weight_characteristics: Optional[List[HeaviestAxleWeightCharacteristic]] = Field(default=None, alias="heaviestAxleWeightCharacteristics")
    number_of_axles_characteristics: Optional[List[NumberOfAxlesCharacteristic]] = Field(default=None, alias="numberOfAxlesCharacteristics")
    emissions: Optional[Emissions] = None
    get_vehicle_characteristics_extension: Optional[ExtensionType] = Field(default=None, alias="get_VehicleCharacteristicsExtension")
    __properties: ClassVar[List[str]] = ["fuelTypes", "loadType", "vehicleEquipment", "vehicleTypes", "vehicleUsage", "yearOfFirstRegistration", "grossWeightCharacteristics", "heightCharacteristics", "lengthCharacteristics", "widthCharacteristics", "heaviestAxleWeightCharacteristics", "numberOfAxlesCharacteristics", "emissions", "get_VehicleCharacteristicsExtension"]

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
        """Create an instance of VehicleCharacteristics from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fuel_types (list)
        _items = []
        if self.fuel_types:
            for _item in self.fuel_types:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fuelTypes'] = _items
        # override the default output from pydantic by calling `to_dict()` of load_type
        if self.load_type:
            _dict['loadType'] = self.load_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vehicle_equipment
        if self.vehicle_equipment:
            _dict['vehicleEquipment'] = self.vehicle_equipment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in vehicle_types (list)
        _items = []
        if self.vehicle_types:
            for _item in self.vehicle_types:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vehicleTypes'] = _items
        # override the default output from pydantic by calling `to_dict()` of vehicle_usage
        if self.vehicle_usage:
            _dict['vehicleUsage'] = self.vehicle_usage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in gross_weight_characteristics (list)
        _items = []
        if self.gross_weight_characteristics:
            for _item in self.gross_weight_characteristics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['grossWeightCharacteristics'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in height_characteristics (list)
        _items = []
        if self.height_characteristics:
            for _item in self.height_characteristics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['heightCharacteristics'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in length_characteristics (list)
        _items = []
        if self.length_characteristics:
            for _item in self.length_characteristics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lengthCharacteristics'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in width_characteristics (list)
        _items = []
        if self.width_characteristics:
            for _item in self.width_characteristics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['widthCharacteristics'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in heaviest_axle_weight_characteristics (list)
        _items = []
        if self.heaviest_axle_weight_characteristics:
            for _item in self.heaviest_axle_weight_characteristics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['heaviestAxleWeightCharacteristics'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in number_of_axles_characteristics (list)
        _items = []
        if self.number_of_axles_characteristics:
            for _item in self.number_of_axles_characteristics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['numberOfAxlesCharacteristics'] = _items
        # override the default output from pydantic by calling `to_dict()` of emissions
        if self.emissions:
            _dict['emissions'] = self.emissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of get_vehicle_characteristics_extension
        if self.get_vehicle_characteristics_extension:
            _dict['get_VehicleCharacteristicsExtension'] = self.get_vehicle_characteristics_extension.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VehicleCharacteristics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fuelTypes": [FuelTypeEnum.from_dict(_item) for _item in obj["fuelTypes"]] if obj.get("fuelTypes") is not None else None,
            "loadType": LoadTypeEnum.from_dict(obj["loadType"]) if obj.get("loadType") is not None else None,
            "vehicleEquipment": VehicleEquipmentEnum.from_dict(obj["vehicleEquipment"]) if obj.get("vehicleEquipment") is not None else None,
            "vehicleTypes": [VehicleTypeEnum.from_dict(_item) for _item in obj["vehicleTypes"]] if obj.get("vehicleTypes") is not None else None,
            "vehicleUsage": VehicleUsageEnum.from_dict(obj["vehicleUsage"]) if obj.get("vehicleUsage") is not None else None,
            "yearOfFirstRegistration": obj.get("yearOfFirstRegistration"),
            "grossWeightCharacteristics": [GrossWeightCharacteristic.from_dict(_item) for _item in obj["grossWeightCharacteristics"]] if obj.get("grossWeightCharacteristics") is not None else None,
            "heightCharacteristics": [HeightCharacteristic.from_dict(_item) for _item in obj["heightCharacteristics"]] if obj.get("heightCharacteristics") is not None else None,
            "lengthCharacteristics": [LengthCharacteristic.from_dict(_item) for _item in obj["lengthCharacteristics"]] if obj.get("lengthCharacteristics") is not None else None,
            "widthCharacteristics": [WidthCharacteristic.from_dict(_item) for _item in obj["widthCharacteristics"]] if obj.get("widthCharacteristics") is not None else None,
            "heaviestAxleWeightCharacteristics": [HeaviestAxleWeightCharacteristic.from_dict(_item) for _item in obj["heaviestAxleWeightCharacteristics"]] if obj.get("heaviestAxleWeightCharacteristics") is not None else None,
            "numberOfAxlesCharacteristics": [NumberOfAxlesCharacteristic.from_dict(_item) for _item in obj["numberOfAxlesCharacteristics"]] if obj.get("numberOfAxlesCharacteristics") is not None else None,
            "emissions": Emissions.from_dict(obj["emissions"]) if obj.get("emissions") is not None else None,
            "get_VehicleCharacteristicsExtension": ExtensionType.from_dict(obj["get_VehicleCharacteristicsExtension"]) if obj.get("get_VehicleCharacteristicsExtension") is not None else None
        })
        return _obj


