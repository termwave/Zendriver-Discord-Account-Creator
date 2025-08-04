import time
import requests
import psutil
import os
from colorama import init, Fore, Style
import requests
import json
import time
import datetime
import random
from enum import Enum
import asyncio
import string
import zendriver as uc
import multiprocessing
import sys
from pystyle import Center
from notifypy import Notify
import hashlib
from datetime import datetime, timedelta, timezone
import shutil
import tempfile
import re
import base64
from PyQt6.QtCore import Qt, QBuffer, QPropertyAnimation, QEasingCurve, QTimer
from PyQt6.QtGui import QPainter, QColor, QFont, QMovie
from PyQt6.QtWidgets import QSplashScreen, QLabel, QGraphicsOpacityEffect
from PyQt6.QtWidgets import QApplication
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import hmac
import httpx
def resource_path(relative_path):
    """Get absolute path to resource, works for PyInstaller & Nuitka."""
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)
class SplashScreen(QSplashScreen):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        with open(resource_path("data/spinner.gif"), "rb") as gif_file:
            gif_data = gif_file.read()
            self.gif_base64 = base64.b64encode(gif_data)
        self.buffer = QBuffer(self)
        self.buffer.setData(base64.b64decode(self.gif_base64))
        self.buffer.open(QBuffer.OpenModeFlag.ReadOnly)
        self.label = QLabel(self)
        self.movie = QMovie()
        self.movie.setDevice(self.buffer)
        self.label.setMovie(self.movie)
        self.movie.jumpToFrame(0)
        size = self.movie.currentImage().size()
        self.resize(size.width() + 40, size.height() + 40)
        self.label.move(20, 20)
        self.label.resize(size)
        screen = QApplication.primaryScreen().geometry()
        self.move((screen.width() - self.width()) // 2,
                  (screen.height() - self.height()) // 2)
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(1.0)
        self.fade_anim = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_anim.setDuration(600)
        self.fade_anim.setStartValue(1.0)
        self.fade_anim.setEndValue(0.0)
    def start(self):
        self.movie.start()
        self.show()
    def fadeOut(self, callback):
        def on_finished():
            self.hide()
            callback()
        self.fade_anim.finished.connect(on_finished)
        self.fade_anim.start()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(24, 24, 24))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(self.rect(), 14, 14)

class MessageSplashScreen(QSplashScreen):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.resize(240, 120)
        screen = QApplication.primaryScreen().geometry()
        self.move((screen.width() - self.width()) // 2,
                  (screen.height() - self.height()) // 2)
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(0)
        self.fade_in = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_in.setDuration(300)
        self.fade_in.setStartValue(0)
        self.fade_in.setEndValue(1)
        self.fade_in.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.fade_out = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_out.setDuration(600)
        self.fade_out.setStartValue(1)
        self.fade_out.setEndValue(0)
        self.fade_out.setEasingCurve(QEasingCurve.Type.OutCubic)
    def showWithFade(self):
        self.show()
        self.fade_in.start()
    def fadeOut(self, callback):
        def on_finished():
            self.hide()
            callback()
        self.fade_out.finished.connect(on_finished)
        self.fade_out.start()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(24, 24, 24))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(self.rect(), 14, 14)
        painter.setPen(QColor(255, 255, 255))
        font = QFont('Segoe UI', 15, QFont.Weight.Bold)
        painter.setFont(font)
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self.message)

init(autoreset=True)

with open('config.json', 'r') as f:
    config = json.load(f)

class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    SUCCESS = 4
    ERROR = 5
    CRITICAL = 6
class Logger:
    def __init__(self, level: LogLevel = LogLevel.DEBUG):
        self.level = level
        self.prefix = "\033[38;5;176m[\033[38;5;97mtermwave\033[38;5;176m] "
        self.WHITE = "\u001b[37m"
        self.MAGENTA = "\033[38;5;97m"
        self.BRIGHT_MAGENTA = "\033[38;2;157;38;255m"
        self.LIGHT_CORAL = "\033[38;5;210m"
        self.RED = "\033[38;5;196m"
        self.GREEN = "\033[38;5;40m"
        self.YELLOW = "\033[38;5;220m"
        self.BLUE = "\033[38;5;21m"
        self.PINK = "\033[38;5;176m"
        self.CYAN = "\033[96m"
    def get_time(self):
        return datetime.now().strftime("%H:%M:%S")
    def _should_log(self, message_level: LogLevel) -> bool:
        return message_level.value >= self.level.value
    def _write(self, level_color, level_tag, message):
        print(f"{self.prefix}[{self.BRIGHT_MAGENTA}{self.get_time()}{self.PINK}] {self.PINK}[{level_color}{level_tag}{self.PINK}] -> {level_color}{message}{Style.RESET_ALL}")
    def info(self, message: str):
        if self._should_log(LogLevel.INFO):
            self._write(self.CYAN, "!", message)
    def success(self, message: str):
        if self._should_log(LogLevel.SUCCESS):
            self._write(self.GREEN, "Success", message)
    def warning(self, message: str):
        if self._should_log(LogLevel.WARNING):
            self._write(self.YELLOW, "Warning", message)
    def error(self, message: str):
        if self._should_log(LogLevel.ERROR):
            self._write(self.RED, "Error", message)
    def debug(self, message: str):
        if self._should_log(LogLevel.DEBUG):
            self._write(self.BLUE, "DEBUG", message)
    def failure(self, message: str):
        if self._should_log(LogLevel.ERROR):
            self._write(self.RED, "Failure", message)
log = Logger()

def generate_random_name():
    return ''.join(random.choices(string.ascii_letters, k=8))

paassword = "$TermTUSiCE2169#"
def account_ratelimit(email=None, nam=None):
    try:
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/json",
            "DNT": "1",
            "Host": "discord.com",
            "Origin": "https://discord.com",
            "Referer": "https://discord.com/register",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Sec-GPC": "1",
            "TE": "trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
            "X-Debug-Options": "bugReporterEnabled",
            "X-Discord-Locale": "en-US",
            "X-Discord-Timezone": "Asia/Calcutta",
        }
        mailbaba = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))
        email = mailbaba + "@gmail.com"
        nam = generate_random_name()
        data = {
            'email': email,
            'password': paassword,
            'date_of_birth': "2000-09-20",
            'username': email,
            'global_name': nam,
            'consent': True,
            'captcha_service': 'hcaptcha',
            'captcha_key': None,
            'invite': None,
            'promotional_email_opt_in': False,
            'gift_code_sku_id': None
        }
        req = requests.post('https://discord.com/api/v9/auth/register', json=data, headers=headers)
        try:
            resp_data = req.json()
        except Exception as je:
            return 1
        if req.status_code == 429 or 'retry_after' in resp_data:
            limit = resp_data.get('retry_after', 1)
            return int(float(limit)) + 1 if limit else 1
        else:
            return 1
    except Exception as e:
        log.failure(f"❌ Account ratelimit crashed: {e}")
        return 1
    
def countdown_timer(duration):
    for i in range(duration):
        sys.stdout.write(
            f"\r\033[38;5;176m[\033[38;5;97mtermwave\033[38;5;176m] "
            f"[{datetime.now().strftime('%H:%M:%S')}]\033[38;5;176m "
            f"[{Fore.CYAN}!{Style.RESET_ALL}\033[38;5;176m] -> "
            f"{Fore.YELLOW}[{i+1:02d}/{duration}] Waiting before generating next token...{Style.RESET_ALL}"
        )
        sys.stdout.flush()
        time.sleep(1)
    print() 

def close_chrome(profile_dir):
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if 'chrome' in proc.info['name'].lower():
                cmd = ' '.join(proc.info['cmdline']).lower()
                if profile_dir.lower() in cmd:
                    proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    shutil.rmtree(profile_dir, ignore_errors=True)

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

async def click_dropdown_option(tab, expected_text):
    js = f"""
        (() => {{
            const options = document.querySelectorAll('div[class*="option"]');
            for (const opt of options) {{
                if (opt.innerText.trim().toLowerCase() === "{expected_text.lower()}") {{
                    opt.click();
                    return true;
                }}
            }}
            return false;
        }})()
    """
    await tab.evaluate(js)

def poll_for_discord_verification(inbox_id, inbox_token):
    scrambled = "4O)QqiTV+(U+?Vi]qe|6..Xe"
    def get_secret_key():
        return ''.join([chr(ord(c) - 2) for c in scrambled])
    def sign_payload(payload: dict, secret: str):
        message = json.dumps(payload, separators=(',', ':')).encode()
        key = secret.encode()
        return hmac.new(key, message, hashlib.sha256).hexdigest()
    secret = get_secret_key()
    for _ in range(500):
        ts = int(time.time() * 1000)
        payload = {
            "inboxId": inbox_id,
            "inboxToken": inbox_token,
            "ts": ts
        }
        payload["key"] = sign_payload(payload, secret)
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(f"{API_URL}/inbox/v1/list", json=payload, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                items = data.get("items")
                if items:
                    message_url = items[0].get("messageURL")
                    if message_url:
                        email_data = requests.get(message_url, timeout=10).json()
                        subject = email_data.get("subject", "")
                        if "Verify" in subject:
                            content = email_data.get("text", "") + email_data.get("html", "")
                            match = re.search(r'https:\/\/click\.discord\.com[^\s"\'<>\\]+', content)
                            if match:
                                link = match.group(0).split("\n")[0].strip()
                                return link
        except:
            pass
        time.sleep(1)

def send_notification(title, message):
    if not config.get("notify", False):
        return
    try:
        notification = Notify()
        notification.application_name = "Termwave"
        notification.title = title
        notification.message = message
        icon_path = config.get("notification_icon")
        if icon_path and os.path.isfile(icon_path):
            notification.icon = icon_path  
        notification.send()
    except Exception as e:
        log.error(f"❌ Notification error: {e}")

DOMAIN = config.get("mail_domain")
API_URL = config.get("mail_api")
def create_inbox():
    scrambled = "4O)QqiTV+(U+?Vi]qe|6..Xe"
    def get_secret_key():
        return ''.join([chr(ord(c) - 2) for c in scrambled])
    def sign_payload(payload: dict, secret: str):
        message = json.dumps(payload, separators=(',', ':')).encode()
        key = secret.encode()
        return hmac.new(key, message, hashlib.sha256).hexdigest()
    def get_random_fr_ip():
        return f"90.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    timestamp = int(time.time() * 1000)
    payload = {
        "ts": timestamp,
        "domain": DOMAIN
    }
    key = get_secret_key()
    payload["key"] = sign_payload(payload, key)
    fake_ip = get_random_fr_ip()
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "fr-FR,fr;q=0.9",
        "X-Forwarded-For": fake_ip,
        "X-Real-IP": fake_ip,
        "Via": fake_ip
    }
    response = httpx.post(f"{API_URL}/inbox/v2/create", json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["id"], data["token"]
    else:
        raise Exception("Inbox creation failed")
    
async def register_and_get_promo(is_last_instance=False):
    temp_profile_dir = tempfile.mkdtemp(prefix="chrome-profile-")
    driver = await uc.start(options={"user_data_dir": temp_profile_dir})
    tab = await driver.get("https://discord.com/register")
    inbox_id, inbox_token = create_inbox()
    await tab.wait_for_ready_state('complete')
    log.info(f"🕒 Loaded Register Page")
    log.info(f"✉️ Using {inbox_id}")
    username = generate_random_name()
    global_name = "Term </>"
    email_input = await tab.select('input[name="email"]', timeout=120_000)
    if email_input:
        await email_input.send_keys(inbox_id)
    else:
        log.error("❌ Email input not found.")
        return
    global_name_input = await tab.select('input[name="global_name"]', timeout=120_000)
    if global_name_input:
        await global_name_input.send_keys(global_name)
    else:
        log.error("❌ Global name input not found.")
        return
    username_input = await tab.select('input[name="username"]', timeout=120_000)
    if username_input:
        await username_input.send_keys(username)
    else:
        log.error("❌ Username input not found.")
        return
    password_input = await tab.select('input[name="password"]', timeout=120_000)
    if password_input:
        await password_input.send_keys(inbox_token)
    else:
        log.error("❌ Password input not found.")
        return
    month_input = await tab.select('#react-select-2-input', timeout=120_000)
    if month_input:
        month = random.choice(months)
        await month_input.click()
        await month_input.send_keys(month)
        await click_dropdown_option(tab, month)
    else:
        log.error("❌ Month input not found.")
        return
    day_input = await tab.select('#react-select-3-input', timeout=120_000)
    if day_input:
        day = f"{random.randint(1, 28)}"
        await day_input.click()
        await day_input.send_keys(day)
        await click_dropdown_option(tab, day)
    else:
        log.error("❌ Day input not found.")
        return
    year_input = await tab.select('#react-select-4-input', timeout=120_000)
    if year_input:
        year = f"{random.randint(1995, 2005)}"
        await year_input.click()
        await year_input.send_keys(year)
        await click_dropdown_option(tab, year)
    else:
        print("❌ Year input not found.")
        return
    submit_button = await tab.select('button[type="submit"]', timeout=120_000)
    if submit_button:
        await submit_button.mouse_click()
        log.info(f"✅ Submitted Registration Form")
    else:
        log.error("❌ Submit button not found.")
        return
    log.warning(f"⚠️ Please Solve Captcha Manually!")
    send_notification("Ultimate", "⚠️ Please solve the CAPTCHA!")
    for attempt in range(300): 
        try:
            current_url = await tab.evaluate("window.location.href")
            if "discord.com/channels/@me" in current_url:
                log.success("🎉 Captcha sucessfully solved by the user!")
                break
        except Exception as e:
            log.error(f"❌ Error while captcha verification - {e}")
        await asyncio.sleep(1)
    else:
        log.errror("❌ CAPTCHA not solved or redirect failed.")
    verify_url = poll_for_discord_verification(inbox_id, inbox_token)
    log.info("✅ Email Verification link fetched!")
    if verify_url:
        await tab.evaluate(f'''
    (() => {{
        window.open("{verify_url}", "_blank");
        return "ok";
    }})()
''')
    else:
        log.error("❌ Could not find verification link in email.")
    tabs = driver.tabs
    verify_tab = tabs[-1] 
    for attempt in range(60):
        try:
            page_text = await verify_tab.evaluate('''
                (() => {
                    return document.body.innerText || "NO_TEXT_FOUND";
                })()
            ''')
            if "email verified" in page_text.lower():
                log.success("🎉 Email verified successfully!")
                close_chrome(temp_profile_dir)
                try:
                    session = requests.Session()
                    with open('tokens.txt', 'a') as f:
                        payload = {
                            'login': inbox_id,
                            'password': inbox_token,
                        }
                        headers = {
                            'Content-Type': 'application/json',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                            'Origin': 'https://discord.com',
                            'Referer': 'https://discord.com/login'
                        }
                        response = session.post('https://discord.com/api/v9/auth/login', json=payload, headers=headers)
                        try:
                            response_data = response.json()
                            if response.status_code == 200 and 'token' in response_data:
                                token = response_data['token']
                                f.write(f'{inbox_id}:{inbox_token}:{token}\n')
                                f.flush()
                                os.fsync(f.fileno())
                                log.success(f"🎉 Fetched token {token[:25]}"+"***")
                            else:
                                log.failure(f"❌ Failed to login to {inbox_id}. Error: {response_data}")
                        except json.JSONDecodeError:
                            log.failure("F❌ ailed to parse response for {email}. Response: {response.text}")
                except Exception as e:
                    log.error(f"❌Error getting token: {e}")
                break
        except Exception as e:
            log.error("❌ Eval failed: {e}")
        await asyncio.sleep(1)
    else:
        log.error("❌ Email verification not detected in time.")
    try:
        await driver.stop()
    except Exception as e:
        log.error(f"❌ Failed to stop browser: {e}")
    if not is_last_instance and config.get("check_ratelimit", True):
        try:
            wait_time = account_ratelimit()
            log.warning(f"⚠️ Rate limited — waiting {wait_time} seconds...")
            send_notification("Ultimate", f"⚠️ Ratelimited for {wait_time} seconds!")
            countdown_timer(wait_time)
        except Exception as e:
            log.error(f"❌ Failed to check rate limit: {e}")

banner = '''
 █    ██  ██▓  ▄▄▄█████▓ ██▓ ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓▓█████ 
 ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██▒▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▓█   ▀ 
▓██  ▒██░▒██░  ▒ ▓██░ ▒░▒██▒▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒███   
▓▓█  ░██░▒██░  ░ ▓██▓ ░ ░██░▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄ 
▒▒█████▓ ░██████▒▒██▒ ░ ░██░▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░▒████▒
░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░
░░▒░ ░ ░ ░ ░ ▒  ░  ░     ▒ ░░  ░      ░  ▒   ▒▒ ░   ░     ░ ░  ░
 ░░░ ░ ░   ░ ░   ░       ▒ ░░      ░     ░   ▒    ░         ░   
   ░         ░  ░        ░         ░         ░  ░           ░  ░
                                                                
'''
def print_gradient_text(text, start_color=(137, 207, 240), end_color=(25, 25, 112)):
    lines = text.split('\n')
    total_lines = len(lines)
    for i, line in enumerate(lines):
        if not line.strip():
            print(line)
            continue
        r = int(start_color[0] + (end_color[0] - start_color[0]) * i / total_lines)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * i / total_lines)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * i / total_lines)
        color_code = f"\033[38;2;{r};{g};{b}m"
        print(f"{color_code}{line}{Style.RESET_ALL}")            
cret = f'''[+] Creator - Termwave'''
def run_register_and_get_promo(is_last_instance=False):
    asyncio.run(register_and_get_promo(is_last_instance))

def main():
    multiprocessing.freeze_support()
    try:
        instance_count = 1
    except ValueError:
        log.warning("⚠️ Invalid input. Defaulting to 1.")
        instance_count = 1
    try:
        max_runs = int(input(Fore.CYAN + f"[{Fore.MAGENTA}?{Fore.CYAN}] Number of accounts to generate (0 = infinite): "))
    except ValueError:
        log.warning("⚠️ Invalid input. Defaulting to 1 account.")
        max_runs = 1
    run_count = 0
    active_processes = []
    while True:
        active_processes = [p for p in active_processes if p.is_alive()]
        if len(active_processes) < instance_count and (max_runs == 0 or run_count < max_runs):
            run_count += 1
            log.info(f"🚀 Starting account #{run_count}")
            try:
                is_last = (max_runs != 0 and run_count == max_runs)
                p = multiprocessing.Process(target=run_register_and_get_promo, args=(is_last,))
                p.start()
                active_processes.append(p)
            except Exception as e:
                log.failure(f"❌ Failed to launch process: {e}")
        if max_runs and run_count >= max_runs and not active_processes:
            break
        time.sleep(1)
    for p in active_processes:
        p.join(timeout=300)
    log.success("🎉 All account generations completed!")

if __name__ == "__main__":
    multiprocessing.freeze_support()
    import sys
    from PyQt6.QtWidgets import QApplication
    from PyQt6.QtCore import QTimer
    def run_cli_logic():
        print("\n")
        print_gradient_text(Center.XCenter(banner))
        print_gradient_text(Center.XCenter(cret))
        print("\n")
        if not config.get("check_ratelimit", True):
            log.warning("⚠️ Rate limit checking is disabled at config.json.")
        if not config.get("notify", True):
            log.warning("⚠️ Notification Alert is disabled at config.json.")
        main()
    def start_message_splash():
        msg = MessageSplashScreen("Made by mfxe\nEnjoy!")
        msg.showWithFade()
        QTimer.singleShot(2500, lambda: msg.fadeOut(continue_to_main))
    def continue_to_main():
        app.quit()  
        run_cli_logic()
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.start()
    QTimer.singleShot(2500, lambda: splash.fadeOut(start_message_splash))
    app.exec()
