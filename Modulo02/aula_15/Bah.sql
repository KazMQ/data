-- SELECT * FROM vendas2;

/*
SELECT produto, quantidadevendida
from vendas2
*/

/*
select Produto, Valor, DataVenda
from vendas2
where DataVenda >= '2024-05-01' and DataVenda <= '2024-12-01'
*/

select Produto, Valor, DataVenda, QuantidadeVendida
from vendas2
where DataVenda between '2024-09-15' and '2024-10-20'
and Categoria = 'Eletrônicos';