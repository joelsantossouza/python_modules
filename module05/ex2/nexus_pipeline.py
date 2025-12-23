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

    def process(self, data: Any) -> Any:
        for stage in self.stages:
            result: Any = stage.process(data)
            if isinstance(result, Dict):
                try:
                    if not result["valid"]:
                        print("ERROR: Invalid processing...")
                        return None
                except Exception:
                    data = f"{result['metadata']} {data}"
            else:
                data = result
        return data



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
            if not isinstance(data["sensor"], str) or not isinstance(data["value"], (int, float)) or not isinstance(data["unit"], str):
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
        return super().process(parsed)


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
        return super().process(parsed)


class StreamAdapter(ProcessingPipeline):
    """Process specific input of type Stream"""

    def __init__(self, pipeline_id: int) -> None:
        if isinstance(pipeline_id, int):
            self.id = pipeline_id
        else:
            print("ERROR: A pipeline ID must be integer")

    def process(self, data: Any) -> Union[str, Any]:
        if not isinstance(data, List):
            print("ERROR: You must pass a valid Stream format")
            return None
        total_temp: float = 0
        ntemps: int = 0
        avg: float = 0
        try:
            for nbr in data:
                ntemps += 1
                total_temp += nbr
            avg = total_temp / ntemps
        except Exception:
            print("ERROR: You must provide numbers in list")
            return None
        parsed: str = f"stream summary: {ntemps} readings, avg: {avg}°C"
        return super().process(parsed)


class NexusManager:
    """Orchestral class that holds all types of pipelines"""

    pipelines: List[ProcessingPipeline] = []
    size: int = 0

    def __init__(self, capacity: int) -> None:
        if isinstance(capacity, int) and capacity >= 0:
            self.capacity = capacity
        else:
            print("ERROR: NexusManager capacity must be unsigned integer")

    def add_stages(self, stages: List[ProcessingStage]) -> None:
        if not isinstance(stages, List):
            print("ERROR: Invalid type of stages")
            return
        for stage in stages:
            for pipeline in self.pipelines:
                pipeline.add_stage(stage)

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        if self.size >= self.capacity:
            print("ERROR: Manager cannot hold more pipelines")
            return
        if isinstance(pipeline, (JSONAdapter, CSVAdapter, StreamAdapter)):
            self.pipelines.append(pipeline)
            self.size += 1
        else:
            print("ERROR: Invalid type of pipeline")

    def process_data(self, data: Any, indexes: Optional[List[int]] = None) -> None:
        lst: List[ProcessingPipeline] = []
        if indexes == None:
            lst: List[ProcessingPipeline] = self.pipelines
        else:
            idx: int = 0
            for value in self.pipelines:
                if idx in indexes:
                    lst.append(value)
                idx += 1
        for value in lst:
            result: str = value.process(data)
            if result != None:
                print(result)


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")

    print("\nInitializing Nexus Manager...")
    nexus: NexusManager = NexusManager(1)
    print("Pipeline capacity: 1000 streams/second")

    nexus.add_stages([InputStage(), TransformStage(), OutputStage()])
    print("\nCreating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    print("\n=== Multi-Format Data Processing ===")

    nexus.add_pipeline(JSONAdapter(0))
    input: Dict = {"sensor":"temp", "value":23.5, "unit":"°C"}
    print("\nProcessing JSON data through pipeline...")
    print(f"Input: {input}")
    print("Transform: Enriched with metadata and validation")
    nexus.process_data(input)
