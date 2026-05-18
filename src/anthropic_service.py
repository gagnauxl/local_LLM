#!/usr/bin/python
import os
from urllib import response

from anthropic import Anthropic
from matplotlib.pylab import block
from openai import api_key

import IQueryLLM as Illm
from anthropic.types import TextBlock

class AnthropicClient(Illm.IQueryLLM):
    def get_client(self) -> Anthropic:
        api_key = os.environ.get("ANTHROPIC_API_KEY")   
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")   
        return Anthropic(api_key= api_key)

    def __init__(self, system_prompt: str):
        self._LLM_client = self.get_client()
        self._system_prompt = system_prompt

    @property
    def system_prompt(self) -> str:
        return self._system_prompt

    def query(self, text: str) -> str:
        answer = self._LLM_client.messages.create(
            model="claude-opus-4-7",
            max_tokens=1024,
            system=self._system_prompt,
            messages=[{"role": "user", "content": text}]
        )
        block = answer.content[0]
        if isinstance(block, TextBlock):
            result = block.text
        else:
            raise RuntimeError(f"Unerwarteter Block-Typ: {type(block).__name__}")
        return result
    
    def query_conversation(self, messages: list) -> str:
        answer = self._LLM_client.messages.create(
            model="claude-opus-4-7",
            max_tokens=1024,
            system=self._system_prompt,
            messages=messages
        )  
        block = answer.content[0]
        if isinstance(block, TextBlock):
            result = block.text
        else:
            raise RuntimeError(f"Unerwarteter Block-Typ: {type(block).__name__}")
        return result