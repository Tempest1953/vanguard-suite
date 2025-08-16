import asyncio
from typing import Dict, Any
class SwarmHub:
    def __init__(self, db, memory):
        self.db, self.memory = db, memory
        self.agents = []
    def register(self, agent):
        self.agents.append(agent)
    async def emit(self, event: Dict[str, Any]):
        tasks = [a.handle(event) for a in self.agents]
        for outputs in await asyncio.gather(*tasks):
            if outputs:
                for e in outputs:
                    await self.emit(e)
