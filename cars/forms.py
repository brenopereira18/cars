from django import forms
from cars.models import Brand, Car


class CarModelForm(forms.ModelForm): #forms.ModelForm: É uma classe fornecida pelo Django que facilita a criação de formulários baseados em modelos. Um ModelForm automaticamente gera campos de formulário com base nos campos de um modelo Django.
    class Meta: #Meta: Esta classe define as configurações que indicam ao Django qual modelo o formulário está representando e quais campos devem ser incluídos no formulário.
        model = Car #Indica que este ModelForm está associado ao modelo Car.
        fields = '__all__' #'__all__': Informa ao Django para incluir todos os campos do modelo Car no formulário.

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$20.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não é possível cadastrar carros fabricados antes de 1975')
        return factory_year


# MÈTODO TRABALHOSO
                
# class CarForm(forms.Form):
#     model = forms.CharField(max_length=200)
#     brand = forms.ModelChoiceField(Brand.objects.all()) #ModelChoiceField significa que o campo é uma lista de opções
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     value = forms.FloatField()
#     photo = forms.ImageField()

#     def save(self): #self: Refere-se à instância do formulário.
#         #cleaned_data é um dicionário que contém os dados do formulário que passaram pelas validações.
#         car = Car(
#             model = self.cleaned_data['model'],
#             brand = self.cleaned_data['brand'],
#             factory_year = self.cleaned_data['factory_year'],
#             model_year = self.cleaned_data['model_year'],
#             plate = self.cleaned_data['plate'],
#             value = self.cleaned_data['value'],
#             photo = self.cleaned_data['photo'],
#         )
#         car.save() #Salva a instância car no banco de dados. Isso cria um novo registro na tabela correspondente ao modelo Car.
#         return car