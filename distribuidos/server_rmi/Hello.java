import java.rmi.*;
import java.rmi.server.*;
import java.util.concurrent.atomic.AtomicInteger;

public class Hello extends UnicastRemoteObject implements HelloInterface {
  private AtomicInteger count = new AtomicInteger();
  public Integer sayHello() throws RemoteException {
    return count.getAndIncrement();
  }
  public Hello() throws RemoteException {
  }
}
