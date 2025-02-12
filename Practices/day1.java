package Practices;
import java.util.Scanner;
public class day1{
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        int row = inp.nextInt();
        System.out.println("The number of rows:"+row);
        int col = inp.nextInt();
        System.out.println("The number of columns:"+col);
        int[][] array = new int[row][col];
        System.out.println("Elements of array are"+arrayinput(array));
        int target = inp.nextInt();
        System.out.println("The target element:"+target);
        System.out.println(TwoDarray(array, target));
        
    }
    static int arrayinput(int[][] arr){
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                Scanner input = new Scanner(System.in);
                arr[i][j] = input.nextInt();
            }
        }
        return 0;
    }
    static int TwoDarray(int[][] arr, int num){
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if(arr[i][j] == num){
                    return i;
                    
                }
            }
        }
        return 0;
    }
}
