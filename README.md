Hello!

Welcome to this app, this is designed to help track your spending!

The app allows you to not just add and delete transactions, categorize them, and display them, but also gives you a hand full of features that allow you to filter through your transactions, so you can better your spending!

Features include:
1. Listing all existing categories
2. Add new categories to the list
3. Modify existing categories
4. Show all transactions
5. Add/create new transactions
6. Delete transactions
7. Summarize all transactions by their date
8. Summarize all transactions by their month
9. Summarize all transactions by their year
10. Summarize all transactions by their category
11. And summarize all transactions by their descriptions

---
Pytests:
```bash
(base) C:\Users\Nathan Cai\Desktop\COSI 103 - Git\PA02 Team 28\pa02-team28\pa02>pytest test_transaction.py
================================================= test session starts =================================================
platform win32 -- Python 3.9.7, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\Nathan Cai\Desktop\COSI 103 - Git\PA02 Team 28\pa02-team28\pa02, configfile: pytest.ini
plugins: anyio-2.2.0
collected 5 items

test_transaction.py .....                                                                                        [100%]

================================================== 5 passed in 0.39s ==================================================
```
---
Pylint:
```bash
(base) C:\Users\Nathan Cai\Desktop\COSI 103 - Git\PA02 Team 28\pa02-team28\pa02>pylint transactions.py
************* Module transactions
transactions.py:5:85: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:51:0: C0301: Line too long (151/100) (line-too-long)
transactions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transactions.py:14:0: C0115: Missing class docstring (missing-class-docstring)
transactions.py:54:8: W0612: Unused variable 'last_rowid' (unused-variable)
transactions.py:59:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:69:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:77:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:86:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:95:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:104:4: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 8.64/10

```
---
Code demo:
```bash
(base) C:\Users\Nathan Cai\Desktop\COSI 103 - Git\PA02 Team 28\pa02-team28\pa02>python tracker.py

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. summarize transactions by description
12. print this menu

> 1
id  name       description
---------------------------------------------
1   test       test test
2   test2      test tht etests
> 2
category name: test3
category description: test
> 3
modifying category
rowid: 2
new category name: test2 -2
new category description: test tested test
> 4
show transactions


itemnumber           amount               category   date       description
---------------------------------------------------------------------------
234                  23452345             2345       2345345    234
1                    23                   23         234        1234
234                  234123               1234       1234       1234
3                    34                   2345       234        1234
34                   3452                 3234       52345      234
23                   234                  23         34         23
23                   234                  2345       234        34
12                   23                   books      20220522   just trial
1                    2                    34         2345678    malai
237                  999                  toys       20220324   trial spending
1                    34                   SUP        20220334   suppper
0                    6                               6          6
1                    2                    3          4          5
1                    23                   malai      2022345    yoyo
112                  23                   234        1234       123
90                   99                   bookies    2022       this is a test
56                   34                   toys       2023       999
85                   89                   69         8998       //
78                   99                   toys       1234       ~~~
1995                 23                   clothes    20223      $$$
1                    1000                 test       20002020   test

> 5
add transaction
itemid: 5
amount spent 1000
what category does this fall under? test
in the order yyyymmdd 20220325
describe your spending I like buying stuff
> 6
Enter an item number to delete: 5
> 7
summarize transactions by date


date       amount
--------------------
4          $2
6          $6
34         $234
234        $291
1234       $234245
2022       $99
2023       $34
8998       $89
20223      $23
52345      $3452
2022345    $23
2345345    $23452345
2345678    $2
20002020   $1000
20220324   $999
20220334   $34
20220522   $23

> 8
Enter a month (1-12): 5


itemnumber           amount               category   date       description
---------------------------------------------------------------------------
12                   23                   books      20220522   just trial
> 9
Enter a year (yyyy): 2022


itemnumber           amount               category   date       description
---------------------------------------------------------------------------
12                   23                   books      20220522   just trial
237                  999                  toys       20220324   trial spending
1                    34                   SUP        20220334   suppper
> 10
Enter a category: books


itemnumber           amount               category   date       description
---------------------------------------------------------------------------
12                   23                   books      20220522   just trial

> 11
Enter a description: just trial


itemnumber           amount               category   date       description
---------------------------------------------------------------------------
12                   23                   books      20220522   just trial

> 12

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. summarize transactions by description
12. print this

> 0
bye
```
