from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum
from gemini_api.client import get_car_ai_description


def car_inventory_update():
    cars_count = Car.objects.all().count() #Armazena o número total de carros no banco de dados.
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    #Usando a função de agregação Sum, calcula a soma de todos os valores do campo value para todos os carros na tabela Car. Acessa o valor agregado diretamente. O resultado de aggregate() é um dicionário, e aqui estamos acessando o valor associado à chave total_value.

    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    ) #Cria um novo registro na tabela CarInventory com os valores de cars_count e cars_value.


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs): 
   car_inventory_update() 


#@receiver: Esse é um decorador que conecta uma função a um sinal específico.
#post_delete: Este é o sinal que é enviado imediatamente após a exclusão de um objeto.
#sender=Car: Especifica que o sinal post_delete deve ser capturado quando ele for emitido por objetos do modelo Car.
@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
#sender: Representa o modelo que emitiu o sinal. Neste caso, é o modelo Car.
#instance é o próprio objeto que está sendo referenciado.
#**kwargs: Permite capturar argumentos adicionais passados pelo sinal, embora eles não estejam sendo usados nesta função.
    

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.description:
        ai_description = get_car_ai_description(instance.model, instance.brand, instance.model_year)
        instance.description = ai_description