# PROJETO CALENDÁRIO DE ANIVERSÁRIOS

## 1 - Descrição
> Este projeto é um teste para uma vaga de Desenvolvedor Python/Django. Nele você, após
> cadastro, poderá registrar e gerenciar eventos de aniversário.

## 2 - Configurando e rodando o projeto

Para o correto funcionamento dos comandos abaixo é aconselhável:
- ter o Python >= 3.8 e o NPM >= 6.14.4 instalados;
- Criar e ativar um ambiente virtual;

  #### 2.1 - Instalando dependências Javascript
  Para o correto funcionamento do projeto, instale as dependência javascript e css através do comando
    
  <code>npm install</code>
  #### 2.2 - Instalando as dependências Python
  Para instalar as dependências Python é só rodar o comando a seguir
  
  <code>pip install -r requirements.txt</code>

  #### 2.3 - Rode as migrações
  <code>python manage.py migrate</code>

  #### 2.4 Sirva a aplicação
  <code>python manage.py runserver</code>

  #### Acesse o seu localhost na porta 8000
  <code>127.0.0.1:8000</code>

## 3 - Usando a Aplicação

Para criar eventos de aniversário é preciso registrar um usuário e logar no sistema. 
Após isso, basta clicar sobre o botão <button>+</button> no menu superior para criar 
o seu evento de aniversário. Também é possível criar ao clicar sobre uma data no calendário.

Para editar ou deletar um evento criado, basta clicar sobre ele.
