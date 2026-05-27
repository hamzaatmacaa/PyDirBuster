import os
import requests
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama for cross-platform colored terminal outputs
init(autoreset=True)

try:
    print(Fore.CYAN + "=== PROFESSIONAL DIRECTORY BRUTE-FORCER & REPORTER ===")

    # 1. Get target configuration from user
    target_url = input("Enter target URL (e.g., https://example.com): ").strip()
    if not target_url.endswith("/"):
        target_url += "/"

    wordlist_path = input("Enter wordlist file path (e.g., wordlist.txt): ").strip()

    # Check if the wordlist file exists
    if not os.path.exists(wordlist_path):
        print(Fore.RED + f"[-] Error: '{wordlist_path}' file not found! Exiting program.")
        exit()

    # 2. Prepare the report file with a unique timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"scan_report_{timestamp}.txt"

    print(Fore.YELLOW + f"\n[+] Scan started...")
    print(Fore.YELLOW + f"[+] Discovered directories will be saved to '{report_file}'\n")

    # Write initial headers to the report file
    with open(report_file, "w", encoding="utf-8") as report:
        report.write(f"=== CYBERSECURITY SCAN REPORT ===\n")
        report.write(f"Target URL: {target_url}\n")
        report.write(f"Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.write(f"=================================\n\n")

    # 3. Core Scanning Loop
    try:
        with open(wordlist_path, "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                
                # Skip empty lines
                if not word:
                    continue
                    
                test_url = target_url + word
                
                try:
                    # Use a real browser User-Agent to bypass simple security filters
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
                    response = requests.get(test_url, headers=headers, timeout=3)
                    
                    log_text = ""
                    
                    # Check HTTP Status Codes
                    if response.status_code == 200:
                        log_text = f"[+] FOUND!       -> {test_url} (200 OK)"
                        print(Fore.GREEN + log_text)
                    elif response.status_code == 403:
                        log_text = f"[/] FORBIDDEN!   -> {test_url} (403 Forbidden)"
                        print(Fore.YELLOW + log_text)
                    elif response.status_code in [301, 302]:
                        log_text = f"[*] REDIRECT     -> {test_url} (301/302 Redirect)"
                        print(Fore.BLUE + log_text)
                    
                    # Append the discovery to our report if a valid status code is found
                    if log_text:
                        with open(report_file, "a", encoding="utf-8") as report:
                            report.write(log_text + "\n")
                        
                except requests.exceptions.RequestException:
                    # Skip connection timeouts or resolution errors quietly
                    pass

    except Exception as e:
        print(Fore.RED + f"[-] An error occurred while reading file: {e}")

    print(Fore.CYAN + f"\n=== Scanning Task Completed ===")
    print(Fore.CYAN + f"[+] Check your final report here: {report_file}")

# IF USER PRESSES CTRL+C, THIS BLOCK WILL EXECUTE
except KeyboardInterrupt:
    print(Fore.RED + f"\n\n[-] Scan interrupted by user. Exiting cleanly...")
    exit(0)
