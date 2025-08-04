<h1 align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&pause=1000&color=00FF00&vCenter=true&multiline=true&width=435&lines=Hey+%F0%9F%91%8B%2C+I'm+Termwave.;I+Create+Ultimate+Tools.+" alt="Typing SVG" /></h1>

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

- 🧬 Created by: **`Termwave`**
- 📎 Discord: `mfxe`
- 💻 License: MIT
- ⚡ Website: [termwave.in](https://termwave.in) | [termwave.space](https://termwave.space)
---

### 💬 Terminal Quote

```bash
[termwave] ➤ "Hack the planet. Or at least the Discord rate limiter."
```

---

> ⚡ Feel free to fork, tweak, or contribute. Stay safe — and don’t abuse this tool.  
### 📡 IncognitoMail Setup & Access

#### 🛠 1. Setup Your Custom Domain (Required First)

To receive mail on your own domain (e.g. `termwave.in`):

1. Go to [https://incognitomail.co/](https://incognitomail.co/)
2. Navigate to the **⚙️ Settings** tab
3. Under **Custom Domain**, enter: `termwave.in`
4. Add the following MX record in your domain DNS:

```
Host: @  
Value: mail.incognitomail.co  
Priority: 10
```

---

#### 📥 2. Access Your Inbox

After setting up your domain:

1. Go to [https://incognitomail.co/](https://incognitomail.co/)
2. Navigate to the **⚙️ Settings** tab
3. Under **Custom Domain**, enter: `termwave.in`
4. Click **Create Custom Email ID**
5. Enter your email ID (e.g. `verify@termwave.in`)
6. (Optional) Enter your token/password if required
7. Click `Create` to open your inbox


