from google.adk.agents import LlmAgent
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..", "..")))
from utils.file_loader import load_instructions_file

requirements_writer_agent = LlmAgent(
    name="requirements_writer_agent",
    model="gemini-2.5-flash-lite",
   # The prompt/instruction that tells the agent what kind of behavior to exhibit.
    # It is loaded from a file
    instruction=load_instructions_file("agents/requirements_writer/instructions.txt"),

    # A short summary of what the agent does.
    # It is loaded from a file
    description=load_instructions_file("agents/requirements_writer/description.txt"),
    output_key="requirements_writer_output"
)
