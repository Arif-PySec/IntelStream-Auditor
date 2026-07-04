import os
import sys
import time
import socket
import requests

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def print_banner():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""
{CYAN}  ___       ___  _ ____  _                                 
 |_ _|_ __ |  _|| / ___|| |_ _ __ ___  __ _ _ __ ___  
  | || '_ \| |_ | \___ \| __| '__/ _ \/ _` | '_ ` _ \ 
  | || | | |  _|| |___) | |_| | |  __/ (_| | | | | | |
 |___|_| |_|_|  |_|____/ \__|_|  \___|\__,_|_| |_| |_|
{GREEN}          [ OSINT FOOTPRINTER & LOG TELEMETRY SUITE ]
          [ Technical Infrastructure: Arif-PySec ]{RESET}
    """
    print(banner)

def username_tracker():
   

    print(f"\n{CYAN}[+] Launching Username OSINT Tracker...{RESET}")
    username = input(f"{YELLOW}Enter target username to scan: {RESET}").strip()
    
    if not username:
        print(f"{RED}[X] Error: Username cannot be blank.{RESET}")
        return

    targets = {
        "GitHub": "https://github.com/{}",
        "GitLab": "https://gitlab.com/{}",
        "Reddit": "https://www.reddit.com/user/{}",
        "LeetCode": "https://leetcode.com/u/{}",
        "Twitch": "https://www.twitch.tv/{}"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print(f"\n{YELLOW}[*] Auditing footprint across platforms for: '{username}'...{RESET}\n")
    time.sleep(0.5)

    for platform, url_template in targets.items():
        url = url_template.format(username)
        try:
            response = requests.get(url, headers=headers, allow_redirects=False, timeout=5)
            if response.status_code == 200:
                print(f"{GREEN}[✓] Found on {platform}:{RESET} {url}")
            elif response.status_code in [301, 302, 404]:
                print(f"{RED}[X] No profile detected on {platform}{RESET}")
            elif response.status_code == 403:
                print(f"{YELLOW}[!] Protected/Blocked on {platform} (Requires Auth){RESET}")
        except requests.RequestException:
            print(f"{YELLOW}[!] Connection timeout on {platform}{RESET}")
            
    input(f"\n{CYAN}Press Enter to return to main menu...{RESET}")


def log_monitor():
   

    log_filename = "security.log"
    
    if not os.path.exists(log_filename):
        with open(log_filename, "w") as f:
            f.write(f"--- LOG MONITOR SUBSYSTEM INITIALIZED [{time.strftime('%X')}] ---\n")

    print(f"\n{CYAN}[+] Active: Monitoring '{log_filename}' for anomalies...{RESET}")
    print(f"{YELLOW}[*] Critical Watchlist: FAILED, UNAUTHORIZED, ROOT, ATTACK{RESET}")
    print(f"{RED} Press Ctrl+C to stop monitoring and return to menu.{RESET}\n")
    
    with open(log_filename, "r") as f:
        f.seek(0, os.SEEK_END)
        try:
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                
                line_upper = line.upper()
                if any(keyword in line_upper for keyword in ["FAILED", "UNAUTHORIZED", "ROOT", "ATTACK"]):
                    print(f"{RED}[ALERT] ⚠️ SUSPICIOUS ACTIVITY DETECTED: {line.strip()}{RESET}")
                else:
                    print(f"{GREEN}[INFO] Log Line: {line.strip()}{RESET}")
        except KeyboardInterrupt:
            print(f"\n{YELLOW}[-] Detaching log monitor...{RESET}")
            time.sleep(1)


def port_scanner():
    """Module C: Scan key Layer 4 ports on a domain or IP with network timeout optimization."""
    print(f"\n{CYAN}[+] Launching Remote Port Scanner...{RESET}")
    target_input = input(f"{YELLOW}Enter target Domain or IP (e.g., scanme.nmap.org): {RESET}").strip()
    
    if not target_input:
        target_input = "127.0.0.1"

    # Step 1: DNS Resolution (Converts domain names like google.com to an actual IP address)
    try:
        print(f"{YELLOW}[*] Resolving target hostname...{RESET}")
        target_ip = socket.gethostbyname(target_input)
        print(f"{GREEN}[✓] Target resolved to IP: {target_ip}{RESET}")
    except socket.gaierror:
        print(f"{RED}[X] Error: Could not resolve hostname. Check your internet connection or URL.{RESET}")
        input(f"\n{CYAN}Press Enter to return to main menu...{RESET}")
        return

    ports_to_scan = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        80: "HTTP",
        8080: "Alternative HTTP", 
        443: "HTTPS"
    }

    
    
    print(f"\n{YELLOW}[*] Scanning remote interfaces (Timeout: 3.5s)...{RESET}\n")
    time.sleep(0.5)

    for port, service in ports_to_scan.items():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3.5) # Dynamic patch for internet latency!
            
            result = s.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"{GREEN}[✓] Port {port} ({service}): OPEN{RESET}")
            else:
                # On the internet, closed often means a firewall dropped our packet
                print(f"{RED}[X] Port {port} ({service}): CLOSED / FILTERED{RESET}")
                
            s.close()
            
        except socket.error:
            print(f"{YELLOW}[!] Network anomaly encountered on port {port}{RESET}")

    input(f"\n{CYAN}Press Enter to return to main menu...{RESET}")

def main():
    while True:
        print_banner()
        print(f"{CYAN}--- MAIN MENU ---{RESET}")
        print(f"{GREEN}[1]{RESET} Run Username OSINT Tracker")
        print(f"{GREEN}[2]{RESET} Run Automated Log Monitor")
        print(f"{GREEN}[3]{RESET} Run Layer 4 Port Scanner")
        print(f"{GREEN}[4]{RESET} Exit Suite")
        
        choice = input(f"\n{YELLOW}Select an option (1-4): {RESET}").strip()
        
        if choice == '1':
            username_tracker()
        elif choice == '2':
            log_monitor()
        elif choice == '3':
            port_scanner()
        elif choice == '4':
            print(f"\n{RED}[-] Shutting down GhostShell. Secure your perimeter.{RESET}\n")
            sys.exit()
        else:
            print(f"\n{RED}[X] Invalid choice. Try again.{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    main()