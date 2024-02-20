from .prompt_template import *

RULE = """● Elemental Selection: Choose elements that form a single-phase solid solution or a simple eutectic system. The elements Al, Co, Cr, Fe, Ni are commonly used in EHEAs due to their compatibility and ability to form stable high-entropy mixtures. 
●  Optional Elements Effect: Cu enhances corrosion resistance and conductivity but may lower thermal stability. Mn alters fluidity and solidification, risking casting defects and phase instability, leading to unwanted phases or microstructures.
●  Atomic Size Difference: The atomic radii of the constituent elements should differ by a margin of 5% to 15%, a range that assists in maintaining a stable solid solution while simultaneously minimizing lattice distortion.
●  Valence Electron Concentration (VEC): The VEC should be in a range that favors the formation of desired phases (like FCC, BCC, or HCP). The phase stability in high entropy alloys is often influenced by the electron concentration. 
●  Mixing Enthalpy: Select elements with negative or low positive mixing enthalpies to promote solid solution formation and reduce the tendency for intermetallic compound formation.
●  Advancing Green Manufacturing: To maintain the intrinsic strength and castability of eutectic high entropy alloys with minimal heat treatment and post-processing, adherence to green manufacturing principles is essential, streamlining the production process.
●  Phase Diagram Analysis: Identify eutectic points where a simple solid solution or a combination of phases (like FCC+B2) can form. Look for compositions that avoid brittle intermetallic phases. Select compositions near eutectic points that favor the formation of desired solid solution phases. 
● Weighted Average Physical Properties: Consider the weighted average of physical properties like melting point, density, and elasticity of the constituent elements."""


EvaluePrompt = CustomPromptTemplate.from_template("""You will act as an expert in materials science, specializing in high entropy alloys (HEAs). Your task is to analyze provided data points, which are based on specific screening rules for HEA components.

Firstly, understand and apply the following screening rules defined as RULE. These rules are crucial for evaluating the potential of each HEA component.

Secondly, evaluate each data point in DATA by assigning a score from 0 to 1, indicating its suitability for experimental validation in high-entropy alloys (HEAs). A score of 1 signifies high relevance. Include a short explanation for each score, focusing on pertinent scientific concepts and considering the complexities and potential results of the experimental process in HEAs.

RULE:
{rule}

DATA:
{data}

Ensure the output for each evaluated data point is formatted as follows, data calculations can be analyzed if necessary. Give me the output directly in the following format without any other information:
{{
    'score': [assigned value],
    'reason': '[brief overview explaining the assigned value]'
}}""")