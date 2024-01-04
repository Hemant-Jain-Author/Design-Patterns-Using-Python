// Define the Product class with two parts
class Product {
    private String partA;
    private String partB;

    public Product(String A, String B) {
        this.partA = A;
        this.partB = B;
    }

    @Override
    public String toString() {
        return String.format("Product : (%s, %s)", partA, partB);
    }
}

// Define an abstract class called Builder
abstract class Builder {
    protected Product product;

    public Builder() {
        this.product = new Product("A default", "B default");
    }

    public abstract Builder setPartA(String A);

    public abstract Builder setPartB(String B);

    public Product getProduct() {
        Product temp = this.product;
        this.product = new Product("A default", "B default"); // assign new product.
        return temp;
    }
}

// Define a ConcreteBuilder class that extends Builder
class ConcreteBuilder extends Builder {
    @Override
    public Builder setPartA(String A) {
        this.product = new Product(A, this.product.toString().split(",")[1].trim());
        return this;
    }

    @Override
    public Builder setPartB(String B) {
        this.product = new Product(this.product.toString().split(",")[0].split(":")[1].trim(), B);
        return this;
    }
}

// Define a Director class that takes a builder object as a parameter
class Director {
    private Builder builder;

    public Director(Builder builder) {
        this.builder = builder;
    }

    public Product construct() {
        return this.builder.setPartA("A1").setPartB("B1").getProduct();
    }

    public Product construct2() {
        this.builder.setPartA("A2");
        this.builder.setPartB("B2");
        return this.builder.getProduct();
    }

    public Product construct3() {
        return this.builder.setPartA("A3").getProduct();
    }
}

// Client code
public class BuilderPattern {
    public static void main(String[] args) {
        Builder builder = new ConcreteBuilder();
        Director director = new Director(builder);

        Product product = director.construct();
        System.out.println(product);

        Product product2 = director.construct2();
        System.out.println(product2);

        Product product3 = director.construct3();
        System.out.println(product3);
    }
}
