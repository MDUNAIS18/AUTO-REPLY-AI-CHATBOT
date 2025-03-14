from openai import OpenAI

# Correctly assigning the API key (enclosed in double quotes)

# Initialize the OpenAI client with the API key
client = OpenAI(
    api_key= "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"
) 

# Your conversation or command content
command = ''' 
Copied text: [11:06 pm, 10/3/2025] Arya: Unais eapude irukan nu kekura 
[11:06 pm, 10/3/2025] Arya: Ena solatum 
[11:07 pm, 10/3/2025] MD UNAIS: Unaku thariyadha msg pannu 
[11:07 pm, 10/3/2025] MD UNAIS: Thariyadha maari kekuriyaa 
[11:07 pm, 10/3/2025] Arya: Theriyatha nala dha kekura 
[11:08 pm, 10/3/2025] MD UNAIS: Daii daiii summa thariyadha maari nadikuradha enta 
[11:09 pm, 10/3/2025] Arya: Unmaya unais 
[11:09 pm, 10/3/2025] MD UNAIS: nee pesu first ava ready pannu
'''

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
  