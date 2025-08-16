class VectorMemory:
    def make_whisperlink(self, domain: str) -> str:
        return f"https://{domain}/wl?k=abc123"
MEM = VectorMemory()
