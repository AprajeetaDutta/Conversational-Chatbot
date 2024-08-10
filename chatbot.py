import os
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

class ChatBot:
    def __init__(self):
        openai_api_key = os.getenv('OPENAI_API_KEY')
        if not openai_api_key:
            raise ValueError("OpenAI API key is missing")

        self.llm = OpenAI(api_key=openai_api_key)
        self.prompt = PromptTemplate(
            input_variables=["question"],
            template="You are a helpful assistant. Answer the following question: {question}"
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def ask(self, question):
        return self.chain.run(question)

if __name__ == "__main__":
    bot = ChatBot()
    while True:
        user_input = input("You: ")
        response = bot.ask(user_input)
        print(f"Bot: {response}")
