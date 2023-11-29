"""
CI/CD
"""
import pandas as pd

def main():
    """
    Main
    """
    data = import_data()
    data = rename_columns(data)

    
def import_data() -> pd.DataFrame:
    """
    Import csv file as a dataframe
    Output: data [pd.DataFrame]
    """
    data = pd.read_csv("data/iris.csv")
    print(data.shape)
    return data

def rename_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Doc
    """
    data_renamed = data.rename(columns={"sepal.length": 'sepal_length',
                                "sepal.width": 'sepal_width',
                                "petal.length": 'petal_length',
                                "petal.width": 'petal_width'})
    
    return data_renamed

    
def data_sample (data: pd.DataFrame) -> pd.DataFrame:
    """
    Une fonction qui prend une partie du Dataset (sample) de 50 lignes
    """
    sampled_dataframe = data.sample(50)
    return sampled_dataframe

def multiplier_dataset(data: pd.DataFrame) -> pd.DataFrame:
    """
    Multiplie le dataset sample par 3

    Paramètres :
        - data : Le DataFrame à multiplier.

    Renvoie :
        Un DataFrame contenant le dataset multiplié.
    """
    multiplied_data = pd.concat([data] * 3, ignore_index=True)

    return multiplied_data



if __name__ == '__main__':
    """
    Doc
    """
    main()