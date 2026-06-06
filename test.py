from agents.requirement_agent import analyze_requirements

print("Starting test...")

result = analyze_requirements(
    "Build an Employee Management System with login and attendance."
)

print("Completed")
print(result)