from .base import Agent
from app.utils.emailer import MAIL
class DealStrikeBot(Agent):
    name = "DealStrikeBot"
    async def handle(self, event):
        out = []
        if event["type"]=="LEAD_READY_FOR_OUTREACH":
            c = event["payload"]["contact"]; subj = event["payload"].get("subject","Quick idea")
            body = event["payload"]["template"].format(**c)
            self.hub.db.log_event("SEQUENCE_SENT", {"contact_id": c["id"]})
            MAIL.send(c["email"], subj, body)
            out.append({"type":"FOLLOWUP_SCHEDULED","payload":{"contact_id":c["id"],"days":3}})
        return out
