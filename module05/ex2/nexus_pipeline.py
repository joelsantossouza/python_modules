from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol

class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...

class ProcessingPipeline(ABS):
    stages: List[ProcessingStage] = []
