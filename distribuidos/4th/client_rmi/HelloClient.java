import java.rmi.*;
import java.util.concurrent.atomic.AtomicInteger;

class HelloClient {
  public static void main (String[] args){
    HelloInterface hello;
    String name = "rmi://localhost/HelloServer";
    Integer count;
    try {
      hello = (HelloInterface)Naming.lookup(name);
      count = hello.sayHello();
      System.out.println(count);
    }
    catch (Exception e){
      System.out.println("HelloClient exception:"+e);
    }
  }
}
