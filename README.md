# Ask GPT

## Description

A CLI to easily ask GPT-3 questions from your terminal.

## Usage

Ask a question (ensure your question is wrapped in quotes), and then sit back and watch the magic of AI happen.

```text
$ ask-gpt "who is the prime minister of canada?"


The prime minister of Canada is Justin Trudeau.
```

Additionally, you can pass the temperature parameter with `-t <float>` like below.

```text
ask-gpt -t 0.9 "best type of food"                                                     


That really depends on what you are looking for. Some of the most popular types of food include Italian, Chinese, Mexican, Mediterranean, American, French, and Japanese.
```

## Configuration

The [configuration](config.json) parameters to call the model with.

### Currently supported parameters

- `temperature` - The temperature of the model. Higher values will result in more creative responses, but also more mistakes. Lower values will result in more conservative responses. `float` value between 0 and 1 inclusive. The default value is 0.

- `max_tokens` - The maximum number of tokens to generate in the completion. The default value is 1,000. More info on tokens can be found [here](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them).

- `completions_model` - The model to use for completions. The default value is `text-davinci-003`. The list of available models can be found [here](https://platform.openai.com/docs/models/gpt-3).

## Installation

### Pre-requisites

1. Ensure you have `docker` installed. Install it [here](https://docs.docker.com/get-docker/) if you don't yet have it.
2. Create an [OpenAI API key](https://beta.openai.com/account/api-keys) (they have free trial keys), and save it in a safe place.
3. Create a `.env` file in the root of the project and add the following line:

```text
OPENAI_API_KEY=<your api key here>
```

### How to install

1. Clone the repo

2. Build a docker image

```sh
docker build -t ask-gpt .
```

3. You should now be able to run the CLI with docker

```sh
docker run -t ask-gpt "why is docker great?"
```

4. (Optional) For a less verbose command, add an alias to your `.bashrc` or `.zshrc` file, or the equivalent for your shell.

```sh
alias ask-gpt="docker run -t ask-gpt"
```

Now you can use

```sh
ask-gpt "why is docker great?"
```

## Potential Future Enhancements

- add more configuration options
- context memory for follow-up questions

