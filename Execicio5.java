package Execicio;

import java.util.Scanner;

public class Execicio5 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner (System.in);
		char letra;
		System.out.println("digite uma letra [M/F]: ");
		letra = entrada.next().charAt(0);
		if (letra == 'M') {
			System.out.println("Masculino");
		}
		else if (letra =='F') {
			System.out.println("Feminino");
		}
		else {
			System.out.println("Inválido");
		}
	}
}
