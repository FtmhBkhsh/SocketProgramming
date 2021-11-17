import java.io.*;
import java.net.*;
import java.util.Scanner;

public class TCPclient {

    public static void main(String arg[]) throws Exception{
        System.out.println("What do you want to do? 0:Encrypt 1:Decrypt ");
        Scanner scanner=new Scanner((System.in));
        String job_num = scanner.nextLine();
        System.out.println("Enter your text: ");
        String original_txt = scanner.nextLine();
        String txt = job_num+original_txt;
        //transformations
        Transformation transformation=new Transformation();
        int[] ascii_vector= transformation.char_to_ascii(txt,job_num);
        //send_over_socket
        Socket client_socket = new Socket("localhost",3000);
        ObjectOutputStream OutputStream=new ObjectOutputStream(client_socket.getOutputStream());
        OutputStream.writeObject(ascii_vector);
        OutputStream.flush();
        //receive_from_socket
        ObjectInputStream InputStream=new ObjectInputStream(client_socket.getInputStream());
        char[] encrypted_txt = (char[]) InputStream.readObject() ;
        transformation.show(encrypted_txt);
    }

}
