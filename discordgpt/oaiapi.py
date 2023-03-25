import openai

class OAI817:
    def __init__(self, config):
        self.config = config
        openai.api_key = config["openai_key"]

    def get_response(self, prompt):
    # Add your OpenAI API call here
    try:
        completions = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a sassy Discord chat bot."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completions.choices[0].message['content']
        return response
    except Exception as e:
        print(f"Error in get_gpt_response: {e}")
        return None

user_prompt = input("Please enter a prompt: ")
response_text = get_gpt_response(user_prompt)
print(response_text)