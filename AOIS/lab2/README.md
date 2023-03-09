## Transformation of logical functions presented in different forms.

### Instalation

Clone repository:
```bash
git clone https://github.com/AlexeyTerleev/labs-sem4/tree/main/AOIS/lab2
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Run

```bash
cd lab1
python3 main.py '{formula}'
```

### Boolean operands
* equivalence: &nbsp; ~
* implication: &nbsp;&nbsp;&nbsp; >   
* disjunction: &nbsp;&nbsp;&nbsp; +
* conjunction: &nbsp;&nbsp; *
* negation: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; !

### Example

#### Input:
```bash
python3 main.py 'x1 + !((x2 + !x3) * !(!x2 * !x3))'
```
#### Output:
```bash
+----+----+----+--------+
| x1 | x2 | x3 | result |
+----+----+----+--------+
| 0  | 0  | 0  |   1    |
| 0  | 0  | 1  |   1    |
| 0  | 1  | 0  |   0    |
| 0  | 1  | 1  |   0    |
| 1  | 0  | 0  |   1    |
| 1  | 0  | 1  |   1    |
| 1  | 1  | 0  |   1    |
| 1  | 1  | 1  |   1    |
+----+----+----+--------+
СДНФ: (!x1 * !x2 * !x3) + (!x1 * !x2 * x3) + (x1 * !x2 * !x3) + (x1 * !x2 * x3) + (x1 * x2 * !x3) + (x1 * x2 * x3)
СКНФ: (x1 + !x2 + x3) * (x1 + !x2 + !x3)

СДНФ (бинарная): +(000, 001, 100, 101, 110, 111)
СКНФ (бинарная): *(010, 011)

СДНФ (десятичная): +(0, 1, 4, 5, 6, 7)
СКНФ (десятичная): *(2, 3)

Индекс: 207
```