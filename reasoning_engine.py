import json

# Load knowledge base from JSON file
def load_knowledge_json(filename='knowledge_base.json'):
    '''Load the knowledge base from a JSON file. If the file does not exist, return an empty knowledge base.'''
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Knowledge base file '{filename}' not found. Starting with an empty knowledge base.")
        return {}

# Convert raw input into structured facts for reasoning
def student_facts(raw_input):
    '''Convert raw user input into structured facts for the reasoning engine.'''
    facts = {}

    gpa = raw_input.get("gpa")
    attendance = raw_input.get("attendance")

    # GPA
    if gpa >= 3.5:
        facts["gpa_category"] = "Above 3.5"
    elif gpa >= 3.0:
        facts["gpa_category"] = "Between 3.0 and 3.49"
    else:
        facts["gpa_category"] = "Below 3.0"

    # Attendance
    if attendance >= 80:
        facts["attendance"] = "Above 80%"
    else:
        facts["attendance"] = "Below 80%"

    # Match JSON keys EXACTLY
    facts["disciplinary_cases"] = raw_input.get("disciplinary", False)
    facts["completed_prerequisites"] = raw_input.get("prerequisites", False)
    facts["outstanding_fees"] = raw_input.get("fees", False)

    return facts

# Forward chaining reasoning engine
def forward_chaining(facts, kb):
    '''Apply the rules in the knowledge base to the given facts and return conclusions and explanations.'''
    conclusions = []
    explanations = []

    for rule in kb["rules"]:
        conditions_met = True
        explanation_details = []

        for key, value in rule["conditions"].items():

            # Handle list values (like GPA range)
            if isinstance(value, list):
                if facts.get(key) not in value:
                    conditions_met = False
                else:
                    explanation_details.append(f"{key} = {facts.get(key)}")

            else:
                if facts.get(key) != value:
                    conditions_met = False
                else:
                    explanation_details.append(f"{key} = {facts.get(key)}")

        if conditions_met:
            conclusions.append(rule["conclusion"])
            explanations.append({
                "rule": rule["name"],
                "details": explanation_details,
                "conclusion": rule["conclusion"]
            })

    return conclusions, explanations

# get user input
def get_user_input():
    '''Prompt the user for input and return it as a structured dictionary.'''
    gpa = float(input("Enter GPA: "))
    attendance = float(input("Enter Attendance (%): "))

    disciplinary = input("Any disciplinary cases? (yes/no): ").lower() == "yes"
    prerequisites = input("Completed prerequisites? (yes/no): ").lower() == "yes"
    fees = input("Any outstanding fees? (yes/no): ").lower() == "yes"

    return {
        "gpa": gpa,
        "attendance": attendance,
        "disciplinary": disciplinary,
        "prerequisites": prerequisites,
        "fees": fees
    }

# display conclusions and explanations
def display_results(conclusions, explanations):
    '''Display the conclusions and explanations in a user-friendly format.'''
    print("\n" + "="*40)
    print("🎓 STUDENT ADVISOR RESULTS")
    print("="*40)

    if conclusions:
        print("\n✅ Conclusions:")
        for c in conclusions:
            print(f"  ✓ {c}")
    else:
        print("\n❌ No conclusions reached.")

    print("\n🧠 Explanation:")
    for exp in explanations:
        print(f"\n➡ {exp['conclusion']}")
        print("   Reason:")
        for detail in exp["details"]:
            print(f"   - {detail}")

# Main execution
if __name__ == "__main__":
    '''Main function to run the reasoning engine.'''
    kb = load_knowledge_json()
    user_input = get_user_input()

    # convert raw input to structured facts
    facts = student_facts(user_input)

    # run reasoning engine
    conclusions, explanations = forward_chaining(facts, kb)

    # display results
    display_results(conclusions, explanations)
