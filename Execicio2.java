package Execio;
import java.util.Scanner;
public class Execicio2 {
 public static void main(String[]args) {
	 Scanner input= new Scanner(System.in);
		System.out.print("Digite um numero: ");
	    int numero1 = input.nextInt ();
		System.out.println("Digite outro numero: ");
		int numero2 = input.nextInt();
		System.out.print("Digite um outro numero: ");
	    int numero3 = input.nextInt ();
		if (numero1 > numero2) {
			System.out.println("Numero maior é: "+numero1+" e o Numero menor é: "+numero2); }
		else if (numero2 > numero3) {
			 System.out.println("Numero maior é: "+numero2+" e o Numero menor é: "+numero3); }
		else{
        	System.out.println("Numero maior é"+numero3+" e o Numero menor é: "+numero1); }
  }
}
