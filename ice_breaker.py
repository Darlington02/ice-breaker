import os
from typing import Tuple
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import summary_parser, Summary

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")

def ice_break_with(name: str) -> Tuple:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)

    summary_template = """
            given the LinkedIn information {information} about a person from I want you to create:
            1. A short summary
            2. Two interesting facts about them

            \n{format_instructions}
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        template=summary_template, 
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template | llm | summary_parser

    res: Summary = chain.invoke(input={"information": linkedin_data})
    return res, linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    print("Ice breaker!")
    ice_break_with(name="Darlington Nnam")
    
