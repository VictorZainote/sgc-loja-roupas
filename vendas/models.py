from django.db import models, transaction

from clientes.models import Cliente
from produtos.models import Produto


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} - {self.produto} ({self.quantidade})"

    def save(self, *args, **kwargs):
        with transaction.atomic():
            venda_anterior = None

            if self.pk:
                venda_anterior = Venda.objects.select_related("produto").get(pk=self.pk)

            if venda_anterior and venda_anterior.produto_id == self.produto_id:
                estoque_disponivel = self.produto.quantidade_estoque + venda_anterior.quantidade

                if estoque_disponivel < self.quantidade:
                    raise ValueError("Estoque insuficiente")

                self.produto.quantidade_estoque = estoque_disponivel - self.quantidade
                self.produto.save()
            else:
                if venda_anterior:
                    venda_anterior.produto.quantidade_estoque += venda_anterior.quantidade
                    venda_anterior.produto.save()

                if self.produto.quantidade_estoque < self.quantidade:
                    raise ValueError("Estoque insuficiente")

                self.produto.quantidade_estoque -= self.quantidade
                self.produto.save()

            self.valor_total = self.produto.preco * self.quantidade
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        with transaction.atomic():
            self.produto.quantidade_estoque += self.quantidade
            self.produto.save()
            return super().delete(*args, **kwargs)
