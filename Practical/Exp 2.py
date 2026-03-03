import pandas as pd

# Example DataFrame
order_data = pd.DataFrame({
    'customer_id':[1,2,1,3,2],
    'order_date':pd.to_datetime(['2024-01-10','2024-01-12','2024-01-15','2024-01-20','2024-01-25']),
    'product_name':['Laptop','Phone','Laptop','Tablet','Phone'],
    'order_quantity':[2,1,3,2,4]
})

print(order_data['customer_id'].value_counts())                 # 1. total orders per customer
print(order_data.groupby('product_name')['order_quantity'].mean()) # 2. avg quantity per product
print(order_data['order_date'].min(), order_data['order_date'].max()) # 3. earliest & latest date