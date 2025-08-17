def send_email(to: str, subject: str, body: str) -> dict:
    """
    Dummy email sender — replace later with real email logic.
    """
    # For now, just pretend we sent it
    return {
        "status": "sent",
        "to": to,
        "subject": subject,
        "preview": body[:50]  # first 50 chars only
    }
