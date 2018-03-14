import java.rmi.*;
import java.rmi.server.*;
import java.util.concurrent.atomic.AtomicInteger;

class HelloServer{
  public static void main (String[] argv){
    try{
      Naming.rebind("rmi://localhost/HelloServer", new Hello());
    }
    catch (Exception e) { }
  }
}
