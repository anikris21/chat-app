from crewai import Task
from tools import tool
from agents import researcher, writer
research_task = Task(
    description=(
        "Identify the next big trend in {topic}."
        "Focus on identifying pros and cons and the overall narrative"
        "your final report should clearly articulate the key points, "
        "its market opportunities, and potential risks"
    ),
    expected_output='A comprehensive 3 paragraph long report on the latest AI trends',
    tools=[tool],
    agent=researcher
)

writer_task = Task(
    description=(
        "Compose insightful article on {topic}."
        "Focus on latest trends and how it's impacting the industries"
        "should be easy to understand, engaging and positive"
        "its market opportunities, and potential risks"
    ),
    expected_output='A comprehensive 4 paragraph on {topic} advancements formatted as markdown',
    tools=[tool],
    agent=writer,
    async_execution=False,
    output_file='new-blog-post.md'
    
)

