import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.mixture import GaussianMixture

def knn_gmm_imputation(df, column_with_missing, n_neighbors=5, n_components=10, random_state=42):
   
    # Step 1: Perform KNN imputation on the selected column
    imputer = KNNImputer(n_neighbors=n_neighbors)
    X_imputed = imputer.fit_transform(df[[column_with_missing]])
    X_imputed = pd.DataFrame(X_imputed, columns=[column_with_missing])
    
    # Step 2: Fit a GMM to the imputed data
    gmm = GaussianMixture(n_components=n_components, random_state=random_state)
    gmm.fit(X_imputed)
    
    # Step 3: Predict cluster assignments
    cluster_assignments = gmm.predict(X_imputed)
    
    # Step 4: Refine imputation using cluster means
    # Create a DataFrame to store refined values
    refined_df = X_imputed.copy()
    
    # Calculate means for each cluster
    cluster_means = np.array([X_imputed[cluster_assignments == i].mean() for i in range(gmm.n_components)])
    
    # Refine the missing values
    for i in range(len(df)):
        if pd.isnull(df.loc[i, column_with_missing]):
            cluster = cluster_assignments[i]
            refined_df.loc[i, column_with_missing] = cluster_means[cluster]
    
    # Update original DataFrame with refined values
    df.update(refined_df)
    
    return df
