from .prompt_template import CustomPromptTemplate

WebSearchPrompt = CustomPromptTemplate.from_template("""Perform a web search on key points related to eutectic high entropy alloy inverse design rules for inclusion in a targeted knowledge base.

Key Points: {key_point}

Objectives:
- Locate pages with detailed information or studies on these points.
- Assess relevance for the knowledge base.

Notes:
- Use specific keywords for relevance to high entropy alloy design.
- Ensure sources are reliable and authoritative.
- Summarize key findings.""")