-- Create the table
CREATE TABLE SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER (
    S_SUPPKEY NUMBER(38,0) NOT NULL,
    S_NAME VARCHAR(25),
    S_ADDRESS VARCHAR(40),
    S_NATIONKEY NUMBER(38,0),
    S_PHONE CHAR(15),
    S_ACCTBAL NUMBER(12,2),
    S_COMMENT VARCHAR(101),

    -- Define the primary key
    CONSTRAINT PK_SUPPLIER PRIMARY KEY (S_SUPPKEY),

    -- Define foreign key constraint
    CONSTRAINT FK_SUPPLIER_NATION FOREIGN KEY (S_NATIONKEY) REFERENCES SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.NATION(N_NATIONKEY)
);
