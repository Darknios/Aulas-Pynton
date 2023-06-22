package fundamentos1;

import java.util.Scanner;
 
public class ex11 {
public static void main(String[]args) {
	Scanner entrada= new Scanner(System.in);
	System.out.println("Digite um numero()");
	 int resp = entrada.nextInt();
	 if (resp >=0) {
		 System.out.println("Numero positivo");
	 }else {
		 System.out.println("Numero negativo");
	 }

}
}