# TD 1

*Java, section « Travaux Dirigés 1 - 4 ». Relecture de ma tentative sur Moodle ([lien](https://learning.esiea.fr/mod/quiz/review.php?attempt=14280&cmid=7026)).*

## Résumé

- **Statut** : Terminée
- **Commencé** : lundi 5 octobre 2026, 13:02
- **Terminé** : lundi 5 octobre 2026, 14:42
- **Durée** : 1 heure 40 min
- **Points** : 20,75/21,00
- **Note** : 19,76 sur 20,00 (98,81%)

## Question 1  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
public class Main {
	public static void main(String[] args) {
          System.out.println("Hello World");
    }
}
```

**Retour Moodle :**

```
Feedback

Résultat attendu
Résultat obtenu

Hello World
Hello World

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 2  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class Main {
	public static void main(String[] args) {
		int i = 0;
		while (i < 10) { 
			System.out.println("Hello World");
			i++;
		}
	}
}
```

**Retour Moodle :**

```
Feedback

Résultat attendu
Résultat obtenu

Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 3  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class Main {
	public static void main(String[] args) {
		int i = 0;
		do {
			System.out.println("Hello World");
			i++;
		} while (i < 10);
	}
}
```

**Retour Moodle :**

```
Feedback

Résultat attendu
Résultat obtenu

Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 4  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class Main {
    public static void main(String[] args) {
        for (int i = 1; i <= 6; i++) {
            System.out.println("Hello World " + i);
        }
    }
}
```

**Retour Moodle :**

```
Feedback

Résultat attendu
Résultat obtenu

Hello World 1
Hello World 2
Hello World 3
Hello World 4
Hello World 5
Hello World 6
Hello World 1
Hello World 2
Hello World 3
Hello World 4
Hello World 5
Hello World 6

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 5  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class Main {
    public static void main(String[] args) {
        String[] tableau = {"one", "two", "three", null, "four", "five"};
        
        for (String element : tableau) {
            System.out.println(element);
        }
    }
}
```

**Retour Moodle :**

```
Feedback

Résultat attendu
Résultat obtenu

one
two
three
null
four
five
one
two
three
null
four
five

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 6  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class Main {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            if (i == 3) {
                System.out.println("i = 3");
                continue;
            }
            System.out.println("Hello World " + i);
        }
    }
}
```

**Retour Moodle :**

```
Feedback

Résultat attendu
Résultat obtenu

Hello World 1
Hello World 2
i = 3
Hello World 4
Hello World 5
Hello World 1
Hello World 2
i = 3
Hello World 4
Hello World 5

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 7  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class Main {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            if (i == 3) {
                System.out.println(" Stop!");
                break;
            }
            System.out.println("Hello World " + i);
        }
    }
}
```

**Retour Moodle :**

```
Feedback

Résultat attendu
Résultat obtenu

Hello World 1
Hello World 2
 Stop!
Hello World 1
Hello World 2
 Stop!

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 8  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class Main {
    public static void main(String[] args) {
        int[][] matrice = {
            {1, 3, 5, 7},
            {2, 4, 6, 8},
            {9, 11, 13, 15}
        };

        for (int i = 0; i < matrice.length; i++) {
            for (int j = 0; j < matrice[i].length; j++) {
                System.out.print(matrice[i][j]);
                if (j < matrice[i].length - 1) {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
```

**Retour Moodle :**

```
Feedback

Résultat attendu
Résultat obtenu

1 3 5 7
2 4 6 8
9 11 13 15
1 3 5 7
2 4 6 8
9 11 13 15

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 9  (Correct; Note de 1,00 sur 1,00)

Que se passera-t-il si l’on exécute le programme suivant ?

**Propositions :**

```
a. Compile time error 
b. Run time error - Checked Exception 
c. Run time error - Unchecked exception 
d. No error, output: 1 2 3 
e. No error, output: 1 2 3 6
```

**Ma réponse :** a. Compile time error  b. Run time error - Checked Exception  c. Run time error - Unchecked exception  d. No error, output: 1 2 3  e. No error, output: 1 2 3 6

**Retour Moodle :**

```
FeedbackCorrectNote pour cet envoi : 1,00/1,00.
```

## Question 10  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class GetBinaryValue {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java GetBinaryValue <decimal integer>");
            return;
        }

        System.out.println("Received " + args.length + " arguments.");
        System.out.println("The arguments are:");
        for (String arg : args) {
            System.out.println(arg);
        }

        int premierNombre = Integer.parseInt(args[0]);
        String representationBinaire = Integer.toBinaryString(premierNombre);
        
        System.out.println("The binary representation of " + premierNombre + " is " + representationBinaire);
    }
}
```

**Retour Moodle :**

```
Feedback

Entrée
Résultat attendu
Résultat obtenu

Usage: java GetBinaryValue <decimal integer>
Usage: java GetBinaryValue <decimal integer>

5 7 9
Received 3 arguments.
The arguments are:
5
7
9
The binary representation of 5 is 101
Received 3 arguments.
The arguments are:
5
7
9
The binary representation of 5 is 101

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 11  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class WrappersDemo {
    public static void main(String[] args) {
        boolean val = Boolean.parseBoolean(args[0]);
        System.out.println("value is: " + val);
    }
}
```

**Retour Moodle :**

```
Feedback

Entrée
Résultat attendu
Résultat obtenu

true
value is: true
value is: true

false
value is: false
value is: false

yes
value is: false
value is: false

non
value is: false
value is: false

TrUE
value is: true
value is: true

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 12  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class WrappersDemo {
    public static void main(String[] args) {
        long val = Long.parseLong(args[0]);
        System.out.println("value is: " + val);
    }
}
```

**Retour Moodle :**

```
Feedback

Entrée
Résultat attendu
Résultat obtenu

-12
value is: -12
value is: -12

18
value is: 18
value is: 18

bonjour
java.lang.NumberFormatException
java.lang.NumberFormatException

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 13  (Correct; Note de 1,00 sur 1,00)

Quel est l’intérêt d’utiliser un wrapper? Sélectionnez toutes les bonnes réponses.

**Propositions :**

```
a. Pour qu'une valeur nulle soit possible. 
b. Pour inclure dans une collection. 
c. Pour traiter de manière générique/polymorphe comme un objet avec d'autres objets. 
d. Les classes wrapper sont utilisées à la place des types primitifs lorsqu'un objet est attendu. 
e. Pour utiliser des méthodes de classe pour convertir des valeurs vers et à partir d'autres types primitifs, pour convertir vers et depuis des chaînes et pour convertir entre des systèmes numériques (décimal, octal, hexadécimal, binaire).
```

**Ma réponse :** a. Pour qu'une valeur nulle soit possible.  b. Pour inclure dans une collection.  c. Pour traiter de manière générique/polymorphe comme un objet avec d'autres objets.  d. Les classes wrapper sont utilisées à la place des types primitifs lorsqu'un objet est attendu.  e. Pour utiliser des méthodes de classe pour convertir des valeurs vers et à partir d'autres types primitifs, pour convertir vers et depuis des chaînes et pour convertir entre des systèmes numériques (décimal, octal, hexadécimal, binaire). / a. Pour qu'une valeur nulle soit possible.  b. Pour inclure dans une collection.  c. Pour traiter de manière générique/polymorphe comme un objet avec d'autres objets.  d. Les classes wrapper sont utilisées à la place des types primitifs lorsqu'un objet est attendu.  e. Pour utiliser des méthodes de classe pour convertir des valeurs vers et à partir d'autres types primitifs, pour convertir vers et depuis des chaînes et pour convertir entre des systèmes numériques (décimal, octal, hexadécimal, binaire). / a. Pour qu'une valeur nulle soit possible.  b. Pour inclure dans une collection.  c. Pour traiter de manière générique/polymorphe comme un objet avec d'autres objets.  d. Les classes wrapper sont utilisées à la place des types primitifs lorsqu'un objet est attendu.  e. Pour utiliser des méthodes de classe pour convertir des valeurs vers et à partir d'autres types primitifs, pour convertir vers et depuis des chaînes et pour convertir entre des systèmes numériques (décimal, octal, hexadécimal, binaire). / a. Pour qu'une valeur nulle soit possible.  b. Pour inclure dans une collection.  c. Pour traiter de manière générique/polymorphe comme un objet avec d'autres objets.  d. Les classes wrapper sont utilisées à la place des types primitifs lorsqu'un objet est attendu.  e. Pour utiliser des méthodes de classe pour convertir des valeurs vers et à partir d'autres types primitifs, pour convertir vers et depuis des chaînes et pour convertir entre des systèmes numériques (décimal, octal, hexadécimal, binaire). / a. Pour qu'une valeur nulle soit possible.  b. Pour inclure dans une collection.  c. Pour traiter de manière générique/polymorphe comme un objet avec d'autres objets.  d. Les classes wrapper sont utilisées à la place des types primitifs lorsqu'un objet est attendu.  e. Pour utiliser des méthodes de classe pour convertir des valeurs vers et à partir d'autres types primitifs, pour convertir vers et depuis des chaînes et pour convertir entre des systèmes numériques (décimal, octal, hexadécimal, binaire).

**Retour Moodle :**

```
FeedbackCorrectNote pour cet envoi : 1,00/1,00.
```

## Question 14  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class WrappersDemo {
    public static void main(String[] args) {
        double val = Double.parseDouble(args[0]);
        System.out.println("value is: " + val);
    }
}
```

**Retour Moodle :**

```
Feedback

Entrée
Résultat attendu
Résultat obtenu

-12.2
value is: -12.2
value is: -12.2

18.9
value is: 18.9
value is: 18.9

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 15  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
import java.util.Scanner;

class QuotientAndRemainder {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int dividend = sc.nextInt();
        int divisor = sc.nextInt();
        
        int quotient = dividend / divisor;
        int remainder = dividend % divisor;
        
        System.out.println("Quotient is " + quotient);
        System.out.println("Remainder is " + remainder);
    }
}
```

**Retour Moodle :**

```
Feedback

Entrée
Résultat attendu
Résultat obtenu

74
9
Quotient is 8
Remainder is 2
Quotient is 8
Remainder is 2

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 16  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class NumberFormatDemo {
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        double nombre = Double.parseDouble(sc.next());

        NumberFormat nf = NumberFormat.getNumberInstance(Locale.FRANCE);
        NumberFormat cf = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        NumberFormat inf = NumberFormat.getIntegerInstance(Locale.FRANCE);

        System.out.println("Number: " + nf.format(nombre));
        System.out.println("Currency: " + cf.format(nombre));
        System.out.println("Integer: " + inf.format(nombre));
    }
}
```

**Retour Moodle :**

```
Feedback

Entrée
Résultat attendu
Résultat obtenu

3535.99
Number: 3 535,99
Currency: 3 535,99 €
Integer: 3 536
Number: 3 535,99
Currency: 3 535,99 €
Integer: 3 536

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 17  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class PhraseDemo {
    public static void main(String[] args) {

        String phrase;
        if (args != null && args.length > 0) {
            phrase = args[0];
        } else {
            phrase = new java.util.Scanner(System.in).nextLine();
        }

        //display the length of the phrase, in characters
        System.out.println("Length of phrase is: " + phrase.length());

        String[] mots = phrase.split(" ");

        //display the words that compose the phrase, one word per line
        System.out.println("Phrase composed of words:");
        for (String mot : mots) {
            System.out.println(mot);
        }

        //display the words that compose the phrase, all lowercase
        System.out.println("All words lowercase:");
        for (String mot : mots) {
            System.out.println(mot.toLowerCase());
        }

        //display the words that compose the phrase, all uppercase
        System.out.println("All words uppercase:");
        for (String mot : mots) {
            System.out.println(mot.toUpperCase());
        }

        //check if the phrase contains a certain word ("in")
        System.out.println("The phrase contains word \"in\":" + phrase.contains("in"));

        //check if the phrase ends with a dot, an exclamation mark or a question mark
        System.out.println("The phrase ends with \".\":" + phrase.endsWith("."));
        System.out.println("The phrase ends with \"!\":" + phrase.endsWith("!"));
        System.out.println("The phrase ends with \"?\":" + phrase.endsWith("?"));

        //replaces all occurences of a certain word by another word ("in" with "out of")
        System.out.println(phrase.replace("in", "out of"));
    }
}
```

**Retour Moodle :**

```
Feedback

Entrée
Résultat attendu
Résultat obtenu

Bonjour tout le monde inhere!
Length of phrase is: 30
Phrase composed of words:
Bonjour
tout
le
monde

inhere!
All words lowercase:
bonjour
tout
le
monde

inhere!
All words uppercase:
BONJOUR
TOUT
LE
MONDE

INHERE!
The phrase contains word "in":true
The phrase ends with ".":false
The phrase ends with "!":true
The phrase ends with "?":false
Bonjour tout le monde  out ofhere!
Length of phrase is: 30
Phrase composed of words:
Bonjour
tout
le
monde

inhere!
All words lowercase:
bonjour
tout
le
monde

inhere!
All words uppercase:
BONJOUR
TOUT
LE
MONDE

INHERE!
The phrase contains word "in":true
The phrase ends with ".":false
The phrase ends with "!":true
The phrase ends with "?":false
Bonjour tout le monde  out ofhere!

JDK 17 is the open-source reference implementation of version 17 of the Java SE Platform, as specified in the Java Community Process.
Length of phrase is: 133
Phrase composed of words:
JDK
17
is
the
open-source
reference
implementation
of
version
17
of
the
Java
SE
Platform,
as
specified
in
the
Java
Community
Process.
All words lowercase:
jdk
17
is
the
open-source
reference
implementation
of
version
17
of
the
java
se
platform,
as
specified
in
the
java
community
process.
All words uppercase:
JDK
17
IS
THE
OPEN-SOURCE
REFERENCE
IMPLEMENTATION
OF
VERSION
17
OF
THE
JAVA
SE
PLATFORM,
AS
SPECIFIED
IN
THE
JAVA
COMMUNITY
PROCESS.
The phrase contains word "in":true
The phrase ends with ".":true
The phrase ends with "!":false
The phrase ends with "?":false
JDK 17 is the open-source reference implementation of version 17 of the Java SE Platform, as specified out of the Java Community Process.
Length of phrase is: 133
Phrase composed of words:
JDK
17
is
the
open-source
reference
implementation
of
version
17
of
the
Java
SE
Platform,
as
specified
in
the
Java
Community
Process.
All words lowercase:
jdk
17
is
the
open-source
reference
implementation
of
version
17
of
the
java
se
platform,
as
specified
in
the
java
community
process.
All words uppercase:
JDK
17
IS
THE
OPEN-SOURCE
REFERENCE
IMPLEMENTATION
OF
VERSION
17
OF
THE
JAVA
SE
PLATFORM,
AS
SPECIFIED
IN
THE
JAVA
COMMUNITY
PROCESS.
The phrase contains word "in":true
The phrase ends with ".":true
The phrase ends with "!":false
The phrase ends with "?":false
JDK 17 is the open-source reference implementation of version 17 of the Java SE Platform, as specified out of the Java Community Process.

Data from the customer base of application monitoring provider New Relic, representing tens of millions of production JVMs, show that LTS releases have almost unanimous deployment!
Length of phrase is: 180
Phrase composed of words:
Data
from
the
customer
base
of
application
monitoring
provider
New
Relic,
representing
tens
of
millions
of
production
JVMs,
show
that
LTS
releases
have
almost
unanimous
deployment!
All words lowercase:
data
from
the
customer
base
of
application
monitoring
provider
new
relic,
representing
tens
of
millions
of
production
jvms,
show
that
lts
releases
have
almost
unanimous
deployment!
All words uppercase:
DATA
FROM
THE
CUSTOMER
BASE
OF
APPLICATION
MONITORING
PROVIDER
NEW
RELIC,
REPRESENTING
TENS
OF
MILLIONS
OF
PRODUCTION
JVMS,
SHOW
THAT
LTS
RELEASES
HAVE
ALMOST
UNANIMOUS
DEPLOYMENT!
The phrase contains word "in":true
The phrase ends with ".":false
The phrase ends with "!":true
The phrase ends with "?":false
Data from the customer base of application monitorout ofg provider New Relic, representout ofg tens of millions of production JVMs, show that LTS releases have almost unanimous deployment!
Length of phrase is: 180
Phrase composed of words:
Data
from
the
customer
base
of
application
monitoring
provider
New
Relic,
representing
tens
of
millions
of
production
JVMs,
show
that
LTS
releases
have
almost
unanimous
deployment!
All words lowercase:
data
from
the
customer
base
of
application
monitoring
provider
new
relic,
representing
tens
of
millions
of
production
jvms,
show
that
lts
releases
have
almost
unanimous
deployment!
All words uppercase:
DATA
FROM
THE
CUSTOMER
BASE
OF
APPLICATION
MONITORING
PROVIDER
NEW
RELIC,
REPRESENTING
TENS
OF
MILLIONS
OF
PRODUCTION
JVMS,
SHOW
THAT
LTS
RELEASES
HAVE
ALMOST
UNANIMOUS
DEPLOYMENT!
The phrase contains word "in":true
The phrase ends with ".":false
The phrase ends with "!":true
The phrase ends with "?":false
Data from the customer base of application monitorout ofg provider New Relic, representout ofg tens of millions of production JVMs, show that LTS releases have almost unanimous deployment!

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 18  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class CompareStrings {

    public static void main (String[] args) {

        if (args == null || args.length < 3) {
            java.util.Scanner sc = new java.util.Scanner(System.in);
            args = new String[] { sc.next(), sc.next(), sc.next() };
        }

        String phrase1 = new String(args[0]);
        String phrase2 = new String(args[1]);
        String phrase3 = new String(args[2]);

        boolean compObject1;
        boolean compContent1;

        boolean compObject2;
        boolean compContent2;

        compObject1 = (phrase1 == phrase2);
        compContent1 = phrase1.equals(phrase2);

        compObject2 = (phrase1 == phrase3);
        compContent2 = phrase1.equals(phrase3);

        System.out.println("Object comparison between first and second: " + compObject1);
        System.out.println("Content (state) comparison between first and second: " + compContent1);

        System.out.println("Object  comparison between first and third: " + compObject2);
        System.out.println("Content (state) comparison between first and third: " + compContent2);

    }
}
```

**Retour Moodle :**

```
Feedback

Entrée
Résultat attendu
Résultat obtenu

Test1 Test1 Test2
Object comparison between first and second: false
Content (state) comparison between first and second: true
Object  comparison between first and third: false
Content (state) comparison between first and third: false
Object comparison between first and second: false
Content (state) comparison between first and second: true
Object  comparison between first and third: false
Content (state) comparison between first and third: false

Test1 Test2 Test1
Object comparison between first and second: false
Content (state) comparison between first and second: false
Object  comparison between first and third: false
Content (state) comparison between first and third: true
Object comparison between first and second: false
Content (state) comparison between first and second: false
Object  comparison between first and third: false
Content (state) comparison between first and third: true

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 19  (Partiellement correct; Note de 0,75 sur 1,00)

Pourquoi les résultats de la comparaison de deux chaînes avec == et equals() sont-ils différents ?
Sélectionnez toutes les bonnes réponses.

**Propositions :**

```
a. La méthode equals compare l'état des objets. 
b. La méthode equals compare les référents des objets. 
c. L'opérateur == compare les référents des objets. 
d. L'opérateur == compare l'état des objets. 
e. Deux objets distincts, comparés à == renverront vrai car les référents sont différents. 
f. Afin de comparer les objets, nous devons redéfinir la méthode equals. 
g. Afin de comparer les objets, nous pouvons simplement utiliser l'opérateur ==. 
h. Afin de comparer l'état de l'objet, utilisez equals(), et afin de comparer l'identité des objets, utilisez l'opérateur ==.
```

**Ma réponse :** a. La méthode equals compare l'état des objets.  b. La méthode equals compare les référents des objets.  c. L'opérateur == compare les référents des objets.  d. L'opérateur == compare l'état des objets.  e. Deux objets distincts, comparés à == renverront vrai car les référents sont différents.  f. Afin de comparer les objets, nous devons redéfinir la méthode equals.  g. Afin de comparer les objets, nous pouvons simplement utiliser l'opérateur ==.  h. Afin de comparer l'état de l'objet, utilisez equals(), et afin de comparer l'identité des objets, utilisez l'opérateur ==. / a. La méthode equals compare l'état des objets.  b. La méthode equals compare les référents des objets.  c. L'opérateur == compare les référents des objets.  d. L'opérateur == compare l'état des objets.  e. Deux objets distincts, comparés à == renverront vrai car les référents sont différents.  f. Afin de comparer les objets, nous devons redéfinir la méthode equals.  g. Afin de comparer les objets, nous pouvons simplement utiliser l'opérateur ==.  h. Afin de comparer l'état de l'objet, utilisez equals(), et afin de comparer l'identité des objets, utilisez l'opérateur ==. / a. La méthode equals compare l'état des objets.  b. La méthode equals compare les référents des objets.  c. L'opérateur == compare les référents des objets.  d. L'opérateur == compare l'état des objets.  e. Deux objets distincts, comparés à == renverront vrai car les référents sont différents.  f. Afin de comparer les objets, nous devons redéfinir la méthode equals.  g. Afin de comparer les objets, nous pouvons simplement utiliser l'opérateur ==.  h. Afin de comparer l'état de l'objet, utilisez equals(), et afin de comparer l'identité des objets, utilisez l'opérateur ==.

**Retour Moodle :**

```
FeedbackPartiellement correctNote pour cet envoi : 0,75/1,00.
```

## Question 20  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class StringBuilderDemo {
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        while (sc.hasNextLine()) {
            String ligne = sc.nextLine();
            if (ligne.equals("*")) {
                break;
            }
            if (sb.length() > 0) {
                sb.append(" ");
            }
            sb.append(ligne);
        }

        System.out.println(sb.toString());
    }
}
```

**Retour Moodle :**

```
Feedback

Entrée
Résultat attendu
Résultat obtenu

Bonjour
!
Il fait
beau
aujourd'hui!
*
Bonjour ! Il fait beau aujourd'hui!
Bonjour ! Il fait beau aujourd'hui!

Afrikaans:    Hello Wêreld!
Albanian:     Përshendetje Botë!
Amharic:      ሰላም ልዑል!
Arabic:       مرحبا بالعالم!
Armenian:     Բարեւ աշխարհ!
Basque:       Kaixo Mundua!
Belarussian:  Прывітанне Сусвет!
Bengali:      ওহে বিশ্ব!
Bulgarian:    Здравей свят!
Catalan:      Hola món!
Chichewa:     Moni Dziko Lapansi!
Chinese:      你好世界！
Croatian:     Pozdrav svijete!
Czech:        Ahoj světe!
Danish:       Hej Verden!
Dutch:        Hallo Wereld!
English:      Hello World!
Estonian:     Tere maailm!
Finnish:      Hei maailma!
French:       Bonjour monde!
Frisian:      Hallo wrâld!
Georgian:     გამარჯობა მსოფლიო!
German:       Hallo Welt!
Greek:        Γειά σου Κόσμε!
Hausa:        Sannu Duniya!
Hebrew:       שלום עולם!
Hindi:        नमस्ते दुनिया!
Hungarian:    Helló Világ!
Icelandic:    Halló heimur!
Igbo:         Ndewo Ụwa!
Indonesian:   Halo Dunia!
Italian:      Ciao mondo!
Japanese:     こんにちは世界！
Kazakh:       Сәлем Әлем!
Khmer:        សួស្តី​ពិភពលោក!
Kyrgyz:       Салам дүйнө!
Lao:          ສະ​ບາຍ​ດີ​ຊາວ​ໂລກ!
Latvian:      Sveika pasaule!
Lithuanian:   Labas pasauli!
Luxemburgish: Moien Welt!
Macedonian:   Здраво свету!
Malay:        Hai dunia!
Malayalam:    ഹലോ വേൾഡ്!
Mongolian:    Сайн уу дэлхий!
Myanmar:      မင်္ဂလာပါကမ္ဘာလောက!
Nepali:       नमस्कार संसार!
Norwegian:    Hei Verden!
Pashto:       سلام نړی!
Persian:      سلام دنیا!
Polish:       Witaj świecie!
Portuguese:   Olá Mundo!
Punjabi:      ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਦੁਨਿਆ!
Romanian:     Salut Lume!
Russian:      Привет мир!
Scots Gaelic: Hàlo a Shaoghail!
Serbian:      Здраво Свете!
Sesotho:      Lefatše Lumela!
Sinhala:      හෙලෝ වර්ල්ඩ්!
Slovenian:    Pozdravljen svet!
Spanish:      ¡Hola Mundo!         // Leading '¡' optional
Sundanese:    Halo Dunya!
Swahili:      Salamu Dunia!
Swedish:      Hej världen!
Tajik:        Салом Ҷаҳон!
Thai:         สวัสดีชาวโลก!
Turkish:      Selam Dünya!
Ukrainian:    Привіт Світ!
Uzbek:        Salom Dunyo!
Vietnamese:   Chào thế giới!
Welsh:        Helo Byd!
Xhosa:        Molo Lizwe!
Yiddish:      העלא וועלט!
Yoruba:       Mo ki O Ile Aiye!
Zulu:         Sawubona Mhlaba!
*
Afrikaans:    Hello Wêreld! Albanian:     Përshendetje Botë! Amharic:      ሰላም ልዑል! Arabic:       مرحبا بالعالم! Armenian:     Բարեւ աշխարհ! Basque:       Kaixo Mundua! Belarussian:  Прывітанне Сусвет! Bengali:      ওহে বিশ্ব! Bulgarian:    Здравей свят! Catalan:      Hola món! Chichewa:     Moni Dziko Lapansi! Chinese:      你好世界！ Croatian:     Pozdrav svijete! Czech:        Ahoj světe! Danish:       Hej Verden! Dutch:        Hallo Wereld! English:      Hello World! Estonian:     Tere maailm! Finnish:      Hei maailma! French:       Bonjour monde! Frisian:      Hallo wrâld! Georgian:     გამარჯობა მსოფლიო! German:       Hallo Welt! Greek:        Γειά σου Κόσμε! Hausa:        Sannu Duniya! Hebrew:       שלום עולם! Hindi:        नमस्ते दुनिया! Hungarian:    Helló Világ! Icelandic:    Halló heimur! Igbo:         Ndewo Ụwa! Indonesian:   Halo Dunia! Italian:      Ciao mondo! Japanese:     こんにちは世界！ Kazakh:       Сәлем Әлем! Khmer:        សួស្តី​ពិភពលោក! Kyrgyz:       Салам дүйнө! Lao:          ສະ​ບາຍ​ດີ​ຊາວ​ໂລກ! Latvian:      Sveika pasaule! Lithuanian:   Labas pasauli! Luxemburgish: Moien Welt! Macedonian:   Здраво свету! Malay:        Hai dunia! Malayalam:    ഹലോ വേൾഡ്! Mongolian:    Сайн уу дэлхий! Myanmar:      မင်္ဂလာပါကမ္ဘာလောက! Nepali:       नमस्कार संसार! Norwegian:    Hei Verden! Pashto:       سلام نړی! Persian:      سلام دنیا! Polish:       Witaj świecie! Portuguese:   Olá Mundo! Punjabi:      ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਦੁਨਿਆ! Romanian:     Salut Lume! Russian:      Привет мир! Scots Gaelic: Hàlo a Shaoghail! Serbian:      Здраво Свете! Sesotho:      Lefatše Lumela! Sinhala:      හෙලෝ වර්ල්ඩ්! Slovenian:    Pozdravljen svet! Spanish:      ¡Hola Mundo!         // Leading '¡' optional Sundanese:    Halo Dunya! Swahili:      Salamu Dunia! Swedish:      Hej världen! Tajik:        Салом Ҷаҳон! Thai:         สวัสดีชาวโลก! Turkish:      Selam Dünya! Ukrainian:    Привіт Світ! Uzbek:        Salom Dunyo! Vietnamese:   Chào thế giới! Welsh:        Helo Byd! Xhosa:        Molo Lizwe! Yiddish:      העלא וועלט! Yoruba:       Mo ki O Ile Aiye! Zulu:         Sawubona Mhlaba!
Afrikaans:    Hello Wêreld! Albanian:     Përshendetje Botë! Amharic:      ሰላም ልዑል! Arabic:       مرحبا بالعالم! Armenian:     Բարեւ աշխարհ! Basque:       Kaixo Mundua! Belarussian:  Прывітанне Сусвет! Bengali:      ওহে বিশ্ব! Bulgarian:    Здравей свят! Catalan:      Hola món! Chichewa:     Moni Dziko Lapansi! Chinese:      你好世界！ Croatian:     Pozdrav svijete! Czech:        Ahoj světe! Danish:       Hej Verden! Dutch:        Hallo Wereld! English:      Hello World! Estonian:     Tere maailm! Finnish:      Hei maailma! French:       Bonjour monde! Frisian:      Hallo wrâld! Georgian:     გამარჯობა მსოფლიო! German:       Hallo Welt! Greek:        Γειά σου Κόσμε! Hausa:        Sannu Duniya! Hebrew:       שלום עולם! Hindi:        नमस्ते दुनिया! Hungarian:    Helló Világ! Icelandic:    Halló heimur! Igbo:         Ndewo Ụwa! Indonesian:   Halo Dunia! Italian:      Ciao mondo! Japanese:     こんにちは世界！ Kazakh:       Сәлем Әлем! Khmer:        សួស្តី​ពិភពលោក! Kyrgyz:       Салам дүйнө! Lao:          ສະ​ບາຍ​ດີ​ຊາວ​ໂລກ! Latvian:      Sveika pasaule! Lithuanian:   Labas pasauli! Luxemburgish: Moien Welt! Macedonian:   Здраво свету! Malay:        Hai dunia! Malayalam:    ഹലോ വേൾഡ്! Mongolian:    Сайн уу дэлхий! Myanmar:      မင်္ဂလာပါကမ္ဘာလောက! Nepali:       नमस्कार संसार! Norwegian:    Hei Verden! Pashto:       سلام نړی! Persian:      سلام دنیا! Polish:       Witaj świecie! Portuguese:   Olá Mundo! Punjabi:      ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਦੁਨਿਆ! Romanian:     Salut Lume! Russian:      Привет мир! Scots Gaelic: Hàlo a Shaoghail! Serbian:      Здраво Свете! Sesotho:      Lefatše Lumela! Sinhala:      හෙලෝ වර්ල්ඩ්! Slovenian:    Pozdravljen svet! Spanish:      ¡Hola Mundo!         // Leading '¡' optional Sundanese:    Halo Dunya! Swahili:      Salamu Dunia! Swedish:      Hej världen! Tajik:        Салом Ҷаҳон! Thai:         สวัสดีชาวโลก! Turkish:      Selam Dünya! Ukrainian:    Привіт Світ! Uzbek:        Salom Dunyo! Vietnamese:   Chào thế giới! Welsh:        Helo Byd! Xhosa:        Molo Lizwe! Yiddish:      העלא וועלט! Yoruba:       Mo ki O Ile Aiye! Zulu:         Sawubona Mhlaba!

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 21  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
public static int fibonacci (int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

**Retour Moodle :**

```
Feedback

Entrée
Résultat attendu
Résultat obtenu

4
3
3

15
610
610

16
987
987

12
144
144

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```
