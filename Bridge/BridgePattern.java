// Abstraction interface
interface Abstraction {
    void operation();
}

// Implementor interface
interface Implementor {
    void operation();
}

// ConcreteImplementor1 class
class ConcreteImplementor1 implements Implementor {
    @Override
    public void operation() {
        System.out.println("ConcreteImplementor1 operation");
    }
}

// ConcreteImplementor2 class
class ConcreteImplementor2 implements Implementor {
    @Override
    public void operation() {
        System.out.println("ConcreteImplementor2 operation");
    }
}

// ConcreteAbstraction class
class ConcreteAbstraction implements Abstraction {
    private Implementor imp;

    public ConcreteAbstraction(Implementor imp) {
        this.imp = imp;
    }

    @Override
    public void operation() {
        imp.operation();
    }
}

// Client code
public class BridgePattern {
    public static void main(String[] args) {
        Implementor c1 = new ConcreteImplementor1();
        Abstraction abstraction = new ConcreteAbstraction(c1);
        abstraction.operation();
    }
}
