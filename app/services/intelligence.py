import re
from app.core.config import settings

class IntelligenceService:
    def __init__(self):
        self.mode = settings.llm_mode.lower()

    def _llm(self):
        if not settings.llm_api_key:
            raise RuntimeError("LLM_MODE=api requires LLM_API_KEY.")
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            api_key=settings.llm_api_key,
            base_url=settings.llm_base_url or None,
            model=settings.llm_model or "gpt-4o-mini",
            temperature=0,
        )

    def _ask(self, instruction: str) -> str:
        response = self._llm().invoke(instruction)
        return response.content if isinstance(response.content, str) else str(response.content)

    def explain(self, language: str, code: str) -> str:
        if self.mode == "api":
            return self._ask(f"Explain this {language} code clearly for a developer. Include purpose, inputs, outputs, flow, edge cases and complexity.\n\n{code}")
        lines = [line.strip() for line in code.splitlines() if line.strip()]
        functions = re.findall(r"\b(?:def|function|public|private|static)\s+([A-Za-z_]\w*)", code)
        return f"Language: {language}\nNon-empty lines: {len(lines)}\nDetected callable names: {', '.join(functions) if functions else 'none detected'}\n\nDemo analysis: local parsing is active. Set LLM_MODE=api for LangChain-powered generation."

    def generate_sql(self, request: str, schema_context: str) -> str:
        if self.mode == "api":
            return self._ask(f"Generate safe read-only MySQL SQL for this request. Return SQL only. Request: {request}\nSchema: {schema_context}")
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
            return self._ask(f"Generate concise technical documentation for this {language} code. Include overview, API/inputs, outputs, implementation notes and examples.\n\n{code}")
        return f"# Generated Documentation\n\n**Language:** {language}\n\n## Purpose\nThis module contains the supplied source snippet.\n\n## Implementation\nDemo mode is active; configure LLM_MODE=api for LangChain-generated documentation."
