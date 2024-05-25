from os import getenv

from phi.llm.openai.like import OpenAILike


class QwenLLM(OpenAILike):
    name: str = "Qwen"
    model: str = "qwen-plus"
    api_key: str = getenv("DASHSCOPE_API_KEY")
    base_url: str = "https://dashscope.aliyuncs.com/compatible-mode/v1"
