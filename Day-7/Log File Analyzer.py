import re

# === Define suspicious patterns ===
THREAT_PATTERNS = [
    r"Failed password",              # SSH brute-force
    r"Invalid user",                 # Unauthorized access
    r"Connection refused",           # Port scan or blocked service
    r"Segmentation fault",           # Crash or exploit attempt
    r"sudo: .*authentication failure",  # Privilege escalation attempt
    r"DROP TABLE",                   # SQL injection
    r"nmap scan",                    # Reconnaissance
    r"XSS attempt",                  # Web exploit
]

def analyze_log(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as log:
            lines = log.readlines()
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return

    print(f"\n🔍 Analyzing log file: {file_path}\n")
    threat_count = 0

    for i, line in enumerate(lines, start=1):
        for pattern in THREAT_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                print(f"⚠️ [Line {i}] Suspicious: {line.strip()}")
                threat_count += 1

    print(f"\n🧠 Threats Detected: {threat_count}")
    if threat_count == 0:
        print("✅ No known threat patterns found.")

if __name__ == "__main__":
    path = input("📄 Enter path to log file: ")
    analyze_log(path)
