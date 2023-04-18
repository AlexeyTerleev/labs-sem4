from src.Table import Table


class PerfectForms:

    @staticmethod
    def perfect_disjunctive(table: Table):
        result = []
        for i in range(len(table.rows[0][1])):
            sub_formulas = []
            for row in table.rows:
                if row[1][i]:
                    curr = []
                    for j in range(len(row[0])):
                        if row[0][j]:
                            curr.append(table.header[0][j])
                        else:
                            curr.append('!' + table.header[0][j])
                    sub_formulas.append(f'({" * ".join(curr)})')
            result.append((table.header[1][i], ' + '.join(sub_formulas)))
        return result

    @staticmethod
    def perfect_conjunctive(table: Table):
        result = []
        for i in range(len(table.rows[0][1])):
            sub_formulas = []
            for row in table.rows:
                if not row[1][i]:
                    curr = []
                    for j in range(len(row[0])):
                        if not row[0][j]:
                            curr.append(table.header[0][j])
                        else:
                            curr.append('!' + table.header[0][j])
                    sub_formulas.append(f'({" + ".join(curr)})')
            result.append((table.header[1][i], ' * '.join(sub_formulas)))
        return result
