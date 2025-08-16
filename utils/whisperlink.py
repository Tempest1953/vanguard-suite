import hashlib
def make_whisperlink(base_domain: str, tag: str, salt: str) -> str:
    sig = hashlib.sha256((tag+salt).encode()).hexdigest()[:8]
    return f"https://{base_domain}/?w={tag}&s={sig}"
