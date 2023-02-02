from dataclasses import dataclass


@dataclass
class Config:
    temperature: float
    max_tokens: int
    completions_model: str


@dataclass
class Usage:
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int


@dataclass
class Answer:
    text: str
    usage: Usage
    estimated_cost: float
