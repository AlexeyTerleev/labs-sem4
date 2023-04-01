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
Формула: a > !(b + c > (a * !c + !b))
Таблица истинности:
 +---+---+---+--------+
| a | b | c | result |
+---+---+---+--------+
| 0 | 0 | 0 |   1    |
| 0 | 0 | 1 |   1    |
| 0 | 1 | 0 |   1    |
| 0 | 1 | 1 |   1    |
| 1 | 0 | 0 |   0    |
| 1 | 0 | 1 |   0    |
| 1 | 1 | 0 |   0    |
| 1 | 1 | 1 |   1    |
+---+---+---+--------+
СДНФ: (!a * !b * !c) + (!a * !b * c) + (!a * b * !c) + (!a * b * c) + (a * b * c)
СКНФ: (!a + b + c) * (!a + b + !c) * (!a + !b + c)

ТДНФ (расчетный метод): (b * c) + (!a)
ТКНФ (расчетный метод): (!a + b) * (!a + c)

ТДНФ (метод Квайна-Мак-Класски): (b * c) + (!a)
ТКНФ (метод Квайна-Мак-Класски): (!a + b) * (!a + c)

ТДНФ (метод Карно): (!a) + (b * c)
ТКНФ (метод Карно): (!a + b) * (!a + c)

Карта Карно:
1 . 1 . 1 . 1
0 . 0 . 1 . 0
```
