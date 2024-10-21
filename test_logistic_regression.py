import pytest
import numpy as np
from logistic_regression import LogisticRegression

@pytest.fixture
def model():
    return LogisticRegression(learning_rate=0.1, num_iterations=1000)

def test_sigmoid(model):
    assert pytest.approx(model.sigmoid(0)) == 0.5
    assert pytest.approx(model.sigmoid(10), abs=1e-4) == 0.9999
    assert pytest.approx(model.sigmoid(-10), abs=1e-4) == 0.0001

def test_fit_predict(model):
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y = np.array([0, 0, 1, 1])
    
    model.fit(X, y)
    predictions = model.predict(X)
    
    assert len(predictions) == len(y)
    assert all(isinstance(pred, int) for pred in predictions)
    assert all(pred in [0, 1] for pred in predictions)

def test_accuracy(model):
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0, 1, 1, 1, 1])
    
    accuracy = model.accuracy(y_true, y_pred)
    assert pytest.approx(accuracy) == 0.8