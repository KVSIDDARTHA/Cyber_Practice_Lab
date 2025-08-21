import hashlib
import os

def hash_file(filepath):
    """Generate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f" File not found: {filepath}")
        return None

def verify_integrity(filepath, expected_hash):
    """Compare current hash with expected hash."""
    current_hash = hash_file(filepath)
    if current_hash is None:
        return False
    return current_hash == expected_hash

if __name__ == "__main__":
    file_path = input(" Enter file path to check: ")
    expected = input(" Enter expected SHA-256 hash: ")

    if verify_integrity(file_path, expected):
        print(" Integrity Verified: File is unchanged.")
    else:
        print(" Integrity Compromised: File may have been modified.")
