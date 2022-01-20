import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;

public class ClientHandler extends Thread {
        private final Socket socket;
        private final ObjectOutputStream outputStream;
        private final ObjectInputStream inputStream;

        public ClientHandler(Socket socket, ObjectOutputStream outputStream, ObjectInputStream inputStream) {
                this.socket = socket;
                this.outputStream=outputStream;
                this.inputStream=inputStream;
        }
        @Override
        public void run() {
                while (true){
                        try{
                              int[] received_txt=(int[]) inputStream.readObject();
                              Transformation transformation=new Transformation();
                              int[] ascii_codes=transformation.remove_first_element(received_txt);
                              transformation.show(ascii_codes);
                              int[][] firstMatrix= transformation.vector_to_matrix(ascii_codes);
                              double[][] secondMatrix;
                              if (received_txt[0]==48){
                                  secondMatrix=(Key.encrypt_key);
                              }
                              else{
                                  secondMatrix=Key.decrypt_key;
                              }
                             int[][] product = transformation.multiply_matrices( firstMatrix,secondMatrix);
                              int[] product_vector=transformation.matrix_to_vector(product);
                              char[] encrypted_txt=transformation.ascii_to_char(product_vector);
                              outputStream.writeObject(encrypted_txt);
                              outputStream.flush();
                        }
                        catch(Exception e){
                                //e.printStackTrace();
                        }
                }
        }
}
