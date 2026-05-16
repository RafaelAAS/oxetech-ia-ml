import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

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
       
        plt.savefig('data_analysis/images/density_distribution.png')
        plt.show()

    def robust_anomaly_isolation(self, data):
        first_quartil = data['area1'].quantile(0.25)
        third_quartil = data['area1'].quantile(0.75)
        iqr = third_quartil - first_quartil

        superior_limit = third_quartil + 1.5 * iqr

        print(f"Superior Limit: {superior_limit}")

        outliers = data[data['area1'] > superior_limit]
        prevalence = outliers['Diagnosis'].mean() * 100

        mean = data['area1'].mean()
        std = data['area1'].std()
        
        plt.figure(figsize=(12, 5))
        sns.boxplot(x=data['area1'])
        sns.stripplot(x=data['area1'], color='red', alpha=0.5, jitter=True)

        plt.axvline(superior_limit, color='black', linestyle='--', linewidth=2,
                    label=f'Limite Superior IQR {superior_limit:.1f}')

        limit_zscore = mean + (3 * std)
        plt.axvline(limit_zscore, color='blue', linestyle='--', linewidth=2,
                    label=f'Limite Z-Score > 3 ({limit_zscore:.1f})')
        plt.title("Comparison of Anomaly")

        plt.legend()
        plt.savefig('data_analysis/images/boxplot_outliers.png')
        plt.show()

        print(f"Prevalence: {prevalence}")

    def mapping(self, data):
        corr_matrix = data.drop(columns=['Diagnosis']).corr()
        plt.figure(figsize=(18, 14))
        sns.heatmap(corr_matrix, cmap='RdBu_r', annot=True, fmt=".2f", vmin=-1, vmax=1, square=True, annot_kws={"size": 7})
        plt.title("Multicollinearity Mapping")

        plt.savefig('data_analysis/images/multicollinearity_map.png')
        plt.show()


if __name__ == "__main__":

    os.makedirs('data_analysis/images', exist_ok=True)

    play = DataBase()
    data = play.struct_database()

    play.biological_asymmetry(data)
    play.robust_anomaly_isolation(data)
    play.mapping(data)
