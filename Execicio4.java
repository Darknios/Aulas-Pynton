package Execicio;
import java.util.Scanner;
public class Execicio4 {
	public static void main(String[] args) {
		Scanner entrada= new Scanner(System.in);
		System.out.print("Digite a sua primeira nota: ");
	    float nota1 = entrada.nextFloat ();
		System.out.print("Digite a sua segunda nota: ");
		float nota2 = entrada.nextFloat();
		float media = (nota1+nota2)/2;
		System.out.print("A sua media é: "+ media);
		
		
	}
}
