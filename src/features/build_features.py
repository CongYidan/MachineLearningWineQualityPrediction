from sklearn.preprocessing import StandardScaler

def select_features(data):
    return data[['fixed acidity', 'volatile acidity', 'citric acid', 'sulphates', 'alcohol']]

def scale_features(features):
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features
