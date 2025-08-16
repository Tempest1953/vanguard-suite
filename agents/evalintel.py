from .base import Agent
class EvalIntelBot(Agent):
    name="EvalIntelBot"
    async def handle(self, event):
        if event["type"]=="SEQUENCE_SENT": self.hub.db.increment("sends")
        return []
