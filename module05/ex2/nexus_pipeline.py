from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol


class ProcessingStage(Protocol):
    """Protocol of a stage: Every stage must have a process()"""

    def process(self, data: Any) -> Any:
        ...


class InputStage:
    """Input validation and parsing"""

    def process(data: Any) -> Dict:
        valid: bool = True
        if data is None:
            valid = False
        return {
            "data": data,
            "valid": valid
        }


class TransformStage:
    """Data transformation and enrichment"""

    def process(data: Any) -> Dict:
        return {
            "metadata": "Processed",
            "data": data
        }


class OutputStage:
    """Output formatting and delivery"""

    def process(data: Any) -> str:
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


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")

    print("\nInitializing Nexus Manager...")
