import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import scrape_linkedin_profile
from tool.tools import get_profile_url_tavily

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    print("hello langchain!")

    summary_template = """
            given the LinkedIn information {information} about a person from I want you to create:
            1. A short summary
            2. Two interesting facts about them
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    # llm = ChatOllama(model="llama3.2")
    chain = summary_prompt_template | llm | StrOutputParser()

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/nnamdarlington/")
    res = chain.invoke(input={"information": linkedin_data})
    print(get_profile_url_tavily("Darlington Nnam"))
