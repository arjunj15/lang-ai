from enum import Enum
from typing import Optional
from pathlib import Path
import os
from pydantic import BaseModel, Field, model_validator
from dotenv import load_dotenv

# Find project root (where pyproject.toml is located)
def find_project_root():
    """Find the project root directory by looking for pyproject.toml."""
    current = Path(__file__).resolve()
    # Start from the current file's directory and walk up
    for parent in current.parents:
        if (parent / "pyproject.toml").exists():
            return parent
    # Fallback to current directory if pyproject.toml not found
    return Path.cwd()

# Load environment variables from .env file in project root
project_root = find_project_root()
env_path = project_root / ".env"
load_dotenv(dotenv_path=env_path, override=True)


class ModelType(str, Enum):
    """Enumeration of supported model types."""
    OLLAMA = "ollama"
    GEMINI = "gemini"


class ModelConfig(BaseModel):
    """Pydantic configuration for model settings."""
    
    model_type: ModelType = Field(
        default_factory=lambda: ModelType(os.getenv("MODEL_TYPE", "ollama").lower()),
        description="Type of model to use: 'ollama' or 'gemini'"
    )
    
    # Ollama-specific settings
    ollama_model_name: Optional[str] = Field(
        default_factory=lambda: os.getenv("OLLAMA_MODEL_NAME", "qwen3:14b"),
        description="Name of the Ollama model (e.g., 'qwen3:14b', 'llama2', etc.)"
    )
    
    ollama_api_base: Optional[str] = Field(
        default_factory=lambda: os.getenv("OLLAMA_API_BASE", "http://localhost:11434"),
        description="Base URL for the Ollama API"
    )
    
    # Gemini-specific settings
    gemini_model_name: Optional[str] = Field(
        default_factory=lambda: os.getenv("GEMINI_MODEL_NAME", "gemini-2.5-flash"),
        description="Name of the Gemini model (e.g., 'gemini-2.5-flash', 'gemini-pro', etc.)"
    )
    
    # Common settings
    stream: bool = Field(
        default_factory=lambda: os.getenv("STREAM", "false").lower() in ("true", "1", "yes"),
        description="Whether to enable streaming responses"
    )
    
    @model_validator(mode='after')
    def validate_model_config(self):
        """Validate that the appropriate model name is provided based on model_type."""
        if self.model_type == ModelType.OLLAMA and not self.ollama_model_name:
            raise ValueError("ollama_model_name is required when model_type is 'ollama'")
        if self.model_type == ModelType.GEMINI and not self.gemini_model_name:
            raise ValueError("gemini_model_name is required when model_type is 'gemini'")
        return self
    
    def get_model_string(self) -> str:
        """Get the model string for LiteLlm based on the configuration."""
        if self.model_type == ModelType.OLLAMA:
            return f"ollama/{self.ollama_model_name}"
        elif self.model_type == ModelType.GEMINI:
            return self.gemini_model_name
        else:
            raise ValueError(f"Unsupported model type: {self.model_type}")
    
    def get_api_base(self) -> Optional[str]:
        """Get the API base URL if applicable (only for Ollama)."""
        if self.model_type == ModelType.OLLAMA:
            return self.ollama_api_base
        return None
    
    def get_model(self):
        """Get the model based on model_type.
        
        Returns:
            - For GEMINI: returns the gemini_model_name (str)
            - For OLLAMA: returns a LiteLlm instance
        """
        if self.model_type == ModelType.GEMINI:
            return self.gemini_model_name
        elif self.model_type == ModelType.OLLAMA:
            from google.adk.models.lite_llm import LiteLlm
            
            model_string = self.get_model_string()
            api_base = self.get_api_base()
            
            kwargs = {
                "model": model_string,
                "stream": self.stream
            }
            
            if api_base:
                kwargs["api_base"] = api_base
            
            return LiteLlm(**kwargs)
        else:
            raise ValueError(f"Unsupported model type: {self.model_type}")
    
    def create_lite_llm(self):
        """Create a LiteLlm instance based on the configuration."""
        from google.adk.models.lite_llm import LiteLlm
        
        model_string = "ollama_chat/"+self.get_model_string()
        api_base = self.get_api_base()
        
        kwargs = {
            "model": model_string,
            "stream": self.stream
        }
        
        if api_base:
            kwargs["api_base"] = api_base
        
        return LiteLlm(**kwargs)


# Default configuration instance
default_config = ModelConfig()

# Convenience function to get model config
def get_model_config() -> ModelConfig:
    """Get the current model configuration."""
    return default_config

# Convenience function to set model config
def set_model_config(config: ModelConfig) -> None:
    """Set the global model configuration."""
    global default_config
    default_config = config

