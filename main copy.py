import random  # We bring in Python’s random tool so we can assign teams randomly later

# This is the list of all possible teams students can join
teams = ["Blue Bears", "Red Bulldogs", "Yellow Tigers", "Green Hornets"]

# This is where the student answers some questions and store their answers
registration = input("Confirmation of Intramurals online registration (yes/no): ").strip().lower()  # Did you register online?
medical = input("Confirmation of medical clearance (yes/no): ").strip().lower()  # Do you have medical clearance?
grade_input = input("Grade level (7-11): ").strip()  # What grade are you in?
section = input("Section (Emerald, Ruby, Sapphire, Opaz, Jade): ").strip()  # Which section are you from?

# This part tries to turn the grade into a number, but if the input isn’t a digit, it stays as None
grade = int(grade_input) if grade_input.isdigit() else None

# Now we start checking the answers step by step
if registration == "yes":  # First check: did the student register?
    if medical == "yes":  # Second check: do they have medical clearance?
        if grade is not None and 7 <= grade <= 10:  # Third check: are they in Grade 7–10?
            team = random.choice(teams)  # If all checks pass, we randomly assign them a team
            print("🎉 Congratulations! You are eligible to join the Intramurals.")  # Success message
            print(f"Team: {team}")  # Shows which team they got
            print(f"Section: {section}")  # this shows their section
        else:
            print("❌ Only students in Grades 7–10 are eligible.")  # Error if grade is outside 7–10
    else:
        print("❌ You must secure a medical clearance to join the Intramurals.")  # Error if no medical clearance
else:
    print("❌ You must register online to join the Intramurals.")  # Error if not registered
