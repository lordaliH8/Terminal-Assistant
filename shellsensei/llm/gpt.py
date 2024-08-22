from openai import OpenAI
import json
from typing import Tuple
from decouple import config


class GPT:
    def __init__(self, model: str = "gpt-3.5-turbo", OPENAI_API_KEY: str = None):
        self.OPENAI_API_KEY = config("OPENAI_API_KEY") if OPENAI_API_KEY is None else OPENAI_API_KEY
        self.client = OpenAI(api_key=self.OPENAI_API_KEY)

        self.model = model

    def query(
        self,
        user_prompt: str,
        respond_in_json: bool = False,
        return_token_count: bool = False,
    ) -> str | dict | Tuple[str | dict, int, int]:
        """
        :param user_prompt: user prompt to pass to the model
        :param respond_in_json: returns dictionary if True, make sure you specify the JSON schema in the user_prompt
        :param return_token_count: returns input and output tokens if True
        :return: response from the model and [optional] token count
        """
        if respond_in_json:
            completion = self.client.chat.completions.create(
                model=self.model,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": "You are a useful assistant."},
                    {"role": "user", "content": user_prompt},
                ],
            )
            res = json.loads(completion.choices[0].message.content)
        else:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a useful assistant."},
                    {"role": "user", "content": user_prompt},
                ],
            )
            res = completion.choices[0].message.content

        if return_token_count:
            return (
                res,
                completion.usage.prompt_tokens,
                completion.usage.completion_tokens,
            )
        else:
            return res
