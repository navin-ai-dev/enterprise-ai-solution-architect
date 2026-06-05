def manager_agent(text):

    tasks = []

    text = text.lower()

    tasks.append("requirements")
    tasks.append("stories")

    if any(word in text for word in [
        "api",
        "endpoint",
        "rest",
        "service"
    ]):
        tasks.append("api")

    if any(word in text for word in [
        "database",
        "table",
        "storage"
    ]):
        tasks.append("database")

    if any(word in text for word in [
        "security",
        "authentication",
        "authorization"
    ]):
        tasks.append("risk")

    tasks.append("testcases")

    return tasks