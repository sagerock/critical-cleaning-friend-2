import openai
import gradio
import config
openai.api_key = config.api_key
messages = [{"role": "system", "content": "You are an expert in critical cleaning in the industries of medical device manufacturing, pharmaceutical manufacturing, electronic manufacturing, cosmetics manufacturing, food and beverage manufacturing, nuclear cleaning, tattoo equipment, cannabis manufacturing, and precision manufacturing"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Your Critical Cleaning Friend")

demo.launch(share=True)