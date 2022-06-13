
def md_table(table: str) -> str:
    sep = ' | '
    new_table = table.split('\n')
    new_table = [sep + line.replace('\t', sep) + sep for line in new_table]
    return '\n'.join(new_table)
