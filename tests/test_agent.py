"""Tests for the agent module."""
import os
import pytest
from unittest.mock import patch, MagicMock
from oju import agent


def test_agent_with_custom_system_prompt(create_test_prompt_file):
    """Test agent with a custom system prompt."""
    with patch('oju.providers.call_openai') as mock_call:
        mock_call.return_value = "Test response"
        
        response = agent.Agent(
            agent_name="test_agent",
            model="gpt-4",
            provider="openai",
            api_key="test_key",
            prompt_input="Test input",
            custom_system_prompt="Custom system prompt"
        )
        
        assert response == "Test response"
        mock_call.assert_called_once_with(
            model="gpt-4",
            system_prompt="Custom system prompt",
            prompt="Test input",
            api_key="test_key"
        )


def test_agent_with_prompt_file(tmp_path, monkeypatch):
    """Test agent with prompt loaded from file."""
    # Create test prompt directory and file
    prompt_dir = tmp_path / "oju" / "prompts" / "test_agent"
    prompt_dir.mkdir(parents=True, exist_ok=True)
    prompt_file = prompt_dir / "prompt.txt"
    prompt_content = "Test system prompt from file"
    prompt_file.write_text(prompt_content)
    
    # Mock the file path resolution to use our temp directory
    def mock_join(*args):
        if 'prompts' in args and 'test_agent' in args:
            return str(prompt_file)
        return os.path.join(*args)
    
    monkeypatch.setattr(os.path, 'join', mock_join)
    
    with patch('oju.providers.call_openai') as mock_call:
        mock_call.return_value = "Test response"
        
        response = agent.Agent(
            agent_name="test_agent",
            model="gpt-4",
            provider="openai",
            api_key="test_key",
            prompt_input="Test input"
        )
        
        assert response == "Test response"
        mock_call.assert_called_once_with(
            model="gpt-4",
            system_prompt=prompt_content,
            prompt="Test input",
            api_key="test_key"
        )


def test_agent_missing_prompt_file():
    """Test agent with non-existent prompt file."""
    with pytest.raises(FileNotFoundError) as excinfo:
        agent.Agent(
            agent_name="non_existent_agent",
            model="gpt-4",
            provider="openai",
            api_key="test_key",
            prompt_input="Test input"
        )
    
    assert "Prompt file not found" in str(excinfo.value)


def test_agent_empty_prompt_file(tmp_path, monkeypatch):
    """Test agent with empty prompt file."""
    # Create test prompt directory and empty file
    prompt_dir = tmp_path / "oju" / "prompts" / "test_agent"
    prompt_dir.mkdir(parents=True, exist_ok=True)
    prompt_file = prompt_dir / "prompt.txt"
    prompt_file.write_text("")
    
    # Mock the file path resolution to use our temp directory
    def mock_join(*args):
        if 'prompts' in args and 'test_agent' in args:
            return str(prompt_file)
        return os.path.join(*args)
    
    monkeypatch.setattr(os.path, 'join', mock_join)
    
    with pytest.raises(ValueError) as excinfo:
        agent.Agent(
            agent_name="test_agent",
            model="gpt-4",
            provider="openai",
            api_key="test_key",
            prompt_input="Test input"
        )
    
    assert "is empty" in str(excinfo.value)


def test_agent_missing_api_key():
    """Test agent with missing API key."""
    with pytest.raises(ValueError) as excinfo:
        agent.Agent(
            agent_name="test_agent",
            model="gpt-4",
            provider="openai",
            api_key="",
            prompt_input="Test input",
            custom_system_prompt="Test prompt"
        )
    
    assert "API key" in str(excinfo.value)


def test_agent_empty_prompt_input():
    """Test agent with empty prompt input."""
    with pytest.raises(ValueError) as excinfo:
        agent.Agent(
            agent_name="test_agent",
            model="gpt-4",
            provider="openai",
            api_key="test_key",
            prompt_input=" ",
            custom_system_prompt="Test prompt"
        )
    
    assert "Prompt input cannot be empty" in str(excinfo.value)


def test_unsupported_provider():
    """Test agent with unsupported provider."""
    with pytest.raises(ValueError) as excinfo:
        agent.Agent(
            agent_name="test_agent",
            model="unknown-model",
            provider="unsupported_provider",
            api_key="test_key",
            prompt_input="Test input",
            custom_system_prompt="Test prompt"
        )
    
    assert "Unsupported provider" in str(excinfo.value)

def test_agent_api_error_handling(tmp_path, monkeypatch):
    """Test agent's error handling when API call fails."""
    # Create test prompt directory and file
    prompt_dir = tmp_path / "oju" / "prompts" / "test_agent"
    prompt_dir.mkdir(parents=True, exist_ok=True)
    prompt_file = prompt_dir / "prompt.txt"
    prompt_content = "Test system prompt from file"
    prompt_file.write_text(prompt_content)
    
    # Mock the file path resolution to use our temp directory
    def mock_join(*args):
        if 'prompts' in args and 'test_agent' in args:
            return str(prompt_file)
        return os.path.join(*args)
    
    monkeypatch.setattr(os.path, 'join', mock_join)
    
    with patch('oju.providers.call_openai') as mock_call:
        mock_call.side_effect = Exception("API Error")
        
        with pytest.raises(Exception) as exc_info:
            agent.Agent(
                agent_name="test_agent",
                model="gpt-4",
                provider="openai",
                api_key="test_key",
                prompt_input="Test input"
            )
        
        assert "Error getting completion from openai (gpt-4): API Error" in str(exc_info.value)
        mock_call.assert_called_once()