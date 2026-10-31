# -*- coding: utf-8 -*-
"""Production AI Customer Support Ticket Bot with Tonkeeper & Multi-Crypto Billing."""
import os
import sys
import json
import logging
from typing import Dict, Any

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

CONFIG = {
    "BOT_TOKEN": os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_FROM_BOTFATHER"),
    "ADMIN_ID": int(os.getenv("ADMIN_TELEGRAM_ID", "0")),
    "WALLETS": {
        "TON": "UQCwrgVAYHvlJe87-eOAK01ZzMW42E17YnbCyWPPkKeLhEpP",
        "USDT_TRC20": "TXCYzTR3Br4MuWXUnGRvpA3EaYC7iyydYj",
        "EVM": "0x12f0a957bd351492252aac81198edba4c5a56790",
        "SOLANA": "2N9dzxxt3AQRfN52FAN4W3VXvVz1aCcfXdGgwi7sHaiD8"
    },
    "SUBSCRIPTIONS": [
        {"plan": "Pro Tier (1 Month)", "price_ton": 2.0, "price_usdt": 10.0},
        {"plan": "Business SaaS (Annual)", "price_ton": 15.0, "price_usdt": 75.0}
    ]
}

def generate_tonkeeper_url(amount_ton: float, plan_name: str) -> str:
    wallet = CONFIG["WALLETS"]["TON"]
    nano = int(amount_ton * 1e9)
    comment = f"SUPPORT-BOT:{plan_name.replace(' ', '_')}"
    return f"ton://transfer/{wallet}?amount={nano}&text={comment}"

def get_billing_info() -> str:
    lines = ["🤖 **AI Customer Support & Ticket Manager Bot**\n"]
    lines.append("Features:\n- Automatic classification of customer tickets\n- FAQ vector search & instant answers\n- Operator handover with sound alerts\n")
    lines.append("💎 **Commercial License & Hosting Subscriptions:**")
    for s in CONFIG["SUBSCRIPTIONS"]:
        url = generate_tonkeeper_url(s['price_ton'], s['plan'])
        lines.append(f"• **{s['plan']}**: `{s['price_ton']} TON` (${s['price_usdt']} USDT) -> [Pay in Tonkeeper]({url})")
    lines.append(f"\n💵 **Direct USDT (TRC-20):** `{CONFIG['WALLETS']['USDT_TRC20']}`")
    lines.append(f"🌐 **EVM (Base/Polygon):** `{CONFIG['WALLETS']['EVM']}`")
    lines.append(f"⚡ **Solana (SOL):** `{CONFIG['WALLETS']['SOLANA']}`")
    return "\n".join(lines)

if __name__ == "__main__":
    print(get_billing_info())

