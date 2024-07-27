import getpass
import os
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv('./.env')

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0 , openai_api_key=os.getenv("openai_api_key"))

prompt = """
Ты помощник по поиску сожителей.Я тебе дам Три вопроса и Три ответа на них от пользователя.Твоя задача в том чтобы проанолизировать эти ответы и выбрать Y или N на каждый ответ
Три вопроса:
Первый вопрос: Употребляете ли вы алкоголь и курите ли? Как вы относитесь к тому, если ваш сожитель будет курить или употреблять алкоголь?
Второй вопрос: Являетесь ли вы верующим человеком? Какое отношение у вас к вере и религиозным практикам? Важно ли для вас, чтобы ваш сожитель разделял ваши религиозные убеждения?
Третий вопрос: Как часто вы убираетесь и поддерживаете чистоту в доме? Как вы относитесь к беспорядку и насколько важно для вас, чтобы ваш сожитель был аккуратен и чистоплотен?
Инструкция как выбрать Y или N:
Первый вопрос: Если пользователь ответил что он курит/употребляет алкоголь или нормально относиться к тому что сожитель курит/употребляет алкоголь ответ должен быть N.Если пользователь ответил что он НЕ курит/употребляет алкоголь или плохо относиться к тому что сожитель курит/употребляет алкоголь ответ должен быть Y.
Второй вопрос: Если пользователь ответил что он религиозный и он хочет чтобы сожител разделял его религиозные убеждения то ответ должет быть N.Если пользователь не религиозный или нормально относиться ко всем вероисповеданиям то ответ должен быть Y.
Третий вопрос: Если пользователь ответил что он нормально относиться к беспорядку или он не чистоплотный то ответ должен быть N.Если пользователь чистоплотный и отрицательно относиться к беспорядку ответ должен быть Y.
Если по ответу не возможно понять Y или N от ответ должен быть Y.
В конце у тебя должно получиться последовательность из трех букв. К примеру: YYN,YNY и так далее

Важно: верни мне только последовательность из трех букв

Ответы от пользователя:
"""

def get_preference(preference: str) -> str:
    modal = prompt + preference
    response = model.invoke(modal)
    return response.content