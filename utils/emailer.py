class Emailer:
    def send(self, to: str, subject: str, body: str) -> str:
        print(f"[DEV SEND] -> {to}: {subject}\n{body}\n"); return "msg_dev_1"
MAIL = Emailer()
