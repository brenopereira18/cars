# Create your views here.

from typing import Any
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from cars.models import Car
from cars.forms import CarModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# CLASS BASED VIEW

class CarsListView(ListView): #ListView é uma CBV genérica que facilita a exibição de listas de objetos de um determinado modelo.
    model = Car #Especifica o modelo Car que esta view vai listar. 
    template_name = 'cars.html' #Especifica o template HTML que será usado para renderizar a lista de carros.
    context_object_name = 'cars' #No template cars.html, você poderá acessar a lista de carros usando a variável cars.

    def get_queryset(self):
        cars = super().get_queryset().order_by('model') #Chama o método get_queryset da classe ListView, que por padrão retorna todos os objetos do modelo Car.
        search = self.request.GET.get('search') #request.GET é um dicionário que contém todos os parâmetros de consulta passados na URL, get('search') tenta pegar o valor associado à chave 'search' na URL
        if search:
            cars = cars.filter(model__icontains=search) #__contains verifica se a string search está contida dentro do valor do campo model. __icontains ignora se é letra maiuscula ou minuscula.
        return cars 
    
    
@method_decorator(login_required(login_url='login'), name='dispatch') #login_required: É um decorator do Django que restringe o acesso a uma view apenas para usuários que estão autenticados. login_url='login': Este argumento especifica a URL para onde o usuário será redirecionado caso ele não esteja autenticado. O dispatch identifica qual método HTTP (GET, POST, ...) está sendo usado na requisição. Com base no método HTTP da requisição, o dispatch invoca o método correspondente da classe (get, post, ...)
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/' #para qual url o usuário deve ser mandado quando realizar o cadastro.


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'    

    def get_success_url(self): #Este método é utilizado para definir a URL para a qual o usuário será redirecionado após a atualização bem-sucedida
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
        #reverse_lazy é uma função que gera a URL no momento em que for realmente necessário.
        #kwargs={'pk': self.object.pk}: Passa o argumento pk como um parâmetro para a URL. A self.object.pk obtém o valor da chave primária do objeto atualizado.


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'




# class NewCarView(View):

#     def get(self, request):
#         new_car_form = CarModelForm() #Cria uma instância vazia do formulário CarForm, que será enviada ao template para ser exibida ao usuário. Isso acontece quando o formulário é solicitado pela primeira vez.
#         return render(
#             request,
#             'new_car.html',
#             { 'new_car_form': new_car_form }
#         )

#     def post(self, request):
#         new_car_form = CarModelForm(request.POST, request.FILES) #request.POST: Contém os dados enviados pelo formulário, request.FILES: Contém os arquivos enviados pelo formulário  
#         if new_car_form.is_valid():
#             new_car_form.save() 
#             return redirect('cars_list') #Após salvar o novo carro, o usuário é redirecionado para uma outra página. Nesse caso, é redirecionado para a view associada à URL com o nome cars_list
#         return render(
#             request,
#             'new_car.html',
#             { 'new_car_form': new_car_form }
#         )
    

# class CarsView(View):

#    def get(self, request): #request é um objeto que representa a requisição HTTP feita pelo navegador.
#        cars = Car.objects.all().order_by('model') #Recupera todos os objetos da classe Car do banco de dados.
#        search = request.GET.get('search')      

#        if search:
#            cars = Car.objects.filter(model__icontains=search) 

#        return render(
#            request, 
#            'cars.html', 
#            {'cars': cars}
#        ) 
#render: É uma função fornecida pelo Django que simplifica o processo de carregar um template,preencher esse template com dados dinâmicos e retornar uma resposta HttpResponse.
# O primeiro parâmetro é o objeto request que representa a requisição HTTP recebida.
# O segundo parâmetro é o nome do arquivo de template que será usado para gerar a resposta. Nesse caso, cars.html é o nome do template.
    

# FUNCTION BASED VIEW

# def cars_view(request): 
#     cars = Car.objects.all().order_by('model') 
#     search = request.GET.get('search')#     

#     if search:
#         cars = Car.objects.filter(model__icontains=search)#         

#     return render(
#         request, 
#         'cars.html', 
#         {'cars': cars}
#     ) 
