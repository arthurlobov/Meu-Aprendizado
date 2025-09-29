# criar uma tabela

create table pessoas (
id int not null auto_increment, <!--Parametro, definição e preencfimento automatico / único -->
nome varchar(30) not null,
nascimento date, <!-- Parametros e definição--> 
sexo enum('M','F'),
peso decimal(5,2),
altura decimal(3,2),
nacionalidade varchar (20) default 'Brasil',
primary key (id)
) default charset = utf8mb3;
describe pessoas <!-- Escrever na tabela-->

# Inserir elementos na tabela

insert into pessoas <!-- inserir na tabela  -->
(nome,nascimento,sexo,peso,altura,nacionalidade) <!-- parametros  -->
values
('Arthur','2006-07-10','M','80.0','1.81','Brasil'); <!-- Valores -->

<!-- Simplificado -->
insert into pessoas values <!-- valores na mesma posição da tabela -->
(default,'Emylly','1999-12-16','F','72','1.76',default);

# Alterar dados da tabela

alter table pessoas <!-- Alterar tabela-->
add column profissao varchar(10); <!-- Adicionar coluna-->


# Selecionar dados da tabela




