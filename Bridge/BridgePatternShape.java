// Abstraction interface
interface Shape {
    void draw();
}

// Implementor interface
interface Color {
    String fill();
}

// Rectangle class
class Rectangle implements Shape {
    private Color imp;

    public Rectangle(Color imp) {
        this.imp = imp;
    }

    @Override
    public void draw() {
        System.out.println("Drawing Rectangle with color " + imp.fill());
    }
}

// Circle class
class Circle implements Shape {
    private Color imp;

    public Circle(Color imp) {
        this.imp = imp;
    }

    @Override
    public void draw() {
        System.out.println("Drawing Circle with color " + imp.fill());
    }
}

// Red class
class Red implements Color {
    @Override
    public String fill() {
        return "Red";
    }
}

// Green class
class Green implements Color {
    @Override
    public String fill() {
        return "Green";
    }
}

// Blue class
class Blue implements Color {
    @Override
    public String fill() {
        return "Blue";
    }
}

// Client code
public class BridgePatternShape {
    public static void main(String[] args) {
        Color c1 = new Red();
        Shape abstraction = new Circle(c1);
        abstraction.draw();

        Color c2 = new Green();
        Shape abstraction2 = new Rectangle(c2);
        abstraction2.draw();
    }
}
