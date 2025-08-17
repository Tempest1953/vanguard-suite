import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Simple email sender
def send_email(to_email: str, subject: str, body: str):
    # Configure your Gmail here
    from_email = "YOUR_GMAIL@gmail.com"
    password = "YOUR_APP_PASSWORD"  # not your real Gmail password (we’ll set this up safely)

    # Build the email
    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        # Connect to Gmail
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        return {"ok": True, "message": "Email sent"}
    except Exception as e:
        return {"ok": False, "error": str(e)}
