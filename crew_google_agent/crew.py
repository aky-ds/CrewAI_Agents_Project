
from crewai import Crew,Process
from tasks import tech_research_task,writer_task
from agents import tech_researcher,writer

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[tech_researcher,writer],
    tasks=[tech_research_task,writer_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'AI in industries'})
print(result)
