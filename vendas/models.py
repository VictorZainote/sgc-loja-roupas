from django.db import models
from produtos.models import Produto
from clientes.models import Cliente

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if self.produto.quantidade_estoque < self.quantidade:
            raise ValueError("Estoque insuficiente")

        self.valor_total = self.produto.preco * self.quantidade

        self.produto.quantidade_estoque -= self.quantidade
        self.produto.save()

        super().save(*args, **kwargs)