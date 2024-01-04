abstract class Handler {
    protected Handler successor = null;

    public Handler(Handler successor) {
        this.successor = successor;
    }

    public abstract void handleRequest();
}

class ConcreteHandler1 extends Handler {
    public ConcreteHandler1(Handler successor) {
        super(successor);
    }

    @Override
    public void handleRequest() {
        if (true) {  // Can handle request.
            System.out.println("Finally handled by ConcreteHandler1");
        } else if (successor != null) {
            System.out.println("Message passed to next in chain by ConcreteHandler1");
            successor.handleRequest();
        }
    }
}

class ConcreteHandler2 extends Handler {
    public ConcreteHandler2(Handler successor) {
        super(successor);
    }

    @Override
    public void handleRequest() {
        if (false) {  // Can't handle request.
            System.out.println("Finally handled by ConcreteHandler2");
        } else if (successor != null) {
            System.out.println("Message passed to next in chain by ConcreteHandler2");
            successor.handleRequest();
        }
    }
}

public class ChainOfResponsibility {
    public static void main(String[] args) {
        ConcreteHandler1 ch1 = new ConcreteHandler1(null);
        ConcreteHandler2 ch2 = new ConcreteHandler2(ch1);
        ch2.handleRequest();
    }
}
