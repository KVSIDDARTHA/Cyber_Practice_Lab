import time

def brute_force(target_password, wordlist):
    print(f"\n Starting brute-force simulation for: {target_password}\n")
    for attempt in wordlist:
        print(f"Trying: {attempt}")
        time.sleep(0.2)  # Simulate delay
        if attempt == target_password:
            print(f"\n✅ Password cracked: {attempt}")
            return True
    print("\n Password not found in wordlist.")
    return False

if __name__ == "__main__":
    target = input(" Enter target password: ")
    wordlist = ["123456", "password", "admin", "letmein", "qwerty", "P@ssw0rd", "welcome", "iloveyou"]

    brute_force(target, wordlist)
