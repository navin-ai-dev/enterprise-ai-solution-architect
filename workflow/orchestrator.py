from agents.requirement_agent import analyze_requirements
from agents.userstory_agent import generate_user_stories
from agents.api_agent import generate_api_design
from agents.database_agent import generate_database_design
from agents.risk_agent import generate_risk_analysis
from agents.testcase_agent import generate_test_cases


def run_workflow(text):

    results = {}

    results["requirements"] = analyze_requirements(text)

    results["stories"] = generate_user_stories(text)

    results["api"] = generate_api_design(text)

    results["database"] = generate_database_design(text)

    results["risk"] = generate_risk_analysis(text)

    results["testcases"] = generate_test_cases(text)

    return results