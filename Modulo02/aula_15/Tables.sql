-- select * from tb_emprestimos
-- select * from tb_usuarios
-- select * from tb_itens_emprestados
-- select * from tb_livros

/* Ajuste de tabela
Alter table tb_usuarios
Modify Column id_usuario int not null auto_increment,
ADD PRIMARY KEY (id_usuario); 

alter table tb_livros
modify column id_livro int not null auto_increment,
add primary key (id_livro);

alter table tb_emprestimos
modify column id_emprestimo int not null auto_increment,
add primary key (id_emprestimo);

alter table tb_itens_emprestados
modify column id_item int not null auto_increment,
add primary key (id_item);
*/

-- Chaves Estrangeiras
/*
ALTER TABLE tb_emprestimos
ADD CONSTRAINT fk_usuario
FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id_usuario);
*/
/*
ALTER TABLE tb_itens_emprestados
ADD CONSTRAINT fk_livro
FOREIGN KEY (id_livro) REFERENCES tb_livros(id_livro);
*/
/*
ALTER TABLE tb_itens_emprestados
ADD CONSTRAINT fk_emprestimo
FOREIGN KEY (id_emprestimo) REFERENCES tb_emprestimos(id_emprestimo);
*/

-- Fim do Relacionamento
/*
Select tb_livros.titulo
from tb_livros, tb_itens_emprestados
where tb_livros.id_livro = tb_itens_emprestados.id_livro
*/

-- Mostrar a data de cada empréstimo e o nome de livros emprestados
/*
Select tb_emprestimos.data_emprestimo, tb_livros.titulo
from tb_emprestimos, tb_itens_emprestados, tb_livros
where tb_emprestimos.id_emprestimo = tb_itens_emprestados.id_emprestimo
and tb_livros.id_livro = tb_itens_emprestados.id_livro;
*/
-- Quais livros foram emprestados no dia 15/10/2024

/*
Select tb_livros.titulo
from tb_livros, tb_itens_emprestados, tb_emprestimos
where tb_livros.id_livro = tb_itens_emprestados.id_livro
and tb_emprestimos.id_emprestimo = tb_itens_emprestados.id_emprestimo
and tb_emprestimos.data_emprestimo = '2024-10-15';
*/

-- Exemplos de Join
/*
SELECT 
  tb_usuarios.nome,
  tb_emprestimos.data_emprestimo
FROM 
  tb_usuarios
JOIN 
  tb_emprestimos ON tb_usuarios.id_usuario = tb_emprestimos.id_usuario;
*/

-- TOTALIZAR OS VALORES POR EMPRÉSTIMO E MOSTRAR OS IDS DOS EMPRÉSTIMOS

SELECT 
  tb_itens_emprestados.id_emprestimo,
  SUM(tb_livros.valor_emprestimo) AS total_emprestimo
FROM 
  tb_itens_emprestados
JOIN 
  tb_livros ON tb_itens_emprestados.id_livro = tb_livros.id_livro
GROUP BY 
  tb_itens_emprestados.id_emprestimo
ORDER BY 
  tb_itens_emprestados.id_emprestimo;
