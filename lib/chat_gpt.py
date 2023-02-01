from typing import Any, cast

import openai

from lib import Answer, Config, Usage


def get_answer(config: Config, prompt: str) -> Answer:
    answer_obj = cast(
        dict[str, Any],
        openai.Completion.create(
            prompt=prompt,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
            model=config.completions_model,
        ),
    )

    return Answer(
        text=answer_obj["choices"][0]["text"].strip(),
        usage=Usage(**answer_obj["usage"]),
    )
