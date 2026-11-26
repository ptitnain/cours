# Exercices supplémentaires

*BD, section « Travaux pratiques ». Relecture de ma tentative sur Moodle ([lien](https://learning.esiea.fr/mod/quiz/review.php?attempt=36388&cmid=9088)).*

## Résumé

- **Statut** : Terminée
- **Commencé** : mardi 24 novembre 2026, 09:22
- **Terminé** : mardi 24 novembre 2026, 11:26
- **Durée** : 2 heures 4 min
- **Note** : 20,00 sur 20,00 (100%)

## Question 1  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT employee_id,
       last_name,
       job_id,
       hire_date AS StartDate
FROM employees
ORDER BY employee_id ASC;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
employee_id  last_name    job_id      StartDate
-----------  -----------  ----------  -----------
100          King         AD_PRES     17-JUN-1987
101          Kochhar      AD_VP       21-SEP-1989
102          De Haan      AD_VP       13-JAN-1993
103          Hunold       IT_PROG     03-JAN-1990
104          Ernst        IT_PROG     21-MAY-1991
105          Austin       IT_PROG     25-JUN-1997
106          Pataballa    IT_PROG     05-FEB-1998
107          Lorentz      IT_PROG     07-FEB-1999
108          Greenberg    FI_MGR      17-AUG-1994
109          Faviet       FI_ACCOUNT  16-AUG-1994
110          Chen         FI_ACCOUNT  28-SEP-1997
111          Sciarra      FI_ACCOUNT  30-SEP-1997
112          Urman        FI_ACCOUNT  07-MAR-1998
113          Popp         FI_ACCOUNT  07-DEC-1999
114          Raphaely     PU_MAN      07-DEC-1994
115          Khoo         PU_CLERK    18-MAY-1995
116          Baida        PU_CLERK    24-DEC-1997
117          Tobias       PU_CLERK    24-JUL-1997
118          Himuro       PU_CLERK    15-NOV-1998
119          Colmenares   PU_CLERK    10-AUG-1999
120          Weiss        ST_MAN      18-JUL-1996
121          Fripp        ST_MAN      10-APR-1997
122          Kaufling     ST_MAN      01-MAY-1995
123          Vollman      ST_MAN      10-OCT-1997
124          Mourgos      ST_MAN      16-NOV-1999
125          Nayer        ST_CLERK    16-JUL-1997
126          Mikkilineni  ST_CLERK    28-SEP-1998
127          Landry       ST_CLERK    14-JAN-1999
128          Markle       ST_CLERK    08-MAR-2000
129          Bissot       ST_CLERK    20-AUG-1997
130          Atkinson     ST_CLERK    30-OCT-1997
131          Marlow       ST_CLERK    16-FEB-1997
132          Olson        ST_CLERK    10-APR-1999
134          Rogers       ST_CLERK    26-AUG-1998
135          Gee          ST_CLERK    12-DEC-1999
136          Philtanker   ST_CLERK    06-FEB-2000
137          Ladwig       ST_CLERK    14-JUL-1995
138          Stiles       ST_CLERK    26-OCT-1997
139          Seo          ST_CLERK    12-FEB-1998
140          Patel        ST_CLERK    06-APR-1998
141          Rajs         ST_CLERK    17-OCT-1995
142          Davies       ST_CLERK    29-JAN-1997
143          Matos        ST_CLERK    15-MAR-1998
144          Vargas       ST_CLERK    09-JUL-1998
146          Partners     SA_MAN      1997-01-05
147          Errazuriz    SA_MAN      1997-03-10
148          Cambrault    SA_MAN      1999-10-15
149          Zlotkey      SA_MAN      2000-01-29
150          Tucker       SA_REP      1997-01-30
151          Bernstein    SA_REP      1997-03-24
152          Hall         SA_REP      1997-08-20
153          Olsen        SA_REP      1998-03-30
154          Cambrault    SA_REP      1998-12-09
155          Tuvault      SA_REP      1999-11-23
156          King         SA_REP      1996-01-30
157          Sully        SA_REP      1996-03-04
158          McEwen       SA_REP      1996-08-01
159          Smith        SA_REP      1997-03-10
160          Doran        SA_REP      1997-12-15
161          Sewall       SA_REP      1998-11-03
162          Vishney      SA_REP      1997-11-11
163          Greene       SA_REP      1999-03-19
164          Marvins      SA_REP      2000-01-24
165          Lee          SA_REP      2000-02-23
166          Ande         SA_REP      2000-03-24
167          Banda        SA_REP      2000-04-21
168          Ozer         SA_REP      1997-03-11
169          Bloom        SA_REP      1998-03-23
170          Fox          SA_REP      1998-01-24
171          Smith        SA_REP      1999-02-23
172          Bates        SA_REP      1999-03-24
173          Kumar        SA_REP      2000-04-21
174          Abel         SA_REP      1996-05-11
175          Hutton       SA_REP      1997-03-19
176          Taylor       SA_REP      1998-03-24
177          Livingston   SA_REP      1998-12-09
178          Stuart       SA_REP      1999-05-03
179          King         SA_REP      1999-07-18
180          Muller       SA_REP      2000-01-17
employee_id  last_name    job_id      StartDate
-----------  -----------  ----------  -----------
100          King         AD_PRES     17-JUN-1987
101          Kochhar      AD_VP       21-SEP-1989
102          De Haan      AD_VP       13-JAN-1993
103          Hunold       IT_PROG     03-JAN-1990
104          Ernst        IT_PROG     21-MAY-1991
105          Austin       IT_PROG     25-JUN-1997
106          Pataballa    IT_PROG     05-FEB-1998
107          Lorentz      IT_PROG     07-FEB-1999
108          Greenberg    FI_MGR      17-AUG-1994
109          Faviet       FI_ACCOUNT  16-AUG-1994
110          Chen         FI_ACCOUNT  28-SEP-1997
111          Sciarra      FI_ACCOUNT  30-SEP-1997
112          Urman        FI_ACCOUNT  07-MAR-1998
113          Popp         FI_ACCOUNT  07-DEC-1999
114          Raphaely     PU_MAN      07-DEC-1994
115          Khoo         PU_CLERK    18-MAY-1995
116          Baida        PU_CLERK    24-DEC-1997
117          Tobias       PU_CLERK    24-JUL-1997
118          Himuro       PU_CLERK    15-NOV-1998
119          Colmenares   PU_CLERK    10-AUG-1999
120          Weiss        ST_MAN      18-JUL-1996
121          Fripp        ST_MAN      10-APR-1997
122          Kaufling     ST_MAN      01-MAY-1995
123          Vollman      ST_MAN      10-OCT-1997
124          Mourgos      ST_MAN      16-NOV-1999
125          Nayer        ST_CLERK    16-JUL-1997
126          Mikkilineni  ST_CLERK    28-SEP-1998
127          Landry       ST_CLERK    14-JAN-1999
128          Markle       ST_CLERK    08-MAR-2000
129          Bissot       ST_CLERK    20-AUG-1997
130          Atkinson     ST_CLERK    30-OCT-1997
131          Marlow       ST_CLERK    16-FEB-1997
132          Olson        ST_CLERK    10-APR-1999
134          Rogers       ST_CLERK    26-AUG-1998
135          Gee          ST_CLERK    12-DEC-1999
136          Philtanker   ST_CLERK    06-FEB-2000
137          Ladwig       ST_CLERK    14-JUL-1995
138          Stiles       ST_CLERK    26-OCT-1997
139          Seo          ST_CLERK    12-FEB-1998
140          Patel        ST_CLERK    06-APR-1998
141          Rajs         ST_CLERK    17-OCT-1995
142          Davies       ST_CLERK    29-JAN-1997
143          Matos        ST_CLERK    15-MAR-1998
144          Vargas       ST_CLERK    09-JUL-1998
146          Partners     SA_MAN      1997-01-05
147          Errazuriz    SA_MAN      1997-03-10
148          Cambrault    SA_MAN      1999-10-15
149          Zlotkey      SA_MAN      2000-01-29
150          Tucker       SA_REP      1997-01-30
151          Bernstein    SA_REP      1997-03-24
152          Hall         SA_REP      1997-08-20
153          Olsen        SA_REP      1998-03-30
154          Cambrault    SA_REP      1998-12-09
155          Tuvault      SA_REP      1999-11-23
156          King         SA_REP      1996-01-30
157          Sully        SA_REP      1996-03-04
158          McEwen       SA_REP      1996-08-01
159          Smith        SA_REP      1997-03-10
160          Doran        SA_REP      1997-12-15
161          Sewall       SA_REP      1998-11-03
162          Vishney      SA_REP      1997-11-11
163          Greene       SA_REP      1999-03-19
164          Marvins      SA_REP      2000-01-24
165          Lee          SA_REP      2000-02-23
166          Ande         SA_REP      2000-03-24
167          Banda        SA_REP      2000-04-21
168          Ozer         SA_REP      1997-03-11
169          Bloom        SA_REP      1998-03-23
170          Fox          SA_REP      1998-01-24
171          Smith        SA_REP      1999-02-23
172          Bates        SA_REP      1999-03-24
173          Kumar        SA_REP      2000-04-21
174          Abel         SA_REP      1996-05-11
175          Hutton       SA_REP      1997-03-19
176          Taylor       SA_REP      1998-03-24
177          Livingston   SA_REP      1998-12-09
178          Stuart       SA_REP      1999-05-03
179          King         SA_REP      1999-07-18
180          Muller       SA_REP      2000-01-17

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 2  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT last_name, salary, commission_pct
FROM employees
WHERE commission_pct IS NOT NULL
ORDER BY 2 DESC, 3 DESC;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
last_name   salary   commission_pct
----------  -------  --------------
Partners    13500.0  0.3
Errazuriz   12000.0  0.3
Ozer        11500.0  0.25
Cambrault   11000.0  0.3
Abel        11000.0  0.3
Vishney     10500.0  0.25
Zlotkey     10500.0  0.2
King        10000.0  0.35
Tucker      10000.0  0.3
Bloom       10000.0  0.2
Fox         9600.0   0.2
Sully       9500.0   0.35
Bernstein   9500.0   0.25
Greene      9500.0   0.15
McEwen      9000.0   0.35
Hall        9000.0   0.25
Hutton      8800.0   0.25
Taylor      8600.0   0.2
Livingston  8500.0   0.2
Stuart      8300.0   0.2
King        8200.0   0.2
Smith       8000.0   0.3
Olsen       8000.0   0.2
Muller      8000.0   0.15
Doran       7500.0   0.3
Cambrault   7500.0   0.2
Smith       7400.0   0.15
Bates       7300.0   0.15
Marvins     7200.0   0.1
Sewall      7000.0   0.25
Tuvault     7000.0   0.15
Lee         6800.0   0.1
Ande        6400.0   0.1
Banda       6200.0   0.1
Kumar       6100.0   0.1
last_name   salary   commission_pct
----------  -------  --------------
Partners    13500.0  0.3
Errazuriz   12000.0  0.3
Ozer        11500.0  0.25
Cambrault   11000.0  0.3
Abel        11000.0  0.3
Vishney     10500.0  0.25
Zlotkey     10500.0  0.2
King        10000.0  0.35
Tucker      10000.0  0.3
Bloom       10000.0  0.2
Fox         9600.0   0.2
Sully       9500.0   0.35
Bernstein   9500.0   0.25
Greene      9500.0   0.15
McEwen      9000.0   0.35
Hall        9000.0   0.25
Hutton      8800.0   0.25
Taylor      8600.0   0.2
Livingston  8500.0   0.2
Stuart      8300.0   0.2
King        8200.0   0.2
Smith       8000.0   0.3
Olsen       8000.0   0.2
Muller      8000.0   0.15
Doran       7500.0   0.3
Cambrault   7500.0   0.2
Smith       7400.0   0.15
Bates       7300.0   0.15
Marvins     7200.0   0.1
Sewall      7000.0   0.25
Tuvault     7000.0   0.15
Lee         6800.0   0.1
Ande        6400.0   0.1
Banda       6200.0   0.1
Kumar       6100.0   0.1

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 3  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT last_name AS "Employee",
       salary AS "Monthly Salary",
       commission_pct
FROM employees
WHERE commission_pct = 0.2
ORDER BY salary ASC;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Employee    Monthly Salary  commission_pct
----------  --------------  --------------
Cambrault   7500.0          0.2
Olsen       8000.0          0.2
King        8200.0          0.2
Stuart      8300.0          0.2
Livingston  8500.0          0.2
Taylor      8600.0          0.2
Fox         9600.0          0.2
Bloom       10000.0         0.2
Zlotkey     10500.0         0.2
Employee    Monthly Salary  commission_pct
----------  --------------  --------------
Cambrault   7500.0          0.2
Olsen       8000.0          0.2
King        8200.0          0.2
Stuart      8300.0          0.2
Livingston  8500.0          0.2
Taylor      8600.0          0.2
Fox         9600.0          0.2
Bloom       10000.0         0.2
Zlotkey     10500.0         0.2

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 4  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT MAX(salary) AS Maximum,
       MIN(salary) AS Minimum,
       SUM(salary) AS Sum,
       ROUND(AVG(salary)) AS Average
FROM employees;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Maximum  Minimum  Sum       Average
-------  -------  --------  -------
24000.0  2100.0   561000.0  7101.0
Maximum  Minimum  Sum       Average
-------  -------  --------  -------
24000.0  2100.0   561000.0  7101.0

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 5  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT job_id,
       ROUND(MAX(salary)) AS Maximum,
       ROUND(MIN(salary)) AS Minimum,
       ROUND(SUM(salary)) AS Sum,
       ROUND(AVG(salary)) AS Average
FROM employees
GROUP BY job_id
ORDER BY job_id ASC;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
job_id      Maximum  Minimum  Sum       Average
----------  -------  -------  --------  -------
AD_PRES     24000.0  24000.0  24000.0   24000.0
AD_VP       17000.0  17000.0  34000.0   17000.0
FI_ACCOUNT  9000.0   6900.0   39600.0   7920.0
FI_MGR      12000.0  12000.0  12000.0   12000.0
IT_PROG     9000.0   4200.0   28800.0   5760.0
PU_CLERK    3100.0   2500.0   13900.0   2780.0
PU_MAN      11000.0  11000.0  11000.0   11000.0
SA_MAN      13500.0  10500.0  47000.0   11750.0
SA_REP      11500.0  6100.0   261900.0  8448.0
ST_CLERK    3600.0   2100.0   52400.0   2758.0
ST_MAN      8200.0   5800.0   36400.0   7280.0
job_id      Maximum  Minimum  Sum       Average
----------  -------  -------  --------  -------
AD_PRES     24000.0  24000.0  24000.0   24000.0
AD_VP       17000.0  17000.0  34000.0   17000.0
FI_ACCOUNT  9000.0   6900.0   39600.0   7920.0
FI_MGR      12000.0  12000.0  12000.0   12000.0
IT_PROG     9000.0   4200.0   28800.0   5760.0
PU_CLERK    3100.0   2500.0   13900.0   2780.0
PU_MAN      11000.0  11000.0  11000.0   11000.0
SA_MAN      13500.0  10500.0  47000.0   11750.0
SA_REP      11500.0  6100.0   261900.0  8448.0
ST_CLERK    3600.0   2100.0   52400.0   2758.0
ST_MAN      8200.0   5800.0   36400.0   7280.0

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 6  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT COUNT(DISTINCT manager_id) AS "Number of Managers"
FROM employees;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Number of Managers
------------------
16
Number of Managers
------------------
16

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 7  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT department_id,
       MAX(salary) - MIN(salary) AS DIFFERENCE
FROM employees
GROUP BY department_id
HAVING COUNT(*) >= 2
ORDER BY DIFFERENCE DESC;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
department_id  DIFFERENCE
-------------  ----------
30             8500.0
80             7400.0
90             7000.0
50             6100.0
100            5100.0
60             4800.0
department_id  DIFFERENCE
-------------  ----------
30             8500.0
80             7400.0
90             7000.0
50             6100.0
100            5100.0
60             4800.0

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 8  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT location_id, street_address, city, state_province, country_name
FROM locations
NATURAL JOIN countries
ORDER BY country_name;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
location_id  street_address                            city                 state_province     country_name
-----------  ----------------------------------------  -------------------  -----------------  ------------------------
2200         12-98 Victoria Street                     Sydney               New South Wales    Australia
2800         Rua Frei Caneca 1360                      Sao Paulo            Sao Paulo          Brazil
1800         147 Spadina Ave                           Toronto              Ontario            Canada
1900         6092 Boxwood St                           Whitehorse           Yukon              Canada
2000         40-5-12 Laogianggen                       Beijing                                 China
2700         Schwanthalerstr. 7031                     Munich               Bavaria            Germany
2100         1298 Vileparle (E)                        Bombay               Maharashtra        India
1000         1297 Via Cola di Rie                      Roma                                    Italy
1100         93091 Calle della Testa                   Venice                                  Italy
1200         2017 Shinjuku-ku                          Tokyo                Tokyo Prefecture   Japan
1300         9450 Kamiya-cho                           Hiroshima                               Japan
3200         Mariano Escobedo 9991                     Mexico City          Distrito Federal,  Mexico
3100         Pieter Breughelstraat 837                 Utrecht              Utrecht            Netherlands
2300         198 Clementi North                        Singapore                               Singapore
2900         20 Rue des Corps-Saints                   Geneva               Geneve             Switzerland
3000         Murtenstrasse 921                         Bern                 BE                 Switzerland
2400         8204 Arthur St                            London                                  United Kingdom
2500         Magdalen Centre, The Oxford Science Park  Oxford               Oxford             United Kingdom
2600         9702 Chester Road                         Stretford            Manchester         United Kingdom
1400         2014 Jabberwocky Rd                       Southlake            Texas              United States of America
1500         2011 Interiors Blvd                       South San Francisco  California         United States of America
1600         2007 Zagora St                            South Brunswick      New Jersey         United States of America
1700         2004 Charade Rd                           Seattle              Washington         United States of America
location_id  street_address                            city                 state_province     country_name
-----------  ----------------------------------------  -------------------  -----------------  ------------------------
2200         12-98 Victoria Street                     Sydney               New South Wales    Australia
2800         Rua Frei Caneca 1360                      Sao Paulo            Sao Paulo          Brazil
1800         147 Spadina Ave                           Toronto              Ontario            Canada
1900         6092 Boxwood St                           Whitehorse           Yukon              Canada
2000         40-5-12 Laogianggen                       Beijing                                 China
2700         Schwanthalerstr. 7031                     Munich               Bavaria            Germany
2100         1298 Vileparle (E)                        Bombay               Maharashtra        India
1000         1297 Via Cola di Rie                      Roma                                    Italy
1100         93091 Calle della Testa                   Venice                                  Italy
1200         2017 Shinjuku-ku                          Tokyo                Tokyo Prefecture   Japan
1300         9450 Kamiya-cho                           Hiroshima                               Japan
3200         Mariano Escobedo 9991                     Mexico City          Distrito Federal,  Mexico
3100         Pieter Breughelstraat 837                 Utrecht              Utrecht            Netherlands
2300         198 Clementi North                        Singapore                               Singapore
2900         20 Rue des Corps-Saints                   Geneva               Geneve             Switzerland
3000         Murtenstrasse 921                         Bern                 BE                 Switzerland
2400         8204 Arthur St                            London                                  United Kingdom
2500         Magdalen Centre, The Oxford Science Park  Oxford               Oxford             United Kingdom
2600         9702 Chester Road                         Stretford            Manchester         United Kingdom
1400         2014 Jabberwocky Rd                       Southlake            Texas              United States of America
1500         2011 Interiors Blvd                       South San Francisco  California         United States of America
1600         2007 Zagora St                            South Brunswick      New Jersey         United States of America
1700         2004 Charade Rd                           Seattle              Washington         United States of America

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 9  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT e.last_name, d.department_id, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
ORDER BY e.last_name ASC;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
last_name    department_id  department_name
-----------  -------------  ---------------
Abel         80             Sales
Ande         80             Sales
Atkinson     50             Shipping
Austin       60             IT
Baida        30             Purchasing
Banda        80             Sales
Bates        80             Sales
Bernstein    80             Sales
Bissot       50             Shipping
Bloom        80             Sales
Cambrault    80             Sales
Cambrault    80             Sales
Chen         100            Finance
Colmenares   30             Purchasing
Davies       50             Shipping
De Haan      90             Executive
Doran        80             Sales
Ernst        60             IT
Errazuriz    80             Sales
Faviet       100            Finance
Fox          80             Sales
Fripp        50             Shipping
Gee          50             Shipping
Greenberg    100            Finance
Greene       80             Sales
Hall         80             Sales
Himuro       30             Purchasing
Hunold       60             IT
Hutton       80             Sales
Kaufling     50             Shipping
Khoo         30             Purchasing
King         90             Executive
King         80             Sales
King         80             Sales
Kochhar      90             Executive
Kumar        80             Sales
Ladwig       50             Shipping
Landry       50             Shipping
Lee          80             Sales
Livingston   80             Sales
Lorentz      60             IT
Markle       50             Shipping
Marlow       50             Shipping
Marvins      80             Sales
Matos        50             Shipping
McEwen       80             Sales
Mikkilineni  50             Shipping
Mourgos      50             Shipping
Muller       80             Sales
Nayer        50             Shipping
Olsen        80             Sales
Olson        50             Shipping
Ozer         80             Sales
Partners     80             Sales
Pataballa    60             IT
Patel        50             Shipping
Philtanker   50             Shipping
Popp         100            Finance
Rajs         50             Shipping
Raphaely     30             Purchasing
Rogers       50             Shipping
Sciarra      100            Finance
Seo          50             Shipping
Sewall       80             Sales
Smith        80             Sales
Smith        80             Sales
Stiles       50             Shipping
Stuart       80             Sales
Sully        80             Sales
Taylor       80             Sales
Tobias       30             Purchasing
Tucker       80             Sales
Tuvault      80             Sales
Urman        100            Finance
Vargas       50             Shipping
Vishney      80             Sales
Vollman      50             Shipping
Weiss        50             Shipping
Zlotkey      80             Sales
last_name    department_id  department_name
-----------  -------------  ---------------
Abel         80             Sales
Ande         80             Sales
Atkinson     50             Shipping
Austin       60             IT
Baida        30             Purchasing
Banda        80             Sales
Bates        80             Sales
Bernstein    80             Sales
Bissot       50             Shipping
Bloom        80             Sales
Cambrault    80             Sales
Cambrault    80             Sales
Chen         100            Finance
Colmenares   30             Purchasing
Davies       50             Shipping
De Haan      90             Executive
Doran        80             Sales
Ernst        60             IT
Errazuriz    80             Sales
Faviet       100            Finance
Fox          80             Sales
Fripp        50             Shipping
Gee          50             Shipping
Greenberg    100            Finance
Greene       80             Sales
Hall         80             Sales
Himuro       30             Purchasing
Hunold       60             IT
Hutton       80             Sales
Kaufling     50             Shipping
Khoo         30             Purchasing
King         90             Executive
King         80             Sales
King         80             Sales
Kochhar      90             Executive
Kumar        80             Sales
Ladwig       50             Shipping
Landry       50             Shipping
Lee          80             Sales
Livingston   80             Sales
Lorentz      60             IT
Markle       50             Shipping
Marlow       50             Shipping
Marvins      80             Sales
Matos        50             Shipping
McEwen       80             Sales
Mikkilineni  50             Shipping
Mourgos      50             Shipping
Muller       80             Sales
Nayer        50             Shipping
Olsen        80             Sales
Olson        50             Shipping
Ozer         80             Sales
Partners     80             Sales
Pataballa    60             IT
Patel        50             Shipping
Philtanker   50             Shipping
Popp         100            Finance
Rajs         50             Shipping
Raphaely     30             Purchasing
Rogers       50             Shipping
Sciarra      100            Finance
Seo          50             Shipping
Sewall       80             Sales
Smith        80             Sales
Smith        80             Sales
Stiles       50             Shipping
Stuart       80             Sales
Sully        80             Sales
Taylor       80             Sales
Tobias       30             Purchasing
Tucker       80             Sales
Tuvault      80             Sales
Urman        100            Finance
Vargas       50             Shipping
Vishney      80             Sales
Vollman      50             Shipping
Weiss        50             Shipping
Zlotkey      80             Sales

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 10  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT e.last_name AS "Employee",
       e.employee_id AS "EMP#",
       m.last_name AS "Manager",
       m.employee_id AS "Mgr#"
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id
ORDER BY e.last_name ASC;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Employee     EMP#  Manager    Mgr#
-----------  ----  ---------  ----
Abel         174   Zlotkey    149
Ande         166   Errazuriz  147
Atkinson     130   Fripp      121
Austin       105   Hunold     103
Baida        116   Raphaely   114
Banda        167   Errazuriz  147
Bates        172   Cambrault  148
Bissot       129   Fripp      121
Bloom        169   Cambrault  148
Cambrault    148   King       100
Chen         110   Greenberg  108
Colmenares   119   Raphaely   114
Davies       142   Mourgos    124
De Haan      102   King       100
Doran        160   Partners   146
Ernst        104   Hunold     103
Errazuriz    147   King       100
Faviet       109   Greenberg  108
Fox          170   Cambrault  148
Fripp        121   King       100
Gee          135   Kaufling   122
Greenberg    108   Kochhar    101
Greene       163   Errazuriz  147
Himuro       118   Raphaely   114
Hunold       103   De Haan    102
Hutton       175   Zlotkey    149
Kaufling     122   King       100
Khoo         115   Raphaely   114
King         156   Partners   146
King         179   Zlotkey    149
Kochhar      101   King       100
Kumar        173   Cambrault  148
Ladwig       137   Vollman    123
Landry       127   Weiss      120
Lee          165   Errazuriz  147
Livingston   177   Zlotkey    149
Lorentz      107   Hunold     103
Markle       128   Weiss      120
Marlow       131   Fripp      121
Marvins      164   Errazuriz  147
Matos        143   Mourgos    124
McEwen       158   Partners   146
Mikkilineni  126   Weiss      120
Mourgos      124   King       100
Muller       180   Zlotkey    149
Nayer        125   Weiss      120
Olson        132   Fripp      121
Ozer         168   Cambrault  148
Partners     146   King       100
Pataballa    106   Hunold     103
Patel        140   Vollman    123
Philtanker   136   Kaufling   122
Popp         113   Greenberg  108
Rajs         141   Mourgos    124
Raphaely     114   King       100
Rogers       134   Kaufling   122
Sciarra      111   Greenberg  108
Seo          139   Vollman    123
Sewall       161   Partners   146
Smith        159   Partners   146
Smith        171   Cambrault  148
Stiles       138   Vollman    123
Stuart       178   Zlotkey    149
Sully        157   Partners   146
Taylor       176   Zlotkey    149
Tobias       117   Raphaely   114
Urman        112   Greenberg  108
Vargas       144   Mourgos    124
Vishney      162   Errazuriz  147
Vollman      123   King       100
Weiss        120   King       100
Zlotkey      149   King       100
Employee     EMP#  Manager    Mgr#
-----------  ----  ---------  ----
Abel         174   Zlotkey    149
Ande         166   Errazuriz  147
Atkinson     130   Fripp      121
Austin       105   Hunold     103
Baida        116   Raphaely   114
Banda        167   Errazuriz  147
Bates        172   Cambrault  148
Bissot       129   Fripp      121
Bloom        169   Cambrault  148
Cambrault    148   King       100
Chen         110   Greenberg  108
Colmenares   119   Raphaely   114
Davies       142   Mourgos    124
De Haan      102   King       100
Doran        160   Partners   146
Ernst        104   Hunold     103
Errazuriz    147   King       100
Faviet       109   Greenberg  108
Fox          170   Cambrault  148
Fripp        121   King       100
Gee          135   Kaufling   122
Greenberg    108   Kochhar    101
Greene       163   Errazuriz  147
Himuro       118   Raphaely   114
Hunold       103   De Haan    102
Hutton       175   Zlotkey    149
Kaufling     122   King       100
Khoo         115   Raphaely   114
King         156   Partners   146
King         179   Zlotkey    149
Kochhar      101   King       100
Kumar        173   Cambrault  148
Ladwig       137   Vollman    123
Landry       127   Weiss      120
Lee          165   Errazuriz  147
Livingston   177   Zlotkey    149
Lorentz      107   Hunold     103
Markle       128   Weiss      120
Marlow       131   Fripp      121
Marvins      164   Errazuriz  147
Matos        143   Mourgos    124
McEwen       158   Partners   146
Mikkilineni  126   Weiss      120
Mourgos      124   King       100
Muller       180   Zlotkey    149
Nayer        125   Weiss      120
Olson        132   Fripp      121
Ozer         168   Cambrault  148
Partners     146   King       100
Pataballa    106   Hunold     103
Patel        140   Vollman    123
Philtanker   136   Kaufling   122
Popp         113   Greenberg  108
Rajs         141   Mourgos    124
Raphaely     114   King       100
Rogers       134   Kaufling   122
Sciarra      111   Greenberg  108
Seo          139   Vollman    123
Sewall       161   Partners   146
Smith        159   Partners   146
Smith        171   Cambrault  148
Stiles       138   Vollman    123
Stuart       178   Zlotkey    149
Sully        157   Partners   146
Taylor       176   Zlotkey    149
Tobias       117   Raphaely   114
Urman        112   Greenberg  108
Vargas       144   Mourgos    124
Vishney      162   Errazuriz  147
Vollman      123   King       100
Weiss        120   King       100
Zlotkey      149   King       100

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 11  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT e.department_id AS department,
       e.last_name AS employee,
       c.last_name AS colleague
FROM employees e
JOIN employees c
  ON e.department_id = c.department_id
 AND e.employee_id <> c.employee_id
ORDER BY e.department_id, e.last_name, c.last_name
LIMIT 10;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
department  employee    colleague
----------  ----------  ----------
30          Baida       Colmenares
30          Baida       Himuro
30          Baida       Khoo
30          Baida       Raphaely
30          Baida       Tobias
30          Colmenares  Baida
30          Colmenares  Himuro
30          Colmenares  Khoo
30          Colmenares  Raphaely
30          Colmenares  Tobias
department  employee    colleague
----------  ----------  ----------
30          Baida       Colmenares
30          Baida       Himuro
30          Baida       Khoo
30          Baida       Raphaely
30          Baida       Tobias
30          Colmenares  Baida
30          Colmenares  Himuro
30          Colmenares  Khoo
30          Colmenares  Raphaely
30          Colmenares  Tobias

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 12  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT last_name, hire_date
FROM employees
WHERE hire_date > (SELECT hire_date FROM employees WHERE last_name = 'Davies')
ORDER BY last_name;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
last_name  hire_date
---------  -----------
Atkinson   30-OCT-1997
Sciarra    30-SEP-1997
last_name  hire_date
---------  -----------
Atkinson   30-OCT-1997
Sciarra    30-SEP-1997

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 13  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT last_name || ',' || job_id AS "Employee and Title"
FROM employees
ORDER BY job_id ASC;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Employee and Title
--------------------
King,AD_PRES
Kochhar,AD_VP
De Haan,AD_VP
Faviet,FI_ACCOUNT
Chen,FI_ACCOUNT
Sciarra,FI_ACCOUNT
Urman,FI_ACCOUNT
Popp,FI_ACCOUNT
Greenberg,FI_MGR
Hunold,IT_PROG
Ernst,IT_PROG
Austin,IT_PROG
Pataballa,IT_PROG
Lorentz,IT_PROG
Khoo,PU_CLERK
Baida,PU_CLERK
Tobias,PU_CLERK
Himuro,PU_CLERK
Colmenares,PU_CLERK
Raphaely,PU_MAN
Partners,SA_MAN
Errazuriz,SA_MAN
Cambrault,SA_MAN
Zlotkey,SA_MAN
Tucker,SA_REP
Bernstein,SA_REP
Hall,SA_REP
Olsen,SA_REP
Cambrault,SA_REP
Tuvault,SA_REP
King,SA_REP
Sully,SA_REP
McEwen,SA_REP
Smith,SA_REP
Doran,SA_REP
Sewall,SA_REP
Vishney,SA_REP
Greene,SA_REP
Marvins,SA_REP
Lee,SA_REP
Ande,SA_REP
Banda,SA_REP
Ozer,SA_REP
Bloom,SA_REP
Fox,SA_REP
Smith,SA_REP
Bates,SA_REP
Kumar,SA_REP
Abel,SA_REP
Hutton,SA_REP
Taylor,SA_REP
Livingston,SA_REP
Stuart,SA_REP
King,SA_REP
Muller,SA_REP
Nayer,ST_CLERK
Mikkilineni,ST_CLERK
Landry,ST_CLERK
Markle,ST_CLERK
Bissot,ST_CLERK
Atkinson,ST_CLERK
Marlow,ST_CLERK
Olson,ST_CLERK
Rogers,ST_CLERK
Gee,ST_CLERK
Philtanker,ST_CLERK
Ladwig,ST_CLERK
Stiles,ST_CLERK
Seo,ST_CLERK
Patel,ST_CLERK
Rajs,ST_CLERK
Davies,ST_CLERK
Matos,ST_CLERK
Vargas,ST_CLERK
Weiss,ST_MAN
Fripp,ST_MAN
Kaufling,ST_MAN
Vollman,ST_MAN
Mourgos,ST_MAN
Employee and Title
--------------------
King,AD_PRES
Kochhar,AD_VP
De Haan,AD_VP
Faviet,FI_ACCOUNT
Chen,FI_ACCOUNT
Sciarra,FI_ACCOUNT
Urman,FI_ACCOUNT
Popp,FI_ACCOUNT
Greenberg,FI_MGR
Hunold,IT_PROG
Ernst,IT_PROG
Austin,IT_PROG
Pataballa,IT_PROG
Lorentz,IT_PROG
Khoo,PU_CLERK
Baida,PU_CLERK
Tobias,PU_CLERK
Himuro,PU_CLERK
Colmenares,PU_CLERK
Raphaely,PU_MAN
Partners,SA_MAN
Errazuriz,SA_MAN
Cambrault,SA_MAN
Zlotkey,SA_MAN
Tucker,SA_REP
Bernstein,SA_REP
Hall,SA_REP
Olsen,SA_REP
Cambrault,SA_REP
Tuvault,SA_REP
King,SA_REP
Sully,SA_REP
McEwen,SA_REP
Smith,SA_REP
Doran,SA_REP
Sewall,SA_REP
Vishney,SA_REP
Greene,SA_REP
Marvins,SA_REP
Lee,SA_REP
Ande,SA_REP
Banda,SA_REP
Ozer,SA_REP
Bloom,SA_REP
Fox,SA_REP
Smith,SA_REP
Bates,SA_REP
Kumar,SA_REP
Abel,SA_REP
Hutton,SA_REP
Taylor,SA_REP
Livingston,SA_REP
Stuart,SA_REP
King,SA_REP
Muller,SA_REP
Nayer,ST_CLERK
Mikkilineni,ST_CLERK
Landry,ST_CLERK
Markle,ST_CLERK
Bissot,ST_CLERK
Atkinson,ST_CLERK
Marlow,ST_CLERK
Olson,ST_CLERK
Rogers,ST_CLERK
Gee,ST_CLERK
Philtanker,ST_CLERK
Ladwig,ST_CLERK
Stiles,ST_CLERK
Seo,ST_CLERK
Patel,ST_CLERK
Rajs,ST_CLERK
Davies,ST_CLERK
Matos,ST_CLERK
Vargas,ST_CLERK
Weiss,ST_MAN
Fripp,ST_MAN
Kaufling,ST_MAN
Vollman,ST_MAN
Mourgos,ST_MAN

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 14  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT job_id, department_id FROM employees WHERE department_id = 10
UNION
SELECT job_id, department_id FROM employees WHERE department_id = 50
UNION
SELECT job_id, department_id FROM employees WHERE department_id = 20
ORDER BY job_id;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
job_id    department_id
--------  -------------
ST_CLERK  50
ST_MAN    50
job_id    department_id
--------  -------------
ST_CLERK  50
ST_MAN    50

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 15  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT employee_id, job_id FROM employees
INTERSECT
SELECT employee_id, job_id FROM job_history
ORDER BY job_id;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
employee_id  job_id
-----------  ------
176          SA_REP
employee_id  job_id
-----------  ------
176          SA_REP

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 16  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT last_name, first_name
FROM employees
WHERE commission_pct IS NULL
ORDER BY last_name ASC;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
last_name    first_name
-----------  -----------
Atkinson     Mozhe
Austin       David
Baida        Shelli
Bissot       Laura
Chen         John
Colmenares   Karen
Davies       Curtis
De Haan      Lex
Ernst        Bruce
Faviet       Daniel
Fripp        Adam
Gee          Ki
Greenberg    Nancy
Himuro       Guy
Hunold       Alexander
Kaufling     Payam
Khoo         Alexander
King         Steven
Kochhar      Neena
Ladwig       Renske
Landry       James
Lorentz      Diana
Markle       Steven
Marlow       James
Matos        Randall
Mikkilineni  Irene
Mourgos      Kevin
Nayer        Julia
Olson        TJ
Pataballa    Valli
Patel        Joshua
Philtanker   Hazel
Popp         Luis
Rajs         Trenna
Raphaely     Den
Rogers       Michael
Sciarra      Ismael
Seo          John
Stiles       Stephen
Tobias       Sigal
Urman        Jose Manuel
Vargas       Peter
Vollman      Shanta
Weiss        Matthew
last_name    first_name
-----------  -----------
Atkinson     Mozhe
Austin       David
Baida        Shelli
Bissot       Laura
Chen         John
Colmenares   Karen
Davies       Curtis
De Haan      Lex
Ernst        Bruce
Faviet       Daniel
Fripp        Adam
Gee          Ki
Greenberg    Nancy
Himuro       Guy
Hunold       Alexander
Kaufling     Payam
Khoo         Alexander
King         Steven
Kochhar      Neena
Ladwig       Renske
Landry       James
Lorentz      Diana
Markle       Steven
Marlow       James
Matos        Randall
Mikkilineni  Irene
Mourgos      Kevin
Nayer        Julia
Olson        TJ
Pataballa    Valli
Patel        Joshua
Philtanker   Hazel
Popp         Luis
Rajs         Trenna
Raphaely     Den
Rogers       Michael
Sciarra      Ismael
Seo          John
Stiles       Stephen
Tobias       Sigal
Urman        Jose Manuel
Vargas       Peter
Vollman      Shanta
Weiss        Matthew

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 17  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT first_name, last_name
FROM employees
WHERE manager_id IS NULL
ORDER BY last_name ASC;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
first_name  last_name
----------  ---------
Steven      King
first_name  last_name
----------  ---------
Steven      King

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 18  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT j.job_title AS "Titre_Emploi",
       AVG(e.salary) AS "Salaire_Moyen"
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
GROUP BY j.job_title
ORDER BY AVG(e.salary) ASC;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Titre_Emploi                   Salaire_Moyen
-----------------------------  ----------------
Stock Clerk                    2757.89473684211
Purchasing Clerk               2780.0
Programmer                     5760.0
Stock Manager                  7280.0
Accountant                     7920.0
Sales Representative           8448.38709677419
Purchasing Manager             11000.0
Sales Manager                  11750.0
Finance Manager                12000.0
Administration Vice President  17000.0
President                      24000.0
Titre_Emploi                   Salaire_Moyen
-----------------------------  ----------------
Stock Clerk                    2757.89473684211
Purchasing Clerk               2780.0
Programmer                     5760.0
Stock Manager                  7280.0
Accountant                     7920.0
Sales Representative           8448.38709677419
Purchasing Manager             11000.0
Sales Manager                  11750.0
Finance Manager                12000.0
Administration Vice President  17000.0
President                      24000.0

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 19  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT last_name, salary
FROM employees
WHERE salary NOT BETWEEN 5000 AND 12000
ORDER BY salary ASC;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
last_name    salary
-----------  -------
Olson        2100.0
Markle       2200.0
Philtanker   2200.0
Landry       2400.0
Gee          2400.0
Colmenares   2500.0
Marlow       2500.0
Patel        2500.0
Vargas       2500.0
Himuro       2600.0
Matos        2600.0
Mikkilineni  2700.0
Seo          2700.0
Tobias       2800.0
Atkinson     2800.0
Baida        2900.0
Rogers       2900.0
Khoo         3100.0
Davies       3100.0
Nayer        3200.0
Stiles       3200.0
Bissot       3300.0
Rajs         3500.0
Ladwig       3600.0
Lorentz      4200.0
Austin       4800.0
Pataballa    4800.0
Partners     13500.0
Kochhar      17000.0
De Haan      17000.0
King         24000.0
last_name    salary
-----------  -------
Olson        2100.0
Markle       2200.0
Philtanker   2200.0
Landry       2400.0
Gee          2400.0
Colmenares   2500.0
Marlow       2500.0
Patel        2500.0
Vargas       2500.0
Himuro       2600.0
Matos        2600.0
Mikkilineni  2700.0
Seo          2700.0
Tobias       2800.0
Atkinson     2800.0
Baida        2900.0
Rogers       2900.0
Khoo         3100.0
Davies       3100.0
Nayer        3200.0
Stiles       3200.0
Bissot       3300.0
Rajs         3500.0
Ladwig       3600.0
Lorentz      4200.0
Austin       4800.0
Pataballa    4800.0
Partners     13500.0
Kochhar      17000.0
De Haan      17000.0
King         24000.0

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 20  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT last_name AS "Employee",
       salary AS "Monthly Salary"
FROM employees
WHERE salary BETWEEN 5000 AND 12000
  AND department_id IN (20, 50)
ORDER BY salary ASC;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Employee  Monthly Salary
--------  --------------
Mourgos   5800.0
Vollman   6500.0
Kaufling  7900.0
Weiss     8000.0
Fripp     8200.0
Employee  Monthly Salary
--------  --------------
Mourgos   5800.0
Vollman   6500.0
Kaufling  7900.0
Weiss     8000.0
Fripp     8200.0

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```
