# 📁 File Store Bot

<p align="center">
  <a href="https://www.python.org">
    <img src="https://ForTheBadge.com/images/badges/made-with-python.svg" width="250">
  </a>
</p>

A fast and scalable Telegram bot to store and retrieve media files via special links.
Built and maintained by **Trinity Mods** under **InfoHub Networks**.

This bot enables creators, admins, and power users to manage, share, and protect digital files effortlessly.

---

## 🛠️ Key Features

* 📦 Store any media (files, videos, documents, etc.) with a unique sharable link
* 🔐 Optional Force Subscribe
* 🚫 Anti-Forward/Protected Mode
* 🌐 Smart Shortlink Integration
* 💳 Premium Mode with Payment Gateway (UPI)
* ⏳ Auto-Delete Timer (Configurable)
* 👥 Admin Management, Stats & Uptime
* 🔗 Batch Link Generation
* ⚙️ Fully Customizable Start/FS/Stats Messages

---

## 🔄 Changelog Highlights

* ✅ Code system: Use `/ch2l` to generate links from unique codes
* 🔐 Fixed force-subscription for single/multiple channels
* ⚙️ Shortlink support with expiry & tutorial
* 💸 Premium verification via UPI and QR Code
* 🔧 Admin tools: add/remove admin, restart, broadcast
* 🔄 Protect content from forwarding (optional)

---

## 🚀 Setup Instructions

### Step 1: Required Commands (BotFather)

```
start - Check whether bot is online 🟢
ch2l - Convert code to link 🧑‍💻
ping - Ping bot 🔄
stats - Bot uptime (admin) ⏱
users - Total users (admin) 👥
batch - Batch link gen (admin) 📂
genlink - Manual link gen (admin) 🔀
```

### Step 2: Deploy

#### Deploy on Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### Deploy on Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/1jKLr4)

#### Deploy on Koyeb

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/Trinity-Mods/filestore&branch=main&name=FileStoreBot)

#### VPS Deployment

```bash
git clone https://github.com/Trinity-Mods/filestore.git
cd filestore
pip3 install -r requirements.txt
# Configure environment variables
python3 main.py
```

---

## 🔑 Required Environment Variables

* `API_HASH` – From [my.telegram.org](https://my.telegram.org/apps)
* `APP_ID` – From [my.telegram.org](https://my.telegram.org/apps)
* `TG_BOT_TOKEN` – From [@BotFather](https://t.me/botfather)
* `OWNER_ID` – Your Telegram ID (use @MissRose\_bot > `/id`)
* `CHANNEL_ID` – Media storage channel ID (e.g. -100xxxxxxxx)
* `DB_URL` – MongoDB connection string (Atlas recommended)
* `DB_NAME` – Name of your DB
* `OWNER_TAG` – Your Telegram handle (without @)

---

## 💎 Premium & Verification (Optional)

* `USE_PAYMENT` – TRUE / FALSE
* `UPI_ID` – Your UPI ID (e.g., abc\@paytm)
* `UPI_IMAGE_URL` – UPI QR image link
* `PRICE1` – ₹20 (7 days)
* `PRICE2` – ₹50 (1 month)
* `PRICE3` – ₹80 (3 months)
* `PRICE4` – ₹150 (6 months)
* `PRICE5` – ₹285 (1 year)

## 🔗 Shortlink System (Optional)

* `USE_SHORTLINK` – TRUE / FALSE
* `SHORTLINK_API_URL` – Your shortlink provider's API endpoint
* `SHORTLINK_API_KEY` – API key
* `VERIFY_EXPIRE` – Expiry in seconds (e.g., 43200 for 12hr)
* `TUT_VID` – Tutorial video for unlocking shortlinks

---

## 🔧 Additional Configurations

* `ADMINS` – Space-separated user IDs of admins
* `START_MESSAGE`, `FORCE_SUB_MESSAGE`, `CUSTOM_CAPTION`, `BOT_STATS_TEXT`, `USER_REPLY_TEXT` – Optional
* `DISABLE_CHANNEL_BUTTON` – TRUE to hide channel buttons
* `PROTECT_CONTENT` – TRUE to block forwarding
* `FORCE_SUB_CHANNEL` – ID of force-subscribe channel
* `TIME` – Auto delete file after X seconds

---

## 🧠 Template Placeholders

Use these in messages:

* `{first}` – First name
* `{last}` – Last name
* `{id}` – Telegram ID
* `{mention}` – User mention
* `{username}` – Username
* `{filename}` – File name
* `{previouscaption}` – Original caption
* `{uptime}` – Bot uptime

---

## 👤 Credits

* 🤖 Built by [@trinityXmods](https://t.me/trinityXmods)
* 🧠 Guided by [@the\_universal\_being](https://t.me/the_universal_being) & [@velvetexams](https://t.me/velvetexams)
* 🧰 Powered by [Pyrogram](https://github.com/pyrogram/pyrogram)

> 🌟 Star this repo if it helped you! ⭐
