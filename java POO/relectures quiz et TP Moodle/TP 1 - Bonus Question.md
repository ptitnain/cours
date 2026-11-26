# TP 1 - Bonus Question

*Java, section « Travail Pratique 1 - Formes ». Relecture de ma tentative sur Moodle ([lien](https://learning.esiea.fr/mod/quiz/review.php?attempt=27181&cmid=7033)).*

## Résumé

- **Statut** : Terminée
- **Commencé** : mardi 3 novembre 2026, 11:37
- **Terminé** : mardi 3 novembre 2026, 12:00
- **Durée** : 22 min 43 s

## Question 1  (Non répondue; Noté sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
//only define : Polygon
//the others already exist!
```

**Mon code / ma réponse :**

```
//only define : Polygon
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
    protected final int hashi() {
        int hash = 7;
        long l = 0;
        for (int i = 0; i < this.vertices.size(); i++) {
            l += this.getDistances().hashCode();
            this.rotateCycle();

        }
        long a = 0;
        for (int i = 0; i < this.vertices.size(); i++) {
            l += this.getAngles().hashCode();
            this.rotateCycle();

        }

        Long n = Double.doubleToLongBits(this.vertices.size() - 1);
        Long L = Double.doubleToLongBits(l);
        Long A = Double.doubleToLongBits(a);

        hash = 97 * hash + (int) (n ^ (n >>> 32));
        hash = 97 * hash + (int) (L ^ (L >>> 32));
        hash = 97 * hash + (int) (A ^ (A >>> 32));
        return hash;
    }

    protected final int hashiBasedOnSet() {
        int hash = 7;

        Set<Double> setDist = new TreeSet<Double>(this.getDistances());
        Set<Double> setAng = new TreeSet<Double>(this.getAngles());

        Long n = Double.doubleToLongBits(this.vertices.size() - 1);
        Long l = Double.doubleToLongBits(setDist.hashCode());
        Long a = Double.doubleToLongBits(setAng.hashCode());

        hash = 97 * hash + (int) (n ^ (n >>> 32));
        hash = 97 * hash + (int) (l ^ (l >>> 32));
        hash = 97 * hash + (int) (a ^ (a >>> 32));
        return hash;
    }


    @Override
    public double area() {
        int n = vertices.size(); // size>2 ensured by the constructor
        double a = 0;
        for (int i = 0; i < n; i++) {
            a += vertices.get(i).getY() * vertices.get((i + 1)%n).getX()
                    - vertices.get((i)%n).getX() * vertices.get((i + 1)%n).getY();
        }
        a = Math.abs(a) / 2;
        return a;
    }

    @Override
    public double perimeter() {
        int size = vertices.size(); 
        double p = 0;
        for (int i = 0; i < size; i++) // CORRECTION : i < size (au lieu de size - 1) pour inclure le dernier segment
            p += Points.distance(vertices.get(i), vertices.get((i + 1)%size));
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

    @Override
    public boolean congruent(Shape s) {
        for (int i = 0; i < this.vertices.size(); i++) {
            if (this.congruentHelper(s)) {
                return true;
            }
            this.rotateCycle();//rotate and check
        }
        return false;
    }

    //object methods
    @Override
    public String toString() {
        return this.getClass().getSimpleName() + "{" + vertices + '}';
    }



    private void rotateCycle() {
        this.vertices.add(this.vertices.remove(0));
    }

    private boolean congruentHelper(Shape s) {
        if (!(s instanceof Polygon)) {
            return false;
        }
        final Polygon other = (Polygon) s;
        boolean sameNbSides, sameLens, sameAngles;

        sameNbSides = (this.nbSides() == other.nbSides());
        sameLens = this.isSameLens(other);
        sameAngles = this.isSameAngles(other);

        return (sameNbSides && sameLens && sameAngles);
    }

    private boolean isSameLens(Polygon other) {
        return this.getDistances().equals(other.getDistances());
    }

    private boolean isSameAngles(Polygon other) {
        return this.getAngles().equals(other.getAngles());
    }

     private int nbSides() {
        return vertices.size(); // CORRECTION : vertices.size() (au lieu de size - 1)
    }

    protected List<Double> getAngles() {
        int size = vertices.size();
        List<Double> angles = new ArrayList<Double>();
        double a1 ;
        for (int i = 0; i < size; i++) {
            a1 = Points.angle(this.vertices.get(i),
                    this.vertices.get((i + 1)%size),
                    this.vertices.get((i + 2)%size));
            angles.add(a1);

        }
        return angles;
    }

    protected List<Double> getDistances() {
        int size = vertices.size();
        List<Double> distances = new ArrayList<Double>();
        double d1;
        for (int i = 0; i < size; i++) {
            d1 = Points.distance(this.vertices.get(i),
                    this.vertices.get((i + 1)%size));
            distances.add(d1);
        }
        return distances;
    }

    private Point getCenter() {
        int size = vertices.size();
        Point G = new Point();
        double xg = 0, yg = 0, p;
        for (int i = 0; i < size - 1; i++) {
            p = vertices.get(i).getX() * vertices.get(i + 1).getY()
                    - vertices.get(i + 1).getX() * vertices.get(i).getY();
            xg += (vertices.get(i).getX() + vertices.get(i + 1).getX()) * p;
            yg += (vertices.get(i).getY() + vertices.get(i + 1).getY()) * p;
        }

        xg = xg / (6 * area());
        yg = yg / (6 * area());
        G.setX(xg);
        G.setY(yg);
        return G;
    }

    //test functions (statoc)
    private static void equalsTest() throws CloneNotSupportedException {
        Point O = new Point(0, 0);
        Point A = new Point(1, 0);
        Point B = new Point(1, 1);
        Point C = new Point(0, 1);

        Polygon p = new Quadrilateral(O, A, B, C);
        Polygon q = new Quadrilateral(O, A, B, C);

        q.move(2, -2);
        q.rotateCycle();

        System.out.println(p);
        System.out.println(q);
        System.out.println(p.equals(q));

    }


    private static void areaTest() {
        Point O = new Point(0, 0);
        Point A = new Point(1, 0);
        Point B = new Point(1, 1);
        Point C = new Point(0, 1);
        Point t[] = {O, A, B, C};
        Polygon p = new Polygon(t);
        p.move(1, 1);
        System.out.println(p.area());


        Point A1 = new Point(1, 1);
        Point B1 = new Point(2, 1);
        Point C1 = new Point(3, 0);
        Point D1 = new Point(3, 2);
        Point E1 = new Point(0, 2);
        Polygon p1 = new Polygon(O,A1,B1,C1,D1, E1);
        p1.move(1, 1);
        System.out.println(p1.area());
    }


    private static void hashCodeTest() throws CloneNotSupportedException {
        Point O = new Point(0, 0);
        Point A = new Point(1, 0);
        Point B = new Point(1, 1);
        Point C = new Point(0, 1);

        Polygon p = new Polygon(O, A, B, C);
        //Polygon q = p.clone();
        Point O1 = new Point(2, -2);
        Point A1 = new Point(3, -2);
        Point B1 = new Point(3, -1);
        Point C1 = new Point(2, -1);
        Polygon q = new Polygon(B1, C1, O1, A1);
        q.move(2, -2);
        q.rotateCycle();
        System.out.println("p.equals(q)" + p.equals(q));
        System.out.println(p.hashCode() + " =? " + q.hashCode());
    }

    public static void PolygonTest() {

        Point O = new Point(0, 0);
        Point A = new Point(0, 1);
        Point B = new Point(3, 2);
        Point C = new Point(-1, 3);
        Point D = new Point(-1, 1);
        Point E = new Point(1, 0);

        System.out.println(Points.intersect(O, A, D, E));

        System.out.println(new Polygon(O, A, B, C, D, E));
    }

    //main:
    public static void main(String... args) throws CloneNotSupportedException {
        hashCodeTest();
    }

}
```

**Correction :** ▸ Montrer / masquer la solution de l’auteur de la question  (Java)//only define : Polygon
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
    protected final int hashi() {
        int hash = 7;
        long l = 0;
        for (int i = 0; i < this.vertices.size(); i++) {
            l += this.getDistances().hashCode();
            this.rotateCycle();

        }
        long a = 0;
        for (int i = 0; i < this.vertices.size(); i++) {
            l += this.getAngles().hashCode();
            this.rotateCycle();

        }

        Long n = Double.doubleToLongBits(this.vertices.size() - 1);
        Long L = Double.doubleToLongBits(l);
        Long A = Double.doubleToLongBits(a);

        hash = 97 * hash + (int) (n ^ (n >>> 32));
        hash = 97 * hash + (int) (L ^ (L >>> 32));
        hash = 97 * hash + (int) (A ^ (A >>> 32));
        return hash;
    }

    protected final int hashiBasedOnSet() {
        int hash = 7;

        Set<Double> setDist = new TreeSet<Double>(this.getDistances());
        Set<Double> setAng = new TreeSet<Double>(this.getAngles());

        Long n = Double.doubleToLongBits(this.vertices.size() - 1);
        Long l = Double.doubleToLongBits(setDist.hashCode());
        Long a = Double.doubleToLongBits(setAng.hashCode());

        hash = 97 * hash + (int) (n ^ (n >>> 32));
        hash = 97 * hash + (int) (l ^ (l >>> 32));
        hash = 97 * hash + (int) (a ^ (a >>> 32));
        return hash;
    }

    @Override
    public double area() {
        int n = vertices.size(); // size>2 ensured by the constructor
        double a = 0;
        for (int i = 0; i < n; i++) {
            a += vertices.get(i).getY() * vertices.get((i + 1)%n).getX()
                    - vertices.get((i)%n).getX() * vertices.get((i + 1)%n).getY();
        }
        a = Math.abs(a) / 2;
        return a;
    }

    @Override
    public double perimeter() {
        int size = vertices.size(); 
        double p = 0;
        for (int i = 0; i < size; i++) // CORRECTION : i < size (au lieu de size - 1) pour inclure le dernier segment
            p += Points.distance(vertices.get(i), vertices.get((i + 1)%size));
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

    @Override
    public boolean congruent(Shape s) {
        for (int i = 0; i < this.vertices.size(); i++) {
            if (this.congruentHelper(s)) {
                return true;
            }
            this.rotateCycle();//rotate and check
        }
        return false;
    }

    //object methods
    @Override
    public String toString() {
        return this.getClass().getSimpleName() + "{" + vertices + '}';
    }

    private void rotateCycle() {
        this.vertices.add(this.vertices.remove(0));
    }

    private boolean congruentHelper(Shape s) {
        if (!(s instanceof Polygon)) {
            return false;
        }
        final Polygon other = (Polygon) s;
        boolean sameNbSides, sameLens, sameAngles;

        sameNbSides = (this.nbSides() == other.nbSides());
        sameLens = this.isSameLens(other);
        sameAngles = this.isSameAngles(other);

        return (sameNbSides && sameLens && sameAngles);
    }

    private boolean isSameLens(Polygon other) {
        return this.getDistances().equals(other.getDistances());
    }

    private boolean isSameAngles(Polygon other) {
        return this.getAngles().equals(other.getAngles());
    }

     private int nbSides() {
        return vertices.size(); // CORRECTION : vertices.size() (au lieu de size - 1)
    }

    protected List<Double> getAngles() {
        int size = vertices.size();
        List<Double> angles = new ArrayList<Double>();
        double a1 ;
        for (int i = 0; i < size; i++) {
            a1 = Points.angle(this.vertices.get(i),
                    this.vertices.get((i + 1)%size),
                    this.vertices.get((i + 2)%size));
            angles.add(a1);

        }
        return angles;
    }

    protected List<Double> getDistances() {
        int size = vertices.size();
        List<Double> distances = new ArrayList<Double>();
        double d1;
        for (int i = 0; i < size; i++) {
            d1 = Points.distance(this.vertices.get(i),
                    this.vertices.get((i + 1)%size));
            distances.add(d1);
        }
        return distances;
    }

    private Point getCenter() {
        int size = vertices.size();
        Point G = new Point();
        double xg = 0, yg = 0, p;
        for (int i = 0; i < size - 1; i++) {
            p = vertices.get(i).getX() * vertices.get(i + 1).getY()
                    - vertices.get(i + 1).getX() * vertices.get(i).getY();
            xg += (vertices.get(i).getX() + vertices.get(i + 1).getX()) * p;
            yg += (vertices.get(i).getY() + vertices.get(i + 1).getY()) * p;
        }

        xg = xg / (6 * area());
        yg = yg / (6 * area());
        G.setX(xg);
        G.setY(yg);
        return G;
    }

    //test functions (statoc)
    private static void equalsTest() throws CloneNotSupportedException {
        Point O = new Point(0, 0);
        Point A = new Point(1, 0);
        Point B = new Point(1, 1);
        Point C = new Point(0, 1);

        Polygon p = new Quadrilateral(O, A, B, C);
        Polygon q = new Quadrilateral(O, A, B, C);

        q.move(2, -2);
        q.rotateCycle();

        System.out.println(p);
        System.out.println(q);
        System.out.println(p.equals(q));

    }

    private static void areaTest() {
        Point O = new Point(0, 0);
        Point A = new Point(1, 0);
        Point B = new Point(1, 1);
        Point C = new Point(0, 1);
        Point t[] = {O, A, B, C};
        Polygon p = new Polygon(t);
        p.move(1, 1);
        System.out.println(p.area());

        Point A1 = new Point(1, 1);
        Point B1 = new Point(2, 1);
        Point C1 = new Point(3, 0);
        Point D1 = new Point(3, 2);
        Point E1 = new Point(0, 2);
        Polygon p1 = new Polygon(O,A1,B1,C1,D1, E1);
        p1.move(1, 1);
        System.out.println(p1.area());
    }

    private static void hashCodeTest() throws CloneNotSupportedException {
        Point O = new Point(0, 0);
        Point A = new Point(1, 0);
        Point B = new Point(1, 1);
        Point C = new Point(0, 1);

        Polygon p = new Polygon(O, A, B, C);
        //Polygon q = p.clone();
        Point O1 = new Point(2, -2);
        Point A1 = new Point(3, -2);
        Point B1 = new Point(3, -1);
        Point C1 = new Point(2, -1);
        Polygon q = new Polygon(B1, C1, O1, A1);
        q.move(2, -2);
        q.rotateCycle();
        System.out.println("p.equals(q)" + p.equals(q));
        System.out.println(p.hashCode() + " =? " + q.hashCode());
    }

    public static void PolygonTest() {

        Point O = new Point(0, 0);
        Point A = new Point(0, 1);
        Point B = new Point(3, 2);
        Point C = new Point(-1, 3);
        Point D = new Point(-1, 1);
        Point E = new Point(1, 0);

        System.out.println(Points.intersect(O, A, D, E));

        System.out.println(new Polygon(O, A, B, C, D, E));
    }

    //main:
    public static void main(String... args) throws CloneNotSupportedException {
        hashCodeTest();
    }

}

**Retour Moodle :**

```
Feedback▸ Montrer / masquer la solution de l’auteur de la question  (Java)//only define : Polygon
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
    protected final int hashi() {
        int hash = 7;
        long l = 0;
        for (int i = 0; i < this.vertices.size(); i++) {
            l += this.getDistances().hashCode();
            this.rotateCycle();

        }
        long a = 0;
        for (int i = 0; i < this.vertices.size(); i++) {
            l += this.getAngles().hashCode();
            this.rotateCycle();

        }

        Long n = Double.doubleToLongBits(this.vertices.size() - 1);
        Long L = Double.doubleToLongBits(l);
        Long A = Double.doubleToLongBits(a);

        hash = 97 * hash + (int) (n ^ (n >>> 32));
        hash = 97 * hash + (int) (L ^ (L >>> 32));
        hash = 97 * hash + (int) (A ^ (A >>> 32));
        return hash;
    }

    protected final int hashiBasedOnSet() {
        int hash = 7;

        Set<Double> setDist = new TreeSet<Double>(this.getDistances());
        Set<Double> setAng = new TreeSet<Double>(this.getAngles());

        Long n = Double.doubleToLongBits(this.vertices.size() - 1);
        Long l = Double.doubleToLongBits(setDist.hashCode());
        Long a = Double.doubleToLongBits(setAng.hashCode());

        hash = 97 * hash + (int) (n ^ (n >>> 32));
        hash = 97 * hash + (int) (l ^ (l >>> 32));
        hash = 97 * hash + (int) (a ^ (a >>> 32));
        return hash;
    }

    @Override
    public double area() {
        int n = vertices.size(); // size>2 ensured by the constructor
        double a = 0;
        for (int i = 0; i < n; i++) {
            a += vertices.get(i).getY() * vertices.get((i + 1)%n).getX()
                    - vertices.get((i)%n).getX() * vertices.get((i + 1)%n).getY();
        }
        a = Math.abs(a) / 2;
        return a;
    }

    @Override
    public double perimeter() {
        int size = vertices.size(); 
        double p = 0;
        for (int i = 0; i < size; i++) // CORRECTION : i < size (au lieu de size - 1) pour inclure le dernier segment
            p += Points.distance(vertices.get(i), vertices.get((i + 1)%size));
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

    @Override
    public boolean congruent(Shape s) {
        for (int i = 0; i < this.vertices.size(); i++) {
            if (this.congruentHelper(s)) {
                return true;
            }
            this.rotateCycle();//rotate and check
        }
        return false;
    }

    //object methods
    @Override
    public String toString() {
        return this.getClass().getSimpleName() + "{" + vertices + '}';
    }

    private void rotateCycle() {
        this.vertices.add(this.vertices.remove(0));
    }

    private boolean congruentHelper(Shape s) {
        if (!(s instanceof Polygon)) {
            return false;
        }
        final Polygon other = (Polygon) s;
        boolean sameNbSides, sameLens, sameAngles;

        sameNbSides = (this.nbSides() == other.nbSides());
        sameLens = this.isSameLens(other);
        sameAngles = this.isSameAngles(other);

        return (sameNbSides && sameLens && sameAngles);
    }

    private boolean isSameLens(Polygon other) {
        return this.getDistances().equals(other.getDistances());
    }

    private boolean isSameAngles(Polygon other) {
        return this.getAngles().equals(other.getAngles());
    }

     private int nbSides() {
        return vertices.size(); // CORRECTION : vertices.size() (au lieu de size - 1)
    }

    protected List<Double> getAngles() {
        int size = vertices.size();
        List<Double> angles = new ArrayList<Double>();
        double a1 ;
        for (int i = 0; i < size; i++) {
            a1 = Points.angle(this.vertices.get(i),
                    this.vertices.get((i + 1)%size),
                    this.vertices.get((i + 2)%size));
            angles.add(a1);

        }
        return angles;
    }

    protected List<Double> getDistances() {
        int size = vertices.size();
        List<Double> distances = new ArrayList<Double>();
        double d1;
        for (int i = 0; i < size; i++) {
            d1 = Points.distance(this.vertices.get(i),
                    this.vertices.get((i + 1)%size));
            distances.add(d1);
        }
        return distances;
    }

    private Point getCenter() {
        int size = vertices.size();
        Point G = new Point();
        double xg = 0, yg = 0, p;
        for (int i = 0; i < size - 1; i++) {
            p = vertices.get(i).getX() * vertices.get(i + 1).getY()
                    - vertices.get(i + 1).getX() * vertices.get(i).getY();
            xg += (vertices.get(i).getX() + vertices.get(i + 1).getX()) * p;
            yg += (vertices.get(i).getY() + vertices.get(i + 1).getY()) * p;
        }

        xg = xg / (6 * area());
        yg = yg / (6 * area());
        G.setX(xg);
        G.setY(yg);
        return G;
    }

    //test functions (statoc)
    private static void equalsTest() throws CloneNotSupportedException {
        Point O = new Point(0, 0);
        Point A = new Point(1, 0);
        Point B = new Point(1, 1);
        Point C = new Point(0, 1);

        Polygon p = new Quadrilateral(O, A, B, C);
        Polygon q = new Quadrilateral(O, A, B, C);

        q.move(2, -2);
        q.rotateCycle();

        System.out.println(p);
        System.out.println(q);
        System.out.println(p.equals(q));

    }

    private static void areaTest() {
        Point O = new Point(0, 0);
        Point A = new Point(1, 0);
        Point B = new Point(1, 1);
        Point C = new Point(0, 1);
        Point t[] = {O, A, B, C};
        Polygon p = new Polygon(t);
        p.move(1, 1);
        System.out.println(p.area());

        Point A1 = new Point(1, 1);
        Point B1 = new Point(2, 1);
        Point C1 = new Point(3, 0);
        Point D1 = new Point(3, 2);
        Point E1 = new Point(0, 2);
        Polygon p1 = new Polygon(O,A1,B1,C1,D1, E1);
        p1.move(1, 1);
        System.out.println(p1.area());
    }

    private static void hashCodeTest() throws CloneNotSupportedException {
        Point O = new Point(0, 0);
        Point A = new Point(1, 0);
        Point B = new Point(1, 1);
        Point C = new Point(0, 1);

        Polygon p = new Polygon(O, A, B, C);
        //Polygon q = p.clone();
        Point O1 = new Point(2, -2);
        Point A1 = new Point(3, -2);
        Point B1 = new Point(3, -1);
        Point C1 = new Point(2, -1);
        Polygon q = new Polygon(B1, C1, O1, A1);
        q.move(2, -2);
        q.rotateCycle();
        System.out.println("p.equals(q)" + p.equals(q));
        System.out.println(p.hashCode() + " =? " + q.hashCode());
    }

    public static void PolygonTest() {

        Point O = new Point(0, 0);
        Point A = new Point(0, 1);
        Point B = new Point(3, 2);
        Point C = new Point(-1, 3);
        Point D = new Point(-1, 1);
        Point E = new Point(1, 0);

        System.out.println(Points.intersect(O, A, D, E));

        System.out.println(new Polygon(O, A, B, C, D, E));
    }

    //main:
    public static void main(String... args) throws CloneNotSupportedException {
        hashCodeTest();
    }

}
```
