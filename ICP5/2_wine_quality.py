import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns


def scatter_plot(x_axis_data, y_axis_data, x_label, y_label, figure_label):
    plt.scatter(x_axis_data, y_axis_data, alpha=.75,
                color='b')  # alpha helps to show overlapping data
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(figure_label)
    plt.show()


def heat_map(matrix):
    sns.heatmap(matrix, xticklabels=matrix.columns, yticklabels=matrix.columns, annot=True)


data = pd.read_csv('Python_Lesson5/winequality-red.csv')
# Clean data for None
data = data.dropna()
corr_matrix = data.corr()
heat_map(corr_matrix)
print("Correlation values for the best case scenario")
print(corr_matrix['quality'].sort_values(ascending=False)[1:4])
print("Correlation values for the worst case scenario")
print(corr_matrix['quality'].sort_values(ascending=True)[:3])


def prediction_with_best_features():
    # considering the best features.
    features = pd.DataFrame(data, columns=['alcohol', 'sulphates', 'citric acid'])
    results = data['quality']
    train_features, test_features, train_results, test_results_actuals = train_test_split(features, results,
                                                                                          random_state=42,
                                                                                          test_size=0.33)
    linear_regression = LinearRegression()
    model = linear_regression.fit(train_features, train_results)
    test_results_predicted = model.predict(test_features)

    print('RMSE for best correlated features: \n', mean_squared_error(test_results_actuals, test_results_predicted))

    scatter_plot(test_results_predicted, test_results_actuals, 'Predicted Price', 'Actual Price',
                 'Linear Regression Model (Best Correlated features')


def prediction_with_all_features():
    # considering the best features.
    features = data.drop(['quality'], axis=1)
    results = data['quality']
    train_features, test_features, train_results, test_results_actuals = train_test_split(features, results,
                                                                                          random_state=42,
                                                                                          test_size=0.33)
    linear_regression = LinearRegression()
    model = linear_regression.fit(train_features, train_results)
    test_results_predicted = model.predict(test_features)

    print('RMSE for all features: \n', mean_squared_error(test_results_actuals, test_results_predicted))

    scatter_plot(test_results_predicted, test_results_actuals, 'Predicted Price', 'Actual Price',
                 'Linear Regression Model (all features)')


prediction_with_best_features()
prediction_with_all_features()