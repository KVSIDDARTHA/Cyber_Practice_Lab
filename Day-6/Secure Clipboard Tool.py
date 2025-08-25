import pyperclip
import time
import os
import platform

def clear_clipboard():
    system = platform.system()
    if system == "Windows":
        os.system("echo off | clip")
    elif system == "Linux":
        os.system("xclip -selection clipboard /dev/null")
    elif system == "Darwin":  # macOS
        os.system("pbcopy < /dev/null")
    print("🧹 Clipboard cleared for privacy.")

def secure_clipboard_copy(data, delay=10):
    pyperclip.copy(data)
    print(f"✅ Copied to clipboard. Will auto-clear in {delay} seconds...")
    time.sleep(delay)
    clear_clipboard()

if __name__ == "__main__":
    secret = input("🔐 Enter sensitive data to copy securely: ")
    secure_clipboard_copy(secret, delay=10)
