from matminer.featurizers.composition.alloy import WenAlloys
from pymatgen.core import Composition
import pandas as pd


def calculate_feature(formula):
    """
    Calculate the feature for a given composition.

    Args:
        composition (str): A string of composition, e.g. "Fe2O3".

    Returns:
        feature (float): The feature calculated from the composition.
    """
    composition = Composition(formula)


    HEA = WenAlloys()
    features = HEA.featurize(comp=composition)

    feature_dict = dict(zip(HEA.feature_labels(), features))
    return {'Standard deviation of Metallic Radius ': f"{round(feature_dict['Yang delta'] * 100, 3)}%",
            "Weighted mean of Valence Electrons ": round(feature_dict["VEC mean"], 3),
            "Mixing enthalpy ": round(feature_dict['Mixing enthalpy'], 3)}


if __name__ == '__main__':
    df = pd.read_excel('D:\yuyouyu\SHU\MaterialFilter\data\Score_Design_v2.xlsx')
    df_result = df['formula'].apply(lambda x: calculate_feature(x)).apply(pd.Series)

    # Concatenate the new columns with the original dataframe
    df_final = pd.concat([df, df_result], axis=1)
    df_final.to_excel('D:\yuyouyu\SHU\MaterialFilter\data\Score_Design_v2.xlsx', index=False)