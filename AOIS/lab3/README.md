## Transformation of logical functions presented in different forms.

### Instalation

Clone repository:
```bash
git clone https://github.com/AlexeyTerleev/labs-sem4/tree/main/AOIS/lab3
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Run

```bash
cd lab3
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
python3 main.py '!(x1 > (x3 * x1) * !(!x2 + !x3))'
```
#### Output:
```bash
Таблица истинности: 
+----+----+----+--------+
| x1 | x2 | x3 | result |
+----+----+----+--------+
| 0  | 0  | 0  |   0    |
| 0  | 0  | 1  |   0    |
| 0  | 1  | 0  |   0    |
| 0  | 1  | 1  |   0    |
| 1  | 0  | 0  |   1    |
| 1  | 0  | 1  |   1    |
| 1  | 1  | 0  |   1    |
| 1  | 1  | 1  |   0    |
+----+----+----+--------+

СДНФ: (x1 * !x2 * !x3) + (x1 * !x2 * x3) + (x1 * x2 * !x3)
СКНФ: (x1 + x2 + x3) * (x1 + x2 + !x3) * (x1 + !x2 + x3) * (x1 + !x2 + !x3) * (!x1 + !x2 + !x3)

ТДНФ (метод Квайна-Мак-Класски): (x1 * !x2) + (x1 * !x3)
ТКНФ (метод Квайна-Мак-Класски): (!x2 + !x3) * (x1)

ТДНФ (расчетный метод): (x1 * !x2) + (x1 * !x3)
ТКНФ (расчетный метод): (!x2 + !x3) * (x1)

ТДНФ (метод Карно): (x1 * !x2) + (x1 * !x3)
ТКНФ (метод Карно): (x1) * (!x2 + !x3)
```
