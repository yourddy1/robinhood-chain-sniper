"""Token Filter — honeypot detection, rug check"""
import re
class RugChecker:
    DANGER_PATTERNS = [r"honeypot", r"max tx", r"blacklist", r"pause", r"proxy", r"upgradable"]
    def check(self, address: str, source_code: str="") -> dict:
        flags = []
        for p in self.DANGER_PATTERNS:
            if re.search(p, source_code, re.I): flags.append(p)
        return {"address": address, "safe": len(flags)==0, "flags": flags, "risk_level": "HIGH" if len(flags)>=3 else "MEDIUM" if flags else "LOW"}
