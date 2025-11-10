# Simple local Hugging Face integration using transformers pipeline
# Runs entirely on your machine (CPU), no API keys or quotas
from transformers import pipeline
from typing import Optional

_generator: Optional[object] = None

def get_local_generator():
    global _generator
    if _generator is None:
        # Choose a small, CPU-friendly model
        # distilgpt2 is good for quick tests; swap later if needed
        _generator = pipeline("text-generation", model="distilgpt2")
    return _generator

def generate_reply(prompt: str, max_length: int = 80) -> str:
    generator = get_local_generator()
    # Return only the continuation after the prompt to keep replies clean
    out = generator(prompt, max_length=max_length, num_return_sequences=1)[0]["generated_text"]
    return out[len(prompt):].strip()