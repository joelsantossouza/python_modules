from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol


class ProcessingStage(Protocol):
    """Protocol of a stage: Every stage must have a process()"""

    def process(self, data: Any) -> Any:
        ...


class InputStage:
    """Input validation and parsing"""

    def process(self, data: Any) -> Dict:
        valid: bool = True
        if data is None:
            valid = False
        return {
            "data": data,
            "valid": valid
        }


class TransformStage:
    """Data transformation and enrichment"""

    def process(self, data: Any) -> Dict:
        return {
            "metadata": "Processed",
            "data": data
        }


class OutputStage:
    """Output formatting and delivery"""

    def process(self, data: Any) -> str:
        return f"Output: {data}"


class ProcessingPipeline(ABC):
    """Abstract class of the structure of a pipeline"""

    stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        if isinstance(stage, (InputStage, TransformStage, OutputStage)):
            self.stages.append(stage)
        else:
            print("ERROR: Invalid type of stage")


class JSONAdapter(ProcessingPipeline):
    """Process specific input of type JSON"""

    def __init__(self, pipeline_id: int) -> None:
        if isinstance(pipeline_id, int):
            self.id = pipeline_id
        else:
            print("ERROR: A pipeline ID must be integer")

    def process(self, data: Any) -> Union[str, Any]:
        if not isinstance(data, Dict):
            print("ERROR: You must pass a valid JSON format")
            return None
        sensor: str = "unknown"
        feedback: str = ""
        try:
            if not isinstance(data["sensor"], str) or not isinstance(data["value"], int) or not isinstance(data["unit"], str):
                raise Exception
            if data["sensor"] == "temp":
                sensor: str = "temperature"
                feedback: str = "(Normal range)" if 2 < data["value"] < 30 else "(Critical range)"
            elif data["sensor"] == "humidity":
                sensor: str = "humidity"
                feedback: str = "(Normal range)" if 20 < data["value"] < 70 else "(Critical range)"
            elif data["sensor"] == "pressure":
                sensor: str = "pressure"
                feedback: str = "(Normal range)" if 100 < data["value"] < 1000 else "(Critical range)"
        except Exception:
            print("ERROR: You must provide a sensor type, its value and the measure unit")
            return None
        parsed: str = f"{sensor} reading: {data['value']}{data['unit']} {feedback}"
        for stage in self.stages:
            result: Any = stage.process(parsed)
            if isinstance(result, Dict):
                try:
                    if not result["valid"]:
                        print("ERROR: Invalid processing...")
                        return None
                except Exception:
                    parsed = f"{result['metadata']} {parsed}"
            else:
                parsed = result
        return parsed


class CSVAdapter(ProcessingPipeline):
    """Process specific input of type CSV"""

    def __init__(self, pipeline_id: int) -> None:
        if isinstance(pipeline_id, int):
            self.id = pipeline_id
        else:
            print("ERROR: A pipeline ID must be integer")

    def process(self, data: Any) -> Union[str, Any]:
        if not isinstance(data, str):
            print("ERROR: You must pass a valid CSV format")
            return None
        csv: List[str] = data.split("\n")
        actions: int = 0
        for row in csv:
            if row != "":
                actions += 1
        parsed: str = f"user activity logged: {actions} actions"
        for stage in self.stages:
            result: Any = stage.process(parsed)
            if isinstance(result, Dict):
                try:
                    if not result["valid"]:
                        print("ERROR: Invalid processing...")
                        return None
                except Exception:
                    parsed = f"{result['metadata']} {parsed}"
            else:
                parsed = result
        return parsed


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")

    print("\nInitializing Nexus Manager...")
    test: CSVAdapter = CSVAdapter(100) 
    result: str = test.process("\n\n\n\n")
    print(result)
