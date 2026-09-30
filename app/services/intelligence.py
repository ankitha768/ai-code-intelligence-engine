import re
from app.core.config import settings

class IntelligenceService:
    def __init__(self):
        self.mode = settings.llm_mode.lower()

    def explain(self, language: str, code: str) -> str:
        if self.mode == "api":
            return self._api_placeholder("Explain", language, code)
        lines = [line.strip() for line in code.splitlines() if line.strip()]
        functions = re.findall(r"\b(?:def|function|public|private|static)\s+([A-Za-z_]\w*)", code)
        return (
            f"Language: {language}\n"
            f"Non-empty lines: {len(lines)}\n"
            f"Detected callable names: {', '.join(functions) if functions else 'none detected'}\n\n"
            "Demo analysis: the snippet was parsed locally. "
            "Set LLM_MODE=api and configure provider credentials for generated natural-language explanations."
        )

    def generate_sql(self, request: str, schema_context: str) -> str:
        if self.mode == "api":
            return self._api_placeholder("SQL", "SQL", request)
        text = request.lower()
        if "count" in text:
            return "SELECT COUNT(*) AS total_records FROM your_table;"
        if "latest" in text or "recent" in text:
            return "SELECT * FROM your_table ORDER BY created_at DESC LIMIT 10;"
        if "average" in text or "avg" in text:
            return "SELECT AVG(numeric_column) AS average_value FROM your_table;"
        return "SELECT * FROM your_table LIMIT 10;"

    def document(self, language: str, code: str) -> str:
        if self.mode == "api":
            return self._api_placeholder("Document", language, code)
        return (
            f"# Generated Documentation\n\n"
            f"**Language:** {language}\n\n"
            "## Purpose\n"
            "This module contains the supplied source snippet.\n\n"
            "## Implementation\n"
            "Review the callable names and control flow in the source code; "
            "enable API mode for richer LLM-generated documentation."
        )

    def _api_placeholder(self, operation: str, language: str, content: str) -> str:
        if not settings.llm_api_key:
            raise RuntimeError("LLM_MODE=api requires LLM_API_KEY.")
        return f"{operation} provider adapter configured for {settings.llm_model or 'configured-model'}."
