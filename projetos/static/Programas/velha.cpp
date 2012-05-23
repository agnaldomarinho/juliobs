// =====================================================================================
//
//       Filename:  velha.cpp
//
//    Description:  Jogo da Velha com Herança
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
#include <cstdlib>
#include "tabuleiro.h"

using namespace std;

// Classe Jogo da Velha com herança da Tabuleiro
class Velha : public Tabuleiro
{
    private:
            int jogador;
            int jogadas;
    public:
            Velha(); //construtor
            char vencedor();
            int getJogador();
            char getLetra();
            int getJogadas();
            bool invalido(int, int);
            void mudaJogador();
            void incrementaJogadas();
};

Velha::Velha()
{
    jogador = 1; // Inicia com o jogador X
    jogadas = 0; // Inicia com 0 jogadas
    setLin(3);   // Jogo possui 3 linhas
    setCol(3);   // Jogo possui 3 colunas
}

void Velha::mudaJogador()
{
    jogador++;
    if (jogador == 3)
        jogador = 1;
}

void Velha::incrementaJogadas()
{
    jogadas++;
}

int Velha::getJogador()
{
     return jogador;
}

char Velha::getLetra()
{
    switch (jogador)
    {
        case 1: return 'X'; break;
        case 2: return 'O'; break;
        default: return 'F'; // Nunca chegará aqui
    }
}

int Velha::getJogadas()
{
    return jogadas;
}

bool Velha::invalido(int px, int py)
{
    if (px < 0 || px > 2 || py < 0 || py > 2)
	    return true;
    return false;
}

char Velha::vencedor()
{
    if (getTab(0,0) == getTab(0,1) && getTab(0,0) == getTab(0,2) && getTab(0,0) != ' ')
       return getTab(0,0);
    if (getTab(1,0) == getTab(1,1) && getTab(1,0) == getTab(1,2) && getTab(1,0) != ' ')
       return getTab(1,0);
    if (getTab(2,0) == getTab(2,1) && getTab(2,0) == getTab(2,2) && getTab(2,0) != ' ')
       return getTab(2,0);
    if (getTab(0,0) == getTab(1,0) && getTab(0,0) == getTab(2,0) && getTab(0,0) != ' ')
       return getTab(0,0);
    if (getTab(0,1) == getTab(1,1) && getTab(0,1) == getTab(2,1) && getTab(0,1) != ' ')
       return getTab(0,1);
    if (getTab(0,2) == getTab(1,2) && getTab(0,2) == getTab(2,2) && getTab(0,2) != ' ')
       return getTab(0,2);
    if (getTab(0,0) == getTab(1,1) && getTab(0,0) == getTab(2,2) && getTab(0,0) != ' ')
       return getTab(0,0);
    if (getTab(0,2) == getTab(1,1) && getTab(0,2) == getTab(2,0) && getTab(0,2) != ' ')
       return getTab(0,2);
    return 0;
}

int main(int argc, char* argv[])
{
    int px, py;

    Velha jogo;

    // Continua se não for última jogada ou já tiver vencedor
    while (jogo.getJogadas() != 9 && !jogo.vencedor())
    {
        // Limpa a Tela
        // system ("CLS");
        system ("clear");
        
        cout << "\t\tJogo da Velha" << endl;
        jogo.desenha(); // desenha tabuleiro
        cout << "Vez do jogador " << jogo.getLetra() << endl;

        // Pede posições enquanto forem invalidas
        do
        {
           cout << "Entre com a posicao" << endl;
           cin >> px >> py;
        }
        while (jogo.invalido(px, py));

        if ( jogo.posicaoOcupada(px, py)) // Verifica disponibilidade da casa
        {
           cout << "jogada invalida" << endl;
           cout << "pressione qualquer tecla para continuar" << endl;

           getchar();
           getchar();
        }
        else
        {
            jogo.preenche(px, py, jogo.getLetra());
            jogo.mudaJogador();
            jogo.incrementaJogadas();
        }
    }

    // Avisa se ouve empate ou quem ganhou
    if (jogo.vencedor() == 0)
       cout << "Houve empate" << endl;
    else
       cout << "O jogador " << jogo.vencedor() << " venceu!" << endl;

    return EXIT_SUCCESS;
}
