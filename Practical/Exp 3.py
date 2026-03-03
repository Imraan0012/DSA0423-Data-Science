import pandas as pd

sales_data = pd.DataFrame({
    'Product': ['Laptop', 'Phone', 'Tablet'],
    'Price': [1000, 500, 300],
    'Quantity': [2, 5, 3]
})

sales_data['Total Sales'] = sales_data['Price'] * sales_data['Quantity']

print(sales_data)