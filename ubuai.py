import ollama 

class Chatbot:
    def __init__(self):
        self.model = "phi3"  
        self.system_prompt = (
            "Reply with only the final answer. "
            "Do NOT provide explanations, thoughts, or reasoning. "
            "Do NOT use LaTeX formatting or special characters like [ \\boxed{} ]. "
            "For example, respond to '8*2' with '16' or to 'hello' with 'Hello!'."
        )

    def get_response(self, user_input):
        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt}, 
                {"role": "user", "content": user_input}
            ]
        )
        return response['message']['content'].strip() 
