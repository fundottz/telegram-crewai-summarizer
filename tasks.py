from crewai import Task

def analysis_task(agent, tools):
    return Task(
        description="Analyze and prioritize the following messages",
        agent=agent,
        tools=tools,
        expected_output="List of prioritized messages with importance scores"
    )

def summary_task(agent):
    return Task(
        description="Create summaries for the prioritized messages",
        agent=agent,
        expected_output="Concise summaries of important messages"
    )

def fetch_messages_task(agent):
    return Task(
        description="Fetch and clean messages from Telegram channels",
        agent=agent,
        tools=[],
        expected_output="List of cleaned messages with id and text"
    )
