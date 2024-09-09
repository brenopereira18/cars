import google.generativeai as genai
import os # Biblioteca nativa do Python para interagir com o sistema operacional. 

#genai.configure(api_key=...): Configura o cliente da API com a chave de API fornecida. Isso é necessário para autenticar e autorizar as solicitações à API do Google Generative AI.
#os.environ.get("GOOGLE_API_KEY"): Obtém o valor da variável de ambiente GOOGLE_API_KEY
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))


def get_car_ai_description(brand, car_model, year):
    #genai.GenerativeModel("gemini-1.5-flash"): Cria uma instância do modelo generativo chamado "gemini-1.5-flash". Este é um modelo pré-treinado oferecido pela API que será usado para gerar o conteúdo desejado.
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    #model.generate_content(...): Utiliza o modelo generativo para criar conteúdo baseado no prompt fornecido.
    response = model.generate_content(  
        f"Me mostre uma descrição de venda para o carro {brand} {car_model} {year} em apenas 250 caracteres. Fale coisas específicas desse modelo. Descreva especificações técnicas desse modelo de carro.",
        #Define as configurações de geração de conteúdo:
        generation_config=genai.types.GenerationConfig(
            max_output_tokens=300  # Ajusta o número máximo de tokens
        )
    )
    #Retorna o texto gerado
    return response.text 
