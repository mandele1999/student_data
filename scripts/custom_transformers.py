# This script contains custom transformers for use in a machine learning pipeline.
# It includes a ColumnNameTransformer that allows for renaming columns after transformation.

from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class ColumnNameTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, transformer, feature_names):
        self.transformer = transformer
        self.feature_names = feature_names

    def fit(self, X, y=None):
        self.transformer.fit(X, y)
        return self

    def transform(self, X):
        X_t = self.transformer.transform(X)
        return pd.DataFrame(X_t, columns=self.feature_names, index=X.index)
