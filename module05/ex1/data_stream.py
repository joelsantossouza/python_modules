from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """A blueprint of how should data streams classes be organized"""

    def __init__(self, stream_id: str) -> None:
        self.id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria != "critical":
            return data_batch
        try:
            ignore: List[Any] = [
                data for data in data_batch
                if (data[:5] == "temp:" and 2 <= float(data[5:]) < 25) or
                (data[:9] == "humidity:" and 20 <= int(data[9:]) < 50) or
                (data[:9] == "pressure:" and 300 <= int(data[9:]) < 1000) or
                (data[:4] == "buy:" and 0 <= int(data[4:]) < 125) or
                (data[:5] == "sell:" and 0 <= int(data[5:]) < 125) or
                (":" not in data)
            ]
            return [data for data in data_batch if data not in ignore]
        except Exception:
            print("ERROR: Invalid data")
            return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "id": {self.id},
            None: None,
            None: None,
            None: None
        }


class SensorStream(DataStream):
    """Sensor to track temperature, humidity and pressure"""

    readings: int = 0
    total_temp: float = 0
    ntemps: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        readings: int = 0
        total_temp: float = 0
        ntemps: int = 0
        for data in data_batch:
            try:
                if data[:5] == "temp:":
                    total_temp += float(data[5:])
                    ntemps += 1
                    readings += 1
                elif data[:9] == "humidity:":
                    readings += 1
                elif data[:9] == "pressure:":
                    readings += 1
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
        self.readings += readings
        self.total_temp += total_temp
        self.ntemps += ntemps
        return f"Sensor analysis: {readings} readings processed, " \
            f"avg temp: {avg}°C"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        try:
            avg: float = self.total_temp / self.ntemps
        except Exception:
            avg: float = 0
        return {
            "id": {self.id},
            "type": "Sensor Stream",
            "readings": {self.readings},
            "avg_temp": {avg},
        }


class TransactionStream(DataStream):
    """Transaction manager counting the profits"""

    operations: int = 0
    profit: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        operations: int = 0
        profit: int = 0
        for transaction in data_batch:
            try:
                if transaction[:4] == "buy:":
                    profit += int(transaction[4:])
                    operations += 1
                elif transaction[:5] == "sell:":
                    profit -= int(transaction[5:])
                    operations += 1
            except Exception:
                print(
                    f"ERROR: '{transaction}' is an invalid value, options:\n"
                    " - buy=value\n"
                    " - sell=value\n"
                )
        self.operations += operations
        self.profit += profit
        return f"Transaction analysis: {operations} operations, " \
            f"net flow: {profit:+d} units"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "id": {self.id},
            "type": "Transaction Stream",
            "operations": {self.operations},
            "profit": {self.profit},
        }


class EventStream(DataStream):
    """Handling event types"""

    events: int = 0
    errors: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        events: int = 0
        errors: int = 0
        for event in data_batch:
            try:
                if event == "error":
                    errors += 1
                    events += 1
                elif event == "login":
                    events += 1
                elif event == "logout":
                    events += 1
            except Exception:
                print(f"ERROR: '{event}' is an invalid value")
                return None
        self.events += events
        self.errors += errors
        return f"Event analysis: {events} events, " \
            f"{errors} error detected"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "id": {self.id},
            "type": "Event Stream",
            "events": {self.events},
            "errors": {self.errors},
        }


class StreamProcessor:
    """Process all type of stream (Sensor, Transaction and Event)"""

    def process_batch(self, data_batch: List[Any]) -> str:
        sensor: SensorStream = SensorStream("SENSOR_002")
        sensor_str: str = sensor.process_batch(data_batch)

        transaction: TransactionStream = TransactionStream("TRANS_002")
        transaction_str: str = transaction.process_batch(data_batch)

        events: EventStream = EventStream("EVENT_002")
        events_str: str = events.process_batch(data_batch)

        return f" - {sensor_str}\n" \
            f" - {transaction_str}\n" \
            f" - {events_str}\n"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        stream: SensorStream = SensorStream(0)
        return stream.filter_data(data_batch, criteria)


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

    print("\n=== Getting Status ===")
    print(f"Sensor: {sensor.get_stats()}")
    print(f"Transaction: {transaction.get_stats()}")
    print(f"Events: {events.get_stats()}")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    stream: StreamProcessor = StreamProcessor()
    input: List[str] = [
        "buy:500", "buy:15", "pressure:100", "error", "temp:-10",
        "login", "sell:500", "logout", "sell:10"
    ]

    print("\nBatch 1 Results:")
    print(stream.process_batch(input))

    print("Stream filtering active: High-priority data only")
    print(f"Filtered results: {stream.filter_data(input, 'critical')}")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
