print("Welcome to Simple Generative AI Model")
user_input=input("Enter a topic(AI,Resume,Interview,ML):").lower()
print("\nGenerated Content:\n")
if "ai" in user_input:
    print("Artificial Intelligence is transforming industries by automating tasks and improving decision-making.")
elif "resume" in user_input:
    print("A strong resume should highlight your skills, projects, and achievements clearly and professionally.")
elif "interview" in user_input:
    print("Interview preparation requires confidence, communication skills, and strong knowledge of your subject.")
elif "ml" in user_input or "machine learning" in user_input:
    print("Machine Learning allows systems to learn from data and improve performance without explicit programming.")
else:
    print("Generative AI creates meaningful content based on the input provided by the user.")
