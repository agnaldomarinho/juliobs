<script language="javascript">
    function checkForm(Form)
    {
        var erros = "";

        erros += checkRA(Form.ra);
        erros += checkSenha(Form.senha);

        if (erros != "")
        {
            alert("Corrija os seguintes erros:\n" + erros);
            return false;
        }

        return true;
    }

    function checkRA(ra)
    {
        if (ra.value == "")
        {
            erro = "Você não digitou um RA.\n";
            ra.style.background = 'Yellow';
            ra.focus();
        }
        else if (isNaN(parseInt(ra.value)))
        {
            erro = "O RA deve conter apenas números.\n";
            ra.style.background = 'Yellow';
            ra.focus();
        }
        else if (ra.value.length != 6)
        {
            erro = "O RA deve possuir 6 dígitos.\n";
            ra.style.background = 'Yellow';
            ra.focus();
        }

        return erro;
    }

    function checkSenha(senha)
    {
        if (senha.value == "")
        {
            erro = "Você não digitou uma senha.\n";
            senha.style.background = 'Yellow';
            senha.focus();
        }

        return erro;
    }
</script>
