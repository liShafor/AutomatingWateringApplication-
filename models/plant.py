import json
import os
from typing import Dict, List, Any


class Plant:
    def __init__(self, name: str, type: str, description: str,
                 watering: str, features: str):
        self.name = name
        self.type = type
        self.description = description
        self.watering = watering
        self.features = features

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "type": self.type,
            "description": self.description,
            "watering": self.watering,
            "features": self.features
        }


class PlantManager:
    def __init__(self, data_file: str = "data/plants.json"):
        self.data_file = data_file
        self.plants: List[Plant] = []  # список объектов Plant
        self.load_plants()

    def load_plants(self) -> List[Plant]:
        try:
            with open(self.data_file, "r", encoding="utf-8") as data_file:
                data = json.load(data_file)
                self.plants = [Plant(**i) for i in data.get("plants", [])]
            return self.plants
        except FileNotFoundError:
            return []

    def save_plants(self):
        data = {"plants": [plant.to_dict() for plant in self.plants]}
        with open(self.data_file, "w", encoding="utf-8") as data_file:
            json.dump(data, data_file, ensure_ascii=False, indent=2)

    def get_all_plants(self) -> List[Plant]:
        return self.plants

    def get_plant_by_name(self, name: str) -> Plant:
        for plant in self.plants:
            if plant.name == name:
                return plant
        return None

    def create_sample_data(self):
        pass

