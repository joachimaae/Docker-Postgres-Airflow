def create_staging_table_query(tabellnavn, column_list):
    '''
    Helper function for creating a staging table for a given column list.
    '''
    staging_init = f"DROP TABLE if exists {tabellnavn}; CREATE TABLE {tabellnavn}("
    for kolonne in column_list :
        staging_init = staging_init + (f"{kolonne} TEXT, ")
    staging_init = staging_init[:-2]
    staging_init += ")"
    return(staging_init)

def create_cast_query(stage, prod, column_list, typelist):
    '''
    Helper function for creating query that casts data types and transfers data from stage to production.
    '''
    query = f"INSERT INTO {prod}({', '.join(column_list)}) SELECT "
    for col_index in range(len(column_list)):
        query = query + (f"CAST({column_list[col_index]} AS {typelist[col_index]}), ")
    query = query[:-2]
    query += f" FROM {stage};"
    print(query)
    return(query)

def add_fact_columns(prod, column_list, typelist):
    '''
    Helper function for adding columns to a fact table.
    '''
    query = ""
    for i in range(len(column_list)):
        query += f"ALTER TABLE {prod} ADD COLUMN IF NOT EXISTS {column_list[i]} {typelist[i]};"
    return(query)
