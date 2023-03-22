from src.Table import Table


class PerfectForms:

    @staticmethod
    def perfect_disjunctive(table: Table):
        sub_formulas = []
        for row in table.rows:
            if row[1]:
                curr = []
                for i in range(len(row[0])):
                    if row[0][i]:
                        curr.append(table.header[0][i])
                    else:
                        curr.append('!' + table.header[0][i])
                sub_formulas.append(f'({" * ".join(curr)})')
        return ' + '.join(sub_formulas)

    @staticmethod
    def perfect_conjunctive(table: Table):
        sub_formulas = []
        for row in table.rows:
            if not row[1]:
                curr = []
                for i in range(len(row[0])):
                    if not row[0][i]:
                        curr.append(table.header[0][i])
                    else:
                        curr.append('!' + table.header[0][i])
                sub_formulas.append(f'({" + ".join(curr)})')
        return ' * '.join(sub_formulas)
