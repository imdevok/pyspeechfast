from typing import Literal

import torch


def make_punctuation_in_text(text: str, lang: Literal["en", "ru"]) -> str:
    """Makes punctuation in input text

    Args:
        text (str): input text without punctuation
        lang (Lang): input text language

    Returns:
        str: object with 'text' field
    """
    model, example_texts, languages, punct, apply_te = torch.hub.load(repo_or_dir='snakers4/silero-models', model='silero_te')

    return apply_te(text, lan=lang)
    
