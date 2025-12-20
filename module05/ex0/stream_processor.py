from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union

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


# class LogProcessor(DataProcessor):

test: TextProcessor = TextProcessor()

print(test.process("Hello Nexus World"))
