# Programa para testar se um site está online

O intuito deste projeto é criar uma aplicação simples que checa se um site está online ou não, utilizando a linguagem Python. O projeto tem caráter pedagógico e busca utilizar instigar a utilização de boas práticas de código, como o próprio versionamento e outras 'boas' práticas, especialmente direcionadas para a linguagem utilizada.


O projeto tem a estrutura listada a seguir:

```
README.md
requirements.txt
site_checker/
├── checker.py
├── cli.py
├── __init__.py
├── __main__.py
```

A ideia do projeto consiste em criar uma função que seja capaz de 'checar' o status de alguma url a ser testa, tarefa esta que será realizada no arquivo **checker.py** o qual contém a lógica de tal tarefa.

O usuário poderá utilizar tal aplicação através de uma *cli* (command line interface), que foi construída utilizando a biblioteca [argparse](https://docs.python.org/3/library/argparse.html).

Nesta versão inicial, a aplicação aceita apenas uma url por vez, e para rodar a aplicação, utilizamos 

```
python -m site_checker -u url

```

Como futuras melhorias, é esperado que seja possível mpliar a função acima para permitir a inclusão de arquivos com listas de URLs no CLI passando um caminho --file path/to/file.csv.


# Creditos

Projeto baseado em:
https://realpython.com/site-connectivity-checker-python/

E também em uma aula do programa de formação [Lighthouse](https://materiais.indicium.tech/lighthouse-formacao-na-area-de-dados-reserva-de-vaga) da empresa [Indicium](https://indicium.tech/).

