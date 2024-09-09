from django.db import models

# Create your models here.

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model): # o nome da classe é qual será o nome da tabela
    id = models.AutoField(primary_key=True) #AutoField funciona como se fosse id SERIAL em sql
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # chave estrangeira que liga a tabela 'Brand'
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True) #blank e null -> campo pode ficar em branco ou ser null
    photo = models.ImageField(upload_to='cars/', blank=True, null=True) # upload_to passa o caminho das imagens quando for enviado a foto
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model
    

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add=True -> significa que a data e hora atuais serão automaticamente registradas quando um novo registro for criado

    class Meta: #A classe interna Meta permite definir metadados para o modelo.
        ordering = ['-created_at'] #indica que os registros devem ser ordenados de forma decrescente pela data de criação (created_at).

    def __str__(self): # determina a representação em string do objeto CarInventory.
        return f'{self.cars_count} - {self.cars_value}'