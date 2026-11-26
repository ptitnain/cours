# TP 1 - Questions 2-10

*Java, section « Travail Pratique 1 - Formes ». Relecture de ma tentative sur Moodle ([lien](https://learning.esiea.fr/mod/quiz/review.php?attempt=22922&cmid=7032)).*

## Résumé

- **Statut** : Terminée
- **Commencé** : lundi 26 octobre 2026, 09:25
- **Terminé** : mardi 3 novembre 2026, 12:00
- **Durée** : 8 jours 2 heures
- **Points** : 9,00/9,00
- **Note** : 19,00 sur 19,00 (100%)

## Question 1  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
//only define : Resizable, Mobile, Shape, Conic and Circle
//the others already exist!

public interface Mobile {
    void move(int dx, int dy);
}

public interface Resizable {
    void resize(int scale);
}

public abstract class Shape implements Mobile {
    public abstract double area();
    public abstract double perimeter();
    public abstract String toString();
}

public abstract class Conic extends Shape implements Resizable {
}

public class Circle extends Conic {
    private Point center;
    private double radius;

    public Circle(Point center, double radius) {
        this.center = center;
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }

    @Override
    public double perimeter() {
        return 2 * Math.PI * radius;
    }

    @Override
    public void move(int dx, int dy) {
        center.move(dx, dy);
    }

    @Override
    public void resize(int scale) {
        radius = radius * Math.sqrt(scale / 100.0);
    }

    @Override
    public String toString() {
        return "Circle[center = " + center + ", radius = " + Math.round(radius * 100) / 100.0 + " ]";
    }
}
```

**Mon code / ma réponse :**

```
//only define : Resizable, Mobile, Shape, Conic and Circle
//the others already exist!
interface Resizable {
    void resize(int scale);
}

interface Mobile {
    void move(int dx,int dy);
}

public abstract class Shape implements Mobile {
    @Override
    public String toString() {
        return this.getClass().getName();
    }

    public abstract double area();

    public abstract double perimeter();
    
}

abstract class Conic extends Shape implements Resizable {

}

class Circle extends Conic {
    private Point center;
    private double radius;

    public Circle(Point center,double radius) {
        this.radius = radius;
        this.center = center;
    }
    
    @Override
    public String toString() {
        double r = BigDecimal.valueOf(radius).setScale(2, RoundingMode.HALF_UP).doubleValue();
        return super.toString() + "[center = " + center +", radius = " + r + " ]";
    }


    @Override
    public double area() {
        return Math.PI*radius*radius;
    }

    @Override
    public double perimeter() {
        return 2*Math.PI*radius;
    }

    @Override
    public void move(int dx, int dy) {
        center.move(dx, dy);
    }

    @Override
    public void resize(int scale) {
        this.radius=this.radius*Math.sqrt(scale/100.0);
    }
}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)//only define : Resizable, Mobile, Shape, Conic and Circle
//the others already exist!
interface Resizable {
    void resize(int scale);
}

interface Mobile {
    void move(int dx,int dy);
}

public abstract class Shape implements Mobile {
    @Override
    public String toString() {
        return this.getClass().getName();
    }

    public abstract double area();

    public abstract double perimeter();
    
}

abstract class Conic extends Shape implements Resizable {

}

class Circle extends Conic {
    private Point center;
    private double radius;

    public Circle(Point center,double radius) {
        this.radius = radius;
        this.center = center;
    }
    
    @Override
    public String toString() {
        double r = BigDecimal.valueOf(radius).setScale(2, RoundingMode.HALF_UP).doubleValue();
        return super.toString() + "[center = " + center +", radius = " + r + " ]";
    }

    @Override
    public double area() {
        return Math.PI*radius*radius;
    }

    @Override
    public double perimeter() {
        return 2*Math.PI*radius;
    }

    @Override
    public void move(int dx, int dy) {
        center.move(dx, dy);
    }

    @Override
    public void resize(int scale) {
        this.radius=this.radius*Math.sqrt(scale/100.0);
    }
}

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

Mobile m;
Point O = new Point(0, 0);
Conic c = new Circle (O, 1.1);
Shape s = c;
m = c;
System.out.println(m);
m.move(1,2);
System.out.println(m);
Circle[center = (0.0,0.0), radius = 1.1 ]
Circle[center = (1.0,2.0), radius = 1.1 ]
Circle[center = (0.0,0.0), radius = 1.1 ]
Circle[center = (1.0,2.0), radius = 1.1 ]

Mobile m;
Resizable r;
Shape s;
Point O = new Point(0, 0);
Conic c = new Circle (O, 1.1);
s = c;
m = s;
r = c;
System.out.println(m);
m.move(1,2);
System.out.println(m);
r.resize(50);
System.out.println(m);

double p = BigDecimal.valueOf(s.perimeter()).setScale(2, RoundingMode.HALF_UP).doubleValue();
double a = BigDecimal.valueOf(s.area()).setScale(2, RoundingMode.HALF_UP).doubleValue();

System.out.println("perimeter = " + p);
System.out.println("area = " + a);
Circle[center = (0.0,0.0), radius = 1.1 ]
Circle[center = (1.0,2.0), radius = 1.1 ]
Circle[center = (1.0,2.0), radius = 0.78 ]
perimeter = 4.89
area = 1.9
Circle[center = (0.0,0.0), radius = 1.1 ]
Circle[center = (1.0,2.0), radius = 1.1 ]
Circle[center = (1.0,2.0), radius = 0.78 ]
perimeter = 4.89
area = 1.9

Tous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)//only define : Resizable, Mobile, Shape, Conic and Circle
//the others already exist!
interface Resizable {
    void resize(int scale);
}

interface Mobile {
    void move(int dx,int dy);
}

public abstract class Shape implements Mobile {
    @Override
    public String toString() {
        return this.getClass().getName();
    }

    public abstract double area();

    public abstract double perimeter();
    
}

abstract class Conic extends Shape implements Resizable {

}

class Circle extends Conic {
    private Point center;
    private double radius;

    public Circle(Point center,double radius) {
        this.radius = radius;
        this.center = center;
    }
    
    @Override
    public String toString() {
        double r = BigDecimal.valueOf(radius).setScale(2, RoundingMode.HALF_UP).doubleValue();
        return super.toString() + "[center = " + center +", radius = " + r + " ]";
    }

    @Override
    public double area() {
        return Math.PI*radius*radius;
    }

    @Override
    public double perimeter() {
        return 2*Math.PI*radius;
    }

    @Override
    public void move(int dx, int dy) {
        center.move(dx, dy);
    }

    @Override
    public void resize(int scale) {
        this.radius=this.radius*Math.sqrt(scale/100.0);
    }
}
CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 2  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
//only define : Polygon, Quadrilateral, IllegalNumberOfVerticesException
//the others already exist!

class IllegalNumberOfVerticesException extends IllegalArgumentException {
    public IllegalNumberOfVerticesException() {
        super();
    }
}

class Polygon extends Shape {
    private List<Point> vertices;

    public Polygon(Point... points) {
        vertices = new ArrayList<>(Arrays.asList(points));
    }

    @Override
    public double area() {
        int n = vertices.size();
        double sum = 0;
        for (int i = 0; i < n; i++) {
            Point a = vertices.get(i);
            Point b = vertices.get((i + 1) % n);
            sum += a.getX() * b.getY() - b.getX() * a.getY();
        }
        return Math.abs(sum) / 2;
    }

    @Override
    public double perimeter() {
        int n = vertices.size();
        double p = 0;
        for (int i = 0; i < n; i++) {
            p += Points.distance(vertices.get(i), vertices.get((i + 1) % n));
        }
        return p;
    }

    @Override
    public void move(int dx, int dy) {
        for (Point v : vertices) {
            v.move(dx, dy);
        }
    }

    @Override
    public String toString() {
        return getClass().getSimpleName() + "{" + vertices + "}";
    }
}

class Quadrilateral extends Polygon {
    public Quadrilateral(Point... points) {
        super(points);
        if (points.length != 4) {
            throw new IllegalNumberOfVerticesException();
        }
    }
}
```

**Mon code / ma réponse :**

```
//only define : Polygon, Quadrilateral, IllegalNumberOfVerticesException
//the others already exist!
class Polygon extends Shape {

    private List<Point> vertices;

    public Polygon(Point... points) {
        String message = Polygons.isSimplePolygon(points);
        if (message != null) {
            throw new IllegalArgumentException(message);
        }
        this.vertices = new ArrayList<Point>();
        this.vertices.addAll(Arrays.asList(points));
    }


    @Override
    public double area() {
        int n = vertices.size(); // size>2 ensured by the constructor
        double a = 0;
        for (int i = 0; i < n; i++) {
      //      a += vertices.get(i).getY() * vertices.get((i + 1)%n).getX()
        //            - vertices.get((i)%n).getX() * vertices.get((i + 1)%n).getY();
        a += vertices.get(i).getX() * vertices.get((i + 1)%n).getY()
                    - vertices.get((i+1)%n).getX() * vertices.get(i%n).getY();
        }
        a = Math.abs(a) / 2;
        return a;
    }

    @Override
    public double perimeter() {
        int size = vertices.size(); // size>2 ensured by the constructor
        double p = 0;
        for (int i = 0; i < size ; i++)
            p +=  Points.distance(vertices.get(i), vertices.get((i + 1)%size));
        return p;
    }

    @Override
    public void move(int dx, int dy) {
        this.vertices.stream().forEach((p) -> {
            p.move(dx, dy);
        });
//        this functional function replaces the following:
//        for(Point p:this.vertices)
//            p.move(dx,dy);
    }

    //object methods
    @Override
    public String toString() {
        return this.getClass().getSimpleName() + "{" + vertices + '}';
    }



}


class Quadrilateral extends Polygon {

    public Quadrilateral(Point... points) {
        super(points);
        if (points.length != 4) {
            throw new IllegalNumberOfVerticesException();
        }
        //also check for equal sides and angles
    }
}

class IllegalNumberOfVerticesException extends java.lang.IllegalArgumentException {

    public IllegalNumberOfVerticesException() {
    }

    public IllegalNumberOfVerticesException(String s) {
        super(s);
    }


}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)//only define : Polygon, Quadrilateral, IllegalNumberOfVerticesException
//the others already exist!
class Polygon extends Shape {

    private List<Point> vertices;

    public Polygon(Point... points) {
        String message = Polygons.isSimplePolygon(points);
        if (message != null) {
            throw new IllegalArgumentException(message);
        }
        this.vertices = new ArrayList<Point>();
        this.vertices.addAll(Arrays.asList(points));
    }

    @Override
    public double area() {
        int n = vertices.size(); // size>2 ensured by the constructor
        double a = 0;
        for (int i = 0; i < n; i++) {
      //      a += vertices.get(i).getY() * vertices.get((i + 1)%n).getX()
        //            - vertices.get((i)%n).getX() * vertices.get((i + 1)%n).getY();
        a += vertices.get(i).getX() * vertices.get((i + 1)%n).getY()
                    - vertices.get((i+1)%n).getX() * vertices.get(i%n).getY();
        }
        a = Math.abs(a) / 2;
        return a;
    }

    @Override
    public double perimeter() {
        int size = vertices.size(); // size>2 ensured by the constructor
        double p = 0;
        for (int i = 0; i < size ; i++)
            p +=  Points.distance(vertices.get(i), vertices.get((i + 1)%size));
        return p;
    }

    @Override
    public void move(int dx, int dy) {
        this.vertices.stream().forEach((p) -> {
            p.move(dx, dy);
        });
//        this functional function replaces the following:
//        for(Point p:this.vertices)
//            p.move(dx,dy);
    }

    //object methods
    @Override
    public String toString() {
        return this.getClass().getSimpleName() + "{" + vertices + '}';
    }

}

class Quadrilateral extends Polygon {

    public Quadrilateral(Point... points) {
        super(points);
        if (points.length != 4) {
            throw new IllegalNumberOfVerticesException();
        }
        //also check for equal sides and angles
    }
}

class IllegalNumberOfVerticesException extends java.lang.IllegalArgumentException {

    public IllegalNumberOfVerticesException() {
    }

    public IllegalNumberOfVerticesException(String s) {
        super(s);
    }

}

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)//only define : Polygon, Quadrilateral, IllegalNumberOfVerticesException
//the others already exist!
class Polygon extends Shape {

    private List<Point> vertices;

    public Polygon(Point... points) {
        String message = Polygons.isSimplePolygon(points);
        if (message != null) {
            throw new IllegalArgumentException(message);
        }
        this.vertices = new ArrayList<Point>();
        this.vertices.addAll(Arrays.asList(points));
    }

    @Override
    public double area() {
        int n = vertices.size(); // size>2 ensured by the constructor
        double a = 0;
        for (int i = 0; i < n; i++) {
      //      a += vertices.get(i).getY() * vertices.get((i + 1)%n).getX()
        //            - vertices.get((i)%n).getX() * vertices.get((i + 1)%n).getY();
        a += vertices.get(i).getX() * vertices.get((i + 1)%n).getY()
                    - vertices.get((i+1)%n).getX() * vertices.get(i%n).getY();
        }
        a = Math.abs(a) / 2;
        return a;
    }

    @Override
    public double perimeter() {
        int size = vertices.size(); // size>2 ensured by the constructor
        double p = 0;
        for (int i = 0; i < size ; i++)
            p +=  Points.distance(vertices.get(i), vertices.get((i + 1)%size));
        return p;
    }

    @Override
    public void move(int dx, int dy) {
        this.vertices.stream().forEach((p) -> {
            p.move(dx, dy);
        });
//        this functional function replaces the following:
//        for(Point p:this.vertices)
//            p.move(dx,dy);
    }

    //object methods
    @Override
    public String toString() {
        return this.getClass().getSimpleName() + "{" + vertices + '}';
    }

}

class Quadrilateral extends Polygon {

    public Quadrilateral(Point... points) {
        super(points);
        if (points.length != 4) {
            throw new IllegalNumberOfVerticesException();
        }
        //also check for equal sides and angles
    }
}

class IllegalNumberOfVerticesException extends java.lang.IllegalArgumentException {

    public IllegalNumberOfVerticesException() {
    }

    public IllegalNumberOfVerticesException(String s) {
        super(s);
    }

}
CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 3  (Correct; Note de 1,00 sur 1,00)

Dans le contexte de la création des classes Polygon et Quadrilateral avec les spécifications données :

**Propositions :**

```
a. IllegalNumberOfVerticesException est une sous-classe de Exception et doit donc toujours être gérée.
 
b. Si Polygon ne lance pas d'exception pour un nombre incorrect de sommets, alors Quadrilateral ne devrait pas non plus.
 
c. IllegalNumberOfVerticesException étant une sous-classe de RuntimeException, il n'est pas nécessaire de la gérer, mais c'est une bonne pratique de le faire.
 
d. Toutes les exceptions en Java doivent être gérées, sinon le code ne compilera pas.
 
e. Le constructeur de Quadrilateral peut lancer une exception même si le constructeur de Polygon ne le fait pas, car il pourrait avoir des contraintes plus strictes.
```

**Ma réponse :** a. IllegalNumberOfVerticesException est une sous-classe de Exception et doit donc toujours être gérée.   b. Si Polygon ne lance pas d'exception pour un nombre incorrect de sommets, alors Quadrilateral ne devrait pas non plus.   c. IllegalNumberOfVerticesException étant une sous-classe de RuntimeException, il n'est pas nécessaire de la gérer, mais c'est une bonne pratique de le faire.   d. Toutes les exceptions en Java doivent être gérées, sinon le code ne compilera pas.   e. Le constructeur de Quadrilateral peut lancer une exception même si le constructeur de Polygon ne le fait pas, car il pourrait avoir des contraintes plus strictes. / a. IllegalNumberOfVerticesException est une sous-classe de Exception et doit donc toujours être gérée.   b. Si Polygon ne lance pas d'exception pour un nombre incorrect de sommets, alors Quadrilateral ne devrait pas non plus.   c. IllegalNumberOfVerticesException étant une sous-classe de RuntimeException, il n'est pas nécessaire de la gérer, mais c'est une bonne pratique de le faire.   d. Toutes les exceptions en Java doivent être gérées, sinon le code ne compilera pas.   e. Le constructeur de Quadrilateral peut lancer une exception même si le constructeur de Polygon ne le fait pas, car il pourrait avoir des contraintes plus strictes.

**Correction :** Les réponses correctes sont : IllegalNumberOfVerticesException étant une sous-classe de RuntimeException, il n'est pas nécessaire de la gérer, mais c'est une bonne pratique de le faire., Le constructeur de Quadrilateral peut lancer une exception même si le constructeur de Polygon ne le fait pas, car il pourrait avoir des contraintes plus strictes.

**Retour Moodle :**

```
FeedbackLes réponses correctes sont : IllegalNumberOfVerticesException étant une sous-classe de RuntimeException, il n'est pas nécessaire de la gérer, mais c'est une bonne pratique de le faire., Le constructeur de Quadrilateral peut lancer une exception même si le constructeur de Polygon ne le fait pas, car il pourrait avoir des contraintes plus strictes.
```

## Question 4  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
//only define : Shape, Circle
//the others already exist!

abstract class Shape implements Mobile {
    public abstract double area();
    public abstract double perimeter();
    public abstract String toString();

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        return true;
    }

    @Override
    public int hashCode() {
        return getClass().hashCode();
    }
}

class Circle extends Conic {
    private Point center;
    private double radius;

    public Circle(Point center, double radius) {
        this.center = center;
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }

    @Override
    public double perimeter() {
        return 2 * Math.PI * radius;
    }

    @Override
    public void move(int dx, int dy) {
        center.move(dx, dy);
    }

    @Override
    public void resize(int scale) {
        radius = radius * Math.sqrt(scale / 100.0);
    }

    @Override
    public boolean equals(Object o) {
        if (!super.equals(o)) return false;   
        Circle c = (Circle) o;                 
        return Double.compare(radius, c.radius) == 0;
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), radius);
    }

    @Override
    public String toString() {
        return "Circle[center = " + center + ", radius = " + Math.round(radius * 100) / 100.0 + " ]";
    }
}
```

**Mon code / ma réponse :**

```
//only define : Shape, Circle
//the others already exist!

public abstract class Shape implements Mobile, Comparable<Shape> {
    @Override
    public String toString() {
        return this.getClass().getName();
    }

    @Override
    public final boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Shape other = (Shape) obj;
        return this.congruent(other);
    }

    public abstract boolean congruent(Shape s);

    public abstract double area();

    public abstract double perimeter();

    @Override
    public final int compareTo(Shape other) {
        if (this.area() == other.area()) {
            return Double.compare(this.perimeter(),other.perimeter());
        } 
        return Double.compare(this.area(),other.area());
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.area(),this.perimeter(),this.hashi());
    }

    protected abstract int hashi();

}

class Circle extends Conic {
    private Point center;
    private double radius;

    public Circle(Point center,double radius) {
        this.radius = radius;
        this.center = center;
    }
    
    @Override
    public String toString() {
        return super.toString() + "[center = " + center +", radius = " + radius + " ]";
    }

    @Override
    public boolean congruent(Shape s) {
        if(!(s instanceof Circle))
            return false;
        final Circle other=(Circle) s;
        return this.radius==other.radius;
    }

    @Override
    public double area() {
        return Math.PI*radius*radius;
    }

    @Override
    public double perimeter() {
        return 2*Math.PI*radius;
    }

    @Override
    public void move(int dx, int dy) {
        center.move(dx, dy);
    }

    @Override
    public void resize(int scale) {
        this.radius=this.radius*scale/100;
    }


    
}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)//only define : Shape, Circle
//the others already exist!

public abstract class Shape implements Mobile, Comparable<Shape> {
    @Override
    public String toString() {
        return this.getClass().getName();
    }

    @Override
    public final boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Shape other = (Shape) obj;
        return this.congruent(other);
    }

    public abstract boolean congruent(Shape s);

    public abstract double area();

    public abstract double perimeter();

    @Override
    public final int compareTo(Shape other) {
        if (this.area() == other.area()) {
            return Double.compare(this.perimeter(),other.perimeter());
        } 
        return Double.compare(this.area(),other.area());
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.area(),this.perimeter(),this.hashi());
    }

    protected abstract int hashi();

}

class Circle extends Conic {
    private Point center;
    private double radius;

    public Circle(Point center,double radius) {
        this.radius = radius;
        this.center = center;
    }
    
    @Override
    public String toString() {
        return super.toString() + "[center = " + center +", radius = " + radius + " ]";
    }

    @Override
    public boolean congruent(Shape s) {
        if(!(s instanceof Circle))
            return false;
        final Circle other=(Circle) s;
        return this.radius==other.radius;
    }

    @Override
    public double area() {
        return Math.PI*radius*radius;
    }

    @Override
    public double perimeter() {
        return 2*Math.PI*radius;
    }

    @Override
    public void move(int dx, int dy) {
        center.move(dx, dy);
    }

    @Override
    public void resize(int scale) {
        this.radius=this.radius*scale/100;
    }

    
}

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)//only define : Shape, Circle
//the others already exist!

public abstract class Shape implements Mobile, Comparable<Shape> {
    @Override
    public String toString() {
        return this.getClass().getName();
    }

    @Override
    public final boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Shape other = (Shape) obj;
        return this.congruent(other);
    }

    public abstract boolean congruent(Shape s);

    public abstract double area();

    public abstract double perimeter();

    @Override
    public final int compareTo(Shape other) {
        if (this.area() == other.area()) {
            return Double.compare(this.perimeter(),other.perimeter());
        } 
        return Double.compare(this.area(),other.area());
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.area(),this.perimeter(),this.hashi());
    }

    protected abstract int hashi();

}

class Circle extends Conic {
    private Point center;
    private double radius;

    public Circle(Point center,double radius) {
        this.radius = radius;
        this.center = center;
    }
    
    @Override
    public String toString() {
        return super.toString() + "[center = " + center +", radius = " + radius + " ]";
    }

    @Override
    public boolean congruent(Shape s) {
        if(!(s instanceof Circle))
            return false;
        final Circle other=(Circle) s;
        return this.radius==other.radius;
    }

    @Override
    public double area() {
        return Math.PI*radius*radius;
    }

    @Override
    public double perimeter() {
        return 2*Math.PI*radius;
    }

    @Override
    public void move(int dx, int dy) {
        center.move(dx, dy);
    }

    @Override
    public void resize(int scale) {
        this.radius=this.radius*scale/100;
    }

    
}

CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 5  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
//only define : Shape
//the others already exist!

abstract class Shape implements Mobile, Comparable<Shape> {
    public abstract double area();
    public abstract double perimeter();

    protected abstract int hashi();
    protected abstract boolean congruent(Shape s);

    @Override
    public String toString() {
        return getClass().getSimpleName();
    }

    @Override
    public final boolean equals(Object o) {
        if (this == o){
            return true;
        }
        if (o == null || getClass() != o.getClass()){
            return false;
        }
        return congruent((Shape) o);
    }

    @Override
    public final int hashCode() {
        return hashi();
    }

    @Override
    public final int compareTo(Shape s) {
        int c = Double.compare(area(), s.area());
        if (c != 0){
            return c;
        }
        return Double.compare(perimeter(), s.perimeter());
    }
}
```

**Mon code / ma réponse :**

```
//only define : Shape
//the others already exist!

public abstract class Shape implements Mobile, Comparable<Shape> {
    @Override
    public String toString() {
        return this.getClass().getName();
    }

    @Override
    public final boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Shape other = (Shape) obj;
        return this.congruent(other);
    }

    public abstract boolean congruent(Shape s);

    public abstract double area();

    public abstract double perimeter();

    @Override
    public final int compareTo(Shape other) {
        if (this.area() == other.area()) {
            return Double.compare(this.perimeter(),other.perimeter());
        } 
        return Double.compare(this.area(),other.area());
    }

    @Override
    public final int hashCode() {
        return Objects.hash(this.area(),this.perimeter(),this.hashi());
    }


    protected abstract int hashi();
}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)//only define : Shape
//the others already exist!

public abstract class Shape implements Mobile, Comparable<Shape> {
    @Override
    public String toString() {
        return this.getClass().getName();
    }

    @Override
    public final boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Shape other = (Shape) obj;
        return this.congruent(other);
    }

    public abstract boolean congruent(Shape s);

    public abstract double area();

    public abstract double perimeter();

    @Override
    public final int compareTo(Shape other) {
        if (this.area() == other.area()) {
            return Double.compare(this.perimeter(),other.perimeter());
        } 
        return Double.compare(this.area(),other.area());
    }

    @Override
    public final int hashCode() {
        return Objects.hash(this.area(),this.perimeter(),this.hashi());
    }

    protected abstract int hashi();
}

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)//only define : Shape
//the others already exist!

public abstract class Shape implements Mobile, Comparable<Shape> {
    @Override
    public String toString() {
        return this.getClass().getName();
    }

    @Override
    public final boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Shape other = (Shape) obj;
        return this.congruent(other);
    }

    public abstract boolean congruent(Shape s);

    public abstract double area();

    public abstract double perimeter();

    @Override
    public final int compareTo(Shape other) {
        if (this.area() == other.area()) {
            return Double.compare(this.perimeter(),other.perimeter());
        } 
        return Double.compare(this.area(),other.area());
    }

    @Override
    public final int hashCode() {
        return Objects.hash(this.area(),this.perimeter(),this.hashi());
    }

    protected abstract int hashi();
}

CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 6  (Correct; Note de 1,00 sur 1,00)

Étant donné l'implémentation décrite des méthodes equals() et compareTo(), sont-elles compatibles?

**Propositions :**

```
a. Non, car bien que deux formes congruentes (equals() renvoyant true) aient toujours la même aire et le même périmètre (compareTo() renvoyant 0), deux formes ayant la même aire et le même périmètre pourraient ne pas être congruentes.
 
b. Oui, car si equals() est vrai, compareTo() sera toujours 0, et vice versa.
 
c. Oui, car ils travaillent tous les deux avec les mêmes propriétés des formes et donneront donc toujours des résultats cohérents.
 
d. Non, car elles abordent des concepts totalement différents et sont mises en œuvre indépendamment.
 
e. Oui, car deux formes congruentes (equals() renvoyant true) ont toujours la même aire et le même périmètre (compareTo() renvoyant 0), et deux formes ayant la même aire et le même périmètre seront toujours congruentes.
```

**Ma réponse :** a. Non, car bien que deux formes congruentes (equals() renvoyant true) aient toujours la même aire et le même périmètre (compareTo() renvoyant 0), deux formes ayant la même aire et le même périmètre pourraient ne pas être congruentes.   b. Oui, car si equals() est vrai, compareTo() sera toujours 0, et vice versa.   c. Oui, car ils travaillent tous les deux avec les mêmes propriétés des formes et donneront donc toujours des résultats cohérents.   d. Non, car elles abordent des concepts totalement différents et sont mises en œuvre indépendamment.   e. Oui, car deux formes congruentes (equals() renvoyant true) ont toujours la même aire et le même périmètre (compareTo() renvoyant 0), et deux formes ayant la même aire et le même périmètre seront toujours congruentes.

**Correction :** La réponse correcte est : Non, car bien que deux formes congruentes (equals() renvoyant true) aient toujours la même aire et le même périmètre (compareTo() renvoyant 0), deux formes ayant la même aire et le même périmètre pourraient ne pas être congruentes.

**Retour Moodle :**

```
FeedbackLa réponse correcte est : Non, car bien que deux formes congruentes (equals() renvoyant true) aient toujours la même aire et le même périmètre (compareTo() renvoyant 0), deux formes ayant la même aire et le même périmètre pourraient ne pas être congruentes.
```

## Question 7  (Correct; Note de 1,00 sur 1,00)

Pourquoi la méthode compareTo() devrait-elle être marquée comme final dans la classe abstraite Shape ?

**Propositions :**

```
a. Pour garantir que tous les sous-types de Shape utilisent la même logique de comparaison, garantissant l'uniformité, respectant le principe de substitution de Liskov et prévenant la modification involontaire par les sous-classes.
 
b. Pour permettre aux sous-classes de redéfinir le mécanisme de comparaison selon leurs besoins.
 
c. Pour rendre la classe Shape immuable et sûre pour les threads.
 
d. Pour augmenter les performances d'exécution de la classe Shape.
 
e. Pour permettre à tous les sous-types de Shape d'implémenter leur propre logique de comparaison unique, permettant un comportement diversifié et encourageant les sous-types à remplacer le mécanisme de comparaison de la superclasse.
```

**Ma réponse :** a. Pour garantir que tous les sous-types de Shape utilisent la même logique de comparaison, garantissant l'uniformité, respectant le principe de substitution de Liskov et prévenant la modification involontaire par les sous-classes.   b. Pour permettre aux sous-classes de redéfinir le mécanisme de comparaison selon leurs besoins.   c. Pour rendre la classe Shape immuable et sûre pour les threads.   d. Pour augmenter les performances d'exécution de la classe Shape.   e. Pour permettre à tous les sous-types de Shape d'implémenter leur propre logique de comparaison unique, permettant un comportement diversifié et encourageant les sous-types à remplacer le mécanisme de comparaison de la superclasse.

**Correction :** La réponse correcte est : Pour garantir que tous les sous-types de Shape utilisent la même logique de comparaison, garantissant l'uniformité, respectant le principe de substitution de Liskov et prévenant la modification involontaire par les sous-classes.

**Retour Moodle :**

```
FeedbackLa réponse correcte est : Pour garantir que tous les sous-types de Shape utilisent la même logique de comparaison, garantissant l'uniformité, respectant le principe de substitution de Liskov et prévenant la modification involontaire par les sous-classes.
```

## Question 8  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
//only define : Folder
//the others already exist!

class Folder {
    private String name;
    private Shape[] shapes;
    private int count;
    private int next;

    public Folder(String name, int size) {
        this.name = name;
        this.shapes = new Shape[size];
    }

    public Folder(String name) {
        this(name, 10);
    }

    public void add(Shape s) {
        shapes[next] = s;
        next = (next + 1) % shapes.length;
        if (count < shapes.length){
            count++;
        }
    }

    public void moveShapes(int dx, int dy) {
        for (int i = 0; i < count; i++) {
            shapes[i].move(dx, dy);
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < count; i++) {
            if (i > 0){
                sb.append(", ");
            }
            sb.append(shapes[i]);
        }
        sb.append("]");
        return "Folder{ name=" + name + ", shapes=" + sb + "}";
    }
}
```

**Mon code / ma réponse :**

```
//only define : Folder
//the others already exist!

class Folder {

    /** The name of the folder. */
    private String name;

    private int size;

    private int index = -1;

    private Shape[] shapes;

    public Folder(String name, int size) {
        this.name = name;
        this.size = size;
        shapes = new Shape[size];
    }

    public Folder(String name) {
        this(name, 10);
    }

    public Folder() {
        this("No name");
    }

    public Folder(int size) {
        this("No name", size);
    }
    public void add(Shape s) {
        index = (index + 1) % size; // it will replace in round cycle if no more space
        shapes[index] = s;
    }

    public void moveShapes(int dx, int dy) {
        for (Shape s : shapes) {
            if (s != null) {
                s.move(dx, dy);
            }
        }
    }

    // ... other details

    @Override
    public String toString() {
        return this.getClass().getSimpleName() + "{ name=" + name + ", shapes=" + Arrays.toString(shapes) + '}';
    }
}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)//only define : Folder
//the others already exist!

class Folder {

    /** The name of the folder. */
    private String name;

    private int size;

    private int index = -1;

    private Shape[] shapes;

    public Folder(String name, int size) {
        this.name = name;
        this.size = size;
        shapes = new Shape[size];
    }

    public Folder(String name) {
        this(name, 10);
    }

    public Folder() {
        this("No name");
    }

    public Folder(int size) {
        this("No name", size);
    }
    public void add(Shape s) {
        index = (index + 1) % size; // it will replace in round cycle if no more space
        shapes[index] = s;
    }

    public void moveShapes(int dx, int dy) {
        for (Shape s : shapes) {
            if (s != null) {
                s.move(dx, dy);
            }
        }
    }

    // ... other details

    @Override
    public String toString() {
        return this.getClass().getSimpleName() + "{ name=" + name + ", shapes=" + Arrays.toString(shapes) + '}';
    }
}

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)//only define : Folder
//the others already exist!

class Folder {

    /** The name of the folder. */
    private String name;

    private int size;

    private int index = -1;

    private Shape[] shapes;

    public Folder(String name, int size) {
        this.name = name;
        this.size = size;
        shapes = new Shape[size];
    }

    public Folder(String name) {
        this(name, 10);
    }

    public Folder() {
        this("No name");
    }

    public Folder(int size) {
        this("No name", size);
    }
    public void add(Shape s) {
        index = (index + 1) % size; // it will replace in round cycle if no more space
        shapes[index] = s;
    }

    public void moveShapes(int dx, int dy) {
        for (Shape s : shapes) {
            if (s != null) {
                s.move(dx, dy);
            }
        }
    }

    // ... other details

    @Override
    public String toString() {
        return this.getClass().getSimpleName() + "{ name=" + name + ", shapes=" + Arrays.toString(shapes) + '}';
    }
}CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 9  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class MemoryFolder extends Folder {
    private final Counter counter;

    public MemoryFolder(Counter counter) {
        super();
        this.counter = counter;
    }

    public MemoryFolder() {
        this(new Counter());
    }

    @Override
    public void moveShapes(int dx, int dy) {
        super.moveShapes(dx, dy);
        counter.inc();
    }

    public int getNbMoves() {
        return counter.getC();
    }

    @Override
    public String toString() {
        return super.toString() + "[moveCount=" + getNbMoves() + "]";
    }
}
```

**Mon code / ma réponse :**

```
//only define : MemoryFolder
//the others already exist!

class MemoryFolder extends Folder {

    private final Counter moveCount;

    public MemoryFolder() {
        moveCount = new Counter();
    }

    public MemoryFolder(Counter c) {
        this.moveCount = c;
    }

    int getNbMoves() {
        return this.moveCount.getC();
    }

    @Override
    public void moveShapes(int dx, int dy) {
        super.moveShapes(dx, dy);
        moveCount.inc();
    }

    @Override
    public String toString() {
        return super.toString()+ "[moveCount=" + moveCount + ']';
    }

}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)//only define : MemoryFolder
//the others already exist!

class MemoryFolder extends Folder {

    private final Counter moveCount;

    public MemoryFolder() {
        moveCount = new Counter();
    }

    public MemoryFolder(Counter c) {
        this.moveCount = c;
    }

    int getNbMoves() {
        return this.moveCount.getC();
    }

    @Override
    public void moveShapes(int dx, int dy) {
        super.moveShapes(dx, dy);
        moveCount.inc();
    }

    @Override
    public String toString() {
        return super.toString()+ "[moveCount=" + moveCount + ']';
    }

}

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)//only define : MemoryFolder
//the others already exist!

class MemoryFolder extends Folder {

    private final Counter moveCount;

    public MemoryFolder() {
        moveCount = new Counter();
    }

    public MemoryFolder(Counter c) {
        this.moveCount = c;
    }

    int getNbMoves() {
        return this.moveCount.getC();
    }

    @Override
    public void moveShapes(int dx, int dy) {
        super.moveShapes(dx, dy);
        moveCount.inc();
    }

    @Override
    public String toString() {
        return super.toString()+ "[moveCount=" + moveCount + ']';
    }

}
CorrectNote pour cet envoi : 1,00/1,00.
```
