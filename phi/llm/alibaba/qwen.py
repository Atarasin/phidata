from os import getenv
from typing import Dict, Any

from phi.llm.openai.like import OpenAILike


class QwenLLM(OpenAILike):
    name: str = "Qwen"
    model: str = "qwen-plus"
    api_key: str = getenv("DASHSCOPE_API_KEY")
    base_url: str = "https://dashscope.aliyuncs.com/compatible-mode/v1"

    @property
    def api_kwargs(self) -> Dict[str, Any]:
        _request_params: Dict[str, Any] = {}
        if self.frequency_penalty:
            _request_params["frequency_penalty"] = self.frequency_penalty
        if self.logit_bias:
            _request_params["logit_bias"] = self.logit_bias
        if self.logprobs:
            _request_params["logprobs"] = self.logprobs
        if self.max_tokens:
            _request_params["max_tokens"] = self.max_tokens
        if self.presence_penalty:
            _request_params["presence_penalty"] = self.presence_penalty
        if self.response_format:
            _request_params["response_format"] = self.response_format
        if self.seed:
            _request_params["seed"] = self.seed
        if self.stop:
            _request_params["stop"] = self.stop
        if self.temperature:
            _request_params["temperature"] = self.temperature
        if self.top_logprobs:
            _request_params["top_logprobs"] = self.top_logprobs
        if self.user:
            _request_params["user"] = self.user
        if self.top_p:
            _request_params["top_p"] = self.top_p
        if self.extra_headers:
            _request_params["extra_headers"] = self.extra_headers
        if self.extra_query:
            _request_params["extra_query"] = self.extra_query
        if self.tools:
            _request_params["tools"] = self.get_tools_for_api()
            # qwen does not support tool_choice now
            # if self.tool_choice is None:
            #     _request_params["tool_choice"] = "auto"
            # else:
            #     _request_params["tool_choice"] = self.tool_choice
        if self.request_params:
            _request_params.update(self.request_params)
        return _request_params
