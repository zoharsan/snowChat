**Table: SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER** (Contains information about suppliers)

- S_SUPPKEY: NUMBER(38,0) - Supplier Identifier (Primary Key)
- S_NAME: VARCHAR(25) - Supplier Name
- S_ADDRESS: VARCHAR(40) - Supplier Address
- S_NATIONKEY: NUMBER(38,0) - Nation Identifier (Foreign Key referencing SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.NATION)
- S_PHONE: CHAR(15) - Supplier Phone Number
- S_ACCTBAL: NUMBER(12,2) - Supplier Account Balance
- S_COMMENT: VARCHAR(101) - Additional comments related to the supplier
