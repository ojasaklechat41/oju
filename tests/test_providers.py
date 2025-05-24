"""Tests for the providers module."""
import pytest
from unittest.mock import patch, MagicMock
from openai import OpenAIError
import anthropic
import google.generativeai as genai
from google.api_core import exceptions as google_exceptions

from oju.providers import (
    call_openai,
    call_claude,
    call_gemini
)


def test_call_openai_success():
    """Test successful OpenAI API call."""
    with patch('oju.providers.OpenAI') as mock_openai:
        # Setup mock response
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_choice = MagicMock()
        mock_message = MagicMock()
        
        mock_message.content = "Test response from OpenAI"
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client
        
        # Call the function
        response = call_openai(
            model="gpt-4",
            system_prompt="Test system prompt",
            prompt="Test input",
            api_key="test_key"
        )
        
        # Assertions
        assert response == "Test response from OpenAI"
        mock_openai.assert_called_once_with(api_key="test_key")
        mock_client.chat.completions.create.assert_called_once()


def test_call_openai_invalid_key():
    """Test OpenAI API call with invalid API key."""
    with patch('oju.providers.OpenAI') as mock_openai:
        mock_client = MagicMock()
        mock_client.chat.completions.create.side_effect = OpenAIError(
            "Incorrect API key provided"
        )
        mock_openai.return_value = mock_client
        
        with pytest.raises(ValueError) as excinfo:
            call_openai(
                model="gpt-4",
                system_prompt="Test system prompt",
                prompt="Test input",
                api_key="invalid_key"
            )
        
        assert "Invalid OpenAI API key" in str(excinfo.value)


def test_call_claude_success():
    """Test successful Anthropic Claude API call."""
    with patch('oju.providers.anthropic.Anthropic') as mock_anthropic:
        # Setup mock response
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_content = MagicMock()
        
        mock_content.text = "Test response from Claude"
        mock_response.content = [mock_content]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client
        
        # Call the function
        response = call_claude(
            model="claude-3-opus-20240229",
            system_prompt="Test system prompt",
            prompt="Test input",
            api_key="test_key"
        )
        
        # Assertions
        assert response == "Test response from Claude"
        mock_anthropic.assert_called_once_with(api_key="test_key")
        mock_client.messages.create.assert_called_once()


def test_call_claude_invalid_key():
    """Test Claude API call with invalid API key."""
    with patch('oju.providers.anthropic.Anthropic') as mock_anthropic:
        # Create a mock client
        mock_client = MagicMock()
        
        # Create a mock exception that will be raised by the API call
        class MockAPIStatusError(Exception):
            def __init__(self, message, response=None, body=None):
                self.message = message
                self.response = response
                self.body = body
                super().__init__(message)
        
        # Set up the side effect to raise our custom exception
        mock_client.messages.create.side_effect = MockAPIStatusError(
            "Invalid API key",
            response=MagicMock(status_code=401),
            body={"error": {"type": "authentication_error"}}
        )
        
        mock_anthropic.return_value = mock_client
        
        # Import the actual exceptions to patch them
        from oju.providers import AnthropicError, RateLimitError, APIConnectionError
        
        # Patch the exception classes to use our mock
        with patch('oju.providers.AnthropicError', MockAPIStatusError), \
             patch('oju.providers.RateLimitError', MockAPIStatusError), \
             patch('oju.providers.APIConnectionError', MockAPIStatusError):
            
            with pytest.raises(ValueError) as excinfo:
                call_claude(
                    model="claude-3-opus-20240229",
                    system_prompt="Test system prompt",
                    prompt="Test input",
                    api_key="invalid_key"
                )
            
            # Verify the error message contains the expected text
            assert "Invalid Anthropic API key" in str(excinfo.value)


def test_call_gemini_success():
    """Test successful Google Gemini API call."""
    with patch('oju.providers.genai') as mock_genai:
        # Setup mock response
        mock_model = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "Test response from Gemini"
        mock_model.generate_content.return_value = mock_response
        mock_genai.GenerativeModel.return_value = mock_model
        
        # Call the function
        response = call_gemini(
            model="gemini-pro",
            system_prompt="Test system prompt",
            prompt="Test input",
            api_key="test_key"
        )
        
        # Assertions
        assert response == "Test response from Gemini"
        mock_genai.configure.assert_called_once_with(api_key="test_key")
        mock_genai.GenerativeModel.assert_called_once_with(model_name="gemini-pro")
        mock_model.generate_content.assert_called_once()


def test_call_gemini_invalid_key():
    """Test Gemini API call with invalid API key."""
    # Import the actual exception to patch it
    from oju.providers import google_exceptions
    
    # Create a mock for the exception
    class MockInvalidArgument(Exception):
        pass
    
    # Patch the genai module
    with patch('oju.providers.genai') as mock_genai:
        # Set up the side effect to raise our custom exception
        mock_genai.configure.side_effect = MockInvalidArgument("API key not valid")
        
        # Patch the exception class to use our mock
        with patch('oju.providers.google_exceptions.InvalidArgument', MockInvalidArgument):
            with pytest.raises(ValueError) as excinfo:
                call_gemini(
                    model="gemini-pro",
                    system_prompt="Test system prompt",
                    prompt="Test input",
                    api_key="invalid_key"
                )
            
            # Verify the error message contains the expected text
            assert "Invalid Google AI API key" in str(excinfo.value)


def test_call_gemini_empty_response():
    """Test Gemini API call with empty response."""
    # Create a response class that matches the expected structure
    class MockResponse:
        def __init__(self, text=None):
            self.text = text
    
    # Patch the genai module
    with patch('oju.providers.genai') as mock_genai:
        # Setup mock response with empty text
        mock_response = MockResponse(text=None)
        
        # Setup the model mock to return our mock response
        mock_model = MagicMock()
        mock_model.generate_content.return_value = mock_response
        
        # Setup the genai mock
        mock_genai.GenerativeModel.return_value = mock_model
        mock_genai.configure.return_value = None
        
        # Test that the function raises the expected exception
        with pytest.raises(Exception) as excinfo:
            call_gemini(
                model="gemini-pro",
                system_prompt="Test system prompt",
                prompt="Test input",
                api_key="test_key"
            )
        
        # Verify the exception message contains the expected text
        assert "No response text was returned from Gemini API" in str(excinfo.value)
        
        # Verify the mocks were called as expected
        mock_genai.configure.assert_called_once_with(api_key="test_key")
        mock_genai.GenerativeModel.assert_called_once_with(model_name="gemini-pro")
        mock_model.generate_content.assert_called_once()


def test_call_gemini_api_error():
    """Test Gemini API call with API error."""
    with patch('oju.providers.genai') as mock_genai:
        # Test PermissionDenied error
        mock_genai.GenerativeModel.side_effect = google_exceptions.PermissionDenied("Invalid API key")
        
        with pytest.raises(ValueError) as exc_info:
            call_gemini(
                model="gemini-pro",
                system_prompt="Test system",
                prompt="Test input",
                api_key="invalid_key"
            )
        assert "Invalid Google AI API key" in str(exc_info.value)
        
        # Test other API error
        mock_genai.GenerativeModel.side_effect = google_exceptions.InvalidArgument("Invalid argument")
        with pytest.raises(Exception) as exc_info:
            call_gemini(
                model="gemini-pro",
                system_prompt="Test system",
                prompt="Test input",
                api_key="test_key"
            )
        assert "Google API error: 400 Invalid argument" in str(exc_info.value)


def test_call_openai_general_error():
    """Test OpenAI API call with general error."""
    with patch('oju.providers.OpenAI') as mock_openai:
        mock_client = MagicMock()
        mock_client.chat.completions.create.side_effect = Exception("General error")
        mock_openai.return_value = mock_client
        
        with pytest.raises(Exception) as exc_info:
            call_openai(
                model="gpt-4",
                system_prompt="Test system",
                prompt="Test input",
                api_key="test_key"
            )
        assert "General error" in str(exc_info.value)


def test_call_claude_general_error():
    """Test Claude API call with general error."""
    with patch('oju.providers.anthropic.Anthropic') as mock_anthropic:
        mock_client = MagicMock()
        mock_client.messages.create.side_effect = Exception("General error")
        mock_anthropic.return_value = mock_client
        
        with pytest.raises(Exception) as exc_info:
            call_claude(
                model="claude-3-opus-20240229",
                system_prompt="Test system",
                prompt="Test input",
                api_key="test_key"
            )
        assert "General error" in str(exc_info.value)


def test_call_openai_successful_response():
    """Test successful OpenAI API call to cover the try block."""
    with patch('oju.providers.OpenAI') as mock_openai:
        # Setup mock response
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_choice = MagicMock()
        mock_message = MagicMock()
        
        mock_message.content = "Test response"
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client
        
        # Call the function
        response = call_openai(
            model="gpt-4",
            system_prompt="Test system",
            prompt="Test input",
            api_key="test_key"
        )
        
        # Verify the response
        assert response == "Test response"
        mock_openai.assert_called_once_with(api_key="test_key")
        mock_client.chat.completions.create.assert_called_once()


def test_call_claude_successful_response():
    """Test successful Claude API call to cover the try block."""
    with patch('oju.providers.anthropic.Anthropic') as mock_anthropic:
        # Setup mock response
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_content = MagicMock()
        
        mock_content.text = "Test response"
        mock_response.content = [mock_content]
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client
        
        # Call the function
        response = call_claude(
            model="claude-3-opus-20240229",
            system_prompt="Test system",
            prompt="Test input",
            api_key="test_key"
        )
        
        # Verify the response
        assert response == "Test response"
        mock_anthropic.assert_called_once_with(api_key="test_key")
        mock_client.messages.create.assert_called_once()


def test_call_gemini_successful_response():
    """Test successful Gemini API call to cover the try block."""
    with patch('oju.providers.genai') as mock_genai:
        # Setup mock response
        mock_model = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "Test response"
        mock_model.generate_content.return_value = mock_response
        mock_genai.GenerativeModel.return_value = mock_model
        
        # Call the function
        response = call_gemini(
            model="gemini-pro",
            system_prompt="Test system",
            prompt="Test input",
            api_key="test_key"
        )
        
        # Verify the response
        assert response == "Test response"
        mock_genai.configure.assert_called_once_with(api_key="test_key")
        mock_genai.GenerativeModel.assert_called_once_with(model_name="gemini-pro")
        mock_model.generate_content.assert_called_once()


def test_call_openai_empty_response():
    """Test OpenAI API call with empty response."""
    with patch('oju.providers.OpenAI') as mock_openai:
        # Setup mock response with empty content
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_choice = MagicMock()
        mock_message = MagicMock()
        
        mock_message.content = None
        mock_choice.message = mock_message
        mock_response.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client
        
        # Call the function
        response = call_openai(
            model="gpt-4",
            system_prompt="Test system",
            prompt="Test input",
            api_key="test_key"
        )
        
        # Verify empty string is returned for empty content
        assert response == ""


def test_call_openai_with_openai_error():
    """Test OpenAI API call with OpenAIError."""
    with patch('oju.providers.OpenAI') as mock_openai:
        # Setup mock to raise OpenAIError
        mock_client = MagicMock()
        mock_client.chat.completions.create.side_effect = OpenAIError("Test error")
        mock_openai.return_value = mock_client
        
        # Test with non-API key related error
        with pytest.raises(Exception) as exc_info:
            call_openai(
                model="gpt-4",
                system_prompt="Test system",
                prompt="Test input",
                api_key="test_key"
            )
        assert "OpenAI API error: Test error" in str(exc_info.value)
        
        # Test with API key related error
        mock_client.chat.completions.create.side_effect = OpenAIError("Incorrect API key")
        with pytest.raises(ValueError) as exc_info:
            call_openai(
                model="gpt-4",
                system_prompt="Test system",
                prompt="Test input",
                api_key="invalid_key"
            )
        assert "Invalid OpenAI API key" in str(exc_info.value)


def test_call_gemini_permission_denied():
    """Test Gemini API call with PermissionDenied error."""
    with patch('oju.providers.genai') as mock_genai:
        # Setup mock to raise PermissionDenied with API key in message
        mock_genai.GenerativeModel.side_effect = google_exceptions.PermissionDenied("API key not valid")
        
        with pytest.raises(ValueError) as exc_info:
            call_gemini(
                model="gemini-pro",
                system_prompt="Test system",
                prompt="Test input",
                api_key="invalid_key"
            )
        assert "Invalid Google AI API key" in str(exc_info.value)


def test_call_gemini_invalid_argument():
    """Test Gemini API call with InvalidArgument error."""
    with patch('oju.providers.genai') as mock_genai:
        # Setup mock to raise InvalidArgument
        mock_genai.GenerativeModel.side_effect = google_exceptions.InvalidArgument("Invalid argument")
        
        with pytest.raises(Exception) as exc_info:
            call_gemini(
                model="gemini-pro",
                system_prompt="Test system",
                prompt="Test input",
                api_key="test_key"
            )
        assert "Google API error: 400 Invalid argument" in str(exc_info.value)
