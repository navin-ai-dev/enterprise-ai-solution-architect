from agents.requirement_agent import analyze_requirements
from agents.userstory_agent import generate_user_stories
from agents.api_agent import generate_api_design
from agents.database_agent import generate_database_design
from agents.risk_agent import generate_risk_analysis
from agents.testcase_agent import generate_test_cases
from agents.manager_agent import manager_agent

def run_workflow(text):

    tasks = manager_agent(text)

    results = {}

    if "requirements" in tasks:
        results["requirements"] = analyze_requirements(text)

    if "stories" in tasks:
        results["stories"] = generate_user_stories(text)

    if "api" in tasks:
        results["api"] = generate_api_design(text)

    if "database" in tasks:
        results["database"] = generate_database_design(text)

    if "risk" in tasks:
        results["risk"] = generate_risk_analysis(text)

    if "testcases" in tasks:
        results["testcases"] = generate_test_cases(text)

    return results