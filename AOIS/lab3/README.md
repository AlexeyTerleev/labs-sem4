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
python3 main.py
```

#### You can insert your formulas by changing variable 'formulas' in main.py (it should be a list)
#### You can connect and disconnect different methods of minimisation just by uncomment and comment the output


### Boolean operands
* equivalence: &nbsp; ~
* implication: &nbsp;&nbsp;&nbsp; >   
* disjunction: &nbsp;&nbsp;&nbsp; +
* conjunction: &nbsp;&nbsp; *
* negation: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; !

### Example

#### Input:
```bash
python3 main.py
```
#### Output:
```bash
Формулы:
res = (!a*!b*p)+(!a*b*!p)+(a*!b*!p)+(a*b*p)
tran = (!a*b*p)+(a*!b*p)+(a*b*!p)+(a*b*p)
Таблица истинности:
+---+---+---+-----+------+
| a | b | p | res | tran |
+---+---+---+-----+------+
| 0 | 0 | 0 |  0  |  0   |
| 0 | 0 | 1 |  1  |  0   |
| 0 | 1 | 0 |  1  |  0   |
| 0 | 1 | 1 |  0  |  1   |
| 1 | 0 | 0 |  1  |  0   |
| 1 | 0 | 1 |  0  |  1   |
| 1 | 1 | 0 |  0  |  1   |
| 1 | 1 | 1 |  1  |  1   |
+---+---+---+-----+------+

СДНФ:
res: (!a * !b * p) + (!a * b * !p) + (a * !b * !p) + (a * b * p)
tran: (!a * b * p) + (a * !b * p) + (a * b * !p) + (a * b * p)

ТДНФ (метод Карно):
res: (!a * !b * p) + (!a * b * !p) + (a * !b * !p) + (a * b * p)
tran: (a * p) + (a * b) + (b * p)

```
