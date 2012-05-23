/*
    Quadrado mágico é uma tabela quadrada de numeros distintos arranjados de forma que a soma
    de uma linha, de uma coluna ou de uma diagonal são sempre iguais a uma constante magica.

    O método siamês permite gerar quadrados magicos de ordem impar:
        1. Inicie com 1 no centro da 1a linha;
        2. O proximo numero será uma linha acima e uma coluna a direita;
        3. Se o numero atual estiver na 1a linha o proximo numero estara na ultima linha;
        4. Se estivar na ultima coluna o proximo estara na 1a;
        5. O numero que segue um multiplo da ordem e colocado uma linha abaixo.

                                                                by Julio
*/

#include <stdio.h>
#include <stdlib.h>

void gerar (int v[][50], int ordem)
{
    int qtd = ordem * ordem; // quantidade de preenchimentos
    int i=0, j=ordem/2; // começa no centro da 1a coluna

    for (int k=1; k<=qtd; k++)
    {
        v[i][j] = k; // preenche o quadrado

        i--; // muda para linha de cima
        j++; // muda para coluna a direita

        if (k%ordem == 0) // quando [i--,j++] ja estiver preenchido
        {
            i += 2; // vai pra linha de baixo
            --j; // permanece na mesma coluna
        }
        else
        {
            if (j==ordem) // se estiver na ultima coluna
                j -= ordem; // vai para a 1a coluna

            else if (i<0) // quando estiver na 1a linha
                i += ordem; // vai para a ultima linha
        }
    }
}

void imprimir (int v[][50], int size)
{
    int i, j;

    for (i=0; i<size; i++)
    {
        for (j=0; j<size; j++)
            printf ("%3d ", v[i][j]);
        printf ("\n");
    }
}

int le_ordem ()
{
    int ord;
    do
    {
        printf ("Digite a ordem: ");
        scanf ("%d", &ord);
    }
    while ( (ord < 3) || (ord%2==0) ); // aceita apenas impares maiores que 1

    return ord;
}

int const_magica(int n)
{
    int cm;

    cm = (n*(n*n + 1))/2;

    return cm;
}

int main (int argc, char** argv)
{
    int a[50][50];
    int ordem;

    ordem = le_ordem();
    gerar(a, ordem);
    imprimir(a, ordem);
    printf ("\nA constante magica vale %d.", const_magica(ordem));

    return (EXIT_SUCCESS);
}
