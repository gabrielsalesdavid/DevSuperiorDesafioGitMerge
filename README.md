Git – Comandos e Merge com conflito

![Git](image/image-1.png)


Git

Clicando com o botão direito do mouse selecione a opção:
“Open Git Bash here”.

![Open Git Bash here](image/image-1-1.png)


Git – git init

Dentro do terminal Git. Digite o seguinte comando:
“git init”.

Este comando seria para inicializar o Git.

![git init](image/image-2.png)


Git – git checkout

Após inicializar o Git. Digite o seguinte comando:
“git checkout -b main”.

Este comando seria para checar ou voltar ao Branch que deseja. Já o “-b” é a forma de criação de Branch. Ou seja, git crie uma branch(-b) “main”.

![git checkout](image/image-3.png)


Git – git remote add origin

Estando na branch main. Digite o seguinte comando:
“git remote add origin <git@github.com:user/repository>”

Este comando seria para adicionar o repositório remoto para o local.

![git remote add origin](image/image-4.png)


Git – git status

Após realizar um projeto ou alteração em seu repositório local. Sempre é necessário digitar o seguinte comando:
“git status”.
O comando “clear” é para limpeza do terminal. Este comando deriva-se do Linux!

Este comando verifica se há alguma informação alterada ou inserida no repositório local!

![git status](image/image-5.png)


Git – git add . & git commit -m

Após verificar se possui alguma informação no repositório local. Digite o seguinte comando no terminal:
“git add .”
&
“git commit -m <“Informativo sobre o que foi feito”>”.

Sempre seguindo essas sequências:
1 – “git add .”.
2 – “git commit -m”.
O comando “git add .”, seria para salvar as alterações do repositório local.
Já o comando “git commit -m”, seria para salvar as versões com as informações para o repositório remoto sobre o que foi feito.

![git add . & git commit -m](image/image-6.png)


Git – git log --oneline

Para verificar os commits feitos. Digite o seguinte comando:
“git log --oneline”.

Este comando seria para verificar os logs sobre os commits que foram feitos e que continua no repositório local.

![git log --oneline](image/image-7.png)


Git – git push -u origin main

Para o envio pela primeira vez do repositório local para o remoto. Digite o seguinte comando:
“git push -u origin main”.

Este comando seria para envios do repositório local para o remoto. Envia todos os dados realizados/alterados(commits).

![git push -u origin main](image/image-8.png)


Git – git pull origin main

Para atualizar o repositorio local. Digite o seguinte comando:
“git pull origin main”.

Este comando seria para trazer ou atualizar tudo que está no repositório remoto para o local.

![git pull origin main](image/image-9.png)


Git – git merge

Para unificar os dados de uma feature para o branch main. Digite o seguinte comando:
“git merge <feature>”.

Este comando unifica/atualiza todas as informações numa branch. Sempre fazemos um merge para o branch que não possui as informações. Ou seja, o branch criada após o main é o que terá as informações novas, assim pegamos esses dados e passamos para o branch que não possui, no caso o main.

![git merge](image/image-10.png)


Git – git remote -v & git remote rm origin

Para verificar uma branch remote ou deletar do repositório local. Digite o seguinte comando:
“git remote -v”.
&
“git remote rm origin”.

O comando: “git remote -v”, verifica em qual repositório remoto o Git está.
Já o comando: “git remote rm origin”, remove o repositório remoto do Git.

![git remote -v & git remote rm origin](image/image-11.png)


Git – git push -u origin <feature>

Para o envio do repositório local para o remoto. Digite o seguinte comando:
“git push -u origin <feature>”.

Este comando seria para envios do repositório local para o remoto. Envia todos os dados realizados/alterados(commits).

![git push -u origin <feature>](image/image-12.png)


Git – git clone

Para clonar o repositório remoto para o local. Digite o seguinte comando:
“git clone <git@github.com:user/repositorioremoto>”.

Este comando seria para envios do repositório local para o remoto. Envia todos os dados realizados/alterados(commits).

![git clone](image/image-13.png)


Git – Merge com conflito

Para realizar um merge da feature para o branch main. Digite o seguinte comando:
“git merge main”.

Este comando seria para mesclar os dados de uma feature que foi clonada e teve dados inseridos sem que a pessoa saiba ou possa ter esquecido sobre os dados a mais no repositório remoto.

![Merge com conflito](image/image-14.png)