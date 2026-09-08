# %%
# import modules
import re


# %%
# define function
def add_sql_statement_terminator_if_missing(sql_str):

    sql_statement_terminator_re = re.compile('.*;\\s*$', re.DOTALL)

    found = sql_statement_terminator_re.fullmatch(sql_str)

    if found is None:
        sql_str = sql_str + ';'

    return sql_str


# %%
