# ⚡ ai-customer-support-ticket-bot

> **24/7 AI-Powered Telegram & Web Customer Support Ticket Bot with Operator Handover & Multi-Chain Crypto Billing.**

[![Latest Release](https://img.shields.io/github/v/release/Kirilka4345/ai-customer-support-ticket-bot?style=for-the-badge&logo=github&color=success)](https://github.com/Kirilka4345/ai-customer-support-ticket-bot/releases/latest)
[![Download Zip](https://img.shields.io/badge/Download_v1.0.0-ZIP-blue?style=for-the-badge&logo=zip)](https://github.com/Kirilka4345/ai-customer-support-ticket-bot/releases/download/v1.0.0/AI-Customer-Support-Ticket-Bot-v1.0.zip)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 🚀 Overview

**ai-customer-support-ticket-bot** is an asynchronous Python boilerplate built to automate customer service inquiries, handle recurring FAQ questions, structure support tickets, and seamlessly escalate complex issues to human operators inside Telegram.

### 🤖 Core Capabilities
- **Automated Ticket Triage:** Categorizes incoming client requests (billing, technical, feature requests, general inquiry).
- **Instant FAQ Resolution:** Provides immediate answers based on your knowledge base, reducing operator load by up to 80%.
- **Seamless Operator Handover:** Transfers active chat threads to human managers with one click, preserving conversation context.
- **Multi-Chain Subscription Billing:** Integrated billing for premium service tiers via TON, USDT (TRC-20), EVM, and Solana with Tonkeeper deeplinks.
- **Persistent State Storage:** Stores open/resolved tickets and user profiles in SQLite / PostgreSQL.

---

## ⚡ Quickstart

### 1. Installation
Clone the repository or [download the release package](https://github.com/Kirilka4345/ai-customer-support-ticket-bot/releases/download/v1.0.0/AI-Customer-Support-Ticket-Bot-v1.0.zip):

```bash
git clone https://github.com/Kirilka4345/ai-customer-support-ticket-bot.git
cd ai-customer-support-ticket-bot
pip install -r requirements.txt
```

### 2. Configuration
Copy `config.example.json` and configure your Telegram bot token and operator Telegram ID:

```json
{
  "bot_token": "YOUR_TELEGRAM_BOT_TOKEN",
  "admin_id": 123456789,
  "wallets": {
    "TON": "UQCwrgVAYHvlJe87-eOAK01ZzMW42E17YnbCyWPPkKeLhEpP",
    "USDT_TRC20": "TXCYzTR3Br4MuWXUnGRvpA3EaYC7iyydYj",
    "EVM": "0x12f0a957bd351492252aac81198edba4c5a56790",
    "SOLANA": "2N9dzxxt3AQRfN52FAN4W3VXvVz1aCcfXdGgwi7sHaiD8"
  }
}
```

### 3. Run
```bash
python support_bot.py
# or double-click run_bot.bat on Windows
```

---

## 💼 Custom Support Bot Development & Enterprise Integrations

Need an AI customer support bot connected to your CRM (HubSpot, Notion, Bitrix24), Zendesk, or custom website chat widget?

I build turnkey customer service automation systems:
- **Integrations:** Telegram, Web Widget, WhatsApp Business API, CRM webhooks.
- **AI Brain:** Custom knowledge base training on your documentation, PDFs, and website FAQs.
- **SLA & Analytics:** Escalation timers, operator response time analytics, and satisfaction rating polls.

### 📩 Contact & Inquiries
- **GitHub:** [@Kirilka4345](https://github.com/Kirilka4345)
- **Direct Crypto Licensing ($15 – $49):**
  - **TON:** `UQCwrgVAYHvlJe87-eOAK01ZzMW42E17YnbCyWPPkKeLhEpP`
  - **USDT (TRC-20):** `TXCYzTR3Br4MuWXUnGRvpA3EaYC7iyydYj`
  - **EVM (Base / ETH):** `0x12f0a957bd351492252aac81198edba4c5a56790`
