from abc import ABC, abstractmethod
from typing import Dict, Any, List
class Agent(ABC):
    name: str = "agent"
    def __init__(self, hub): self.hub = hub
    @abstractmethod
    async def handle(self, event: Dict[str, Any]) -> List[Dict[str, Any]]: ...
