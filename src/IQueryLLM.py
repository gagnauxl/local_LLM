#!/usr/bin/python

# Interface für LLM-Clients
# Defines contract, but checks only existence of methods, not their implementation
# to check if methods are implemented correctly use:
# python -m mypy .\src\<file_name>.py
from abc import ABC, abstractmethod

class IQueryLLM(ABC):
    @property
    @abstractmethod
    def system_prompt(self) -> str: ...
    @abstractmethod
    def query(self, text: str) -> str:
        pass
    @abstractmethod
    def query_conversation(self, messages: list) -> str:
        pass
