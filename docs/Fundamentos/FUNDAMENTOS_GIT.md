# Fundamentos do Git

## 📖 O que é Git?

Git é um **sistema de controle de versão distribuído** que permite rastrear alterações no código-fonte ao longo do tempo. Desenvolvido por Linus Torvalds em 2005, Git se tornou o padrão da indústria para versionamento de software.

### Características Principais

- **Distribuído**: Cada desenvolvedor tem uma cópia completa do repositório
- **Rápido**: Operações locais são muito rápidas
- **Seguro**: Usa hash SHA-1 para garantir integridade
- **Flexível**: Suporta múltiplos fluxos de trabalho
- **Confiável**: Dados nunca são perdidos

## 🏗️ Conceitos Fundamentais

### Repository (Repositório)

Um repositório é o local onde todo o histórico de versões do projeto é armazenado. Pode ser:

- **Local**: Armazenado na máquina do desenvolvedor
- **Remoto**: Armazenado em um servidor (como GitHub)

### Commit

Um commit é um "snapshot" do projeto em um momento específico. Cada commit contém:
- Hash SHA-1 (identificador único)
- Autor e data
- Mensagem descritiva
- Referência ao commit anterior (parent)

```
commit abc123def456
Author: Gabriel Sales <email@example.com>
Date:   Wed Nov 20 10:30:00 2025

    Adiciona fundamentos do Git
```

### Branch (Ramificação)

Uma branch é uma linha independente de desenvolvimento. Permite trabalhar em features sem afetar o código principal.

```
        feature/nova-funcionalidade
             |
        -----|-----
       /      
main  ------
       \
        bugfix/corrigir-erro
```

**Branch padrão**: `main` (anteriormente `master`)

### Staging Area (Área de Preparação)

É um intermediário entre o diretório de trabalho e o repositório. Permite escolher quais alterações vão para o próximo commit.

```
Working Directory  →  Staging Area  →  Repository
    (modificado)     (preparado)       (confirmado)
```

### HEAD (Cabeça)

É um apontador que indica em qual branch/commit você está trabalhando atualmente.

## 🔄 Fluxo de Trabalho Git

```
1. Modificar arquivos no Working Directory
   ↓
2. git add (transferir para Staging Area)
   ↓
3. git commit (confirmar no Repository)
   ↓
4. git push (enviar para repositório remoto)
```

### Estados dos Arquivos

Um arquivo pode estar em um de três estados:

| Estado | Descrição |
|--------|-----------|
| **Untracked** | Arquivo novo, não rastreado pelo Git |
| **Staged** | Arquivo preparado para commit (git add) |
| **Committed** | Arquivo confirmado no repositório |

## 🌳 Estrutura Interna do Git

### Objetos Git

Git armazena 4 tipos de objetos:

1. **Blob**: Conteúdo de um arquivo
2. **Tree**: Estrutura de diretórios
3. **Commit**: Um commit do repositório
4. **Tag**: Uma referência a um commit específico

### Diretório .git

Quando você inicializa um repositório (`git init`), é criado um diretório `.git` com:

```
.git/
├── objects/       # Armazena blobs, trees, commits
├── refs/          # Referências a commits (branches, tags)
├── HEAD           # Aponta para a branch atual
├── config         # Configurações do repositório
└── logs/          # Histórico de referências
```

## 🔐 Segurança e Integridade

Git usa **SHA-1 hashing** para garantir que dados não sejam alterados:

```
Qualquer alteração no arquivo
         ↓
Hash SHA-1 muda
         ↓
Git detecta inconsistência
```

## 🌐 Repositórios Remotos

Um repositório remoto é uma cópia do repositório em um servidor (GitHub, GitLab, Bitbucket, etc.).

### Origin

`origin` é o nome padrão do repositório remoto principal:

```bash
git remote add origin https://github.com/usuario/repositorio.git
```

## 📊 Tipos de Merge

### Fast-Forward Merge

Quando a branch está adiante de main, o merge é direto:

```
feature  ----C1--C2
                 /
main  ----C0----
```

### Three-Way Merge

Quando ambas as branches têm commits, Git cria um novo commit:

```
feature  ----C1--C2
            /      \
main  ----C0------C3 (merge commit)
            \    /
hotfix       --C2'
```

## ⚠️ Conflitos de Merge

Conflitos ocorrem quando a mesma linha foi alterada em branches diferentes:

```
<<<<<<< HEAD
código da main
=======
código da feature
>>>>>>> feature
```

**Resolução**: Editar manualmente o arquivo e escolher qual versão manter.

## 💡 Boas Práticas

1. **Commits Frequentes**: Faça commits pequenos e com propósito
2. **Mensagens Claras**: Descreva o que foi alterado e por quê
3. **Branches Significativas**: Use nomes descritivos (feature/login, bugfix/erro-404)
4. **Sempre Sincronize**: Faça pull antes de começar a trabalhar
5. **Revise Antes de Fazer Push**: Verifique as alterações com git diff

## 🎯 Modelo de Branching Comum

```
main (produção)
  ↓
develop (desenvolvimento)
  ├─ feature/nova-funcionalidade
  └─ bugfix/corrigir-erro
```

## 📚 Próximas Etapas

Consulte [COMANDOS_GIT.md](COMANDOS_GIT.md) para uma referência completa de todos os comandos Git disponíveis.

---

**Autor**: Gabriel Sales David  
**Data**: 20 de novembro de 2025
