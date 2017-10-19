### Deploy

Você vai precisar de

- Ansible instalado no seu ambiente
- Acesso SSH às instâncias listadas nos inventários (dir `inventory/`)
- `/etc/hosts` configurado para resolver os nomes das instâncias listadas nos
  inventários (ver `etc.hosts.example`)

Deploy

    $ ./deploy production master

Em que

- `master` é o nome do branch que se quer implantar
- É necessário garantir que o branch esteja no repositório remoto

Observações

- Decidimos ter apenas o ambiente de production para o Rambo para concentrar as
  informações (que são essenciais para a acurácia do algoritmo) na base de dados
  de produção

eitaaa