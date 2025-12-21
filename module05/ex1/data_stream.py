from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataStream(ABC):
    """A blueprint of how should data streams classes be organized"""

    def __init__(self, stream_id: str) -> None:
        self.id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...


class SensorStream(DataStream):
    """Sensor to track temperature, humidity and pressure"""

    def process_batch(self, data_batch: List[Any]) -> str:
        readings: int = 0
        total_temp: float = 0
        ntemps: int = 0
        for data in data_batch:
            readings += 1
            try:
                if data[:5] == "temp:":
                    total_temp += float(data[5:])
                    ntemps += 1
            except Exception:
                print(
                    f"ERROR: '{data}' is an invalid value, options:\n"
                    " - temp=value\n"
                    " - humidity=value\n"
                    " - pressure=value\n"
                )
        try:
            avg: float = total_temp / ntemps
        except ZeroDivisionError:
            avg: float = 0
        return f"Sensor analysis: {readings} readings processed, " \
                f"avg temp: {avg}°C"


class TransactionStream(DataStream):
    """Transaction manager counting the profits"""

    def process_batch(self, data_batch: List[Any]) -> str:
        operations: int = 0
        profit: int = 0
        for transaction in data_batch:
            operations += 1
            try:
                if transaction[:4] == "buy:":
                    profit += int(transaction[4:])
                elif transaction[:5] == "sell:":
                    profit -= int(transaction[5:])
            except Exception:
                print(
                    f"ERROR: '{transaction}' is an invalid value, options:\n"
                    " - buy=value\n"
                    " - sell=value\n"
                )
        return f"Transaction analysis: {operations} operations, " \
                f"new flow: {profit:+d} units"


class EventStream(DataStream):
    """Handling event types"""

    def process_batch(self, data_batch: List[Any]) -> str:
        events: int = 0
        errors: int = 0
        for event in data_batch:
            try:
                if event == "error":
                    errors += 1
                events += 1
            except Exception:
                print(f"ERROR: '{event}' is an invalid value")
        return f"Event analysis: {events} events, " \
                f"{errors} error detected"


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    sensor: SensorStream = SensorStream("SENSOR_001")
    input: List[str] = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Stream ID: {sensor.id}, Type: Environmental Data")
    print(f"Processing sensor batch: {input}")
    print(sensor.process_batch(input))

    print("\nInitializing Transaction Stream...")
    transaction: TransactionStream = TransactionStream("TRANS_001")
    input: List[str] = ["buy:100", "sell:150", "buy:75"]
    print(f"Stream ID: {transaction.id}, Type: Financial Data")
    print(f"Processing transaction batch: {input}")
    print(transaction.process_batch(input))

    print("\nInitializing Event Stream...")
    events: EventStream = EventStream("EVENT_001")
    input: List[str] = ["login", "error", "logout"]
    print(f"Stream ID: {events.id}, Type: System Events")
    print(f"Processing event batch: {input}")
    print(events.process_batch(input))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
