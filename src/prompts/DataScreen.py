from .prompt_template import CustomPromptTemplate



KeyPoints = """1. Composition Rule: Select alloys containing Al, Co, Cr, Fe, and Ni. Optionally include Mu and Cu. The possibility of forming eutectic high-entropy alloys in other systems should be evaluated.
2. Performance Rule: Choose alloys with Ultimate Tensile Strength (UTS) over 1000 MPa and Elongation (EL) above 15%. Additionally, considering the reliability of data, higher performance is always better.
3. Manufacturing Rule: Prefer alloys that require minimal heat treatment and cold rolling, in line with green manufacturing principles."""

DataScreeenPrompt = CustomPromptTemplate.from_template("""Review the rows in the provided Excel file to determine if they meet the requirements of key aspects of eutectic high entropy alloy design. Each row must be assessed to ensure it conforms to the specified key points. The entries should satisfy the following key points:

Key Points:
{KeyPoints}
                                                       
Please review each row listed below and output a list indicating whether each row meets these requirements, denoted as 1 (meets requirements) or 0 (does not meet requirements).

Output format:
- List of whether each row meets the requirements: [Meets Requirements for Row 1, Meets Requirements for Row 2, ...], 
Example:
If the first row meets the requirements and the second does not, the output should be [1, 0].

Data details:
{data}
""")