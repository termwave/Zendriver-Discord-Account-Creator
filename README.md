
<h1 align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&duration=3000&pause=500&center=true&vCenter=true&width=435&lines=🧠+Ultimate+Discord+Account+Generator;🌐+By+Termwave_;⚡Email+Verification+%7C+Token+Extractor" alt="Typing SVG" />
</h1>

```
 █    ██  ██▓  ▄▄▄█████▓ ██▓ ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓▓█████ 
 ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██▒▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▓█   ▀ 
▓██  ▒██░▒██░  ▒ ▓██░ ▒░▒██▒▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒███   
▓▓█  ░██░▒██░  ░ ▓██▓ ░ ░██░▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄ 
▒▒█████▓ ░██████▒▒██▒ ░ ░██░▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░▒████▒
░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░
░░▒░ ░ ░ ░ ░ ▒  ░  ░     ▒ ░░  ░      ░  ▒   ▒▒ ░   ░     ░ ░  ░
 ░░░ ░ ░   ░ ░   ░       ▒ ░░      ░     ░   ▒    ░         ░   
   ░         ░  ░        ░         ░         ░  ░           ░  ░
```

> 🎯 **Advanced Discord Account Generator**  
> 🧠 Powered by `zendriver`, `Playwright`, `httpx`, and custom PyQt6 splash interface.

---

### 🛠 Features

- ✅ **Auto Registration** with Discord
- 🧩 **Manual CAPTCHA Solving Required** with browser window
- 📧 **Instant Email Verification**
- 🔐 **Token Fetcher** and storage
- 📥 **Inbox system using custom API (hmac-signed)**
- ⚠️ **Rate Limit Detection & Handling**
- 🎨 **Terminal-styled Splash Screens**
- 🔔 **Custom Notification Alerts** (Desktop toast via Notify)

---

### 📦 Requirements

Install all dependencies:

```bash
pip install -r req.txt
```

Or manually install:

```bash
pip install requests psutil colorama zendriver pystyle notify-py PyQt6 urllib3 beautifulsoup4 httpx
```

---

### 🚀 Usage

```bash
python term.py
```

📌 **Note**:  
First, edit your `config.json` with the following:

```json
{
  "check_ratelimit": true,
  "notify": true,
  "notification_icon": "data/pack.ico",
  "mail_api": "https://api.incognitomail.co/",
  "mail_domain": "termwave.in"
}
```

---

### 🔒 Output

Tokens are saved in:

```
tokens.txt ➤ format: email:password:token
```

---

### 👨‍💻 Author

- 🧬 Created by: **`Termwave_`**
- 📎 Discord: `termwave`
- 💻 License: MIT

---

### 💬 Terminal Quote

```bash
[termwave] ➤ "Hack the planet. Or at least the Discord rate limiter."
```

---

> ⚡ Feel free to fork, tweak, or contribute. Stay safe — and don’t abuse this tool.  
