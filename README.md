# 📁 File Store Bot

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&duration=2500&pause=500&color=33FFAA&width=700&lines=Bot+That+Stores+%26+Shares+Files+via+Special+Links;Includes+Code+System,+Premium+Access,+Shorteners+%26+More!" alt="Bot Features Animation">
</p>

<p align="center">
  <strong>Made with ❤️ by :</strong>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/f7653b1e-e2b1-4897-9de1-f830aca391b6" width="240px" alt="Trinity Mods Logo"/>
</p>

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width="230px" alt="Made with Python">
  </a>
</p>

---

## 🤖 About

**File Store Bot** by **Trinity Mods** is a powerful and flexible Telegram bot that enables secure file storage and sharing through unique links. With advanced features like premium access, shorteners, verification, and more — it’s your complete solution for managing file-based content on Telegram.

---

## 🆕 Changelog Highlights

- 🔐 **Code System** – Share access via simple codes instead of long URLs  
- 🔁 **/ch2l Command** – Instantly convert codes into direct download links  
- 🔗 **Global Shortener Support** – Automatically shorten all links  
- ⏳ **Expiry Timer** – Automatically delete files after a defined period  
- 💎 **Premium Mode** – Monetize your content with tiered access control  

---

## 💡 Key Features

- 📎 Multi-file support with custom captions  
- 🔒 Anti-forwarding (protected content)  
- ➕ Force-subscribe up to 2 channels  
- 🛠️ Fully customizable texts (start, caption, force-sub, etc.)  
- 🔗 Optional shortlink integration with verification  
- 💸 Inbuilt UPI/QR payment system for premium content  

---

## 🚀 Deployment Options

Choose your preferred platform:

<br>

[![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)  
[![Railway Deploy](https://railway.app/button.svg)](https://railway.app/new/template/1jKLr4)  
[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/Trinity-Mods/filestore&branch=main&name=TrinityFileBot)

<br>

Or deploy manually on your VPS:

```bash
git clone https://github.com/Trinity-Mods/filestore.git
cd filestore
pip3 install -r requirements.txt
python3 main.py
```

---

## 📜 Commands Overview

| Command | Description |
|--------|-------------|
| `/start` | Check if the bot is online |
| `/ping` | Ping the bot |
| `/ch2l` | Convert a code into a direct link |
| `/stats` | Bot uptime (admin only) |
| `/users` | View registered user count |
| `/batch` | Generate bulk links (admin only) |
| `/genlink` | Manually create a link (admin only) |
| `/auth` | Grant access + notify owner |
| `/add_prem` | Add premium access (admin only) |
| `/restart` | Restart the bot (admin only) |
| `/admins`, `/add_admin`, `/del_admin` | Admin control commands |

---

## ⚙️ Environment Variables

Refer to the full list in [`.envtemplate`](https://github.com/Trinity-Mods/filestore/blob/main/.envtemplate.txt). Key variables include:

- **TG_BOT_TOKEN, APP_ID, API_HASH** – Telegram Bot credentials  
- **DB_URL, DB_NAME, CHANNEL_ID, OWNER_ID, OWNER_TAG** – Core configurations  
- **USE_SHORTLINK, SHORTLINK_API_KEY, VERIFY_EXPIRE, TUT_VID** – Shortlink & verification  
- **USE_PAYMENT, UPI_ID, UPI_IMAGE_URL, PRICE1–PRICE5** – Payment integration  

---

## 🧙‍♂️ Developers

<p align="center">
  <a href="https://t.me/trinityXmods">
    <img src="https://img.shields.io/badge/🧠 TrinityXmods-Developer-blue?style=for-the-badge&logo=telegram" alt="TrinityXmods">
  </a>
  <br><br>
  <a href="https://t.me/velvetexams">
    <img src="https://img.shields.io/badge/🎓 Dr. Aarav-Architect-blueviolet?style=for-the-badge&logo=telegram" alt="Velvet Exams">
  </a>
  <br><br>
  <a href="https://t.me/the_universal_being">
    <img src="https://img.shields.io/badge/🔬 Ragnar Lothbrok-Mastermind-darkgreen?style=for-the-badge&logo=telegram" alt="The Universal Being">
  </a>
</p>

---

## 🌟 Support & Feedback

If you find this project useful, please:

- ⭐ Star the repo on GitHub  
- 📢 Share it with others  
- 🧑‍💻 Contribute or report issues  

📦 **GitHub**: [Trinity-Mods](https://github.com/Trinity-Mods)  
📢 **Telegram**: [@trinitymods](https://t.me/trinitymods)  
🤝 **Collaborations / Custom Bots**: Contact [@the_universal_being](https://t.me/the_universal_being) directly on Telegram.

> *Built with purpose. Delivered with power.*

---

© 2025 Trinity Mods · Powered by InfoHub Networks
