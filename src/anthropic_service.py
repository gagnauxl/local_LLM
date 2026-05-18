#!/usr/bin/python
import os

from anthropic import Anthropic
from openai import api_key

import IQueryLLM as Illm
from LLM_query import chat_anthropic, get_client

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
        messages = [
            {"role": "user", "content": text}
        ]
        answer = self._LLM_client.messages.create(
            model="claude-opus-4-7",
            max_tokens=1024,
            system=self._system_prompt,
            messages=messages
        )
        return answer.content[0].text
    
    def query_conversation(self, messages: list) -> str:
        llm_client = get_client()
        messages = []
        while True:
            user_message = input('Your input: ')

            if user_message.lower() in {'q', 'exit', 'halt', 'quit'}:
                break

            messages.append({"role": "user", "content": user_message})

            answer = chat_anthropic(llm_client, messages, self._system_prompt)
            print(answer)
            messages.append({"role": "assistant", "content": answer})
        return messages