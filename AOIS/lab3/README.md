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
python3 main.py '!(b + c > (a * !c + !b))'
```
#### Output:
```bash
Формула: !(b + c > (a * !c + !b))
Таблица истинности:
 +---+---+---+--------+
| a | b | c | result |
+---+---+---+--------+
| 0 | 0 | 0 |   0    |
| 0 | 0 | 1 |   0    |
| 0 | 1 | 0 |   1    |
| 0 | 1 | 1 |   1    |
| 1 | 0 | 0 |   0    |
| 1 | 0 | 1 |   0    |
| 1 | 1 | 0 |   0    |
| 1 | 1 | 1 |   1    |
+---+---+---+--------+
СДНФ: (!a * b * !c) + (!a * b * c) + (a * b * c)
СКНФ: (a + b + c) * (a + b + !c) * (!a + b + c) * (!a + b + !c) * (!a + !b + c)

ТДНФ (расчетный метод): (!a * b) + (b * c)
ТКНФ (расчетный метод): (!a + c) * (b)

ТДНФ (метод Квайна-Мак-Класски): (!a * b) + (b * c)
ТКНФ (метод Квайна-Мак-Класски): (!a + c) * (b)

a\bc
ТДНФ (метод Карно): (!a * b) + (b * c)
ТКНФ (метод Карно): (b) * (!a + c)

Карта Карно:
+------+----+----+----+----+
| a\bc | 00 | 01 | 11 | 10 |
+------+----+----+----+----+
|  0   | 0  | 0  | 1  | 1  |
|  1   | 0  | 0  | 1  | 0  |
+------+----+----+----+----+
```
