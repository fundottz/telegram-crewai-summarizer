import asyncio
from crewai import Crew
from agents import NewsAnalyzer, ContentSummarizer
from tools import clean_text, analyze_importance, create_summary
from tasks import analysis_task, summary_task, fetch_messages_task
import config
from telegram_fetcher import TelegramFetcher

class TelegramDigestAgent:
    def __init__(self):
        self.fetcher = TelegramFetcher()
        self.news_analyzer = NewsAnalyzer()
        self.summarizer = ContentSummarizer()

    async def generate_digest(self):
        # Start the Telegram client
        await self.fetcher.client.start()

        # Create tasks for the agents
        fetch_task_obj = fetch_messages_task(self.fetcher)
        analysis_task_obj = analysis_task(self.news_analyzer, [clean_text, analyze_importance])
        summary_task_obj = summary_task(self.summarizer)

        # Create and run the crew
        crew = Crew(
            agents=[self.fetcher, self.news_analyzer, self.summarizer],
            tasks=[fetch_task_obj, analysis_task_obj, summary_task_obj],
            tools=[clean_text, analyze_importance, create_summary],
            verbose=True
        )

        result = crew.kickoff()

        # Format and send the digest
        digest = self.format_digest(result)
        await self.send_digest(digest)

        # Disconnect the Telegram client
        await self.fetcher.client.disconnect()

    def format_digest(self, content: str) -> str:
        """Format the digest content"""
        if config.OUTPUT_SETTINGS['format'] == 'markdown':
            return f"# Daily News Digest\n\n{content}"
        return content

    async def send_digest(self, digest: str):
        """Send the digest to the specified destination"""
        if config.OUTPUT_SETTINGS['send_to'] == 'saved_messages':
            await self.fetcher.client.send_message('me', digest)
        else:
            # Add logic for other destinations
            pass

async def main():
    agent = TelegramDigestAgent()
    await agent.generate_digest()

if __name__ == "__main__":
    asyncio.run(main())
