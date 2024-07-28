import pytest
import pandas as pd
from analyze_orders import load_data, compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, top_customers_by_revenue

@pytest.fixture
def sample_data():
    data = {
        'order_id': [1, 2, 3, 4, 5],
        'customer_id': [1, 2, 1, 3, 2],
        'order_date': ['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-15', '2023-03-01'],
        'product_id': [101, 102, 103, 104, 105],
        'product_name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
        'product_price': [10.0, 20.0, 30.0, 40.0, 50.0],
        'quantity': [1, 2, 3, 4, 5]
    }
    return pd.DataFrame(data)

def test_compute_monthly_revenue(sample_data):
    result = compute_monthly_revenue(sample_data)
    expected = pd.Series([30.0, 150.0, 250.0], index=pd.PeriodIndex(['2023-01', '2023-02', '2023-03'], freq='M'))
    pd.testing.assert_series_equal(result, expected)

def test_compute_product_revenue(sample_data):
    result = compute_product_revenue(sample_data)
    expected = pd.Series([10.0, 40.0, 90.0, 160.0, 250.0], index=['Product A', 'Product B', 'Product C', 'Product D', 'Product E'])
    pd.testing.assert_series_equal(result, expected)

def test_compute_customer_revenue(sample_data):
    result = compute_customer_revenue(sample_data)
    expected = pd.Series([100.0, 290.0, 160.0], index=[1, 2, 3])
    pd.testing.assert_series_equal(result, expected)

def test_top_customers_by_revenue(sample_data):
    result = top_customers_by_revenue(sample_data, top_n=2)
    expected = pd.Series([290.0, 160.0], index=[2, 3])
    pd.testing.assert_series_equal(result, expected)
