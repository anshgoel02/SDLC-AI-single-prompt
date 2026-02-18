from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


# Holds end-to-end state for the single-node BRD generation workflow.
class BRDState(BaseModel):
    inputs: List[str] = Field(default_factory=list)
    source_texts: List[str] = Field(default_factory=list)
    image_paths: List[str] = Field(default_factory=list)
    brd_markdown: str = ""
    output_markdown_path: Optional[str] = None
    output_docx_path: Optional[str] = None
