import numpy as np
from logistic_regression import LogisticRegression

def generate_sample_data(num_samples=100, num_features=2):
    np.random.seed(42)
    X = np.random.randn(num_samples, num_features)
    y = (X[:, 0] + X[:, 1] > 0).astype(int)
    return X, y

def run_e2e_test():
    print("Running end-to-end test for LogisticRegression")

    # Generate sample data
    X, y = generate_sample_data()
    print(f"Generated {len(X)} samples with {X.shape[1]} features")

    # Split data into train and test sets
    split_index = int(0.8 * len(X))
    X_train, X_test = X[:split_index], X[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]

    # Initialize and train the model
    model = LogisticRegression(learning_rate=0.1, num_iterations=1000)
    model.fit(X_train, y_train)
    print("Model training completed")

    # Make predictions on the test set
    y_pred = model.predict(X_test)
    print("Predictions made on test set")

    # Calculate and print accuracy
    accuracy = model.accuracy(y_test, y_pred)
    print(f"Test accuracy: {accuracy:.2f}")

    # Print some sample predictions
    print("\nSample predictions:")
    for i in range(min(5, len(y_test))):
        print(f"True: {y_test[i]}, Predicted: {y_pred[i]}")

    return accuracy


if __name__ == "__main__":
    accuracy = run_e2e_test()
    assert accuracy > 0.7, f"Test failed: accuracy {accuracy} is below threshold of 0.7"
    print("End-to-end test passed successfully!")