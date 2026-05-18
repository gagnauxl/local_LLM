#!/usr/bin/python

import requests

import IQueryLLM as Illm
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"

class OllamaClient(Illm.IQueryLLM):
    def __init__(self, system_prompt: str):
        self._system_prompt = system_prompt

    @property
    def system_prompt(self) -> str:
        return self._system_prompt

    def query(self, text: str) -> str:
        messages_with_system_prompt = [
            {"role": "system", "content": self._system_prompt},
            {"role": "user", "content": text}
        ]
        payload = {
            "model": MODEL,
            "messages": messages_with_system_prompt,
            "stream": False
        }
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json()["message"]["content"]
    def query_conversation(self, messages: list) -> str:
        messages_with_system_prompt = [
            {"role": "system", "content": self._system_prompt},
        ]
        messages_with_system_prompt.extend(messages)  # Füge die User-Nachricht hinzu
        payload = {
            "model": MODEL,
            "messages": messages_with_system_prompt,
            "stream": False
        }
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json()["message"]["content"]
    
if __name__ == "__main__":
    client = OllamaClient("haha")
    response = client.query("Wie geht es dir?")
    print(response)