from langchain_groq import ChatGroq
import os
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.2-90b-text-preview")
# Directly specifying the API key in the code without using environment variables
llm = ChatGroq(groq_api_key="YOUR_API_KEY_HERE", model_name="llama-3.2-90b-text-preview")



if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)
