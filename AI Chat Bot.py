import openai

# Set your OpenAI API key
openai.api_key = REPLACE THIS TEXT WITH API KEY #ATTENTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def ask_openai(prompt):
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",  
        prompt=prompt,
        max_tokens=150,  
        stop=None,  
        temperature=0.7,  
        top_p=1.0  
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to the OpenAI ChatBot!")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'exit':
            print("ChatBot: Goodbye!")
            break
        
        response = ask_openai(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
