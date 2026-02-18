from __future__ import annotations

import os
from typing import Any, Dict, List, Tuple
import base64
import mimetypes
from pathlib import Path

import requests

_CACHED_TOKEN: str | None = None


# Fetches and caches bearer token for model-as-a-service authentication.
def _get_token() -> str:
    global _CACHED_TOKEN
    if _CACHED_TOKEN:
        return _CACHED_TOKEN

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    if not client_id or not client_secret:
        raise EnvironmentError("CLIENT_ID and CLIENT_SECRET are required to generate the access token.")

    auth_base_url = "https://daia.privatelink.azurewebsites.net/authentication-service/api/v1/auth"
    response = requests.post(
        auth_base_url + "/generate-token",
        json={"client_id": client_id, "client_secret": client_secret},
        verify=False,
        timeout=30,
    )
    response.raise_for_status()
    token = response.json().get("token")
    if not token:
        raise RuntimeError("Token not found in authentication response.")
    _CACHED_TOKEN = token
    return token


# Builds multimodal message content with text and optional base64-embedded images.
def _build_content(prompt: str, image_paths: List[str] | None = None) -> Any:
    if not image_paths:
        return prompt

    content: List[Dict[str, Any]] = [{"type": "text", "text": prompt}]
    for image_path in image_paths:
        path = Path(image_path)
        if not path.exists():
            continue
        mime_type, _ = mimetypes.guess_type(str(path))
        if not mime_type:
            mime_type = "image/png"
        image_bytes = path.read_bytes()
        encoded = base64.b64encode(image_bytes).decode("ascii")
        content.append(
            {
                "type": "image_url",
                "image_url": {"url": f"data:{mime_type};base64,{encoded}"},
            }
        )
    return content


# Calls the chat-completions endpoint and returns assistant text content.
def generate_text(prompt: str, max_tokens: int = 100000, image_paths: List[str] | None = None) -> str:
    model_base_url = "https://daia.privatelink.azurewebsites.net/model-as-a-service"
    model = os.getenv("MODEL_AS_A_SERVICE_MODEL", "gpt-5")
    headers = {"Authorization": f"Bearer {_get_token()}"}
    payload: Dict[str, Any] = {
        "model": model,
        "messages": [{"role": "user", "content": _build_content(prompt, image_paths)}],
        "max_tokens": max_tokens,
    }
    response = requests.post(
        model_base_url + "/chat/completions",
        json=payload,
        headers=headers,
        verify=False,
        timeout=(30,300),
    )
    response.raise_for_status()
    data = response.json()
    try:
        return data["choices"][0]["message"]["content"]
    except Exception as exc:
        raise RuntimeError(f"Unexpected response format: {data}") from exc


# Provides a lightweight token estimate based on character count.
def estimate_tokens(text: str) -> int:
    if not text:
        return 0
    return max(1, len(text) // 4)


# Executes generation and returns output plus estimated token usage metadata.
def generate_text_with_usage(
    prompt: str,
    max_tokens: int = 100000,
    image_paths: List[str] | None = None,
) -> Tuple[str, dict]:
    output = generate_text(prompt, max_tokens=max_tokens, image_paths=image_paths)
    usage = {
        "prompt_tokens": estimate_tokens(prompt),
        "completion_tokens": estimate_tokens(output),
    }
    usage["total_tokens"] = usage["prompt_tokens"] + usage["completion_tokens"]
    return output, usage
