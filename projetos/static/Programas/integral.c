/*
 * =====================================================================================
 *
 *       Filename:  integral.c
 *
 *    Description:  Calcula integrais definidas pelo método do trapézio usando ponteiro
 *                  para funcoes.
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
#include <math.h>

#define dx 0.00001

float f1 (float x);
float f2 (float x);
float f3 (float x);
float f4 (float x);
float f5 (float x);
float f6 (float x);
float f7 (float x);
float integral ( float (*f)(float), float x1, float x2);

int main (int argc, char** argv)
{
    int k;
    float a1, a2;
    char funcao;

    printf ("1. y = x\n" );
    printf ("2. y = sin(x)\n");
    printf ("3. y = cos(x)\n");
    printf ("4. y = x²\n");
    printf ("5. y = x³\n");
    printf ("6. y = 10\n");
    printf ("7. y = 1/x\n");

    printf ( "\n\nDigite qual funcao: ");
    scanf ("%d", &k);

    printf ( "\nDigite a1 , a2: ");
    scanf ("%f %f", &a1, &a2);

    switch (k)
    {
        case 1:
            printf ("\nA integral vale %f\n", integral(f1, a1, a2)); break;
        case 2:
            printf ("\nA integral vale %f\n", integral(f2, a1, a2)); break;
        case 3:
            printf ("\nA integral vale %f\n", integral(f3, a1, a2)); break;
        case 4:
            printf ("\nA integral vale %f\n", integral(f4, a1, a2)); break;
        case 5:
            printf ("\nA integral vale %f\n", integral(f5, a1, a2)); break;
        case 6:
            printf ("\nA integral vale %f\n", integral(f6, a1, a2)); break;
        case 7:
            printf ("\nA integral vale %f\n", integral(f7, a1, a2)); break;
        default:
            printf ("Opção inválida\n");
    }

    return (EXIT_SUCCESS);
}

float integral ( float (*f)(float), float x1, float x2)
{
    float i, area = 0;

    i = x1+dx;

    while ( i <= x2 )
    {
        area += ((f(i) + f(i+dx)) * dx) / 2.0;
        i += dx;
    }

    return area;
}

float f1 (float x)
{
    return x;
}

float f2 (float x)
{
    return sin(x);
}

float f3 (float x)
{
    return cos(x);
}

float f4 (float x)
{
    return (x*x);
}

float f5 (float x)
{
    return (x*x*x);
}

float f6 (float x)
{
    return (10);
}

float f7 (float x)
{
    return (1/x);
}
