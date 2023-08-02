**Table: SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER** (Contains information about customers)

- C_CUSTKEY: NUMBER(38,0) - Customer Identifier (Primary Key)
- C_NAME: VARCHAR(25) - Customer Name
- C_ADDRESS: VARCHAR(40) - Customer Address
- C_NATIONKEY: NUMBER(38,0) - Nation Identifier (Foreign Key referencing SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.NATION)
- C_PHONE: CHAR(15) - Customer Phone Number
- C_ACCTBAL: NUMBER(12,2) - Customer Account Balance
- C_MKTSEGMENT: VARCHAR(10) - Market Segment the customer belongs to
- C_COMMENT: VARCHAR(117) - Additional comments related to the customer
