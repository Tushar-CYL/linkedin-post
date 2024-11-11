from langchain_groq import ChatGroq
import os
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.2-90b-text-preview")
# Directly specifying the API key in the code without using environment variables
llm = ChatGroq(groq_api_key="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", model_name="llama-3.2-90b-text-preview")



if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)
