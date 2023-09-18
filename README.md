# tp-PDS-UFMG-2023-2
Repositorio destinado ao trabalho pratico principal da disciplina de pratica e desenvolvimento de software da UFMG no semestre de 2023/2.

## Objetivo
Criar um site de avaliação de matérias da UFMG no qual alunos podem dar uma nota e um comentário opcional para os cursos disponíveis, pesquisar a nota de cursos existentes e avaliar comentários como úteis ou não. Além disso, haverá perfis de moderadores, usuários e administradores, cada um com um papel no sistema. Os usuários se registram, avaliam disciplinas e comentários. Os Administradores aceitam ou recusam a inscrição de um novo usuário visando garantir a não duplicidade de usuários e criam novas disciplinas que podem ser avaliadas. Os moderadores podem reter comentários inapropriados e banir usuários que repetidademente fazem comentários inapropriados. Para isso, ele terá acesso a ferramentas que facilitam isso, como por exemplo o número de vezes que um usuário teve comentários retidos.

## Escopo
O escopo do trabalho será fazer algo que implemente o básico do sistema acima, pelo menos separando a ideia de usuário e administrador, permitindo a criação de matérias, contas e avaliação de disciplinas.

## Membros do grupo
Kael Soares Augusto - Backend/Bando de Dados

Lucas Rios Bicalho- FullStack

Wilgnert de Alcântara Rodrigues Batista - Frontend

Alefi Santos Cunha - FullStack

## Tecnologias
Frontend - Streamlit

Backend - Python

Interface entre Front/Back/BD - Python

Banco de dados - SQLite3 como biblioteca do python

Cada uma dos papeis acima serão escritos em arquivos distintos conectados apenas pela interface.

## Mockup das telas
https://www.figma.com/file/GgoWNFy6FsBBNRZGE9kFZo/Untitled?type=design&node-id=0%3A1&mode=design&t=rIuS1MoNBmvwylYb-1
## Historias do Sprint
1. Eu, como gerente do sistema, gostaria de adicionar disciplinas a serem avaliadas
    1. Criar tabela disciplinas no Banco de Dados [Kael]
    2. Criar funções de criar e remover disciplina no dominio [Lucas]
    3. Criar função adaptadora de 2. para 1 [Lucas]
    4. Criar página no front-end que chama a função de criar/remover disciplina [Wilgnert]
2. Eu, como aluno e usuário, gostaria de criar uma conta no sistema
    1. Criar tabela alunos no Banco de Dados [Kael]
    2. Criar funções para adicionar alunos no sistema no dominio [Lucas]
    3. Criar função adaptadora de 2. para 1 [Alefi]
    4. Criar página no front-end que chama a função de criar/remover disciplina [Wilgnert]
3. Eu, como gerente do sistema, gostaria de aceitar ou recusar o registro de um aluno
    1. Criar tabela a-serem-registrados [Kael]
    2. Criar funções para adicionar alunos a essa tabela [Kael]
    3. Criar funções para mover um aluno dessa tabela para a de alunos (registrados) [Alefi]
    4. Criar página no front-end que permite aceitar/recusar a entrada de um aluno [Wilgnert]
    5. Fazer com que a história 2. agora jogue alunos na tabela a-serem-registrados [Kael]
4. Eu, como aluno e usuário, gostaria de poder colocar a foto da minha carteira no sistema para ser validada (e como gerente ver essa imagem)
    1. Adicionar coluna de imagem para as tabelas a-serem-registrados e alunos [Kael]
    2. Criar funções para adicionar imagens no dominio e adaptadores [Alefi]
    3. Fazer com que o site mostre a imagem na tela da história 3. [Wilgnert]
5. Eu, como aluno e usuário, gostaria de votar em uma disciplina com a possibilidade de um comentário opcional
    1. Criar tabela de reviews no Banco de Dados e integrar ela com a de Disciplinas [Kael]
    2. Criar reviews no dominio [Lucas]
    3. Criar adaptador para criação de reviews. [Alefi]
    4. Criar pagina para criação de reviews. [Wilgnert]
6. Eu, como aluno e usuário, gostaria de pesquisar dentre as disciplinas existentes no sistema e ver seus reviews
    1. Criar função que retorna as disciplinas e os reviews do banco de dados [Lucas]
    2. Criar página de review de disciplinas com as reviews do BD [Wilgnert]
    3. Adicionar barra de pesquisa para as disciplinas [Alefi]
7. Eu, como gerente do sistema, gostaria de ter um login único e com privilegios maiores
    1. Criar tabela gerentes no Banco de Dados [Kael]
    2. Criar funções de adicionar e remover gerentes no back-end (exclusivo) [Kael]
    3. Permitir login por meio da tabela gerente [Lucas]
8. Eu, como aluno e usuário, gostaria de logar no sistema se minha conta for aceita ou ter um aviso que ela está pendente ou recusada
    1. Criar página para alunos que estão na tabela a-serem-registrados [Wilgnert]
    2. Mostrar aviso do status atual do aluno entre [rejeitado, em espera] caso aluno não esteja na tabela aluno. [Alefi]
    3. Permitir login de alunos na tabela a-serem-registrados [Lucas]

## Historias do Produto
1. Eu, como gerente do sistema, gostaria de adicionar disciplinas a serem avaliadas
2. Eu, como aluno e usuário, gostaria de criar uma conta no sistema
3. Eu, como gerente do sistema, gostaria de aceitar ou recusar o registro de um aluno
4. Eu, como aluno e usuário, gostaria de ver as disciplinas que ainda não votei
5. Eu, como aluno e usuário, gostaria de pesquisar dentre as disciplinas existentes no sistema
6. Eu, como aluno e usuário, gostaria de votar em uma disciplina com a possibilidade de um comentário opcional
7. Eu, como aluno e usuário, gostaria de votar se um comentário foi ou não útil
8. Eu, como moderador do sistema, gostaria de poder deletar comentários inadequados
9. Eu, como gerente do sistema, gostaria de ver a foto da carteira de um aluno antes de aceitar ou recusar sua inscrição
10. Eu, como aluno e usuário, gostaria de poder colocar a foto da minha carteira no sistema para ser validada
11. Eu, como gerente do sistema, gostaria de ver os alunos e disciplinas registradas no momento
12. Eu, como moderador do sistema, gostaria de ver os alunos que tiveram seus comentários deletados
13. Eu, como moderador do sistema, gostaria de poder banir alunos com comentários inadequados recorrentes
14. Eu, como gerente do sistema, gostaria de ter um login único e com privilegios maiores
15. Eu, como aluno e usuário, gostaria de logar no sistema se minha conta for aceita ou ter um aviso que ela está pendente ou recusada

