# criar uma tabela

create table pessoas (
id int not null auto_increment, <!--Parametro, definição e preenchimento automatico-->
nome varchar(30) not null,
nascimento date, <!-- Parametros e definição--> 
sexo enum('M','F'),
peso decimal(5,2),
altura decimal(3,2),
nacionalidade varchar (20) default 'Brasil',
primary key (id)
) default charset = utf8mb3;
describe pessoas <!-- Escrever na tabela-->

create table if not exists curso ( <!-- criar tabela se ela não existe -->
id int not null auto_increment,
nome varchar(30) not null unique,  <!-- Obrigatório e único -->
descricao text,
carga int unsigned,
totaulas int,
ano year default '2016',
primary key (id) <!-- Chave primária -->
) default charset = utf8bm3;
# Inserir elementos na tabela

insert into pessoas <!-- inserir na tabela  -->
(nome,nascimento,sexo,peso,altura,nacionalidade) <!-- parametros  -->
values
('Arthur','2006-07-10','M','80.0','1.81','Brasil'); <!-- Valores -->

<!-- Simplificado -->
insert into pessoas values <!-- valores na mesma posição da tabela -->
(default,'Emylly','1999-12-16','F','72','1.76',default);

# Modificar elementos na tabela

update curso <!-- Altere o valor onde = ? -->
set nome = 'HTML5' where id = 1 <!-- set do valor -->
limit 1; <!-- Limita a quantidade de linhas que esse código pode atingir -->

delete from curso <!-- deletar linha -->
where id=8;

# Alterar dados da tabela

alter table pessoas <!-- Alterar tabela -->
add column profissao varchar(10); <!-- Adicionar coluna -->

alter table pessoas
drop column profissao; <!-- Deletar coluna -->

alter table pessoas
add column profissao varchar(10) after nome; <!-- Depois da coluna -->

alter table pessoas
add column profissao varchar(10) first; <!-- Primeira coluna -->

alter table pessoas
modify column profissao varchar(20) not null default ''; <!-- Modificar detalhes da coluna -->

alter table pessoas
change profissao prof varchar(20) not null default ''; <!-- Modificar nome e detalhes da coluna (obrigatótio) -->

alter table pessoas
rename to gafanhotos; <!-- Alterar nome da tabela -->

create table if not exists curso (
	nome varchar(30) not null unique,
    descricao text,
    carga int unsigned,
    totaulas int,
    ano year default '2016'
) default charset = utf8bm3;


# Selecionar dados da tabela




