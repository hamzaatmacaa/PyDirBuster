# PyDirBuster - Automated Directory Brute-Forcer

A lightweight, beginner-friendly Red Team automation tool written in Python. It scans web servers for hidden directories and sensitive files using a custom wordlist and automatically logs discovered valid endpoints.

## 💡 Inspiration & Relationship to DirBuster
This project is heavily inspired by legendary cybersecurity tools like **DirBuster** and its modern counterparts like **Gobuster** and **ffuf**. 

**PyDirBuster** is a lightweight Python clone designed to help understand the **Core Engine** logic behind these professional tools. Just like them, it analyzes HTTP status codes (`200`, `403`, `301/302`) to uncover hidden directories during the reconnaissance phase of a penetration test.

## ✨ Features
* **Multi-Status Tracking:** Detects `200 OK` (Accessible), `403 Forbidden` (Restricted/Protected), and `301/302 Redirect` codes.
* **Pre-configured Wordlist:** Comes packaged with a curated `wordlist.txt` containing 50+ of the most commonly targeted directories in real pentests.
* **Automated Reporting:** Saves all successfully discovered paths into a unique text report named with a precise timestamp.
* **WAF Bypass Capabilities:** Mimics a legitimate browser by utilizing a custom `User-Agent` header to prevent instant detection by basic bot filters.
* **Colorized Console Output:** Uses `colorama` for clean visual scanning logs (Green = Found, Yellow = Forbidden, Blue = Redirect).

## 🚀 Installation & Usage

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com
   cd PyDirBuster
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the tool (You can use the built-in `wordlist.txt` or supply your own):
   ```bash
   python3 PyDirBuster.py
   ```

## 📋 Requirements (`requirements.txt`)
Ensure you have a `requirements.txt` file in your main directory containing the following:
```text
requests
colorama
```

## 🛠️ Roadmap (Future Enhancements)
Planned updates for upcoming releases of this tool:
* **Multithreading:** Implementing concurrent requests to significantly increase scan speed.
* **Recursive Scanning:** Automatically diving deeper into discovered subdirectories for exhaustive enumeration.

## ⚠️ Disclaimer
This tool was developed strictly for educational purposes, security awareness, and ethical penetration testing. Do not run this script against any server or infrastructure without explicit, written permission from the target owner. The author accepts no liability for any unauthorized actions, misuse, or damage caused by this utility.
