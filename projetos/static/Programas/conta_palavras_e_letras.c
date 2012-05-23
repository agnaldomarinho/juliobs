/*
 * =====================================================================================
 *
 *       Filename:  conta_palavras_e_letras.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  ??/??/2009
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Julio Batista Silva (351202), juliob91(at)gmail.com
 *        Company:  UFSCar
 *
 * =====================================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int conta_letras (char *c)
{
    int i = 0;
    while ( *c != '\0')
    {
        *c++;
        i++;
    }
    return i;
}

int conta_letras2 (char *c)
{
    int i = 0;
    while ( *c != '\0')
    {
        while (*c == ' ' && *c != '\0')
            c++;
        
        i++;
        c++;
    }
    return i;
}

int conta_palavras (char *c)
{
    int i = 0;
    while ( *c != '\0')
    {
        while (*c != ' ' && *c != '\0')
            c++;
        
        while (*c == ' ' && *c != '\0')
            c++;
        
        i++;
    }
    return i;
}


int main (int argc, char** argv)
{
    char nome[15];

    printf("Digite um nome: ");
    scanf("%[^\n]", nome);
    printf ("%s", nome);

    printf ("\nLetras com espacos: %d", conta_letras(nome));
    printf ("\nLetras sem espacos: %d", conta_letras2(nome));
    printf ("\nPalavras: %d\n", conta_palavras(nome));

    return (EXIT_SUCCESS);
}
