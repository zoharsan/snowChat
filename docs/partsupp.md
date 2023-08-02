**Table: SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.PARTSUPP** (Contains information about suppliers and their parts)

- PS_PARTKEY: NUMBER(38,0) - Part Identifier (Composite Primary Key, Foreign Key referencing SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.PART)
- PS_SUPPKEY: NUMBER(38,0) - Supplier Identifier (Composite Primary Key, Foreign Key referencing SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER)
- PS_AVAILQTY: NUMBER(38,0) - Available quantity of the part from the supplier
- PS_SUPPLYCOST: NUMBER(12,2) - Cost of supplying the part from the supplier
- PS_COMMENT: VARCHAR(199) - Additional comments related to the part-supplier relationship
