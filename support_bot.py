# -*- coding: utf-8 -*-
"""Subscription billing-text prototype; no AI or Telegram service is implemented."""
from decimal import Decimal, InvalidOperation
from urllib.parse import urlencode
import os
import sys
import json
import logging
from typing import Dict, Any

if hasattr(sys.stdout, "reconfigure"):
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
    try:
        value = Decimal(str(amount_ton)) * Decimal(1000000000)
        if not value.is_finite() or value <= 0 or value != value.to_integral_value():
            raise ValueError("Amount must be positive, finite and exact to nanoTON")
        nano = int(value)
    except InvalidOperation as exc:
        raise ValueError("Invalid TON amount") from exc
    comment = f"SUPPORT-BOT:{plan_name.replace(' ', '_')}"
    return f"ton://transfer/{wallet}?" + urlencode({"amount": nano, "text": comment})

def get_billing_info() -> str:
    lines = ["🤖 **AI Customer Support & Ticket Manager Bot**\n"]
    lines.append("Scope: subscription text and payment-link generation only. No AI, ticket storage or hosted service.\n")
    lines.append("💎 **Example subscription plans (demonstration only):**")
    for s in CONFIG["SUBSCRIPTIONS"]:
        url = generate_tonkeeper_url(s['price_ton'], s['plan'])
        lines.append(f"• **{s['plan']}**: `{s['price_ton']} TON` (${s['price_usdt']} USDT) -> [Pay in Tonkeeper]({url})")
    lines.append(f"\n💵 **Direct USDT (TRC-20):** `{CONFIG['WALLETS']['USDT_TRC20']}`")
    lines.append(f"🌐 **EVM (Base/Polygon):** `{CONFIG['WALLETS']['EVM']}`")
    lines.append(f"⚡ **Solana (SOL):** `{CONFIG['WALLETS']['SOLANA']}`")
    return "\n".join(lines)

if __name__ == "__main__":
    print(get_billing_info())
