from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm() #UserCreationForm: É um formulário fornecido pelo Django para facilitar o processo de criação de novos usuários.
    return render(
        request,
        'register.html',
        {'user_form': user_form}
    )

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"] #Extrai o valor do campo "username" do formulário submetido.
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password) #authenticate: Verifica as credenciais e, se forem válidas, retorna um objeto User. Se não forem válidas, retorna None.
        if user is not None:
            login(request, user) #Se a autenticação for bem-sucedida, a função login do Django é chamada para autenticar o usuário na sessão.
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm() #AuthenticationForm: É um formulário fornecido pelo Django para facilitar o processo de login dos usuários.
    return render(
        request,
        'login.html',
        {'login_form': login_form}
    )

def logout_view(request):
    logout(request) #Ela encerra a sessão do usuário, removendo todos os dados relacionados à sessão. Isso efetivamente "desloga" o usuário, ou seja, o usuário não está mais autenticado no sistema.
    return redirect('cars_list')