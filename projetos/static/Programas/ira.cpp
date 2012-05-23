// =====================================================================================
// 
//       Filename:  ira.cpp
// 
//    Description:  Lê o arquivo de texto historico.txt e calcula o IRA do aluno.
//                  O arquivo "historico.txt" é gerado passando o "historico.html",
//                  disponível no Progradweb, pelo seguinte script (junte em uma linha):
//
//                  grep -B 2 -A 1 "<td width='19%'>" historico.html |
//                  awk '{ if ( NR > 5 && (NR-2)%5 != 0 ) { print $0; } }' |
//                  sed -e "s/^\(.*\)size='1'>\(.*\)<\/f\(.*\)/\2/; s/&nbsp;/0/;
//                  s/--//; s/Reprovado nota/Reprovado/" > historico.txt
//
//                  grep -B 2 -A 1 "<td width='19%'>" historico.html | awk '{ if ( NR > 5 && (NR-2)%5 != 0 ) { print $0; } }' | sed -e "s/^\(.*\)size='1'>\(.*\)<\/f\(.*\)/\2/; s/&nbsp;/0/;s/--//; s/Reprovado nota/Reprovado/" > historico.txt
//
//                  Trata o status "Pendente", que ocorre quando a nota da recuperação
//                  ainda não foi publicada, como uma reprovação.
//                  
//        Version:  1.0
//        Created:  07/12/2011 12:28:31 PM
//       Revision:  none
//       Compiler:  g++
// 
//         Author:  Julio Batista Silva (351202), juliob91(at)gmail.com
//        Company:  UFSCar
// 
// =====================================================================================

#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
using namespace std;

#define DEBUG 0

// Total de créditos para me formar em Eng. de Computação.
const int TOTAL = 274;

int main()
{
    string resultado;
    double nota, nota_ponderada=0.0;
    double ira;
    double creditos, creditos_solicitados=0.0, creditos_desistentes=0.0,
           creditos_trancados=0.0, creditos_aprovados=0.0, creditos_reprovados=0.0;

    // Abre e verifica o arquivo
    ifstream historico("historico.txt", ios::in);

    if (!historico)
    {
        cerr << "Erro ao abrir arquivo" << endl;
        return 1;
    }

    // Efetua leitura dos dados
    while(historico >> nota >> resultado >> creditos)
    {
        if (resultado == "Aprovado")
            creditos_aprovados += creditos;

        else if (resultado == "Cancelado")
        {
            // Créditos trancados não são contados como solicitados
            creditos_solicitados -= creditos;
            creditos_trancados += creditos;
        }

        else if (resultado == "Reprovado" || resultado == "Pendente")
            creditos_reprovados += creditos;

        else if (resultado == "Desistente")
            creditos_desistentes += creditos;

        creditos_solicitados += creditos;
        nota_ponderada += creditos * nota;
    }

    // Realiza o cálculo do IRA
    ira = 1000 * ( (nota_ponderada/creditos_solicitados) * (2 - 2*(creditos_desistentes/creditos_solicitados) - creditos_trancados/creditos_solicitados) );
    
    cout << "IRA: " << ira << endl;

    // Calcula porcentagem concluída
    cout << "Porcentagem concluída: " << fixed << setprecision(2) << 100.0*creditos_aprovados/(double)TOTAL << "%" << endl;

#if DEBUG
    cout << "Créditos Solicitados: "    << creditos_solicitados << endl;
    cout << "Créditos Aprovados: "      << creditos_aprovados << endl;
    cout << "Créditos Reprovados: "     << creditos_reprovados << endl;
    cout << "Créditos Cancelados: "     << creditos_trancados << endl;
    cout << "Créditos Desistentes: "    << creditos_desistentes << endl;
#endif

    // Fecha o arquivo
    historico.close();

    return 0;
}
