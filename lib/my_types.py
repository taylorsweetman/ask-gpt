from dataclasses import dataclass


@dataclass
class Config:
    temperature: float
    max_tokens: int
    completions_model: str
