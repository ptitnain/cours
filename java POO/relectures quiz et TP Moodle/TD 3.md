# TD 3

*Java, section « Travaux Dirigés 1 - 4 ». Relecture de ma tentative sur Moodle ([lien](https://learning.esiea.fr/mod/quiz/review.php?attempt=36536&cmid=7028)).*

## Résumé

- **Statut** : Terminée
- **Commencé** : mardi 24 novembre 2026, 13:12
- **Terminé** : mardi 24 novembre 2026, 16:12
- **Durée** : 3 heures
- **Points** : 19,00/19,00
- **Note** : 20,00 sur 20,00 (100%)

## Question 1  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
abstract class Figure {

    public abstract void draw();
    public abstract void translate(double delta);
    public abstract void rotate(double theta);

    public void translateAndRotate(double delta, double theta) {
        translate(delta);
        rotate(theta);
    }

    public static void draw(Figure[] shapes) {
        for (Figure f : shapes)
            f.draw();
    }

    public static void translate(double delta, Figure[] shapes) {
        for (Figure f : shapes)
            f.translate(delta);
    }

    public static void rotate(double theta, Figure[] shapes) {
        for (Figure f : shapes)
            f.rotate(theta);
    }
}





class Point extends Figure {
	private double x, y;

	public Point(double abs, double ord) {
		x = abs;
		y = ord;
	}

	public void translate(double d) {
		x += d;
		y += d;
	}
	
	public void rotate (double theta) {
		double x1, y1, angle, c, s;
		//angle (en degrés)
		angle = Math.toRadians(theta);
		
		c = Math.cos (angle);
		s = Math.sin (angle);
		x1 = this.x * c - this.y * s;
		y1 = this.x * s + this.y * c;
		this.x = x1;
		this.y = y1;
	}

	public double getX() {
		return x;
	}

	public double getY() {
		return y;
	}

	

	@Override
	public String toString() {
		return "Point [x=" +  String.format("%.2f", x) + ", y=" + String.format("%.2f", y) + "]";
	}


	@Override
	public void draw() {
		System.out.println("drawing a point.");
		
	}


}

class Circle extends Figure{
	
	private Point center;
	private double radius;
	
	public Circle (Point p, double r) {
		p = new Point(p.getX(), p.getY());
		this.center = p;		
		this.radius  = r;
	}
	
	@Override
	public void draw() {
		System.out.println("drawing a circle.");
	}

	@Override
	public void translate(double delta) {
		this.center.translate(delta);
	}

	@Override
	public void rotate(double theta) {
		this.center.rotate(theta);
	}
	
	@Override
	public String toString() {
		return "Circle [center=" + center + ", radius=" + radius + "]\n";
	}

}

class Ellipse extends Figure {
	
	private Point foci1, foci2;
	private double d;
	
	public Ellipse(Point f1, Point f2, double d) {
		f1 = new Point(f1.getX(), f1.getY());
		f2 = new Point(f2.getX(), f2.getY());
		this.foci1=f1;
		this.foci2=f2;
		this.d = d;
	}

	@Override
	public void draw() {
		System.out.println("drawing a ellipse.");
		
	}

	@Override
	public void translate(double delta) {
		this.foci1.translate(delta);
		this.foci2.translate(delta);
		
	}

	@Override
	public void rotate(double theta) {
		this.foci1.rotate(theta);
		this.foci2.rotate(theta);
	}

	@Override
	public String toString() {
		return "Ellipse [foci1=" + foci1 + ", foci2=" + foci2 + ", d=" + d + "]\n";
	}

}

class Triangle extends Figure {
	private Point[] vertices;

	@Override
	public void draw() {
		System.out.println("drawing a triangle.");
	}

	public Triangle(Point... v) {
		this.vertices = v;
		for (int i = 0; i < 3; i++)
			v[i] = new Point(v[i].getX(), v[i].getY());
	}

	@Override
	public String toString() {
		return "Triangle [vertices=" + Arrays.toString(vertices) + "]\n";
	}

	@Override
	public void translate(double delta) {
		for (Point p : this.vertices)
			p.translate(delta);

	}

	@Override
	public void rotate(double theta) {
		for (Point p : this.vertices)
			p.rotate(theta);
	}

}

class Rectangle extends Figure {
	
	private Point [] vertices;
	
	public Rectangle (Point ... v) {
		this.vertices = v;
		for (int i = 0; i<4;i++)
			v[i] = new Point(v[i].getX(), v[i].getY());
	}
	
	
	@Override
	public String toString() {
		return "Rectangle [vertices=" + Arrays.toString(vertices) + "]\n";
	}


	@Override
	public void draw() {
		System.out.println("drawing a rectangle.");
	}

	@Override
	public void translate(double delta) {
		for (Point p: this.vertices)
			p.translate(delta);
		
	}

	@Override
	public void rotate(double theta) {
		for (Point p: this.vertices)
			p.rotate(theta);
	}

	
}
```

**Mon code / ma réponse :**

```
abstract class Figure {
	public abstract void draw();
	public abstract void translate(double delta);
	public abstract void rotate(double theta);
	
	public void translateAndRotate(double delta, double theta) {
		this.translate(delta);
		this.rotate(theta);
	}

	public static void translate(double delta, Figure ...figures) {
		for (Figure f: figures)
			f.translate(delta);
	}

	public static void rotate(double theta, Figure ...figures) {
		for (Figure f: figures)
			f.rotate(theta);		
	}
	
	public static void draw(Figure ...figures) {
		for (Figure f: figures)
			f.draw();		
	}

}

class Point extends Figure {
	private double x, y;

	public Point(double abs, double ord) {
		x = abs;
		y = ord;
	}

	public void translate(double d) {
		x += d;
		y += d;
	}
	
	public void rotate (double theta) {
		double x1, y1, angle, c, s;
		//angle (en degrés)
		angle = Math.toRadians(theta);
		
		c = Math.cos (angle);
		s = Math.sin (angle);
		x1 = this.x * c - this.y * s;
		y1 = this.x * s + this.y * c;
		this.x = x1;
		this.y = y1;
	}

	public double getX() {
		return x;
	}

	public double getY() {
		return y;
	}

	

	@Override
	public String toString() {
		return "Point [x=" +  String.format("%.2f", x) + ", y=" + String.format("%.2f", y) + "]";
	}


	@Override
	public void draw() {
		System.out.println("drawing a point.");
		
	}


}

class Circle extends Figure{
	
	private Point center;
	private double radius;
	
	public Circle (Point p, double r) {
		p = new Point(p.getX(), p.getY());
		this.center = p;		
		this.radius  = r;
	}
	
	@Override
	public void draw() {
		System.out.println("drawing a circle.");
	}

	@Override
	public void translate(double delta) {
		this.center.translate(delta);
	}

	@Override
	public void rotate(double theta) {
		this.center.rotate(theta);
	}
	
	@Override
	public String toString() {
		return "Circle [center=" + center + ", radius=" + radius + "]\n";
	}

}

class Ellipse extends Figure {
	
	private Point foci1, foci2;
	private double d;
	
	public Ellipse(Point f1, Point f2, double d) {
		f1 = new Point(f1.getX(), f1.getY());
		f2 = new Point(f2.getX(), f2.getY());
		this.foci1=f1;
		this.foci2=f2;
		this.d = d;
	}

	@Override
	public void draw() {
		System.out.println("drawing a ellipse.");
		
	}

	@Override
	public void translate(double delta) {
		this.foci1.translate(delta);
		this.foci2.translate(delta);
		
	}

	@Override
	public void rotate(double theta) {
		this.foci1.rotate(theta);
		this.foci2.rotate(theta);
	}

	@Override
	public String toString() {
		return "Ellipse [foci1=" + foci1 + ", foci2=" + foci2 + ", d=" + d + "]\n";
	}

}

class Triangle extends Figure {
	private Point[] vertices;

	@Override
	public void draw() {
		System.out.println("drawing a triangle.");
	}

	public Triangle(Point... v) {
		this.vertices = v;
		for (int i = 0; i < 3; i++)
			v[i] = new Point(v[i].getX(), v[i].getY());
	}

	@Override
	public String toString() {
		return "Triangle [vertices=" + Arrays.toString(vertices) + "]\n";
	}

	@Override
	public void translate(double delta) {
		for (Point p : this.vertices)
			p.translate(delta);

	}

	@Override
	public void rotate(double theta) {
		for (Point p : this.vertices)
			p.rotate(theta);
	}

}

class Rectangle extends Figure {
	
	private Point [] vertices;
	
	public Rectangle (Point ... v) {
		this.vertices = v;
		for (int i = 0; i<4;i++)
			v[i] = new Point(v[i].getX(), v[i].getY());
	}
	
	
	@Override
	public String toString() {
		return "Rectangle [vertices=" + Arrays.toString(vertices) + "]\n";
	}


	@Override
	public void draw() {
		System.out.println("drawing a rectangle.");
	}

	@Override
	public void translate(double delta) {
		for (Point p: this.vertices)
			p.translate(delta);
		
	}

	@Override
	public void rotate(double theta) {
		for (Point p: this.vertices)
			p.rotate(theta);
	}

	
}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)abstract class Figure {
	public abstract void draw();
	public abstract void translate(double delta);
	public abstract void rotate(double theta);
	
	public void translateAndRotate(double delta, double theta) {
		this.translate(delta);
		this.rotate(theta);
	}

	public static void translate(double delta, Figure ...figures) {
		for (Figure f: figures)
			f.translate(delta);
	}

	public static void rotate(double theta, Figure ...figures) {
		for (Figure f: figures)
			f.rotate(theta);		
	}
	
	public static void draw(Figure ...figures) {
		for (Figure f: figures)
			f.draw();		
	}

}

class Point extends Figure {
	private double x, y;

	public Point(double abs, double ord) {
		x = abs;
		y = ord;
	}

	public void translate(double d) {
		x += d;
		y += d;
	}
	
	public void rotate (double theta) {
		double x1, y1, angle, c, s;
		//angle (en degrés)
		angle = Math.toRadians(theta);
		
		c = Math.cos (angle);
		s = Math.sin (angle);
		x1 = this.x * c - this.y * s;
		y1 = this.x * s + this.y * c;
		this.x = x1;
		this.y = y1;
	}

	public double getX() {
		return x;
	}

	public double getY() {
		return y;
	}

	

	@Override
	public String toString() {
		return "Point [x=" +  String.format("%.2f", x) + ", y=" + String.format("%.2f", y) + "]";
	}

	@Override
	public void draw() {
		System.out.println("drawing a point.");
		
	}

}

class Circle extends Figure{
	
	private Point center;
	private double radius;
	
	public Circle (Point p, double r) {
		p = new Point(p.getX(), p.getY());
		this.center = p;		
		this.radius  = r;
	}
	
	@Override
	public void draw() {
		System.out.println("drawing a circle.");
	}

	@Override
	public void translate(double delta) {
		this.center.translate(delta);
	}

	@Override
	public void rotate(double theta) {
		this.center.rotate(theta);
	}
	
	@Override
	public String toString() {
		return "Circle [center=" + center + ", radius=" + radius + "]\n";
	}

}

class Ellipse extends Figure {
	
	private Point foci1, foci2;
	private double d;
	
	public Ellipse(Point f1, Point f2, double d) {
		f1 = new Point(f1.getX(), f1.getY());
		f2 = new Point(f2.getX(), f2.getY());
		this.foci1=f1;
		this.foci2=f2;
		this.d = d;
	}

	@Override
	public void draw() {
		System.out.println("drawing a ellipse.");
		
	}

	@Override
	public void translate(double delta) {
		this.foci1.translate(delta);
		this.foci2.translate(delta);
		
	}

	@Override
	public void rotate(double theta) {
		this.foci1.rotate(theta);
		this.foci2.rotate(theta);
	}

	@Override
	public String toString() {
		return "Ellipse [foci1=" + foci1 + ", foci2=" + foci2 + ", d=" + d + "]\n";
	}

}

class Triangle extends Figure {
	private Point[] vertices;

	@Override
	public void draw() {
		System.out.println("drawing a triangle.");
	}

	public Triangle(Point... v) {
		this.vertices = v;
		for (int i = 0; i < 3; i++)
			v[i] = new Point(v[i].getX(), v[i].getY());
	}

	@Override
	public String toString() {
		return "Triangle [vertices=" + Arrays.toString(vertices) + "]\n";
	}

	@Override
	public void translate(double delta) {
		for (Point p : this.vertices)
			p.translate(delta);

	}

	@Override
	public void rotate(double theta) {
		for (Point p : this.vertices)
			p.rotate(theta);
	}

}

class Rectangle extends Figure {
	
	private Point [] vertices;
	
	public Rectangle (Point ... v) {
		this.vertices = v;
		for (int i = 0; i<4;i++)
			v[i] = new Point(v[i].getX(), v[i].getY());
	}
	
	
	@Override
	public String toString() {
		return "Rectangle [vertices=" + Arrays.toString(vertices) + "]\n";
	}

	@Override
	public void draw() {
		System.out.println("drawing a rectangle.");
	}

	@Override
	public void translate(double delta) {
		for (Point p: this.vertices)
			p.translate(delta);
		
	}

	@Override
	public void rotate(double theta) {
		for (Point p: this.vertices)
			p.rotate(theta);
	}

	
}

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)abstract class Figure {
	public abstract void draw();
	public abstract void translate(double delta);
	public abstract void rotate(double theta);
	
	public void translateAndRotate(double delta, double theta) {
		this.translate(delta);
		this.rotate(theta);
	}

	public static void translate(double delta, Figure ...figures) {
		for (Figure f: figures)
			f.translate(delta);
	}

	public static void rotate(double theta, Figure ...figures) {
		for (Figure f: figures)
			f.rotate(theta);		
	}
	
	public static void draw(Figure ...figures) {
		for (Figure f: figures)
			f.draw();		
	}

}

class Point extends Figure {
	private double x, y;

	public Point(double abs, double ord) {
		x = abs;
		y = ord;
	}

	public void translate(double d) {
		x += d;
		y += d;
	}
	
	public void rotate (double theta) {
		double x1, y1, angle, c, s;
		//angle (en degrés)
		angle = Math.toRadians(theta);
		
		c = Math.cos (angle);
		s = Math.sin (angle);
		x1 = this.x * c - this.y * s;
		y1 = this.x * s + this.y * c;
		this.x = x1;
		this.y = y1;
	}

	public double getX() {
		return x;
	}

	public double getY() {
		return y;
	}

	

	@Override
	public String toString() {
		return "Point [x=" +  String.format("%.2f", x) + ", y=" + String.format("%.2f", y) + "]";
	}

	@Override
	public void draw() {
		System.out.println("drawing a point.");
		
	}

}

class Circle extends Figure{
	
	private Point center;
	private double radius;
	
	public Circle (Point p, double r) {
		p = new Point(p.getX(), p.getY());
		this.center = p;		
		this.radius  = r;
	}
	
	@Override
	public void draw() {
		System.out.println("drawing a circle.");
	}

	@Override
	public void translate(double delta) {
		this.center.translate(delta);
	}

	@Override
	public void rotate(double theta) {
		this.center.rotate(theta);
	}
	
	@Override
	public String toString() {
		return "Circle [center=" + center + ", radius=" + radius + "]\n";
	}

}

class Ellipse extends Figure {
	
	private Point foci1, foci2;
	private double d;
	
	public Ellipse(Point f1, Point f2, double d) {
		f1 = new Point(f1.getX(), f1.getY());
		f2 = new Point(f2.getX(), f2.getY());
		this.foci1=f1;
		this.foci2=f2;
		this.d = d;
	}

	@Override
	public void draw() {
		System.out.println("drawing a ellipse.");
		
	}

	@Override
	public void translate(double delta) {
		this.foci1.translate(delta);
		this.foci2.translate(delta);
		
	}

	@Override
	public void rotate(double theta) {
		this.foci1.rotate(theta);
		this.foci2.rotate(theta);
	}

	@Override
	public String toString() {
		return "Ellipse [foci1=" + foci1 + ", foci2=" + foci2 + ", d=" + d + "]\n";
	}

}

class Triangle extends Figure {
	private Point[] vertices;

	@Override
	public void draw() {
		System.out.println("drawing a triangle.");
	}

	public Triangle(Point... v) {
		this.vertices = v;
		for (int i = 0; i < 3; i++)
			v[i] = new Point(v[i].getX(), v[i].getY());
	}

	@Override
	public String toString() {
		return "Triangle [vertices=" + Arrays.toString(vertices) + "]\n";
	}

	@Override
	public void translate(double delta) {
		for (Point p : this.vertices)
			p.translate(delta);

	}

	@Override
	public void rotate(double theta) {
		for (Point p : this.vertices)
			p.rotate(theta);
	}

}

class Rectangle extends Figure {
	
	private Point [] vertices;
	
	public Rectangle (Point ... v) {
		this.vertices = v;
		for (int i = 0; i<4;i++)
			v[i] = new Point(v[i].getX(), v[i].getY());
	}
	
	
	@Override
	public String toString() {
		return "Rectangle [vertices=" + Arrays.toString(vertices) + "]\n";
	}

	@Override
	public void draw() {
		System.out.println("drawing a rectangle.");
	}

	@Override
	public void translate(double delta) {
		for (Point p: this.vertices)
			p.translate(delta);
		
	}

	@Override
	public void rotate(double theta) {
		for (Point p: this.vertices)
			p.rotate(theta);
	}

	
}

CorrectNote pour cet envoi : 1,00/1,00.
```

## Description

On souhaite disposer de classes permettant de manipuler des figures géométriques Figure. On souhaite pouvoir caractériser celles qui possèdent certaines fonctionnalités en leur demandant d’implémenter des interfaces, à savoir :

IDisplayable : pour celles qui disposeront d’une méthode:

void display()

ITransformable:  pour celles qui disposeront des deux méthodes suivantes :

void translation (double delta)
void rotation (double angle)

## Question 2  (Terminé; Non noté)

Dessinez le diagramme UML de classes qui représente les classes et les interfaces mentionnées en 30.c (ci dessous)

Mettez un lien vers la figures, que vous mettez dans un espaces partageable.

**Propositions :**

```
Texte de réponse Question 2
```

## Question 3  (Correct; Note de 2,00 sur 2,00)

(énoncé vide)

**Mon code / ma réponse :**

```
public interface IDisplayable {
    void display();
}

public interface ITransformable {
    void translation(double delta);
    void rotation(double angle);
}

public class Point implements IDisplayable {
    public Point() {
    }

    public void display() {
        System.out.println("Point.display()");
    }
}

public class Rectangle implements IDisplayable, ITransformable {
    public Rectangle() {
    }

    public void display() {
        System.out.println("Rectangle.display()");
    }

    public void translation(double delta) {
        System.out.println("Rectangle.translation()");
    }

    public void rotation(double angle) {
        System.out.println("Rectangle.rotation()");
    }
}
```

**Mon code / ma réponse :**

```
public interface ITransformable {
	public void translation (double delta);
	public void rotation (double angle);

}

public interface IDisplayable {
	public void display();
}



public class Point implements IDisplayable {

	public void display() {
		System.out.println("Point.display()");
	}
}

public class Rectangle implements IDisplayable, ITransformable {

	public void display() {
		System.out.println("Rectangle.display()");
	}
	
	public void translation (double delta) {
		System.out.println("Rectangle.translation()");
	}
	
	public void rotation (double angle) {
		System.out.println("Rectangle.rotation()");
	}

}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)public interface ITransformable {
	public void translation (double delta);
	public void rotation (double angle);

}

public interface IDisplayable {
	public void display();
}

public class Point implements IDisplayable {

	public void display() {
		System.out.println("Point.display()");
	}
}

public class Rectangle implements IDisplayable, ITransformable {

	public void display() {
		System.out.println("Rectangle.display()");
	}
	
	public void translation (double delta) {
		System.out.println("Rectangle.translation()");
	}
	
	public void rotation (double angle) {
		System.out.println("Rectangle.rotation()");
	}

}

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)public interface ITransformable {
	public void translation (double delta);
	public void rotation (double angle);

}

public interface IDisplayable {
	public void display();
}

public class Point implements IDisplayable {

	public void display() {
		System.out.println("Point.display()");
	}
}

public class Rectangle implements IDisplayable, ITransformable {

	public void display() {
		System.out.println("Rectangle.display()");
	}
	
	public void translation (double delta) {
		System.out.println("Rectangle.translation()");
	}
	
	public void rotation (double angle) {
		System.out.println("Rectangle.rotation()");
	}

}
CorrectNote pour cet envoi : 2,00/2,00.
```

## Question 4  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
import java.util.*;

class ComparatorCircle implements Comparator<Circle> {
	public int compare(Circle c1, Circle c2){
	    return Double.compare(c1.getRadius(), c2.getRadius());
	}
}

class Circle {
	private int x,y;
	private double radius;
	public Circle (int x, int y, double radius) {
		this.x = x;
		this.y = y;
		this.radius = radius;
	}
	public void display () {
		System.out.println("Coordinates: " + x + ", " + y + "; radius: " + radius);
	}
	public double getRadius() {
		return radius;
	}
	public int getX() {
		return x;
	}
}
```

**Mon code / ma réponse :**

```
import java.util.*;

class ComparatorCircle implements Comparator<Circle> {
	
	public int compare (Circle c1, Circle c2) {
		//Returns a negative integer, zero, or a positive integer as the first argument is less than, equal to, or greater than the second.
		double r1 = c1.getRadius();
		double r2 = c2.getRadius();
		
		int result = 0;
		if (r1 < r2) result = -1;
		else if (r1 > r2) result = 1;
		else result = 0;
		
		return result;
	}
}

class Circle {
	private int x,y;
	private double radius;
	public Circle (int x, int y, double radius) {
		this.x = x;
		this.y = y;
		this.radius = radius;
	}
	public void display () {
		System.out.println("Coordinates: " + x + ", " + y + "; radius: " + radius);
	}
	public double getRadius() {
		return radius;
	}
	public int getX() {
		return x;
	}
}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)import java.util.*;

class ComparatorCircle implements Comparator<Circle> {
	
	public int compare (Circle c1, Circle c2) {
		//Returns a negative integer, zero, or a positive integer as the first argument is less than, equal to, or greater than the second.
		double r1 = c1.getRadius();
		double r2 = c2.getRadius();
		
		int result = 0;
		if (r1 < r2) result = -1;
		else if (r1 > r2) result = 1;
		else result = 0;
		
		return result;
	}
}

class Circle {
	private int x,y;
	private double radius;
	public Circle (int x, int y, double radius) {
		this.x = x;
		this.y = y;
		this.radius = radius;
	}
	public void display () {
		System.out.println("Coordinates: " + x + ", " + y + "; radius: " + radius);
	}
	public double getRadius() {
		return radius;
	}
	public int getX() {
		return x;
	}
}

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)import java.util.*;

class ComparatorCircle implements Comparator<Circle> {
	
	public int compare (Circle c1, Circle c2) {
		//Returns a negative integer, zero, or a positive integer as the first argument is less than, equal to, or greater than the second.
		double r1 = c1.getRadius();
		double r2 = c2.getRadius();
		
		int result = 0;
		if (r1 < r2) result = -1;
		else if (r1 > r2) result = 1;
		else result = 0;
		
		return result;
	}
}

class Circle {
	private int x,y;
	private double radius;
	public Circle (int x, int y, double radius) {
		this.x = x;
		this.y = y;
		this.radius = radius;
	}
	public void display () {
		System.out.println("Coordinates: " + x + ", " + y + "; radius: " + radius);
	}
	public double getRadius() {
		return radius;
	}
	public int getX() {
		return x;
	}
}CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 5  (Correct; Note de 5,00 sur 5,00)

(énoncé vide)

**Mon code / ma réponse :**

```
class Product implements Comparable<Product> {
    private String name;
    private int price;
    private LocalDate manDate;

    public Product(String n, int p, LocalDate d) {
        this.name = n;
        this.price = p;
        this.manDate = d;
    }

    public String getName() {
        return this.name;
    }

    public int getPrice(){
        return this.price;
    }

    public LocalDate getManDate(){
        return this.manDate;
    }

    @Override
    public String toString(){
        return this.name;
    }

    @Override
    public int compareTo(Product other) {
        return this.name.compareTo(other.name);
    }
}

class PriceComparator implements Comparator<Product> {
    @Override
    public int compare(Product p1, Product p2) {
        return Integer.compare(p1.getPrice(), p2.getPrice());
    }
}

class DateComparator implements Comparator<Product> {
    @Override
    public int compare(Product p1, Product p2) {
        return p1.getManDate().compareTo(p2.getManDate());
    }
}
```

**Mon code / ma réponse :**

```
class Product implements Comparable <Product>{
    private String name;
    private int price;
    private LocalDate manDate;
  
    public Product(String n, int p, LocalDate d) {
        this.name = n;
        this.price = p;
        this.manDate = d;
    }
    
    public String getName() {
        return this.name;
    }
    
    public int getPrice(){
        return this.price;
    }
      
    public LocalDate getManDate(){
        return this.manDate;
    }
    
    @Override
    public String toString(){
        return this.name;
    }
      
    @Override
    public int compareTo (Product p){
        return this.name.compareTo(p.name);
    }
      
}

class PriceComparator implements Comparator<Product>{
    @Override
    public int compare (Product p1, Product p2){
        return Integer.compare(p1.getPrice(),p2.getPrice());
    }
}

class DateComparator implements Comparator<Product>{
    @Override
    public int compare (Product p1, Product p2){
        return p1.getManDate().compareTo(p2.getManDate());
    }
}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)class Product implements Comparable <Product>{
    private String name;
    private int price;
    private LocalDate manDate;
  
    public Product(String n, int p, LocalDate d) {
        this.name = n;
        this.price = p;
        this.manDate = d;
    }
    
    public String getName() {
        return this.name;
    }
    
    public int getPrice(){
        return this.price;
    }
      
    public LocalDate getManDate(){
        return this.manDate;
    }
    
    @Override
    public String toString(){
        return this.name;
    }
      
    @Override
    public int compareTo (Product p){
        return this.name.compareTo(p.name);
    }
      
}

class PriceComparator implements Comparator<Product>{
    @Override
    public int compare (Product p1, Product p2){
        return Integer.compare(p1.getPrice(),p2.getPrice());
    }
}

class DateComparator implements Comparator<Product>{
    @Override
    public int compare (Product p1, Product p2){
        return p1.getManDate().compareTo(p2.getManDate());
    }
}

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

Checker.checkPrivate(s);

Product [] products = new Product[3];
products[0]= new Product ("p1", 14, LocalDate.of(2021, 11, 15));
products[1]= new Product ("p3", 13, LocalDate.of(2021, 11, 16));
products[2]= new Product ("p2", 15, LocalDate.of(2021, 11, 14));
Arrays.sort(products);
System.out.println(Arrays.toString(products));
[p1, p2, p3]
[p1, p2, p3]

Product [] products = new Product[3];
products[0]= new Product ("p1", 14, LocalDate.of(2021, 11, 15));
products[1]= new Product ("p3", 13, LocalDate.of(2021, 11, 16));
products[2]= new Product ("p2", 15, LocalDate.of(2021, 11, 14));
Arrays.sort(products, new PriceComparator());
System.out.println(Arrays.toString(products));
[p3, p1, p2]
[p3, p1, p2]

Product [] products = new Product[3];
products[0]= new Product ("p1", 14, LocalDate.of(2021, 11, 15));
products[1]= new Product ("p3", 13, LocalDate.of(2021, 11, 16));
products[2]= new Product ("p2", 15, LocalDate.of(2021, 11, 14));
Arrays.sort(products, new DateComparator());
System.out.println(Arrays.toString(products));
[p2, p1, p3]
[p2, p1, p3]

Tous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)class Product implements Comparable <Product>{
    private String name;
    private int price;
    private LocalDate manDate;
  
    public Product(String n, int p, LocalDate d) {
        this.name = n;
        this.price = p;
        this.manDate = d;
    }
    
    public String getName() {
        return this.name;
    }
    
    public int getPrice(){
        return this.price;
    }
      
    public LocalDate getManDate(){
        return this.manDate;
    }
    
    @Override
    public String toString(){
        return this.name;
    }
      
    @Override
    public int compareTo (Product p){
        return this.name.compareTo(p.name);
    }
      
}

class PriceComparator implements Comparator<Product>{
    @Override
    public int compare (Product p1, Product p2){
        return Integer.compare(p1.getPrice(),p2.getPrice());
    }
}

class DateComparator implements Comparator<Product>{
    @Override
    public int compare (Product p1, Product p2){
        return p1.getManDate().compareTo(p2.getManDate());
    }
}CorrectNote pour cet envoi : 5,00/5,00.
```

## Question 6  (Correct; Note de 1,00 sur 1,00)

Quelle sortie le programme fournit:

import java.util.*;
public class Essai {
   public static void main (String [] args) {
      LinkedList liste = new LinkedList ();
      liste.add(3); 
      liste.add(5);  
      liste.add(3); 
      liste.add(12); 
      liste.add(3);
      System.out.println(liste);
      liste.remove(3); 
      System.out.println(liste);
      liste.remove(Integer.valueOf(3)); 
      System.out.println(liste);
      Iterator it = liste.iterator();
      while (it.hasNext()) {
         if (it.next()==Integer.valueOf(3)) 
         it.remove();
      }
      System.out.println(liste); 
   }
}

**Propositions :**

```
a. [3, 5, 3, 12, 3]
[3, 5, 3, 3]
[5, 3, 3]
[5] 
b. [3, 5, 3, 12, 3]
[3, 5, 12, 3]
[5, 12, 3]
[5, 12] 
c. [3, 5, 3, 12, 3]
[3, 5, 3, 3]
[5, 3, 3]
[5, 3] 
d. [3, 5, 3, 12, 3]
[5, 3, 12, 3]
[5, 12, 3]
[5, 12]
```

**Ma réponse :** a. [3, 5, 3, 12, 3] [3, 5, 3, 3] [5, 3, 3] [5]  b. [3, 5, 3, 12, 3] [3, 5, 12, 3] [5, 12, 3] [5, 12]  c. [3, 5, 3, 12, 3] [3, 5, 3, 3] [5, 3, 3] [5, 3]  d. [3, 5, 3, 12, 3] [5, 3, 12, 3] [5, 12, 3] [5, 12]

**Correction :** La réponse correcte est : [3, 5, 3, 12, 3]
[3, 5, 3, 3]
[5, 3, 3]
[5]

**Retour Moodle :**

```
FeedbackVotre réponse est correcte.La réponse correcte est : [3, 5, 3, 12, 3]
[3, 5, 3, 3]
[5, 3, 3]
[5]
```

## Question 7  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
import java.util.*;

class DemoIterator {

    private ArrayList<Integer> tab;

    DemoIterator(ArrayList<Integer> tab) {
        this.tab = tab;
    }

    void displayFromFirstToLastElement() {
        Iterator<Integer> it = tab.iterator();
        while (it.hasNext()) {
            System.out.print(it.next() + " ");
        }
    }

    void displayFromLastToFirstElement() {
        ListIterator<Integer> it = tab.listIterator(tab.size());
        while (it.hasPrevious()) {
            System.out.print(it.previous() + " ");
        }
    }

    void displayElementsAtEvenPositions() {
        Iterator<Integer> it = tab.iterator();
        int position = 0;
        while (it.hasNext()) {
            Integer value = it.next();
            if (position % 2 == 0) {
                System.out.print(value + " ");
            }
            position++;
        }
    }

    void setNegativeElementsToZeroUsingSet() {
        for (int i = 0; i < tab.size(); i++) {
            if (tab.get(i) < 0) {
                tab.set(i, 0);
            }
        }
    }

    void setNegativeElementsToZeroUsingIterator() {
        ListIterator<Integer> it = tab.listIterator();
        while (it.hasNext()) {
            if (it.next() < 0) {
                it.set(0);
            }
        }
    }
}
```

**Mon code / ma réponse :**

```
public class DemoIterator {
	
    ArrayList<Integer> tab = new ArrayList<Integer>();
    
    DemoIterator(ArrayList<Integer> tab) {
        //add some values in the ArrayList
		this.tab = tab;
     }
    
    void displayFromFirstToLastElement (){
        ListIterator<Integer> it = tab.listIterator();
		while (it.hasNext())
			System.out.print(it.next() + " ");
    }
    
    void displayFromLastToFirstElement (){
        ListIterator<Integer> lit = tab.listIterator(tab.size());
		while (lit.hasPrevious())
			System.out.print(lit.previous() + " ");
    }
    
    void displayElementsAtEvenPositions (){
        ListIterator<Integer> ite = tab.listIterator();		
        while (ite.hasNext())    { 
            System.out.print(ite.next() + " ") ;
            if (ite.hasNext()) 
                ite.next();    
        } 
    }
    
    void setNegativeElementsToZeroUsingSet() {
        for (int i=0 ; i<tab.size() ; i++) {
			if (tab.get(i) < 0) 
				tab.set (i, 0); 
		}
    }
    
    void setNegativeElementsToZeroUsingIterator() {
        ListIterator <Integer> itz = tab.listIterator() ;
		while (itz.hasNext()) {
			Integer i = itz.next();
			if ( i < 0) 
				itz.set(0) ;
		}
    }
    
}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)public class DemoIterator {
	
    ArrayList<Integer> tab = new ArrayList<Integer>();
    
    DemoIterator(ArrayList<Integer> tab) {
        //add some values in the ArrayList
		this.tab = tab;
     }
    
    void displayFromFirstToLastElement (){
        ListIterator<Integer> it = tab.listIterator();
		while (it.hasNext())
			System.out.print(it.next() + " ");
    }
    
    void displayFromLastToFirstElement (){
        ListIterator<Integer> lit = tab.listIterator(tab.size());
		while (lit.hasPrevious())
			System.out.print(lit.previous() + " ");
    }
    
    void displayElementsAtEvenPositions (){
        ListIterator<Integer> ite = tab.listIterator();		
        while (ite.hasNext())    { 
            System.out.print(ite.next() + " ") ;
            if (ite.hasNext()) 
                ite.next();    
        } 
    }
    
    void setNegativeElementsToZeroUsingSet() {
        for (int i=0 ; i<tab.size() ; i++) {
			if (tab.get(i) < 0) 
				tab.set (i, 0); 
		}
    }
    
    void setNegativeElementsToZeroUsingIterator() {
        ListIterator <Integer> itz = tab.listIterator() ;
		while (itz.hasNext()) {
			Integer i = itz.next();
			if ( i < 0) 
				itz.set(0) ;
		}
    }
    
}

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

ArrayList<Integer> tab = new ArrayList<Integer>();
tab.add(1);
tab.add(3);
tab.add(-6);
tab.add(10);
tab.add(1);
tab.add(100);
tab.add(-500);
DemoIterator di = new DemoIterator(tab);
di.setNegativeElementsToZeroUsingSet();
di.displayFromFirstToLastElement();
1 3 0 10 1 100 0
1 3 0 10 1 100 0

ArrayList<Integer> tab = new ArrayList<Integer>();
tab.add(1);
tab.add(3);
tab.add(-6);
tab.add(10);
tab.add(1);
tab.add(100);
tab.add(-500);
DemoIterator di = new DemoIterator(tab);
di.displayFromLastToFirstElement();
-500 100 1 10 -6 3 1
-500 100 1 10 -6 3 1

ArrayList<Integer> tab = new ArrayList<Integer>();
tab.add(1);
tab.add(3);
tab.add(-6);
tab.add(10);
tab.add(1);
tab.add(100);
tab.add(-500);
DemoIterator di = new DemoIterator(tab);
di.setNegativeElementsToZeroUsingIterator();
di.displayFromFirstToLastElement();
1 3 0 10 1 100 0
1 3 0 10 1 100 0

Tous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)public class DemoIterator {
	
    ArrayList<Integer> tab = new ArrayList<Integer>();
    
    DemoIterator(ArrayList<Integer> tab) {
        //add some values in the ArrayList
		this.tab = tab;
     }
    
    void displayFromFirstToLastElement (){
        ListIterator<Integer> it = tab.listIterator();
		while (it.hasNext())
			System.out.print(it.next() + " ");
    }
    
    void displayFromLastToFirstElement (){
        ListIterator<Integer> lit = tab.listIterator(tab.size());
		while (lit.hasPrevious())
			System.out.print(lit.previous() + " ");
    }
    
    void displayElementsAtEvenPositions (){
        ListIterator<Integer> ite = tab.listIterator();		
        while (ite.hasNext())    { 
            System.out.print(ite.next() + " ") ;
            if (ite.hasNext()) 
                ite.next();    
        } 
    }
    
    void setNegativeElementsToZeroUsingSet() {
        for (int i=0 ; i<tab.size() ; i++) {
			if (tab.get(i) < 0) 
				tab.set (i, 0); 
		}
    }
    
    void setNegativeElementsToZeroUsingIterator() {
        ListIterator <Integer> itz = tab.listIterator() ;
		while (itz.hasNext()) {
			Integer i = itz.next();
			if ( i < 0) 
				itz.set(0) ;
		}
    }
    
}CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 8  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
public class NaturalInteger {
    private int n;

    public NaturalInteger(int n) throws ErrorConst {
        if (n < 0) {
            throw new ErrorConst("Valeur négative : " + n);
        }
        this.n = n;
    }

    public int getN() {
        return n;
    }

    public static void main(String[] args) {
        try {
            NaturalInteger n1 = new NaturalInteger(20);
            System.out.println("n1 = " + n1.getN());
        } catch (ErrorConst e) {
            System.out.println("construction error!");
            System.exit(-1);
        }
    }
}

class ErrorConst extends Exception {
    public ErrorConst(String message) {
        super(message);
    }
}
```

**Mon code / ma réponse :**

```
public class NaturalInteger {
	private int n;
	
	public NaturalInteger (int n) throws ErrorConst {
		if (n<0) throw new ErrorConst();
		this.n = n;
	}
	public int getN() {
		return n;
	}
}

public class ErrorConst extends Exception
{
}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)public class NaturalInteger {
	private int n;
	
	public NaturalInteger (int n) throws ErrorConst {
		if (n<0) throw new ErrorConst();
		this.n = n;
	}
	public int getN() {
		return n;
	}
}

public class ErrorConst extends Exception
{
}

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

try {
   NaturalInteger n2 = new NaturalInteger(-12);
   System.out.println("n2 = " + n2.getN());
}
catch (ErrorConst e) {
   System.out.println("construction error!");
   System.exit(-1);
}
construction error!
construction error!

Tous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)public class NaturalInteger {
	private int n;
	
	public NaturalInteger (int n) throws ErrorConst {
		if (n<0) throw new ErrorConst();
		this.n = n;
	}
	public int getN() {
		return n;
	}
}

public class ErrorConst extends Exception
{
}CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 9  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
public class NaturalInteger {
    private int n;

    public NaturalInteger(int n) throws ErrorConst {
        if (n < 0) {
            throw new ErrorConst(n);
        }
        this.n = n;
    }

    public int getN() {
        return n;
    }

    public static void main(String[] args) {
        try {
            NaturalInteger n1 = new NaturalInteger(102);
            System.out.println("n1 = " + n1.getN());
        } catch (ErrorConst e) {
            System.out.println("try to initialize a natural integer with " + e.getValue());
            System.exit(-1);
        }
    }
}

class ErrorConst extends Exception {
    private int value;

    public ErrorConst(int value) {
        super("Valeur invalide : " + value);
        this.value = value;
    }

    public int getValue() {
        return value;
    }
}
```

**Mon code / ma réponse :**

```
public class NaturalInteger {
	private int n;
	
	public NaturalInteger (int n) throws ErrorConst {
		if (n<0) throw new ErrorConst(n);
		this.n = n;
	}
	public int getN() {
		return n;
	}
}

public class ErrorConst extends Exception
{
	private int value;
	public ErrorConst (int value) {
		this.value = value;
	}
	public int getValue() {
		return value;
	}
}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)public class NaturalInteger {
	private int n;
	
	public NaturalInteger (int n) throws ErrorConst {
		if (n<0) throw new ErrorConst(n);
		this.n = n;
	}
	public int getN() {
		return n;
	}
}

public class ErrorConst extends Exception
{
	private int value;
	public ErrorConst (int value) {
		this.value = value;
	}
	public int getValue() {
		return value;
	}
}

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

try {
\tNaturalInteger n1 = new NaturalInteger(-132);
\tSystem.out.println("n1 = " + n1.getN());
}
catch (ErrorConst e) {
\tSystem.out.println("error: natural integer with negative value " + e.getValue());
\tSystem.exit(-1);
}
error: natural integer with negative value -132
error: natural integer with negative value -132

Tous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)public class NaturalInteger {
	private int n;
	
	public NaturalInteger (int n) throws ErrorConst {
		if (n<0) throw new ErrorConst(n);
		this.n = n;
	}
	public int getN() {
		return n;
	}
}

public class ErrorConst extends Exception
{
	private int value;
	public ErrorConst (int value) {
		this.value = value;
	}
	public int getValue() {
		return value;
	}
}CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 10  (Correct; Note de 4,00 sur 4,00)

(énoncé vide)

**Mon code / ma réponse :**

```
abstract class File {
    private String name;

    public File(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public abstract int getSize();

    public abstract boolean contains(File f);
}

class SimpleFile extends File {
    private int size;

    public SimpleFile(String name, int size) {
        super(name);
        this.size = size;
    }

    @Override
    public int getSize() {
        return size;
    }

    @Override
    public boolean contains(File f) {
        return this == f;
    }
}

class Folder extends File {
    private ArrayList<File> content = new ArrayList<>();

    public Folder(String name) {
        super(name);
    }

    public boolean add(File f) {
        if (this.contains(f) || f.contains(this)) {
            return false;
        }
        return content.add(f);
    }

    @Override
    public int getSize() {
        int total = 0;
        for (File f : content) {
            total += f.getSize();
        }
        return total;
    }

    @Override
    public boolean contains(File f) {
        if (this == f) {
            return true;
        }
        for (File c : content) {
            if (c.contains(f)) {
                return true;
            }
        }
        return false;
    }
}
```

**Mon code / ma réponse :**

```
abstract class File {
  private String name;
  
  
  public File(String n) {
    this.name = n;
  }

  public String getName() {
    return name;
  }

  public abstract int getSize();
  
  public abstract boolean contains (File f);
  
}

class SimpleFile extends File {
  private int size;
  
  public int getSize() {
    return size;
  }

  public SimpleFile(String n, int s) {
    super(n);
    this.size = s;
  }
  public boolean contains (File f) {
    return (this == f);
  }
}
class Folder extends File {
  private ArrayList<File> content;
  
  public Folder(String n) {
    super(n);
    content = new ArrayList<File>();
  }
  public boolean add (File f) {
    if (this.contains(f)) return false;
    if (f.contains(this)) return false;
    return content.add(f);
  }
  
  public boolean contains (File f) {
    boolean b = (this == f);
    for(File e: this.content) {
      b |= e.contains(f);
    }
    return b;
  }
  @Override
  public int getSize() {
    int taille = 0;
    for(File f: content)
      taille += f.getSize();
    return taille;
  }

}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)abstract class File {
  private String name;
  
  
  public File(String n) {
    this.name = n;
  }

  public String getName() {
    return name;
  }

  public abstract int getSize();
  
  public abstract boolean contains (File f);
  
}

class SimpleFile extends File {
  private int size;
  
  public int getSize() {
    return size;
  }

  public SimpleFile(String n, int s) {
    super(n);
    this.size = s;
  }
  public boolean contains (File f) {
    return (this == f);
  }
}
class Folder extends File {
  private ArrayList<File> content;
  
  public Folder(String n) {
    super(n);
    content = new ArrayList<File>();
  }
  public boolean add (File f) {
    if (this.contains(f)) return false;
    if (f.contains(this)) return false;
    return content.add(f);
  }
  
  public boolean contains (File f) {
    boolean b = (this == f);
    for(File e: this.content) {
      b |= e.contains(f);
    }
    return b;
  }
  @Override
  public int getSize() {
    int taille = 0;
    for(File f: content)
      taille += f.getSize();
    return taille;
  }

}

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

Checker.checkHierarchy(s);
Checker.checkPrivate(s);
Checker.checkPublic(s);

Folder root = new Folder("root");
Folder r1 = new Folder("r1");
root.add(r1);
Folder r2 = new Folder("r2");
root.add(new SimpleFile("test.txt", 4));
r1.add(r2);
r2.add(new SimpleFile("test2.txt", 14));
r1.add(new SimpleFile("test1.txt", 11));
System.out.println("root size: " + root.getSize());
root size: 29
root size: 29

Folder root = new Folder("root");
Folder r1 = new Folder("r1");
root.add(r1);
Folder r2 = new Folder("r2");
root.add(new SimpleFile("test.txt", 4));
r1.add(r2);
r2.add(new SimpleFile("test2.txt", 14));
r1.add(new SimpleFile("test1.txt", 11));
System.out.println("root size: " + root.getSize());
System.out.println(root.add(root));
System.out.println("root size: " + root.getSize());
root size: 29
false
root size: 29
root size: 29
false
root size: 29

Folder root = new Folder("root");
Folder r1 = new Folder("r1");
root.add(r1);
Folder r2 = new Folder("r2");
root.add(new SimpleFile("test.txt", 4));
r1.add(r2);
r2.add(new SimpleFile("test2.txt", 14));
r1.add(new SimpleFile("test1.txt", 11));
System.out.println("root size: " + root.getSize());
System.out.println(r1.add(root));
System.out.println("root size : " + root.getSize());
root size: 29
false
root size : 29
root size: 29
false
root size : 29

Folder root = new Folder("root");
Folder r1 = new Folder("r1");
root.add(r1);
Folder r2 = new Folder("r2");
root.add(new SimpleFile("test.txt", 4));
r1.add(r2);
r2.add(new SimpleFile("test2.txt", 14));
File t1 = new SimpleFile("test1.txt", 11);
r1.add(t1);

System.out.println("r2.add(root): " + r2.add(root));
r2.add(root): false
r2.add(root): false

Folder root = new Folder("root");
Folder r1 = new Folder("r1");
root.add(r1);
Folder r2 = new Folder("r2");
root.add(new SimpleFile("test.txt", 4));
r1.add(r2);
r2.add(new SimpleFile("test2.txt", 14));
File t1 = new SimpleFile("test1.txt", 11);
r1.add(t1);
System.out.println("root.add(r2): " + root.add(r2));
root.add(r2): false
root.add(r2): false

Folder root = new Folder("root");
Folder r1 = new Folder("r1");
root.add(r1);
Folder r2 = new Folder("r2");
root.add(new SimpleFile("test.txt", 24));
r1.add(r2);
r2.add(new SimpleFile("test2.txt", 14));
r1.add(new SimpleFile("test1.txt", 11));
System.out.println("root size: " + root.getSize());

Folder r3 = new Folder("r3");
r3.add(new SimpleFile("test3.txt", 104));
r2.add(r3);
System.out.println("root size: " + root.getSize());
root size: 49
root size: 153
root size: 49
root size: 153

Tous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)abstract class File {
  private String name;
  
  
  public File(String n) {
    this.name = n;
  }

  public String getName() {
    return name;
  }

  public abstract int getSize();
  
  public abstract boolean contains (File f);
  
}

class SimpleFile extends File {
  private int size;
  
  public int getSize() {
    return size;
  }

  public SimpleFile(String n, int s) {
    super(n);
    this.size = s;
  }
  public boolean contains (File f) {
    return (this == f);
  }
}
class Folder extends File {
  private ArrayList<File> content;
  
  public Folder(String n) {
    super(n);
    content = new ArrayList<File>();
  }
  public boolean add (File f) {
    if (this.contains(f)) return false;
    if (f.contains(this)) return false;
    return content.add(f);
  }
  
  public boolean contains (File f) {
    boolean b = (this == f);
    for(File e: this.content) {
      b |= e.contains(f);
    }
    return b;
  }
  @Override
  public int getSize() {
    int taille = 0;
    for(File f: content)
      taille += f.getSize();
    return taille;
  }

}
CorrectNote pour cet envoi : 4,00/4,00.
```

## Question 11  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
import java.util.*;

public class Index {
    private TreeMap<String, TreeSet<Integer>> index;

    public Index() {
        index = new TreeMap<String, TreeSet<Integer>>();
    }

    public void add(String entry, int number) {
        if (!index.containsKey(entry)) {
            index.put(entry, new TreeSet<Integer>());
        }
        index.get(entry).add(number);
    }

    public void list() {
        Set<Map.Entry<String, TreeSet<Integer>>> elementsIndex = index.entrySet();
        for (Map.Entry<String, TreeSet<Integer>> currentElement : elementsIndex) {
            System.out.println(currentElement.getKey() + ":" + currentElement.getValue());
        }
    }
}
```

**Mon code / ma réponse :**

```
public class Index {
	//attribute of type TreeMap <String, TreeSet <Integer>>
	private Map <String, TreeSet <Integer>> map;

	//constructor
	public Index () {
		//index initialisation
		map = new TreeMap <String, TreeSet <Integer>>();
	}

	public void add (String entry, int number) {
		//if the entry does not exist in the index, we add it, we associate it with the number
		//else, we add the page number to the set of numbers that are already associated to the entry
		TreeSet<Integer> set = map.get(entry);
		if (set == null){
		    set = new TreeSet<Integer>();
		}
		set.add(number);
		map.put(entry, set);
		
	}
	public void list() {
		map.forEach((k, v) -> System.out.println((k + ":" + v)));
	}
}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)public class Index {
	//attribute of type TreeMap <String, TreeSet <Integer>>
	private Map <String, TreeSet <Integer>> map;

	//constructor
	public Index () {
		//index initialisation
		map = new TreeMap <String, TreeSet <Integer>>();
	}

	public void add (String entry, int number) {
		//if the entry does not exist in the index, we add it, we associate it with the number
		//else, we add the page number to the set of numbers that are already associated to the entry
		TreeSet<Integer> set = map.get(entry);
		if (set == null){
		    set = new TreeSet<Integer>();
		}
		set.add(number);
		map.put(entry, set);
		
	}
	public void list() {
		map.forEach((k, v) -> System.out.println((k + ":" + v)));
	}
}

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)public class Index {
	//attribute of type TreeMap <String, TreeSet <Integer>>
	private Map <String, TreeSet <Integer>> map;

	//constructor
	public Index () {
		//index initialisation
		map = new TreeMap <String, TreeSet <Integer>>();
	}

	public void add (String entry, int number) {
		//if the entry does not exist in the index, we add it, we associate it with the number
		//else, we add the page number to the set of numbers that are already associated to the entry
		TreeSet<Integer> set = map.get(entry);
		if (set == null){
		    set = new TreeSet<Integer>();
		}
		set.add(number);
		map.put(entry, set);
		
	}
	public void list() {
		map.forEach((k, v) -> System.out.println((k + ":" + v)));
	}
}CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 12  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
public class Index {
    private TreeMap<String, TreeSet<Integer>> index;

    public Index() {
        index = new TreeMap<String, TreeSet<Integer>>();
    }

    public void add(String entry, int number) {
        if (!index.containsKey(entry)) {
            index.put(entry, new TreeSet<Integer>());
        }
        index.get(entry).add(number);
    }

    public void list() {
        index.forEach((entry, pages) ->
            System.out.println(entry + ":" + pages));
    }

    public void listInvertedIndex() {
        TreeMap<Integer, TreeSet<String>> inverted = new TreeMap<Integer, TreeSet<String>>();

        index.forEach((entry, pages) ->
            pages.forEach(page ->
                inverted.computeIfAbsent(page, k -> new TreeSet<String>()).add(entry)));

        inverted.forEach((page, entries) ->
            System.out.println(page + ":" + entries));
    }
}
```

**Mon code / ma réponse :**

```
public class Index {
	private Map <String, TreeSet <Integer>> map;
	private Map <Integer, TreeSet <String>> imap;

	public Index () {
		map = new TreeMap <String, TreeSet <Integer>>();
		imap = new TreeMap <Integer, TreeSet <String>>();

	}

	public void add (String entry, int number) {
		TreeSet<Integer> set = map.get(entry);
		if (set == null){
		    set = new TreeSet<Integer>();
		}
		set.add(number);
		map.put(entry, set);
		
		TreeSet<String> iset = imap.get(number);
		if (iset == null){
		    iset = new TreeSet<String>();
		}
		iset.add(entry);
		imap.put(number, iset);
	}
	public void list() {
		map.forEach((k, v) -> System.out.println((k + ":" + v)));
	}

    public void listInvertedIndex() {
		imap.forEach((k, v) -> System.out.println((k + ":" + v)));
	}
}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)public class Index {
	private Map <String, TreeSet <Integer>> map;
	private Map <Integer, TreeSet <String>> imap;

	public Index () {
		map = new TreeMap <String, TreeSet <Integer>>();
		imap = new TreeMap <Integer, TreeSet <String>>();

	}

	public void add (String entry, int number) {
		TreeSet<Integer> set = map.get(entry);
		if (set == null){
		    set = new TreeSet<Integer>();
		}
		set.add(number);
		map.put(entry, set);
		
		TreeSet<String> iset = imap.get(number);
		if (iset == null){
		    iset = new TreeSet<String>();
		}
		iset.add(entry);
		imap.put(number, iset);
	}
	public void list() {
		map.forEach((k, v) -> System.out.println((k + ":" + v)));
	}

    public void listInvertedIndex() {
		imap.forEach((k, v) -> System.out.println((k + ":" + v)));
	}
}

**Retour Moodle :**

```
FeedbackTous les tests ont été réussis ! ▸ Montrer / masquer la solution de l’auteur de la question  (Java)public class Index {
	private Map <String, TreeSet <Integer>> map;
	private Map <Integer, TreeSet <String>> imap;

	public Index () {
		map = new TreeMap <String, TreeSet <Integer>>();
		imap = new TreeMap <Integer, TreeSet <String>>();

	}

	public void add (String entry, int number) {
		TreeSet<Integer> set = map.get(entry);
		if (set == null){
		    set = new TreeSet<Integer>();
		}
		set.add(number);
		map.put(entry, set);
		
		TreeSet<String> iset = imap.get(number);
		if (iset == null){
		    iset = new TreeSet<String>();
		}
		iset.add(entry);
		imap.put(number, iset);
	}
	public void list() {
		map.forEach((k, v) -> System.out.println((k + ":" + v)));
	}

    public void listInvertedIndex() {
		imap.forEach((k, v) -> System.out.println((k + ":" + v)));
	}
}CorrectNote pour cet envoi : 1,00/1,00.
```
