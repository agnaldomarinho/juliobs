// =====================================================================================
// 
//       Filename:  alunos_binario.cpp
// 
//    Description:  Registro de notas de alunos usando arquivos binários
// 
//        Version:  1.0
//        Created:  27-11-2009 09:24:36
//       Revision:  none
//       Compiler:  g++
// 
//         Author:  Julio Batista Silva, 351202
//        Company:  UFSCar
// 
// =====================================================================================

#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>
#include <cstring>
using namespace std;

#ifndef ALUNO_H
#define ALUNO_H
class Aluno
{
    public:
        Aluno (int=0, string="Nome", float=0.0, float=0.0, float=0.0);

        void setRA(int);
        void setNome(string);
        void setP1(float);
        void setP2(float);
        void setP3(float);

        int getRA() const;
        int getP1() const;
        int getP2() const;
        int getP3() const;
        const char* getNome() const;

    private:
        char Nome[50];
        int RA;
        float P1;
        float P2;
        float P3;
};
#endif

Aluno::Aluno(int ra, string nome, float p1, float p2, float p3)
{
    setNome(nome);
    setRA(ra);
    setP1(p1);
    setP2(p2);
    setP3(p3);
}

void Aluno::setRA(int ra)
{
    RA = ra>0?ra:0;
}

void Aluno::setNome(string nome_string)
{
    const char *nome = nome_string.data();

    int tamanho = strlen(nome);

    // Tamanho máximo é 49 + '\0'
    tamanho = (tamanho<50?tamanho:49);

    // Copia caracteres para Nome
    strncpy(Nome, nome, tamanho);

    // Adiciona '\0' na última posição
    Nome[tamanho] = '\0';
}

void Aluno::setP1(float p1)
{
    P1 = (p1>= 0 && p1 <= 10)?p1:0;
}

void Aluno::setP2(float p2)
{
    P2 = (p2>= 0 && p2 <= 10)?p2:0;
}

void Aluno::setP3(float p3)
{
    P3 = (p3>= 0 && p3 <= 10)?p3:0;
}

int Aluno::getRA() const
{
    return RA;
}

int Aluno::getP1() const
{
    return P1;
}

int Aluno::getP2() const
{
    return P2;
}

int Aluno::getP3() const
{
    return P3;
}

const char* Aluno::getNome() const
{
    return Nome;
}


// =====================================================================================
//             Funções Úteis
// =====================================================================================
 
// Protótipo
void outputLine(ostream&, const Aluno&);

void outputLine(ostream &output, const Aluno &record)
{
    output << left << setw(10) << record.getRA()
           << setw(40) << record.getNome()
           << setw(4) << setprecision(2) << record.getP1()
           << setw(4) << setprecision(2) << record.getP2()
           << setw(4) << setprecision(2) << record.getP3()
           << endl;
}

int main()
{

    int p1, p2, p3, ra, opcao;
    char nome[50];
    Aluno estudante;

    cout << "Digite uma opção: ";
    cin >> opcao;

    // Criar arquivo
    if (opcao == 1)
    {
        ofstream alunos("alunos_bin.dat", ios::binary);

        if (!alunos)
        {
            cerr << "Erro ao abrir arquivo" << endl;
            exit(1);
        }

        // Reserva espaço para 100 registros no arquivo
        for (int i=0; i < 100; i++)
            alunos.write( reinterpret_cast< const char* >(&estudante), sizeof(Aluno) );
        
        alunos.close();
    }

    // Escrever no Arquivo
    if (opcao == 2)
    {
        ofstream alunos("alunos_bin.dat", ios::binary);

        if (!alunos)
        {
            cerr << "Erro ao abrir arquivo" << endl;
            exit(1);
        }

        cout << "Digite o RA do aluno: ";
        cin >> ra;
        estudante.setRA(ra);

        while ( estudante.getRA() > 0 && estudante.getRA() <= 100)
        {
            cin.getline(nome, 50);
            cout << "Digite o nome do aluno: ";
            cin.getline(nome, 50);
            estudante.setNome(nome);

            cout << "Digite a nota da P1: ";
            cin >> p1;
            estudante.setP1(p1);

            cout << "Digite a nota da P2: ";
            cin >> p2;
            estudante.setP2(p2);

            cout << "Digite a nota da P3: ";
            cin >> p3;
            estudante.setP3(p3);

            // Procura posição do RA
            alunos.seekp( (estudante.getRA() - 1) * sizeof (Aluno) );

            // Escreve no arquivo
            alunos.write( reinterpret_cast<const char*>(&estudante), sizeof(Aluno) );
            
            cout << "\nDigite o RA do aluno [1-100]: ";
            cin >> ra;
            estudante.setRA(ra);
        }

        alunos.close();
    }

    // Ler arquivo
    if (opcao == 3)
    {
        ifstream alunos("alunos_bin.dat", ios::binary);

        if (!alunos)
        {
            cerr << "Erro ao abrir arquivo" << endl;
            exit(1);
        }

        // Imprime primeira linha
        cout << left << setw(10) << "RA"
               << setw(40) << "Nome"
               << setw(4) << setprecision(2) << "P1"
               << setw(4) << setprecision(2) << "P2"
               << setw(4) << setprecision(2) << "P3"
               << endl;

        // Lê o primeiro regsitro do arquivo
        alunos.read ( reinterpret_cast< char * > (&estudante), sizeof(Aluno) );

        // Lê todos os outros registros
        while (alunos && !alunos.eof())
        {
            if (estudante.getRA() !=  0)
                outputLine( cout, estudante);

            // Lê o próximo
            alunos.read ( reinterpret_cast< char * > (&estudante), sizeof(Aluno) );
        }

        alunos.close();
    }

    return 0;
}
