from .base import Agent
from app.utils.whisperlink import make_whisperlink
from app.config import settings
class InvestorLensBot(Agent):
    name="InvestorLensBot"
    async def handle(self, event):
        if event["type"]=="NEW_ACCOUNT":
            acct = event["payload"]["company"]
            contact = self.hub.db.pick_contact(acct["id"])
            hook = f"{acct['name']} + Braylock: reduce time-to-diligence by 70%"
            contact.update({"name":contact.get("name","Leader"),
                            "hook":hook,
                            "whisperlink": make_whisperlink(settings.BASE_DOMAIN, acct["domain"], settings.WHISPERLINK_SALT),
                            "product": event["payload"].get("product","CFOCore.com"),
                            "email": contact.get("email", f"contact@{acct['domain']}"),
                            "company": acct["name"]})
            template = "Hi {name} — quick idea on {product}: {hook}. {whisperlink}"
            return [{"type":"LEAD_READY_FOR_OUTREACH","payload":{"contact":contact,"template":template,"subject":f"Fast idea on {contact['product']}"}}]
        return []
