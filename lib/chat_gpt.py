from typing import Generator, cast

import openai

from lib import Config

MODELS = ["davinci", "curie", "babbage", "ada"]


def get_answer(config: Config, prompt: str) -> Generator[str, None, None]:
    completion_generator = cast(
        Generator,
        openai.Completion.create(
            prompt=prompt,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
            model=config.completions_model,
            stream=True,
        ),
    )

    for x in completion_generator:
        yield x["choices"][0]["text"]
