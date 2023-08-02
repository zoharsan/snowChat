**Table: SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.NATION** (Contains information about nations)

- N_NATIONKEY: NUMBER(38,0) - Nation Identifier (Primary Key)
- N_NAME: VARCHAR(25) - Nation Name
- N_REGIONKEY: NUMBER(38,0) - Region Identifier (Foreign Key referencing SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.REGION)
- N_COMMENT: VARCHAR(152) - Additional comments related to the nation
