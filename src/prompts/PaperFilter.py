from .prompt_template import CustomPromptTemplate



KeyPoints = """1. Inclusion of elements Al, Co, Cr, Fe, Ni (mandatory) and Mu, Cu (optional) in the eutectic high entropy alloy.
2. Process features like cold rolling, heat treatment temperature, and time.
3. Focus on high UTS (Ultimate Tensile Strength) and EL (Elongation) in eutectic high entropy alloy design."""

PaperFilterPrompt = CustomPromptTemplate.from_template("""Review the provided literature to determine its relevance to key aspects of eutectic high entropy alloy design. Add it to the knowledge base for inverse design rules if relevant. The literature should partially or fully relate to these key points:

Key Points:
{KeyPoints}

Output format:
- {{"Relevance": 1}} (for high relevance, suitable for the knowledge base)
- {{"Relevance": 0}} (for low relevance, unsuitable for the knowledge base)

Document details:
- Title: {title}
- Abstract: {abstract}

Please output either {{"Relevance": 1}} or {{"Relevance": 0}}, without providing reasons or restating the information from the document I provided.
""")