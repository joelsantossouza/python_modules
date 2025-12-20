from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataStream(ABC):
    """A blueprint of how should data streams classes be organized"""

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

class SensorStream(DataStream):
    """Sensor to track temperature, humidity and pressure"""

    def process_batch(self, data_batch: List[Any]) -> str:
        readings: int = 0
        total_temp: int = 0
        ntemps: int = 0
        for data in data_batch:
            readings += 1
            try:
                if data[:5] == "temp:":
                    total_temp += int(data[5:])
                    ntemps += 1
            except Exception:
                print(f"ERROR: '{data}' has invalid value")
        return f"Sensor analysis: {readings} readings processed, " \
                f"avg temp: {total_temp / ntemps}°C"


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    sensor: SensorStream = SensorStream("001")
    print(sensor.process_batch([22.5, 65]))
