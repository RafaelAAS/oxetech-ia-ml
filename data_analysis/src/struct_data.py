import pandas as pd

from ucimlrepo import fetch_ucirepo


class DataBase:

    def struct_database(self):
        breast_cancer_wisconsin_diagnostic = fetch_ucirepo(id=17)
        
        feature = breast_cancer_wisconsin_diagnostic.data.features
        target = breast_cancer_wisconsin_diagnostic.data.targets

        data = pd.concat([feature, target], axis=1)
        data['Diagnosis'] = data['Diagnosis'].replace('M', 1)
        data['Diagnosis'] = data['Diagnosis'].replace('B', 0)
        print(data.shape)


if __name__ == "__main__":

    play = DataBase()
    play.struct_database()
