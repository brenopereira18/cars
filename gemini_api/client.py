import google.generativeai as genai
import os 
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_car_ai_description(brand, car_model, year):
    model = genai.GenerativeModel("gemini-1.5-flash")    
   
    response = model.generate_content(  
        f"Me mostre uma descrição de venda para o carro {brand} {car_model} {year} em apenas 250 caracteres. Fale coisas específicas desse modelo. Descreva especificações técnicas desse modelo de carro.",        
        generation_config=genai.types.GenerationConfig(
            max_output_tokens=300  
        )
    )    
    return response.text 
