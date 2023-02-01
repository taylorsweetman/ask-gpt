# Ask GPT

## Description

A CLI to easily ask GPT-3 questions from your terminal.

## Usage

Ask a question (ensure your question is wrapped in quotes)

```text
$ ask-gpt "who is the prime minister of canada?"
The prime minister of Canada is Justin Trudeau.
```

Ask a question with the verbose flag to see details about token usage, the current config, and the estimated cost of the request.

```text
$ ask-gpt -v "show me a hello world in rust"
fn main() {
    println!("Hello, world!");
}

~~~~~
Usage(completion_tokens=18, prompt_tokens=7, total_tokens=25)
Config(temperature=0, max_tokens=1000, completions_model='text-davinci-003')
Estimated cost: $0.000500
```

## Configuration

The [configuration](config.json) parameters to call the model with.

### Currently supported parameters

- `temperature` - The temperature of the model. Higher values will result in more creative responses, but also more mistakes. Lower values will result in more conservative responses. The default value is 0.

- `max_tokens` - The maximum number of tokens to generate in the completion. The default value is 1,000. More info on tokens can be found [here](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them).

- `completions_model` - The model to use for completion. The default value is `text-davinci-003`. The list of available models can be found [here](https://platform.openai.com/docs/models/gpt-3).

## Installation

### Pre-requisites

1. Ensure you have docker installed.
2. Create an [OpenAI API key](https://beta.openai.com/account/api-keys) (they have free trial keys) and save it in a safe place.
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
docker run ask-gpt "why is docker great?"
```

4. (Optional) For a less verbose command, add an alias to your `.bashrc` or `.zshrc` file, or the equivalent for your shell.

```sh
alias ask-gpt="docker run ask-gpt"
```

Now you can use

```sh
ask-gpt "why is docker great?"
```

## Potential Future Enhancements

- add more configuration options
- stream tokens as they become available
