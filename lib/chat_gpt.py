from typing import Any, cast

import openai

from lib import Answer, Config, Usage

MODELS = ["davinci", "curie", "babbage", "ada"]


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

    usage = Usage(**answer_obj["usage"])

    return Answer(
        text=answer_obj["choices"][0]["text"].strip(),
        usage=usage,
        estimated_cost=get_cost(config, usage),
    )


def get_cost(config: Config, usage: Usage) -> float:
    COST_PER_MILLI = {
        "davinci": 0.02,
        "curie": 0.002,
        "babbage": 0.0005,
        "ada": 0.0004,
    }

    model_in_use = next(filter(lambda m: m in config.completions_model, MODELS))
    return usage.total_tokens / 1000 * COST_PER_MILLI[model_in_use]
