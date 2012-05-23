// =====================================================================================
//
//       Filename:  tabuleiro.h
//
//    Description:  Classe para jogos de Tabuleiro
//
//        Version:  1.0
//        Created:  22-10-2009 10:55:27
//       Revision:  none
//       Compiler:  g++
//
//         Author:  Julio Batista Silva, 351202
//        Company:  UFSCar
//
// =====================================================================================

#include <stdio.h>
#include <iostream>
#include <new>
#include <cstdlib>

using namespace std;

// Classe para jogos de tabuleiro
class Tabuleiro
{
    private:
            char **tabuleiro; // Matriz para tabuleiro
            int linhas;       // Número de linhas
            int colunas;      // Número de colunas
    public:
            Tabuleiro(int linhas=8, int colunas=8); // Construtor, padrão 8x8
            ~Tabuleiro();
            void setLin(int);
            void setCol(int);
            bool posicaoOcupada(int, int);
            char getTab(int, int);
            void preenche(int, int, char);
            void desenha();
};

// Construtor com parâmetros
Tabuleiro::Tabuleiro(int lin, int col)
{
    int i, j;

    linhas = lin;
    colunas = col;

    // Aloca matriz
    tabuleiro = new char*[linhas];

        for (i = 0; i < linhas; i++)
            tabuleiro[i] = new char[colunas];

    // Zera zera matriz
    for (i=0; i<linhas; i++)
    {
        for (j=0; j < colunas; j++)
            tabuleiro[i][j] = ' ';
    }
}

// Destrutor
Tabuleiro::~Tabuleiro()
{
    delete[] tabuleiro;
}

// Verifica se a posição está ocupada
bool Tabuleiro::posicaoOcupada(int lin, int col)
{
    if ( tabuleiro[lin][col] != ' ')
        return true;
    return false;
}

void Tabuleiro::setLin(int lin)
{
    linhas = lin;
}

void Tabuleiro::setCol(int col)
{
    colunas = col;
}

// Retorna letra de uma posição
char Tabuleiro::getTab(int linha, int coluna)
{
    return tabuleiro[linha][coluna];
}

// Insere numero em uma posição
void Tabuleiro::preenche(int lin, int col, char letra)
{
    tabuleiro[lin][col] = letra;
}

void Tabuleiro::desenha()
{
    int i, j;

    // Número das colunas
    cout << "   ";
    for (i=0; i < colunas; i++)
        cout << i << " ";
    cout << endl;

    // Traços para melhor aparência
    cout << "   ";
    for (i = 0; i < colunas; i++)
        cout << "--";
    cout << endl;

    for (i=0; i < linhas; i++)
    {
        // Número das linhas
        cout << i << " |";
        for (j=0; j < colunas; j++)
        {
            cout << tabuleiro[i][j] << "|";
        }

        cout << endl;
    }

    // Traços para melhor aparência
    cout << "   ";
    for (i = 0; i < colunas; i++)
        cout << "--";
    cout << endl;

}
