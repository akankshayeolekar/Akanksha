import re

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[\W_]", password):
        score += 1

    strength = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    return strength[score-1] if score > 0 else "Very Weak"

# Example usage
password = "My$tr0ngP@ss"
print("Password Strength:", check_password_strength(password))