

import time
from agents.requirement_agent import analyze_requirements
from agents.userstory_agent import generate_user_stories
from agents.api_agent import generate_api_design
from agents.manager_agents import manager_agent
from agents.architecture_agent import generate_architecture
def run_workflow(text):

    tasks = manager_agent(text)

    results = {}

    if "requirements" in tasks:
        results["requirements"] = analyze_requirements(text)

    if "stories" in tasks:
        results["stories"] = generate_user_stories(text)

    if "api" in tasks:
        results["api"] = generate_api_design(text)
        results["architecture"] = generate_architecture(text)
    return results