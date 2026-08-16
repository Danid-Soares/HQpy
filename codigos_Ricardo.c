#include <stdio.h>
#include <stdbool.h>
#include <math.h>

    void exer1(){
        float custoFabrica, distribuidor, impostos, custoConsumidor;

        printf("Digite o custo de fabrica do veiculo: ");
        scanf("%f", &custoFabrica);

        distribuidor = custoFabrica * 0.12;
        impostos = custoFabrica * 0.45;
        custoConsumidor = custoFabrica + distribuidor + impostos;

        printf("O custo final ao consumidor é: R$ %.2f\n", custoConsumidor);
    }

    void exer2(){
        int Hamburguer, Cheeseburguer, BatataFrita, Refrigerante, Milkshake;
        float subtotal, totalfinal;

        printf("Digite a qtd de Hamburgueres:");
        scanf("%i", &Hamburguer);
        printf("Digite a qtd de Cheeseburguer:");
        scanf("%i", &Cheeseburguer);
        printf("Digite a qtd de Batata Frita:");
        scanf("%i", &BatataFrita);
        printf("Digite a qtd de Refrigerante:");
        scanf("%i", &Refrigerante);
        printf("Digite a qtd de Milkshake:");
        scanf("%i", &Milkshake);

        subtotal = (Hamburguer * 2.50) + (Cheeseburguer * 3.30) + (BatataFrita * 1.50) + (Refrigerante * 0.60) + (Milkshake * 1.70);
        totalfinal = subtotal + (subtotal * 0.10);

        printf("O valor final de sua compra é: R$ %.2f\n", totalfinal);
    }

    void exer3(){
        float S1, S2, S3, T, produto, area;

        printf("Digite um lado do triangulo(S1):");
        scanf("%f", &S1);
        printf("Digite um lado do triangulo(S2):");
        scanf("%f", &S2);
        printf("Digite um lado do triangulo(S3):");
        scanf("%f", &S3);

        T = (S1 + S2 + S3)/2.0;
        produto = T*(T-S1)*(T-S2)*(T-S3);
        area = pow(produto, 1.0/3.0);

        printf("A area do triangulo e: %.2f\n", area);
    }

    void exer4(){
    float valor;
    printf("Digite o valor do indice de poluicao: ");
    scanf("%f", &valor);

    if (valor >= 0.50) {
        printf("Avisar as industrias A, B e C.\n");
    }
    else if (valor >= 0.40) {
        printf("Avisar A e B\n");
    }
    else if (valor >= 0.30) {
        printf("Avisa a industria A\n");
    }
    else {
        printf("Indice aceitavel\n");
    }
}

int main(int argc, char *argv[]){
    //exer1;
    //exer2;
    //exer3;
    //exer4;

    return 0;
}