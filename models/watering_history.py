import json
import os
from typing import List, Dict, Any
from datetime import datetime


class WateringRecord:
    def __init__(self, data: str, time: str, status: str, duration: str = "",
                 water_used: str = ""):
        self.data = data
        self.time = time
        self.status = status
        self.duration = duration
        self.water_used = water_used

    def to_dict(self) -> Dict[str, Any]:
        return {
            "data": self.data,
            "time": self.time,
            "status": self.status,
            "duration": self.duration,
            "water_used": self.water_used
        }


class HistoryManager:
    def __init__(self, data_file: str = " data/watering_history.json"):
        self.data_file = data_file
        self.history: List[WateringRecord] = []
        self.load_history()

    def load_history(self) -> List[WateringRecord]:
        try:
            with open(self.data_file, "r", encoding="utf-8") as d_file:
                data = json.load(d_file)
                self.history = [WateringRecord(**i) for i in data.get("history", [])]
            return self.history
        except FileNotFoundError:
            return []

    def save_history(self):
        data = {
            "history": [i.to_dict() for i in self.history]
        }
        with open(self.data_file, "w", encoding="utf-8") as d_file:
            json.dump(data, d_file, ensure_ascii=False, indent=2)

    def add_record(self, plant: str, status: str, duration: str = "", water_used: str = ""):
        now = datetime.now()
        record = WateringRecord(
            date=now.strftime("%Y-%m-%d"),
            time=now.strftime("%H:%M"),
            plant=plant,
            status=status,
            duration=duration,
            water_used=water_used
        )
        self.history.append(record)
        self.save_history()

    def get_all_records(self) -> List[WateringRecord]:
        return self.history

    def get_records_by_plant(self, plant_name: str) -> List[WateringRecord]:
        return [record for record in self.history if record.plant == plant_name]

    def create_sample_data(self):
        pass
