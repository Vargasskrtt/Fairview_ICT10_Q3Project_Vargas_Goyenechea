import random

# List of all possible teams
teams = ["Blue Bears", "Red Bulldogs", "Yellow Tigers", "Green Hornets"]

# Ask the user for details
registration = input("Confirmation of Intramurals online registration (yes/no): ").strip().lower()
medical = input("Confirmation of medical clearance (yes/no): ").strip().lower()
grade_input = input("Grade level (7-11): ").strip()
section = input("Section (Emerald, Ruby, Sapphire, Opaz, Jade): ").strip()

# Turn grade into a number if possible
grade = int(grade_input) if grade_input.isdigit() else None

# Check if the user registered
if registration == "yes":
    # Check if the user has medical clearance
    if medical == "yes":
        # Check if grade is valid (7–10 only)
        if grade is not None and 7 <= grade <= 10:
            # Pick a random team
            team = random.choice(teams)
            print("🎉 Congratulations! You are eligible to join the Intramurals.")
            print(f"Team: {team}")
            print(f"Section: {section}")
        else:
            print("❌ Only students in Grades 7–10 are eligible.")
    else:
        print("❌ You must secure a medical clearance to join the Intramurals.")
else:
    print("❌ You must register online to join the Intramurals.")
