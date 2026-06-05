def manager_agent(text):

    tasks = []

    text = text.lower()

    tasks.append("requirements")
    tasks.append("stories")

    if "api" in text:
        tasks.append("api")

    if "database" in text:
        tasks.append("database")

    if "security" in text:
        tasks.append("risk")

    tasks.append("testcases")

    return tasks