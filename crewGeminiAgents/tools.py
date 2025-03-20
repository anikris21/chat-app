from dotenv import load_dotenv
load_dotenv()

import os
from crewai_tools import SerperDevTool


os.environ['SERPER_KEY'] = os.getenv('SERPER_KEY')


tool = SerperDevTool()