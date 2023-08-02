**Table: SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.LINEITEM** (Contains information about individual line items of orders)

- L_ORDERKEY: NUMBER(38,0) - Order Identifier (Primary Key, Foreign Key referencing SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERS)
- L_PARTKEY: NUMBER(38,0) - Part Identifier (Foreign Key referencing SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.PART)
- L_SUPPKEY: NUMBER(38,0) - Supplier Identifier (Foreign Key referencing SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER)
- L_LINENUMBER: NUMBER(38,0) - Line Number of the item in the order (Primary Key)
- L_QUANTITY: NUMBER(12,2) - Quantity of the item in the order
- L_EXTENDEDPRICE: NUMBER(12,2) - Extended Price of the item (Quantity * Price)
- L_DISCOUNT: NUMBER(12,2) - Discount applied to the item
- L_TAX: NUMBER(12,2) - Tax amount on the item
- L_RETURNFLAG: CHAR(1) - Indicates if the item was returned or not
- L_LINESTATUS: CHAR(1) - Status of the item line (e.g., shipped, pending)
- L_SHIPDATE: DATE - Date when the item was shipped
- L_COMMITDATE: DATE - Date when the order was committed
- L_RECEIPTDATE: DATE - Date when the item was received
- L_SHIPINSTRUCT: VARCHAR(25) - Shipping instructions for the item
- L_SHIPMODE: VARCHAR(10) - Shipping mode for the item
- L_COMMENT: VARCHAR(44) - Additional comments related to the line item
