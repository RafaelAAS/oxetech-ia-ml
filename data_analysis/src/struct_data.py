import matplotlib.pyplot as plt
import pandas as pd

from ucimlrepo import fetch_ucirepo


class DataBase:

    def struct_database(self) -> object:
        breast_cancer_wisconsin_diagnostic = fetch_ucirepo(id=17)
        
        feature = breast_cancer_wisconsin_diagnostic.data.features
        target = breast_cancer_wisconsin_diagnostic.data.targets

        data = pd.concat([feature, target], axis=1)
        data['Diagnosis'] = data['Diagnosis'].replace('M', 1)
        data['Diagnosis'] = data['Diagnosis'].replace('B', 0)
        print(data.shape)

        return data

    def biological_asymmetry(self, data: object):
        mean = data['area1'].mean()
        median = data['area1'].median()
        standard_deviation = data['area1'].std()
        symmetry = data['area1'].skew()

        print(f"Mean: {mean} | Median: {median} | SD: {standard_deviation} | Symmetry: {symmetry}")

        data['area1'].plot.density()
        plt.title("Density Distribution - Cell Nucleus Area")
        plt.xlabel("Area (area1)")
        plt.ylabel("Density")
        plt.show()


if __name__ == "__main__":

    play = DataBase()
    data = play.struct_database()

    play.biological_asymmetry(data)
