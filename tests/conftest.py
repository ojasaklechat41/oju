"""Test configuration and fixtures for the oju package."""
import os
import pytest
from unittest.mock import Mock, patch

# Sample API responses
SAMPLE_OPENAI_RESPONSE = {
    "choices": [
        {
            "message": {
                "content": "Test response from OpenAI",
                "role": "assistant"
            },
            "finish_reason": "stop",
            "index": 0
        }
    ]
}

SAMPLE_ANTHROPIC_RESPONSE = {
    "content": [
        {
            "text": "Test response from Claude",
            "type": "text"
        }
    ],
    "id": "msg_123",
    "model": "claude-3-opus-20240229",
    "role": "assistant",
    "stop_reason": "end_turn",
    "type": "message",
    "usage": {
        "input_tokens": 10,
        "output_tokens": 20
    }
}

SAMPLE_GEMINI_RESPONSE = {
    "text": "Test response from Gemini"
}

@pytest.fixture
def mock_openai_response():
    """Mock OpenAI response."""
    mock_response = Mock()
    mock_response.choices = [Mock(message=Mock(content="Test response from OpenAI"))]
    return mock_response

@pytest.fixture
def mock_anthropic_response():
    """Mock Anthropic response."""
    mock_response = Mock()
    mock_response.content = [Mock(text="Test response from Claude")]
    return mock_response

@pytest.fixture
def mock_gemini_response():
    """Mock Gemini response."""
    mock_response = Mock()
    mock_response.text = "Test response from Gemini"
    return mock_response

@pytest.fixture
def create_test_prompt_file(tmp_path):
    """Create a temporary prompt file for testing."""
    def _create_file(content="Test system prompt"):
        prompt_dir = tmp_path / "prompts" / "test_agent"
        prompt_dir.mkdir(parents=True, exist_ok=True)
        prompt_file = prompt_dir / "prompt.txt"
        prompt_file.write_text(content)
        return str(prompt_file)
    return _create_file
