from crewai import Task
from tools import tool
from agents import tech_researcher,writer

# Research task
tech_research_task = Task(
  description=(
    "Identify the  trends in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    
  ),
  expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
  tools=[tool],
  agent=tech_researcher,
)

# News Article
writer_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    
  ),
  expected_output='A 4 paragraph article on {topic} advancements and drew conclusions.',
  tools=[tool],
  agent=writer,
  async_execution=False,
  output_file='article.md'  
)