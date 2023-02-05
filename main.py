import argparse
import os

import openai
from dotenv import load_dotenv

from lib import get_answer, get_config


def setup():
    # add API key
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # load config
    config = get_config()

    # parse args
    parser = argparse.ArgumentParser(
        description="Ask ChatGPT a question from your terminal."
    )
    parser.add_argument(
        "question",
        type=str,
        nargs=1,
        help='your question prompt for ChatGPT, make sure you wrap the question in quotes (")',
    )
    args = parser.parse_args()

    return config, args


def main():
    config, args = setup()

    answer = get_answer(config, args.question[0])
    for word in answer:
        print(word, end="")
    print()


if __name__ == "__main__":
    main()
