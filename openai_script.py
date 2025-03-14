from openai import OpenAI

# Correctly assigning the API key (enclosed in double quotes)

# Initialize the OpenAI client with the API key
client = OpenAI(
    api_key= # add your api key
) 

# Your conversation or command content
command =  

# there add the command like the message form the terminal output use the ''' ''' for ckeck the command is for the sender. 


# Calling OpenAI API to generate a response
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "you are a virtual assistant named unais skilled in general tasks like Aleva and Google Cloud"},
        {"role": "user", "content": command}
    ]
)

# Print the completion result
print(completion['choices'][0]['message']['content'])
  
