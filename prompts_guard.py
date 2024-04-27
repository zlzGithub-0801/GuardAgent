CodeHeader = """import tools
CheckAccess = tools.check_access
"""

Example_Decomposition = """
Agent specification: {agent_specification}
User request: {user_request}
{decomposition_examples}
Agent input: {agent_input}
Agent output: {agent_output}
Task decomposition:
"""

SYSTEM_PROMPT_DECOMPOSITION = """You are the planner of a helpful AI assistant designed to provide guardrail to protect AI agents.
You will be provided with the following information.
1) Agent specification: A description of the agent to be protected, including the input and output to the agent and how the agent works.
2) User request: A description of the desired agent behavior by the user.
3) Agent input: An inference-time input to the agent to be protected.
4) Agent output: An inference-time output by the agent to be protected.
You need to first read the "user request" carefully and then generate a few subtasks for checking whether the "agent input" and the "agent output" satisfy the user request.
You will be provided several related examples.
Follow the examples to complete the "task decomposition" for the given "agent input" and "agent output".
"""

SYSTEM_PROMPT = """You are a helpful AI assistant designed to provide guardrail to protect AI agents.
You will be provided with the following information.
1) Agent specification: A description of the agent to be protected, including the input and output to the agent and how the agent works.
2) User request: A description of the desired agent behavior by the user.
3) Agent input: An inference-time input to the agent to be protected.
4) Agent output: An inference-time output by the agent to be protected.
You need to first read the "user request" carefully and then check whether the "agent input" and the "agent output" satisfy the user request.
This task will be completed in two steps: task decomposition and code generation.
In the task decomposition step, you will be given several examples, following which you decompose the task into multiple subtasks.
In the code generation step, you will be given more examples, following which you generate executable python code based on the task decomposition.
The code you generated will then be executed with the output indicating whether the user request is satisfied or not.
If the user request is satisfied, you will print the output of the agent to be protected.
Otherwise, you need to print the error message specified in the user request.
Print "TERMINATE" in the end when everything is done."""

GuardAgent_Message_Prompt = """You can use the following functions:
(1) CheckAccess
{examples}
(END OF EXAMPLES)
Agent input:
{agent_input}
Agent output:
{agent_output}
Task decomposition:
{subtasks}
Solution: """

DEFAULT_USER_PROXY_AGENT_DESCRIPTIONS = {
    "ALWAYS": "An attentive HUMAN user who can answer questions about the task, and can perform tasks such as running Python code or inputting command line commands at a Linux terminal and reporting back the execution results.",
    "TERMINATE": "A user that can run Python code or input command line commands at a Linux terminal and report back the execution results.",
    "NEVER": "A user that can run Python code or input command line commands at a Linux terminal and report back the execution results.",
}

CodeDebugger = """Given a question:
{subtasks}
The user have written code with the following functions:
(1) CheckAccess

The code is as follows:
{code}

The execution result is:
{error_info}

Please check the code and point out the most possible reason to the error.
"""

