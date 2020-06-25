import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn import metrics

credit_info = pd.read_csv("CC.csv")

print(credit_info.isnull().sum())
credit_info = credit_info.fillna(credit_info.mean())
print(credit_info.isnull().sum())
sns.FacetGrid(credit_info, hue="TENURE", height=4).map(plt.scatter, "PURCHASES", "ONEOFF_PURCHASES").add_legend()
plt.show()
sns.FacetGrid(credit_info, hue="TENURE", height=4).map(plt.scatter, "MINIMUM_PAYMENTS", "PRC_FULL_PAYMENT").add_legend()
plt.show()

print("Original Data size=", credit_info.shape)
x = credit_info.iloc[:, 1:18]
y = credit_info.iloc[:, -1]
print(x.shape, y.shape)

# see how many samples we have of each Tenure
print(credit_info["TENURE"].value_counts())

inertia_list = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    inertia_list.append(kmeans.inertia_)

plt.plot(range(1, 11), inertia_list)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns=x.columns)

nclusters = 3  # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(x)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(x)
score = metrics.silhouette_score(x, y_cluster_kmeans)
print(score)

km.fit(X_scaled)
y_cluster_kmeans = km.predict(X_scaled)
score = metrics.silhouette_score(X_scaled, y_cluster_kmeans)
print(score)

pca = PCA(n_components=5)
x_pca = pca.fit_transform(X_scaled_array)
df2 = pd.DataFrame(data=x_pca, columns=["pc1", "pc2", "pc3", "pc4", "pc5"])

km.fit(df2)
df2['results'] = km.predict(df2)
score = metrics.silhouette_score(x, y_cluster_kmeans)
print(score)
sns.FacetGrid(df2, hue="results", height=4).map(plt.scatter, "pc1", "pc2").add_legend()
plt.show()
# print(final_df)
