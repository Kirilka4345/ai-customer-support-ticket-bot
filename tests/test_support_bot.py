# -*- coding: utf-8 -*-
"""Unit tests for AI Customer Support Ticket Bot."""
import unittest
import sys
from pathlib import Path

# Add parent directory to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from support_bot import CONFIG, generate_tonkeeper_url, get_billing_info

class TestSupportBot(unittest.TestCase):
    def test_tonkeeper_url_generation(self):
        """Test Tonkeeper deep link generation and plan formatting."""
        url = generate_tonkeeper_url(2.0, "Pro Tier (1 Month)")
        self.assertTrue(url.startswith("ton://transfer/"))
        self.assertIn("amount=2000000000", url)
        self.assertIn("text=SUPPORT-BOT%3APro_Tier_%281_Month%29", url)
        self.assertIn(CONFIG["WALLETS"]["TON"], url)

    def test_wallets_configuration(self):
        """Verify all accepted payment chain wallets exist and match address specifications."""
        wallets = CONFIG.get("WALLETS", {})
        self.assertIn("TON", wallets)
        self.assertIn("USDT_TRC20", wallets)
        self.assertIn("EVM", wallets)
        self.assertIn("SOLANA", wallets)
        self.assertTrue(wallets["TON"].startswith("UQ"))
        self.assertTrue(wallets["USDT_TRC20"].startswith("T"))
        self.assertTrue(wallets["EVM"].startswith("0x"))

    def test_subscriptions_schema(self):
        """Verify subscription plans schema and non-zero pricing."""
        subs = CONFIG.get("SUBSCRIPTIONS", [])
        self.assertGreaterEqual(len(subs), 1)
        for s in subs:
            self.assertIn("plan", s)
            self.assertIn("price_ton", s)
            self.assertIn("price_usdt", s)
            self.assertGreater(s["price_ton"], 0)
            self.assertGreater(s["price_usdt"], 0)

    def test_billing_info(self):
        """Verify formatted billing text contains all plans and deep links."""
        info = get_billing_info()
        self.assertIn("Tonkeeper", info)
        self.assertIn("Direct USDT", info)
        for s in CONFIG["SUBSCRIPTIONS"]:
            self.assertIn(s["plan"], info)

if __name__ == "__main__":
    unittest.main()
