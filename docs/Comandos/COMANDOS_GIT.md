# Referência Completa de Comandos Git

## 🎯 Comandos Essenciais

### git init
Inicializa um novo repositório Git local.

```bash
git init
```

**Quando usar**: Quando você quer começar a versionar um projeto novo  
**Resultado**: Cria um diretório `.git` com a estrutura necessária

---

### git config
Configura informações do usuário Git.

```bash
# Configuração global
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"

# Configuração local (apenas para esse repositório)
git config user.name "Seu Nome"
git config user.email "seu.email@example.com"

# Listar configurações
git config --list
```

**Dica**: Configure globalmente uma vez e use localmente quando precisar de sobrescrita

---

### git status
Mostra o status atual do repositório.

```bash
git status

# Versão mais compacta
git status -s
```

**O que mostra**:
- Arquivos não rastreados (Untracked)
- Arquivos modificados mas não preparados
- Arquivos preparados para commit
- Branch atual

---

### git add
Adiciona alterações à staging area.

```bash
# Adicionar um arquivo específico
git add nome-arquivo.txt

# Adicionar todos os arquivos
git add .

# Adicionar com padrão
git add *.html

# Adicionar interativamente (escolher qual alteração adicionar)
git add -p
```

**Staging Area**: Área intermediária onde você prepara o que vai para o próximo commit

---

### git commit
Registra as alterações no repositório.

```bash
# Commit simples
git commit -m "Descrição do commit"

# Commit com descrição detalhada
git commit -m "Título do commit" -m "Descrição detalhada das alterações"

# Adicionar e fazer commit simultaneamente
git commit -am "Descrição" # (apenas arquivos já rastreados)

# Alterar o último commit
git commit --amend -m "Nova mensagem"

# Commit sem alterações (útil para triggerar CI/CD)
git commit --allow-empty -m "Commit vazio"
```

**Boas Práticas de Mensagem**:
- Comece com verbo (Adiciona, Corrige, Remove)
- Use presente
- Seja específico
- Máximo 50 caracteres na primeira linha

---

### git log
Exibe o histórico de commits.

```bash
# Histórico completo
git log

# Uma linha por commit
git log --oneline

# Últimos N commits
git log -n 5

# Com estatísticas
git log --stat

# Com diferenças
git log -p

# Gráfico de branches
git log --graph --oneline --all

# Filtrar por autor
git log --author="Gabriel"

# Filtrar por data
git log --since="2025-01-01" --until="2025-12-31"

# Buscar por mensagem
git log --grep="feature"
```

---

### git diff
Mostra diferenças entre versões.

```bash
# Diferenças não preparadas (entre working e staging)
git diff

# Diferenças preparadas (entre staging e último commit)
git diff --cached
# ou
git diff --staged

# Diferenças entre branches
git diff main feature

# Diferenças entre commits específicos
git diff abc123 def456

# Mostrar apenas nomes de arquivos alterados
git diff --name-only
```

---

## 🌿 Comandos de Branch

### git branch
Gerencia branches.

```bash
# Listar branches locais
git branch

# Listar todas as branches (local e remota)
git branch -a

# Listar com últimos commits
git branch -v

# Criar nova branch
git branch nome-da-branch

# Deletar branch
git branch -d nome-da-branch

# Forçar deleção
git branch -D nome-da-branch

# Renomear branch
git branch -m nome-antigo nome-novo

# Criar branch a partir de um commit específico
git branch nome-branch abc123def
```

**Convenção de Nomes**:
- `feature/nome-feature`
- `bugfix/nome-bug`
- `hotfix/nome-hotfix`
- `release/versao`

---

### git checkout
Muda para uma branch ou restaura arquivos.

```bash
# Mudar para uma branch existente
git checkout nome-da-branch

# Criar e mudar para nova branch
git checkout -b nome-da-branch

# Restaurar arquivo para o estado do último commit
git checkout -- nome-arquivo.txt

# Restaurar para um commit específico
git checkout abc123def

# Voltar para branch anterior
git checkout -
```

### git switch (alternativa moderna)
Comando mais novo e intuitivo para trocar branches.

```bash
# Mudar de branch
git switch nome-da-branch

# Criar e mudar para nova branch
git switch -c nome-da-branch

# Voltar para branch anterior
git switch -
```

---

## 🔀 Merge e Rebase

### git merge
Combina branches.

```bash
# Fazer merge de uma branch na atual
git merge nome-da-branch

# Merge sem criar commit de merge
git merge --squash nome-da-branch

# Merge especificando estratégia
git merge -s recursive nome-da-branch

# Abortar um merge em progresso
git merge --abort
```

**Tipos de Merge**:
1. **Fast-Forward**: Move o apontador quando possível
2. **Three-Way Merge**: Cria commit de merge quando necessário

---

### git rebase
Reaplica commits em outra base.

```bash
# Rebase na branch main
git rebase main

# Rebase interativo dos últimos 3 commits
git rebase -i HEAD~3

# Opções no rebase interativo:
# pick   - usar commit
# reword - usar mas editar mensagem
# squash - combinar com anterior
# drop   - deletar

# Abortar rebase
git rebase --abort
```

⚠️ **Cuidado**: Não faça rebase em commits já enviados (push)

---

## 📤 Comandos Remotos

### git remote
Gerencia repositórios remotos.

```bash
# Listar repositórios remotos
git remote

# Listar com URLs
git remote -v

# Adicionar novo remoto
git remote add origin https://github.com/usuario/repo.git

# Alterar URL de um remoto
git remote set-url origin https://github.com/novo-usuario/repo.git

# Ver detalhes de um remoto
git remote show origin

# Remover remoto
git remote remove origin

# Renomear remoto
git remote rename origin novo-nome
```

---

### git push
Envia commits para o repositório remoto.

```bash
# Push da branch atual
git push

# Push para remoto e branch específicos
git push origin main

# Push de todas as branches
git push origin --all

# Push de tags
git push origin --tags

# Deletar branch remota
git push origin --delete nome-branch

# Forçar push (usar com cuidado!)
git push origin main --force

# Push com tracking automático
git push -u origin nome-branch
```

---

### git pull
Obtém e integra alterações do repositório remoto.

```bash
# Pull padrão (fetch + merge)
git pull

# Pull especificando branch
git pull origin main

# Pull com rebase (em vez de merge)
git pull --rebase

# Pull sem fazer integração automática
git fetch
```

**Diferença**:
- `git pull` = `git fetch` + `git merge`
- `git pull --rebase` = `git fetch` + `git rebase`

---

### git fetch
Obtém atualizações do repositório remoto sem integrar.

```bash
# Fetch de todos os remotos
git fetch

# Fetch de um remoto específico
git fetch origin

# Fetch de branch específica
git fetch origin main

# Fetch de todas as branches
git fetch --all
```

---

## 📋 Comandos de Histórico e Desfazer

### git reset
Desfaz commits mas mantém/remove alterações.

```bash
# Desfaz último commit, mantendo alterações no staging
git reset --soft HEAD~1

# Desfaz último commit, mantendo alterações no working directory
git reset --mixed HEAD~1
# ou
git reset HEAD~1

# Desfaz último commit, descartando alterações
git reset --hard HEAD~1

# Resetar arquivo específico
git reset HEAD nome-arquivo.txt

# Resetar para commit específico
git reset abc123def
```

**Modos**:
- `--soft`: Mantém alterações staged
- `--mixed`: Mantém alterações no working directory
- `--hard`: Remove todas as alterações

---

### git revert
Cria novo commit desfazendo alterações.

```bash
# Reverter último commit
git revert HEAD

# Reverter commit específico
git revert abc123def

# Reverter sem criar commit
git revert -n abc123def
```

**Diferença com reset**:
- `reset`: Apaga histórico (não use em commits já enviados)
- `revert`: Cria novo commit desfazendo (seguro para histórico compartilhado)

---

### git restore
Restaura arquivos (Git 2.23+).

```bash
# Descartar alterações no working directory
git restore nome-arquivo.txt

# Remover do staging
git restore --staged nome-arquivo.txt

# Restaurar para commit específico
git restore --source=abc123def nome-arquivo.txt
```

---

## 🏷️ Tags

### git tag
Cria referências nominadas para commits específicos.

```bash
# Criar tag leve
git tag v1.0.0

# Criar tag anotada
git tag -a v1.0.0 -m "Versão 1.0.0"

# Listar tags
git tag

# Listar com padrão
git tag -l "v1.*"

# Ver detalhes de tag
git show v1.0.0

# Deletar tag local
git tag -d v1.0.0

# Deletar tag remota
git push origin --delete v1.0.0

# Fazer push de tags
git push origin v1.0.0

# Push de todas as tags
git push origin --tags
```

---

## 🛠️ Comandos Úteis

### git stash
Salva alterações temporariamente.

```bash
# Guardar alterações
git stash

# Guardar com mensagem
git stash save "descrição"

# Listar stashes
git stash list

# Aplicar último stash
git stash apply

# Aplicar e remover stash
git stash pop

# Remover stash específico
git stash drop stash@{0}

# Remover todos os stashes
git stash clear

# Ver diferenças do stash
git stash show
```

---

### git clean
Remove arquivos não rastreados.

```bash
# Ver o que seria removido (dry-run)
git clean -n

# Remover arquivos não rastreados
git clean -f

# Remover arquivos e diretórios
git clean -fd

# Remover arquivos ignorados também
git clean -fdx

# Modo interativo
git clean -i
```

---

### git cherry-pick
Aplica commits específicos na branch atual.

```bash
# Aplicar commit único
git cherry-pick abc123def

# Aplicar múltiplos commits
git cherry-pick abc123def def456ghi

# Aplicar intervalo de commits
git cherry-pick abc123def..def456ghi

# Continuar após resolver conflitos
git cherry-pick --continue

# Abortar
git cherry-pick --abort
```

---

### git blame
Mostra quem modificou cada linha.

```bash
# Ver autor de cada linha
git blame nome-arquivo.txt

# Ver com data
git blame -L 10,20 nome-arquivo.txt

# Formato customizado
git blame --date=short nome-arquivo.txt
```

---

### git bisect
Encontra commit que introduziu um bug.

```bash
# Iniciar
git bisect start

# Marcar commit problemático
git bisect bad

# Marcar commit correto
git bisect good abc123def

# Git divide o intervalo automaticamente
# Após testar, marque como good ou bad

# Finalizar
git bisect reset
```

---

## 🚨 Resolução de Conflitos

Quando há conflito no merge:

```bash
# 1. Ver status
git status

# 2. Abrir arquivo e resolver manualmente
# Procure por:
# <<<<<<< HEAD (sua versão)
# =======
# >>>>>>> branch-name (outra versão)

# 3. Escolher uma versão e remover marcadores

# 4. Adicionar e fazer commit
git add .
git commit -m "Resolve conflito de merge"

# Ou abortar se precisar
git merge --abort
```

---

## 📊 Combinações Úteis

```bash
# Ver últimos commits com gráfico
git log --graph --oneline --decorate --all

# Ver alterações não enviadas
git log origin/main..main

# Verificar antes de push
git diff origin/main main

# Listar arquivos alterados no último commit
git diff-tree --no-commit-id --name-only -r HEAD

# Ver todos os commits hoje
git log --since="00:00:00" --oneline

# Copiar hash do último commit
git rev-parse HEAD
```

---

## 💡 Dicas de Produtividade

1. **Alias úteis**:
```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --graph --oneline --decorate --all'
```

2. **Verificar antes de enviar**:
```bash
git diff origin/main main
```

3. **Desfazer último push** (use com cuidado):
```bash
git push origin main --force
```

---

## 📚 Recursos

- [Documentação Oficial Git](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com)
- [Pro Git Book](https://git-scm.com/book)

---

**Autor**: Gabriel Sales David  
**Data**: 20 de novembro de 2025  
**Versão**: 1.0
