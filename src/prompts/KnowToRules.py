from .prompt_template import CustomPromptTemplate


EvaluePrompt = CustomPromptTemplate.from_template("""
Create screening rules for high-entropy alloy compositions to identify candidates for experimental validation, based on the provided information.

The structure of the rules is as follows:
Elemental Selection: Focus on elements like Al, Co, Cr, Fe, Ni, known for forming stable high-entropy mixtures.
Atomic Size Difference: Aim for a moderate size difference (about 5%) among elements to enhance stability and solid solution formation.

Note:
- Output multiple rules, separated by Markdown syntax.
- Employ a logical, systematic approach.

Provided Information:
{info}

Screening Rules:
""")