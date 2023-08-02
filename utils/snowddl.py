class Snowddl:
    """
    Snowddl class loads DDL files for various tables in a database.

    Attributes:
        ddl_dict (dict): dictionary of DDL files for various tables in a database.

    Methods:
        load_ddls: loads DDL files for various tables in a database.
    """

    def __init__(self):
        self.ddl_dict = self.load_ddls()

    @staticmethod
    def load_ddls():
        ddl_files = {
            "CUSTOMER": "sql/ddl_customer.sql",
            "LINEITEM": "sql/ddl_lineitem.sql",
            "NATION": "sql/ddl_nation.sql",
            "PART": "sql/ddl_part.sql",
            "PARTSUPP": "sql/ddl_partsupp.sql",
            "REGION": "sql/ddl_region.sql",
            "SUPPLIER": "sql/ddl_supplier.sql"
        }

        ddl_dict = {}
        for table_name, file_name in ddl_files.items():
            with open(file_name, "r") as f:
                ddl_dict[table_name] = f.read()
        return ddl_dict
