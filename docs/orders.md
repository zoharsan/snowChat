**Table: SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS** (Contains information about orders placed by customers)

O_ORDERKEY: NUMBER(38,0) - Order Identifier (Primary Key)
O_CUSTKEY: NUMBER(38,0) - Customer Identifier (Foreign Key referencing SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER)
O_ORDERSTATUS: VARCHAR(1) - Status of the order (e.g., pending, shipped)
O_TOTALPRICE: NUMBER(12,2) - Total price of the order
O_ORDERDATE: DATE - Date when the order was placed
O_ORDERPRIORITY: VARCHAR(15) - Priority of the order
O_CLERK: VARCHAR(15) - Clerk who processed the order
O_SHIPPRIORITY: NUMBER(38,0) - Shipping priority for the order
O_COMMENT: VARCHAR(79) - Additional comments related to the order
