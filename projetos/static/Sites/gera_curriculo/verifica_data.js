// Verifica data de Nascimento
function verificaData()
{
    var vetor_data = document.getElementById('nascimento').value.split('/');

    // jan = 0; fev = 1 ...
    var dia = vetor_data[0];
    var mes = vetor_data[1] - 1;
    var ano = vetor_data[2];

    // Se algum campo estiver vazio, retorna falso
    if (!dia || !mes || !ano)
    {
        alert("Data de nascimento inválida");
        return false;
    }

    // Quantia de dias no mês
    var tamanhoMes = new Array(31,28,31,30,31,30,31,31,30,31,30,31);

    // Verifica ano Bissexto
    if ((ano % 4 == 0 && ano % 100 != 0) || ano % 400 == 0)
        tamanhoMes[1] = 29;
    
    // Verifica se dia é maior que a quantidade de dias do mês 
    if (dia < 1 || dia > tamanhoMes[mes])
    {
        alert("Dia de nascimento inválido");
        return false;
    }

    // jan = 0; dez = 11; 
    if (mes < 0 || mes > 11)
    {
        alert("Mês de nascimento inválido");
        return false;
    }

    return true;
}
