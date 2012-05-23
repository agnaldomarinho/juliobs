// =====================================================================================
// 
//       Filename:  radiorelogio.cpp
// 
//    Description:  Rádio-relógio com herança múltipla
// 
//        Version:  1.0
//        Created:  29-10-2009 10:54:21
//       Revision:  none
//       Compiler:  g++
// 
//         Author:  Julio Batista Silva, 351202
//        Company:  UFSCar
// 
//  Dificuldades e observações:
//  -> Limite de 108000 KHz para frequência FM
//  -> O relógio não altera o horário sozinho
//  -> 
//
// =====================================================================================

#include <iostream>
#include <cstdlib>
using namespace std;

// =====================================================================================
//        Class:  Data
//  Description: Ajusta a data 
// =====================================================================================

class Data
{
    private:
        int Dia;
        int Mes;
        int Ano;

        void set_Dia(int);
        void set_Mes(int);
        void set_Ano(int);
    
    public:
        Data();
        void imprime_data();
        bool e_bissexto();

        void ajustar_data();
};

// Construtor
Data::Data ()
{
    Dia = 1;
    Mes = 1;
    Ano = 2009;
}

// Mostra a data na tela
void Data::imprime_data()
{
    cout << "Data:\t\t\t" << Dia << "/" << Mes << "/" << Ano << endl;
}

// Altera valor do Dia
void Data::set_Dia(int dia)
{
    int max;
     
    switch (Mes)
    {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12: max = 31; break;
        case 2: max = e_bissexto()?29:28; break;
        case 4:
        case 6:
        case 9:
        case 11: max = 30; break;
    }
          
     if ( dia < max )
     {
         Dia = dia;
     }
}

// Altera valor do Mês
void Data::set_Mes(int mes)
{
    if (mes > 0 && mes <= 12) 
        Mes = mes;
}

// Altera valor do Ano
void Data::set_Ano(int ano)
{
    if (ano >= 2000)
        Ano = ano;
}

// Nessa ordem, para evitar 30/02/2009, etc.
void Data::ajustar_data()
{
    int dia, mes, ano;

    cout << "Digite o dia: "; cin >> dia;
    cout << "Digite o mes: "; cin >> mes;
    cout << "Digite o ano: "; cin >> ano;

    set_Ano(ano);
    set_Mes(mes);
    set_Dia(dia);
}

// Verifica se o Ano é bissexto
bool Data::e_bissexto()
{
    int x = Ano;
    
    if  ( Ano % 100 == 0)
        x = Ano/100;
    
    if ( x%4 == 0)
        return true;
    
    return false;
}

// =====================================================================================
//        Class:  Relogio
//  Description:  Ajusta o horário
// =====================================================================================

class Relogio
{
	private:
		int Segundo;
		int Minuto;
		int Hora;
	
    public:
		Relogio();
		Relogio(int, int, int);

        void ajustar_relogio();
        void imprime_relogio();
};

// Construtor sem parametros
Relogio::Relogio()
{
	Segundo = 0;
	Minuto = 0;
	Hora = 0;
}

// Pergunta pelo horário
// Se algum valor for inválido mantem o anterior
void Relogio::ajustar_relogio()
{
    int h, m, s;

    Hora = Minuto = Segundo = 0;

    cout << "Digite as horas: ";    cin >> h;
    cout << "Digite os minutos: ";  cin >> m;
    cout << "Digite os segundos: "; cin >> s;

    if (h >=0 && h < 24)
        Hora = h;
    if (m >= 0 && m < 60)
        Minuto = m;
    if (s >= 0 && s < 60)
        Segundo = s;
}

// Mostra o horário na tela
void Relogio::imprime_relogio()
{
	cout << "Hora:\t\t\t" << Hora << ":" << Minuto << ":" << Segundo << endl;
}

// =====================================================================================
//        Class:  Radio
//  Description:  
// =====================================================================================

class Radio
{
    private:
            bool estado_radio;
            int frequencia; // inteiro, pois e KHz

    public:
            Radio();
            Radio(bool, int);
            
            void radio_OnOff();
            void sintonizar_radio();
            
            void imprime_radio();

};

Radio::Radio()
{
    estado_radio = true;
    frequencia = 953000;
}

Radio::Radio(bool estador, int freq)
{
    estado_radio = estador;
    frequencia = freq;
}

void Radio::radio_OnOff()
{
    if (estado_radio)
        estado_radio = false;
    else
        estado_radio = true;
}

void Radio::sintonizar_radio()
{
    int freq;

    cout << "Digite a frequencia (0-108000): ";
    cin >> freq;

    if (freq > 0 && freq < 108000)
        frequencia = freq;
}

// Exibe informações sobre o rádio
void Radio::imprime_radio()
{
    cout << "Frequência do rádio:\t" << frequencia << " KHz" << endl;
    cout << "Estado do rádio:\t"; 
            if (estado_radio)
                cout << "Ligado" << endl;
            else
                cout << "Desligado" << endl;
}

// =====================================================================================
//        Class:  RadioRelogio
//  Description:  Radio-relógio com herança múltipla
// =====================================================================================

class RadioRelogio : public Radio, public Relogio, public Data 
{
    private:
            bool despertar;
            int despertar_h;
            int despertar_min;
            int despertar_s;
            bool tipo_alarme; // 1-música, 0-rádio
            
            void set_DespertarH(int);
            void set_DespertarMin(int);
            void set_DespertarSec(int);

    public:
            RadioRelogio();

            void set_TipoAlarme();

            void ajustar_despertador();
            void imprime_RadioRelogio();
            void despertador_OnOff();
};

// Construtor
RadioRelogio::RadioRelogio()
{
    despertar =     false;
    despertar_h =   0;
    despertar_min = 0;
    despertar_s =   0;
    tipo_alarme =   0;
}

// Alterna entre tipos de alarme (música-rádio)
void RadioRelogio::set_TipoAlarme()
{
    if (tipo_alarme)
        tipo_alarme = false;
    else
        tipo_alarme = true;
}

// Muda horário de despertar
void RadioRelogio::set_DespertarH(int hora)
{
    if (hora >= 0 && hora < 24)
        despertar_h = hora;
}

void RadioRelogio::set_DespertarMin(int minuto)
{
    if (minuto >= 0 && minuto < 60)
        despertar_min = minuto;
}

void RadioRelogio::set_DespertarSec(int segundo)
{
    if (segundo >= 0 && segundo < 60)
        despertar_s = segundo;
}

// Liga/Desliga despertador
void RadioRelogio::despertador_OnOff()
{
    if (despertar)
        despertar = false;
    else
        despertar = true;
}

// Ajusta despertador
void RadioRelogio::ajustar_despertador()
{
    int h, m, s;

    cout << "Digite as horas: ";    cin >> h;
    cout << "Digite os minutos: ";  cin >> m;
    cout << "Digite os segundos: "; cin >> s;

    set_DespertarH(h);
    set_DespertarMin(m);
    set_DespertarSec(s);
}

// Exibe informações sobre o rádio-relógio
void RadioRelogio::imprime_RadioRelogio()
{
    // system("CLS");
    system("clear");

    imprime_data();
    imprime_relogio();
    imprime_radio();

    cout << "Despertar:\t\t";
            if(despertar)
                cout << "Sim" << endl;
            else
                cout << "Não" << endl;

    cout << "Hora de despertar:\t" << despertar_h << ":" << despertar_min << ":" << despertar_s << endl;
    
    cout << "Tipo de alarme:\t\t";
            if(tipo_alarme)
                cout << "Música" << endl;
            else
                cout << "Rádio" <<endl;

    cout << endl;
}

int main()
{
    int opcao;

    // Cria objeto
    RadioRelogio radiorelogio;

    // Menu com opções
    do
    {
        cout << "Digite o número correspondente à opção desejada" << endl << endl;

        cout << "\t1 - Ajustar data"          << endl;
        cout << "\t2 - Ajustar relógio"       << endl;
        cout << "\t3 - Ajustar despertador"   << endl;
        cout << "\t4 - Tipo de alarme"        << endl; 
        cout << "\t5 - Sintonizar rádio"      << endl;
        cout << "\t6 - On/Off despertador"    << endl;
        cout << "\t7 - On/Off rádio"          << endl;
        cout << "\t8 - Desligar rádio-relógio"<< endl;

        cout << "Opção: "; cin >> opcao;

        switch (opcao)
        {
            case 1: radiorelogio.ajustar_data();        break;
            case 2: radiorelogio.ajustar_relogio();     break;
            case 3: radiorelogio.ajustar_despertador(); break;
            case 4: radiorelogio.set_TipoAlarme();      break;
            case 5: radiorelogio.sintonizar_radio();    break;
            case 6: radiorelogio.despertador_OnOff();   break;
            case 7: radiorelogio.radio_OnOff();         break;
        }

        radiorelogio.imprime_RadioRelogio();

    } while (opcao != 8);

    return EXIT_SUCCESS;
}
