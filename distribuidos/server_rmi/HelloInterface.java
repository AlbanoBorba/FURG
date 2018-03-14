import java.rmi.*;
import java.util.concurrent.atomic.AtomicInteger;

public interface HelloInterface extends Remote {
  public Integer sayHello() throws RemoteException;
}
