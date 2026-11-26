# TD 2

*Java, section « Travaux Dirigés 1 - 4 ». Relecture de ma tentative sur Moodle ([lien](https://learning.esiea.fr/mod/quiz/review.php?attempt=14985&cmid=7027)).*

## Résumé

- **Statut** : Terminée
- **Commencé** : mardi 6 octobre 2026, 08:50
- **Terminé** : mardi 6 octobre 2026, 11:57
- **Durée** : 3 heures 6 min
- **Points** : 19,00/19,00
- **Note** : 20,00 sur 20,00 (100%)

## Question 1  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class UppercaseName
{
	public static void main (String args[])
	{
	    String[] nameList = new String[5];
	    Scanner scanner = new Scanner(System.in);
		
		for (int i = 0; i < 5; i++) {
			nameList[i] = scanner.nextLine();
		}

        for(String nom : nameList){
            System.out.println(nom.toUpperCase());
        }
		
	}
}
```

**Retour Moodle :**

```
Feedback

Entrée
Résultat attendu
Résultat obtenu

Jean-Marc
Kevin
Maria
Alexander
Julia
JEAN-MARC
KEVIN
MARIA
ALEXANDER
JULIA
JEAN-MARC
KEVIN
MARIA
ALEXANDER
JULIA

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 2  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class SimplePoint {
    private char name;
    private double absc;
    
    public SimplePoint(char name, double absc){
        this.name=name;
        this.absc=absc;
    }

    public void display(){
        System.out.println("Nom: " + name + " abscisse: " + absc);
    }

    public void translate(double number){
        this.absc=absc + number;
    }

    public String toString() {
        return name + ": " + absc;
    }
}
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

//test toString
SimplePoint p = new SimplePoint('P', -11.3);
System.out.println("The point is: " + p);
The point is: P: -11.3
The point is: P: -11.3

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 3  (Correct; Note de 2,00 sur 2,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class BankAccount {
    private int balance;
    
    public BankAccount (int balance){
        this.balance = balance;
    }
    
    public int getBalance(){
        return this.balance;
    }
    
    public void deposit(int amount){
        if (amount <0){
            System.out.println("Error");
        } else{
            this.balance = balance+amount;
        }
    }
    
    public void withdrawal(int amount){
        if (amount<0 || amount>balance){
            System.out.println("Error");
        } else{
            this.balance = balance-amount;
        }
    }
}
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

BankAccount ba = new BankAccount(100);
ba.deposit(50);
ba.withdrawal(-5);
System.out.println(ba.getBalance());
Error
150
Error
150

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 2,00/2,00.
```

## Question 4  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class FinalAttributes {
    private final float x;
    private final int n = 10;
    private final int p = 2;
	public FinalAttributes (float r) {
	     x = r;
	}
    
}
```

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 5  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class Point {
    private int abscissa;
    private int ordinate;

    public Point (int a, int o) {
        this.abscissa = a;
        this.ordinate = o;
    }

    public int getAbscissa() {
        return this.abscissa;
    }

    public int getOrdinate() {
        return this.ordinate;
    }

    public void setAbscissa(int abs) {
        this.abscissa = abs;
    }

    public void setOrdinate(int ord) {
        this.ordinate = ord;
    }
}
```

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 6  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class MethodOverloadExample {
	public void f (int n)  {
	    System.out.println(n);
	}

	public void g (float x) {
	    System.out.println(x);
	}
	public void g (final double y) {
	    System.out.println(y);
	}
	public void h (long n){
	    System.out.println(n);
	}

}
```

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 7  (Correct; Note de 2,00 sur 2,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class Physicist {
    private String name;
    private LocalDate date;
    private String pays;

    public Physicist(String name, LocalDate date, String pays) {
        this.name = name;
        this.pays = pays;
        if (date == null || date.isBefore(LocalDate.of(0, 1, 1)) || date.isAfter(LocalDate.now())) {
            this.date = null;
        } else {
            this.date = date;
        }
    }

    public Physicist(String name, LocalDate date) {
        this(name, date, null);
    }

    public Physicist(String name) {
        this(name, null, null);
    }

    public void setBirthDate(LocalDate date) {
        if (date != null && !date.isBefore(LocalDate.of(0, 1, 1)) && !date.isAfter(LocalDate.now())) {
            this.date = date;
        }
    }

    public String toString() {
        String s = name;
        if (date != null) {
            s = s + "," + date;
        }
        if (pays != null) {
            s = s + "," + pays;
        }
        return s;
    }
}
```

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! CorrectNote pour cet envoi : 2,00/2,00.
```

## Question 8  (Correct; Note de 2,00 sur 2,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class Vector3d {
    private double x;
    private double y;
    private double z;

    public Vector3d(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public String toString() {
        return "<" + x + ", " + y + ", " + z + " >";
    }

    public void display() {
        System.out.println(this);
    }

    public double norm() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    public static Vector3d addition(Vector3d a, Vector3d b) {
        return new Vector3d(a.x + b.x, a.y + b.y, a.z + b.z);
    }

    public double scalarProduct(Vector3d other) {
        return x * other.x + y * other.y + z * other.z;
    }
}
```

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! CorrectNote pour cet envoi : 2,00/2,00.
```

## Description

En cliquant PAGE SUIVANTE, Je confirme avoir bien compris que le jour de l'examen, je n'aurais pas le moyen d'excecuter le code de l'exercice suivant pour voir ce que ça donne. Et par suite, le vrai objectif de l'exercice suivant est de comprendre l'ordre chronologique de l'état de la mémoire lors de l'exécution d'un programme Java, des
création des objets, des initialisations par défaut des attributs, et des initialisations par constructeurs.

## Question 9  (Correct; Note de 2,00 sur 2,00)

Exécutez le programme suivant qui exemplifie l’héritage et observez l’ordre d’initialisation des différents éléments:
public class Insect {
	protected int i = 9;
	protected int j;
	public Insect() {
		display("Insect constructor i = " + i + ", j = " + j);
		j = 39;
	}
	static private int x1 = display("static Insect.x1 initialized");
	static public int display(String s) {
		System.out.println(s);
		return 47;
	}
}

public class Beetle extends Insect {
	private int k = display("Beetle.k initialized");
	public Beetle() {
		display ("Beetle constructor");
		display ("k = " + k);
		display ("j = " + j);
	}
	static private int x2 = display ("static Beetle.x2 initialized");
	public static void main(String[] args) {
		display ("Entered main");
		Beetle b = new Beetle();
	}
}
 Les lignes apparaîtront comme suit:

    Vide 1 Question 9 static Insect.x1 initializedstatic Beetle.x2 initializedEntered mainInsect constructor i = 9, j = 0Beetle.k initializedBeetle constructork = 47j = 39 
    Vide 2 Question 9 static Insect.x1 initializedstatic Beetle.x2 initializedEntered mainInsect constructor i = 9, j = 0Beetle.k initializedBeetle constructork = 47j = 39 
    Vide 3 Question 9 static Insect.x1 initializedstatic Beetle.x2 initializedEntered mainInsect constructor i = 9, j = 0Beetle.k initializedBeetle constructork = 47j = 39 
    Vide 4 Question 9 static Insect.x1 initializedstatic Beetle.x2 initializedEntered mainInsect constructor i = 9, j = 0Beetle.k initializedBeetle constructork = 47j = 39 
    Vide 5 Question 9 static Insect.x1 initializedstatic Beetle.x2 initializedEntered mainInsect constructor i = 9, j = 0Beetle.k initializedBeetle constructork = 47j = 39 
    Vide 6 Question 9 static Insect.x1 initializedstatic Beetle.x2 initializedEntered mainInsect constructor i = 9, j = 0Beetle.k initializedBeetle constructork = 47j = 39 
    Vide 7 Question 9 static Insect.x1 initializedstatic Beetle.x2 initializedEntered mainInsect constructor i = 9, j = 0Beetle.k initializedBeetle constructork = 47j = 39 
    Vide 8 Question 9 static Insect.x1 initializedstatic Beetle.x2 initializedEntered mainInsect constructor i = 9, j = 0Beetle.k initializedBeetle constructork = 47j = 39

**Ma réponse :** static Insect.x1 initialized

**Ma réponse :** static Beetle.x2 initialized

**Ma réponse :** Entered main

**Ma réponse :** Insect constructor i = 9, j = 0

**Ma réponse :** Beetle.k initialized

**Ma réponse :** Beetle constructor

**Ma réponse :** k = 47

**Ma réponse :** j = 39

**Retour Moodle :**

```
FeedbackYour answer is correct.
```

## Question 10  (Correct; Note de 1,00 sur 1,00)

Completez le diagramme UML de classes qui représente les classes Beetle et Insect. En cas de confusion dans l'ordre des éléments, suivre l'ordre alphanumérique sur le nom des éléments. Le constructeur est avant les autres méthodes.public class Insect {
	protected int i = 9;
	protected int j;
	public Insect() {
		display("Insect constructor i = " + i + ", j = " + j);
		j = 39;
	}
	static private int x1 = display("static Insect.x1 initialized");
	static public int display(String s) {
		System.out.println(s);
		return 47;
	}
}

public class Beetle extends Insect {
	private int k = display("Beetle.k initialized");
	public Beetle() {
		display ("Beetle constructor");
		display ("k = " + k);
		display ("j = " + j);
	}
	static private int x2 = display ("static Beetle.x2 initialized");
	public static void main(String[] args) {
		display ("Entered main");
		Beetle b = new Beetle();
	}
}

**Retour Moodle :**

```
FeedbackYour answer is correct.
```

## Question 11  (Correct; Note de 3,00 sur 3,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class Point {
    private int x, y;

    public Point (int abs, int ord)  {
        x = abs;
        y = ord;
    }

    public void translate (int d) {
        x += d;
        y += d;
    }

    public int getX() { return x; }

    public int getY() { return y; }

    public String toString() {
        return "[" + x + "," + y + "]";
    }
}

class Point3D extends Point {
    private int z;

    public Point3D (int x, int y, int z) {
        super(x, y);
        this.z = z;
    }

    public int getZ() { return z; }

    public void setZ(int z) { this.z = z; }

    public String toString() {
        return super.toString() + "[" + z + "]";
    }

    public void translate (int d) {
        super.translate(d);
        z += d;
    }
}
```

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! CorrectNote pour cet envoi : 3,00/3,00.
```

## Question 12  (Terminé; Non noté)

Dessinez le diagramme UML de classes qui représente les classes Point, Point3D et leur relation.

Téléchargez votre diagramme.

**Propositions :**

```
Texte de réponse Question 12
```

## Question 13  (Correct; Note de 2,00 sur 2,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class Vehicle {
    private String maker;
    private String model;

    public Vehicle(String maker, String model) {
        this.maker = maker;
        this.model = model;
    }

    public String toString() {
        return maker + " " + model;
    }
}

class Car extends Vehicle {
    private int year;

    public Car(String maker, String model, int year) {
        super(maker, model);
        this.year = year;
    }

    public String toString() {
        return super.toString() + " " + year;
    }
}

class Train extends Vehicle {
    private String country;

    public Train(String maker, String model, String country) {
        super(maker, model);
        this.country = country;
    }

    public String toString() {
        return super.toString() + " " + country;
    }
}
```

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! CorrectNote pour cet envoi : 2,00/2,00.
```
