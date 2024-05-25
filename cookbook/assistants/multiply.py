from phi.assistant import Assistant
from phi.llm.alibaba import QwenLLM
from phi.llm.together import Together

from phi.utils.log import set_log_level_to_debug

set_log_level_to_debug()


def multiply(first_int: int, second_int: int) -> str:
    """Multiply two integers together."""
    return str(first_int * second_int)


def add(first_int: int, second_int: int) -> str:
    """Add two integers."""
    return str(first_int + second_int)


def exponentiate(base: int, exponent: int) -> str:
    """Exponentiate the base to the exponent power."""
    return str(base**exponent)


# assistant = Assistant(tools=[multiply, add, exponentiate])
# assistant = Assistant(llm=QwenLLM(), tools=[multiply, add, exponentiate])
assistant = Assistant(llm=Together(), tools=[multiply, add, exponentiate])
# assistant.print_response(
#     "Take 3 to the fifth power and multiply that by the sum of twelve and three, then square the whole result. Only show the result.",
#     stream=False
# )
assistant.print_response(
    "What is the result of multiplying 5 by 7?",
    stream=False
)
