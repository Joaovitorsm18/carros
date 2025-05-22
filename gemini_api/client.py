import os
import google.generativeai as genai

def get_car_ia_bio(model, brand, year):
    prompt = """
    Me mostre uma descrição de venda para um carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo de carro. Descreva especificações
    """

    prompt = prompt.format(brand, model, year)
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text