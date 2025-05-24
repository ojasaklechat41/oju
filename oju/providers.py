"""
Module for handling different LLM provider APIs.

This module provides functions to interact with various language model providers
like OpenAI, Anthropic, and Google's Gemini.
"""

from typing import Dict, Any, Optional

from openai import OpenAI, OpenAIError
import anthropic
from anthropic import AnthropicError, RateLimitError, APIConnectionError
import google.generativeai as genai
from google.api_core import exceptions as google_exceptions


def call_openai(model: str, system_prompt: str, prompt: str, api_key: str) -> str:
    """
    Call the OpenAI API with the given parameters.

    Args:
        model: The model to use (e.g., 'gpt-4', 'gpt-3.5-turbo').
        system_prompt: The system prompt to guide the model's behavior.
        prompt: The user's input prompt.
        api_key: The OpenAI API key.

    Returns:
        The generated text response from the model.

    Raises:
        ValueError: If the API key is invalid or missing.
        Exception: For errors during the API call.
    """
    if not api_key:
        raise ValueError("OpenAI API key is required")

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=2000,
        )
        return response.choices[0].message.content or ""
    except OpenAIError as e:
        error_msg = f"OpenAI API error: {str(e)}"
        if "Incorrect API key" in str(e):
            raise ValueError("Invalid OpenAI API key") from e
        raise Exception(error_msg) from e


def call_claude(model: str, system_prompt: str, prompt: str, api_key: str) -> str:
    """
    Call the Anthropic Claude API with the given parameters.

    Args:
        model: The model to use (e.g., 'claude-3-opus-20240229', 'claude-3-sonnet-20240229').
        system_prompt: The system prompt to guide the model's behavior.
        prompt: The user's input prompt.
        api_key: The Anthropic API key.

    Returns:
        The generated text response from the model.

    Raises:
        ValueError: If the API key is invalid or missing.
        Exception: For errors during the API call.
    """
    if not api_key:
        raise ValueError("Anthropic API key is required")

    try:
        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model=model,
            system=system_prompt,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=4000,
            temperature=0.7,
        )
        return response.content[0].text
    except (AnthropicError, RateLimitError, APIConnectionError) as e:
        error_msg = f"Anthropic API error: {str(e)}"
        error_str = str(e).lower()
        if "invalid" in error_str and "api key" in error_str:
            raise ValueError("Invalid Anthropic API key") from e
        raise Exception(error_msg) from e


def call_gemini(model: str, system_prompt: str, prompt: str, api_key: str) -> str:
    """
    Call the Google Gemini API with the given parameters.

    Args:
        model: The model to use (e.g., 'gemini-pro').
        system_prompt: The system prompt to guide the model's behavior.
        prompt: The user's input prompt.
        api_key: The Google AI API key.

    Returns:
        The generated text response from the model.

    Raises:
        ValueError: If the API key is invalid or missing.
        Exception: For errors during the API call.
    """
    if not api_key:
        raise ValueError("Google AI API key is required")

    try:
        genai.configure(api_key=api_key)
        model_instance = genai.GenerativeModel(model_name=model)
        
        # Combine system prompt and user prompt
        full_prompt = f"{system_prompt}\n\nUser: {prompt}\n\nAssistant:"
        
        response = model_instance.generate_content(
            full_prompt,
            safety_settings={
                "HARASSMENT": "BLOCK_NONE",
                "HATE_SPEECH": "BLOCK_NONE",
                "SEXUALLY_EXPLICIT": "BLOCK_NONE",
                "DANGEROUS_CONTENT": "BLOCK_NONE",
            }
        )
        
        if not response.text:
            raise ValueError("No response text was returned from Gemini API")
            
        return response.text
    except (google_exceptions.InvalidArgument, google_exceptions.PermissionDenied) as e:
        # Fixed: Check for "api key" in the error message (case insensitive)
        error_str = str(e).lower()
        if "api key" in error_str:
            raise ValueError("Invalid Google AI API key") from e
        raise Exception(f"Google API error: {str(e)}") from e
    except Exception as e:
        raise Exception(f"Error calling Gemini API: {str(e)}") from e