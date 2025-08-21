import re
import math

def calculate_entropy(password):
    charset_size = 0
    if re.search(r"[a-z]", password):
        charset_size += 26
    if re.search(r"[A-Z]", password):
        charset_size += 26
    if re.search(r"\d", password):
        charset_size += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset_size += len("!@#$%^&*(),.?\":{}|<>")

    entropy = len(password) * math.log2(charset_size) if charset_size else 0
    return round(entropy, 2)

def evaluate_strength(password):
    entropy = calculate_entropy(password)
    print(f"\nPassword: {password}")
    print(f"Entropy: {entropy} bits")

    if entropy < 28:
        return "Very Weak – easily guessable"
    elif entropy < 36:
        return "Weak – vulnerable to brute-force"
    elif entropy < 60:
        return "Moderate – decent for general use"
    else:
        return "Strong – secure for sensitive systems"

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    result = evaluate_strength(pwd)
    print(f"Strength Evaluation: {result}")
