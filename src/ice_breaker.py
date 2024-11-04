import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")

information = """
    Darlington Nnam is a seasoned Blockchain Engineer and Entrepreneur. He's the co-founder of Horus Labs and The Garage.

    With a diverse set of Engineering skills, he's committed to building secure and innovative blockchain solutions to onboard more persons to web3.

    He's also a passionate and committed learner who believes that he can learn anything if he sets his mind to it.

    His favorite quote is "Dare to be different, the world is counting on it"!
"""

if __name__ == "__main__":
    print("hello langchain!")

    summary_template = """
            given the information {information} about a person from I want you to create:
            1. A short summary
            2. Two interesting facts about them
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})
    print(res)
