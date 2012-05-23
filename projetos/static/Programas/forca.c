#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#define TAM 15

void linhas(int tamanho, char a[TAM])
{
    int i;

    for (i=0; i<tamanho; i++)
        a[i] = '_';
}

void boneco(erros)
{
    switch (erros)
    {
        case 0:
            printf ("\t\t  _______\n\t\t |      |\n\t\t        |\n\t\t        |\n\t\t        |\n\t\t        |\n\t\t       _|_\n"); break;
        case 1:
            printf ("\t\t  _______\n\t\t |      |\n\t\t O      |\n\t\t        |\n\t\t        |\n\t\t        |\n\t\t       _|_\n"); break;
        case 2:
            printf ("\t\t  _______\n\t\t |      |\n\t\t O      |\n\t\t |      |\n\t\t        |\n\t\t        |\n\t\t       _|_\n"); break;
        case 3:
            printf ("\t\t  _______\n\t\t |      |\n\t\t O      |\n\t\t/|      |\n\t\t        |\n\t\t        |\n\t\t       _|_\n"); break;
        case 4:
            printf ("\t\t  _______\n\t\t |      |\n\t\t O      |\n\t\t/|\\     |\n\t\t        |\n\t\t        |\n\t\t       _|_\n"); break;
        case 5:
            printf ("\t\t  _______\n\t\t |      |\n\t\t O      |\n\t\t/|\\     |\n\t\t |      |\n\t\t        |\n\t\t       _|_\n"); break;
        case 6:
            printf ("\t\t  _______\n\t\t |      |\n\t\t O      |\n\t\t/|\\     |\n\t\t |      |\n\t\t/       |\n\t\t       _|_\n"); break;
        case 7:
            printf ("\t\t  _______\n\t\t |      |\n\t\t O      |\n\t\t/|\\     |\n\t\t |      |\n\t\t/ \\     |\n\t\t       _|_\n");break;
    }
}

void sorteia (char palavra[TAM])
{
    srand(time(NULL));

    char *a[] = {"arara", "baleia", "cavalo", "dromedario", "esquilo", "foca", "gato", "hipopotamo", "iguana", "jabuti", "leao", "macaco", "ornitorrinco", "pato"};

    strcpy(palavra, a[rand()%14]);
}

int main (int argc, char** argv)
{
    char palavra[TAM], letra, novo[TAM], repete = 's';
    int tamanho, erros, i, troca, vit;

    while (repete == 's')
    {
        system ("clear");

        // Inicia variaveis
        erros = troca = vit = 0;

        // Limpa memoria
        for (i=0; i<TAM; i++)
        {
            palavra[i] = '\0';
            novo[i] = '\0';
        }

        sorteia(palavra);

        tamanho = strlen(palavra);

        // Desenha traços _
        linhas(tamanho, novo);

        while ( (erros < 7) && (vit == 0) )
        {
            printf("\t\t\tJOGO da FORCA \n\n\n");

            boneco (erros);

            printf("\t%s\n\n", novo);

            printf (" Digite uma letra: ");
            scanf (" %c", &letra);

            troca = 0;
            for (i=0; i<tamanho; i++)
            {
                if (palavra[i] == letra)
                {
                    novo[i] = letra;
                    troca = 1;
                }
            }
            if (troca == 0)
                erros++;

            system ("clear");

            // Compara palavra original com a nova
            vit = 1;
            for (i=0; i<tamanho; i++)
            {
                if (novo[i] != palavra[i])
                    vit = 0;
            }
        }

        // Verifica Vitoria
        if (vit)
            printf ("\nParabens!!!");
        else
        {
            printf ("\nPerdeu kkkk\n");
            printf ("\nO certo é \"%s\"", palavra);
        }

        // Pergunta para jogar de novo
        do
        {
            system("clear");
            printf ("\nMais uma vez?: ");
            scanf (" %c", &repete);
        }
        while (( repete != 's' ) && ( repete != 'n'));

    }

    return (EXIT_SUCCESS);
}
