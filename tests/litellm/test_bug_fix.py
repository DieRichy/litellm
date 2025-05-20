from crewai import Agent
from src.Tools import search_tool,scrape_tool,read_resume,semantic_search_resume
from crewai import LLM

# LLM Config
llm = LLM(model="ollama/deepseek-llm:latest", base_url="http://localhost:11434")

# Research Agent 1
researcher = Agent(
    role="Tech Job Researcher",
    goal="Make sure to do amazing analysis on job posting to help job applicants",
    tools=[scrape_tool, search_tool],
    llm=llm,
    verbose=True,
    backstory=(
        "As a Job Researcher, your prowess in navigating and extracting "
        "critical information from job postings is unmatched. Your skills "
        "help pinpoint the necessary qualifications and skills sought by "
        "employers, forming the foundation for effective application tailoring."
    )
)
