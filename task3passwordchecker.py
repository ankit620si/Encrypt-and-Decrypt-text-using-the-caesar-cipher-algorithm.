import re

def assess_password_strength(password):
    # Define criteria checks
    length_ok = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Score the password
    score = sum([length_ok, has_upper, has_lower, has_digit, has_special])

    # Determine strength level
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Generate feedback
    feedback = []
    if not length_ok:
        feedback.append("- Use at least 8 characters.")
    if not has_upper:
        feedback.append("- Include at least one uppercase letter.")
    if not has_lower:
        feedback.append("- Include at least one lowercase letter.")
    if not has_digit:
        feedback.append("- Include at least one number.")
    if not has_special:
        feedback.append("- Include at least one special character (e.g., !, @, #).")

    return strength, feedback

def main():
    print("🔐 Password Strength Checker")
    password = input("Enter your password: ")

    strength, feedback = assess_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for item in feedback:
            print(item)
    else:
        print("Your password is strong! ✅")

if __name__ == "__main__":
    main()
