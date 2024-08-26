from e2e_logistic_regression import run_e2e_test


def test_e2e():
    accuracy = run_e2e_test()
    assert accuracy > 0.7, f"E2E test failed: accuracy {accuracy} is below threshold of 0.7"