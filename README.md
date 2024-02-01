# Ionic Commerce tool for Haystack

Ionic Haystack provides an Agent Tool integration to Ionic Commerce. This tool will enable e-commerce for your agent , allowing your users to ask for product recommendations and purchase products through the agent chat interface.

## Installation

You can install the package from PyPI using `pip`:
```sh
python3 -m pip install ionic-haystack
```

or `poetry`:

```sh
poetry add ionic-haystack
```

## Usage
Get started quickly using Ionic Commerce with Haystack by creating an IonicShoppingTool and adding it to your agent's tools.
```python
import os
from haystack.agents import Tool
from haystack.agents.conversational import ConversationalAgent
from haystack.agents.memory import ConversationMemory
from haystack.nodes import PromptNode

from ionic_haystack.prompt_templates import ionic_template
from ionic_haystack.tool import IonicShoppingTool

ionic_node = IonicShoppingTool(api_key="my_ionic_api_key")
ionic_tool = Tool(
    name="Ionic",
    pipeline_or_node=ionic_node,
    description=ionic_template
)

memory = ConversationMemory()
prompt_node = PromptNode("gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY") , max_length=256, stop_words=["Observation:"])
agent = ConversationalAgent(prompt_node, tools=[ionic_tool],  memory=memory, prompt_template="deepset/conversational-agent")
```

## Examples
- Example Ionic Agent: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ioniccommerce/ionic_haystack/blob/main/examples/example_ionic_agent.ipynb)