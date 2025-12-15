# Projeto de Herança de Templates com Jinja2

Este é um projeto demonstrativo que ilustra o uso de herança de templates com Jinja2, utilizando Python puro e o framework CSS PicoCSS.

## Sobre o Projeto

O projeto demonstra conceitos fundamentais de templates em Python:

- **Herança de Templates**: Uso de templates base para manter consistência visual
- **Reutilização de Componentes**: Includes para elementos comuns como navbar
- **Renderização Dinâmica**: Passagem de variáveis do Python para os templates
- **Estilização Moderna**: Uso do PicoCSS no modo light para um design limpo e responsivo

## Estrutura do Projeto

```
./
├── app.py                      # Servidor HTTP com Jinja2
├── README.md                   # Este arquivo
└── templates/
    ├── base.html               # Template base com estrutura HTML
    ├── index.html              # Página inicial com boas-vindas e vídeos
    ├── about.html              # Página sobre o canal Regis do Python
    ├── templates.html          # Página sobre herança de templates
    └── includes/
        └── navbar.html         # Menu de navegação reutilizável
```

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação
- **Jinja2**: Motor de templates para Python
- **http.server**: Servidor HTTP embutido no Python
- **PicoCSS**: Framework CSS minimalista e responsivo

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. Clone ou baixe este repositório

```bash
git clone https://github.com/rg3915/heranca-templates-python.git
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv .venv
```

3. Ative o ambiente virtual:

**Linux/Mac:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

4. Instale as dependências:
```bash
pip install jinja2
```

5. Execute o servidor:
```bash
python app.py
```

6. Acesse no navegador:
```
http://localhost:8000
```

## Páginas Disponíveis

- **/** - Página inicial com boas-vindas e vídeos sobre Django
- **/templates** - Explicação detalhada sobre herança de templates com Jinja2
- **/sobre** - Página sobre o canal Regis do Python

## Funcionalidades do Jinja2 Demonstradas

### 1. Herança de Templates
```jinja2
{% extends "base.html" %}
```

### 2. Blocos de Conteúdo
```jinja2
{% block title %}Meu Título{% endblock %}
{% block content %}Meu conteúdo{% endblock %}
```

### 3. Includes
```jinja2
{% include 'includes/navbar.html' %}
```

### 4. Variáveis
```jinja2
{{ nome }}
{{ item.titulo }}
```

### 5. Estruturas de Controle
```jinja2
{% for item in items %}
    {{ item.titulo }}
{% endfor %}
```

## Sobre o Canal Regis do Python

Este projeto foi criado seguindo os conceitos ensinados no canal **Regis do Python**, um canal dedicado ao ensino de Python e Django.

- YouTube: [RegisdoPython](https://www.youtube.com/c/RegisdoPython)

## Licença

Este projeto é livre para uso educacional e demonstrativo.

## Contribuições

Sinta-se à vontade para fazer fork, melhorar e compartilhar este projeto.
