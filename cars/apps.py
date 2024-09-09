from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    def ready(self):
        import cars.signals
#O método ready() é usado para executar código de inicialização específico quando a aplicação Django está pronta. Esse método é particularmente útil quando você precisa configurar aspectos adicionais do aplicativo, como conectar sinais (signals) ou realizar outras tarefas que devem ocorrer quando a aplicação é carregada.