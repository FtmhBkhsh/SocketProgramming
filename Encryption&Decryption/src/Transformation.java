import java.util.Arrays;

public class Transformation {

    public static int[] char_to_ascii (String txt,String job_num){
        int negative_num=0;
        for (int j = 0; j < txt.length(); j++) {
            if((int) txt.charAt(j)== (int) '-') {
                negative_num=negative_num+1;
            }
        }


        int[] ascii = new int[txt.length()-negative_num];
        for(int i=0,k=0;i<txt.length()-negative_num;i++) {
            if((int) txt.charAt(k)== (int) '-' & Integer.parseInt(job_num)!=0){
                ascii[i] = ((int) txt.charAt(k+1))*-1;
                k=k+2;
            }
            else {
                ascii[i] = (int) txt.charAt(k);;
                k++;
            }
        }
    return ascii;
    }

    public static char[] ascii_to_char (int[] ascii){
        int negative_num=0;
        for (int j = 0; j < ascii.length; j++) {
            if(ascii[j]<0) {
                negative_num=negative_num+1;
                }
            }
        char[] chars = new char[(ascii.length)+negative_num];

        for (int j = 0, k = 0; j < (ascii.length); j++) {
            if(ascii[j]>=0) {
                chars[k] = (char) ascii[j];
                k++;
            }
            else{
                chars[k]= '-';
                chars[k+1]= (char) (ascii[j]*(-1));
                k=k+2;
            }
        }
        return chars;
    }

    public static int[] remove_first_element(int[] array){
        int[] modifiedArray = Arrays.copyOfRange(array, 1, array.length);
        return modifiedArray;
    }

    public static int[] matrix_to_vector(int[][] txt_matrix){
        int[] txt_vector = new int[txt_matrix[0].length * txt_matrix.length];
        int des_pos=0;
        for (int i=0;i<txt_matrix.length;i++) {
            System.arraycopy(txt_matrix[i], 0, txt_vector, des_pos, txt_matrix[i].length);
            des_pos+=txt_matrix[0].length;
        }
        return txt_vector;
    }

    public static int[][] vector_to_matrix(int[] txt_vector){
        int[][] txt_matrix = new int[(txt_vector.length+1)/2][2];
        for (int j = 0; j < txt_vector.length; j++) {
            txt_matrix[(j)/2][j%2]=txt_vector[j];
        }
        return txt_matrix;
    }

    public static int[][] multiply_matrices(int[][] firstMatrix, double[][] secondMatrix){
        int row = firstMatrix.length;
        int[][] product = new int[row][2];
        //temp is used to convert final element of product to integer
        double temp=0;
        try {
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < 2; j++) {
                    for (int k = 0; k < 2; k++) {
                        temp += firstMatrix[i][k] * secondMatrix[k][j];
                    }
                    product[i][j]=(int)temp;
                    temp=0;
                }
            }
        }
        catch(Exception e){
            e.printStackTrace();
        }
        return product;
    }

    public static void show(int[] data) {
        System.out.print("received data:");
        for (int j = 0; j < data.length; j++) {
            System.out.print(data[j] + " ");
        }
    }
    public static void show(char[] data){
        System.out.print("received data:");
            for (int j = 0; j < data.length; j++) {
                System.out.print(data[j] + " ");
            }

    }
}
