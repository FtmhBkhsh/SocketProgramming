import java.io.*;
import java.net.*;

public class TCPserver {
    public static void main(String arg[]) throws Exception{
        ServerSocket welcome_socket=new ServerSocket(3000);
        System.out.println("server is ready...");
        while (true){
            try{
                Socket connection_socket = welcome_socket.accept();
                System.out.println("\na request received");
                ObjectOutputStream outputStream=new ObjectOutputStream(connection_socket.getOutputStream());
                ObjectInputStream inputStream=new ObjectInputStream(connection_socket.getInputStream());
                new ClientHandler(connection_socket, outputStream, inputStream).start();
            }
            catch(Exception e){
                break;
            }
        }

    }
}
