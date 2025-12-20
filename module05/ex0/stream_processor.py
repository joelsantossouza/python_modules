from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    """A blueprint for the class of data process"""
    @abstractmethod
    def process(self, data: Any) -> str:
        ...

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Process list of numbers returning the total sum, size, average"""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Validation: Invalid numeric data"
        total: int = 0
        size: int = 0
        for number in data:
            total += number
            size += 1
        avg: float = total / size
        return f"Processed {size} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        try:
            for element in data:
                element + 0
            print("Validation: Numeric data verified")
            return True
        except TypeError:
            return False


class TextProcessor(DataProcessor):
    """Process strings returning the number of words and size"""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Validation: Invalid text data"
        length: int = 0
        nwords: int = 0
        first: bool = True
        for chr in data:
            length += 1
            if (chr >= '\t' and chr <= '\r') or chr == ' ':
                first = True
                continue
            if first:
                nwords += 1
                first = False
        return f"Processed text: {length} characters, {nwords} words"

    def validate(self, data: Any) -> bool:
        try:
            for element in data:
                element + "validation"
            print("Validation: Text data verified")
            return True
        except TypeError:
            return False


class LogProcessor(DataProcessor):
    """Process log information returning a useful message"""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Validation: Invalid log data"
        if data[:7] == "ERROR: ":
            return f"[ALERT] ERROR level detected: {data[7:]}"
        elif data[:6] == "INFO: ":
            return f"[INFO] INFO level detected: {data[6:]}"

    def validate(self, data: Any) -> bool:
        try:
            data + "validation"
        except TypeError:
            return False
        if data[:7] == "ERROR: " or data[:6] == "INFO: ":
            print("Validation: Log entry verified")
            return True
        return False


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    nbrs: list[int] = [1, 2, 3, 4, 5]
    process_nbr: NumericProcessor = NumericProcessor()
    print(f"Processing data: {nbrs}")
    result: str = process_nbr.process(nbrs)
    print(process_nbr.format_output(result))

    print("\nInitializing Text Processor...")
    text: str = "Hello Nexus World"
    process_text: TextProcessor = TextProcessor()
    print(f"Processing data: \"{text}\"")
    result: str = process_text.process(text)
    print(process_text.format_output(result))

    print("\nInitializing Log Processor...")
    log: str = "ERROR: Connection timeout"
    process_log: LogProcessor = LogProcessor()
    print(f"Processing data: \"{log}\"")
    result: str = process_log.process(log)
    print(process_log.format_output(result))

    print("\n=== Polymorphic Processing Demo ===")
