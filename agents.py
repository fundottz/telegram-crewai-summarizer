from crewai import Agent

class NewsAnalyzer(Agent):
    role = 'News Analyzer'
    goal = 'Analyze and prioritize news content from Telegram channels'
    backstory = "You are an expert news analyst who can quickly identify important information and prioritize content based on relevance and importance."
    verbose = True

class ContentSummarizer(Agent):
    role = 'Content Summarizer'
    goal = 'Create concise and informative summaries of news content'
    backstory = "You are a skilled content summarizer who can extract key information and present it in a clear, concise manner."
    verbose = True
