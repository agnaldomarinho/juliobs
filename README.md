# juliobs.com

Este é o código fonte do meu [site](http://juliobs.com) em Django.

## Tecnologias
*   Python
*   Django
*   HTML5
*   CSS3
*   jQuery

## Instruções
Crie um arquivo chamado _local_settings.py_ no mesmo diretório do
_settings.py_, contendo as configurações do seu servidor. Exemplo:

    # -*-*- encoding: utf-8 -*-*-
    DEBUG = True

    ADMINS = (
            ('Admin', 'admin@example.com'),
    )

    DB_ENGINE = 'django.db.backends.postgresql_psycopg2'
    DB_NAME = 'seu_djangodb'
    DB_USER = 'seu_usuario'
    DB_PASSWORD = 'sua_senha'
    DB_HOST = ''
    DB_PORT = ''

    SECRET_KEY = '0123456789-sua_secret_key-9876543210'

Crie a pasta media: `mkdir juliobs/juliobs/arquivos/media`

Instale os aplicativos de terceiros: `pip2 install imagestore`

Rode os scripts para coletar arquivos estáticos e sincronizar o banco de dados:
`./manage.py collectstatic`, `./manage.py syncdb` e `./manage.py migrate`.

Se você não criou um superusuário na etapa anterior, crie agora
(`./manage.py createsuperuser`)

Se der erro na etapa anterior, corrija seu locale e tente novamente:

    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8

## Licença
Enquanto penso melhor sobre quais licenças usar, este projeto será apenas
_source-available_, mas não _free software_. O mesmo vale para as imagens e
textos. (Você pode estudar o código e criar um fork, mas não gerar derivados).

Deixo claro que pretendo alterar essa licença o quanto antes e gostaria de
sugestões sobre como fazer isso corretamente. Minha ideia atual é usar **GNU
AGPLv3** para o código e **Creative Commons** com _attribution_ e _share
alike_ (CC BY-SA) para as imagens e textos.

Mas antes preciso verificar se todos os _3rd party_ apps e scripts são
compatíveis com a AGPLv3 e avaliar se uma licença mais permissiva não seria
mais apropriada.

## TODO
*   Terminar internacionalização
*   Traduzir este README para inglês
