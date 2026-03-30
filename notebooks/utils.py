import os
from dotenv import load_dotenv
from anthropic import AnthropicVertex


def setup_client():
    load_dotenv()
    
    client = AnthropicVertex(
        region=os.environ["GCP_REGION"],
        project_id=os.environ["GCP_PROJECT_ID"],
    )

    model = os.environ["CLAUDE_MODEL"]
    
    return client, model


def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})


def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})


def chat(client, model, messages, system=None, temperature=1.0):
    parameters = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
    }

    if system:
        parameters["system"] = system
    
    message = client.messages.create(**parameters)

    return message.content[0].text
