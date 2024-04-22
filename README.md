# self_improving_ai
This AI will follow the prompt and improve its code. It is recommended to use model LLAMA 3 70B or better.
I used a local server using LM studio (PORT 1263 !!!) . This code does not contain a model or server; you must configure the server yourself.

This code uses the local API to instruct the agent to improve itself; the agent sees the log + initial prompt as a prompt. Thus, the agent sees the entire history of his own actions. The agent is instructed to use the command line, and the code in this repository formats the agent's response and executes it through the CMD. Before each run of the code, you must press ENTER (for your safety). Or you can simply remove the very bottom line in the format_answer.py file, which makes the self-improvement recursive and without any human intervention.
To run just use the Run.py file
The Start from scratch.py file will clear the log and the agent will start over, however, I intentionally took the log checkpoint when the agent has already read each of its code files and is ready to improve itself.
Good luck !
I disclaim responsibility for any consequences of the singularity.
