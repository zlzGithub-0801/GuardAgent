import os


def openai_config(model):
    if model == 'gpt-3.5-turbo':
        config = {
            "model": "gpt-3.5-turbo",
            # "api_key": "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",
            "api_key": "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",
        }
    else:
        config = {
            "model": "gpt-4",
            # "api_key": "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",
            "api_key": "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",
        }

    return config


def llm_config_list(seed, config_list):
    llm_config_list = {
        "functions": [
            {
                "name": "python",
                "description": "run the entire code and return the execution result. Only generate the code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cell": {
                            "type": "string",
                            "description": "Valid Python code to execute.",
                        }
                    },
                    "required": ["cell"],
                },
            },
        ],
        "config_list": config_list,
        "timeout": 120,
        "cache_seed": seed,
        "temperature": 0,
    }
    return llm_config_list