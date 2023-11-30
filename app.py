import google.generativeai as palm
palm.configure(api_key='AIzaSyCw9UHFLxolOl9fEBLnwFedqMBC6Sj8nPk')
# Use the palm.list_models function to find available models:
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
def solution(name):
    prompt = name
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )
    result=completion.result 
    return result

from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('front.html')
@app.route('/home')
def home():
    return render_template('bot2.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    bot_response = generate_response(user_message)  # Implement your bot logic here
    return jsonify({'response': bot_response})

def generate_response(user_message):
    # Implement your chatbot logic here
    if "your name" in user_message or user_message=="hi" or "hello" in user_message or "hey" in user_message:
        responses=" Hi , My name is Rahu"
    elif "who made you" in user_message or "your architect" in user_message or "your maker" in user_message:
        responses="I was created by Sourashis Sarkar"
    else:
       if solution(user_message)=="None":
           responses="I don't understand"
       else:
           responses = solution(user_message)
    return responses
 
if __name__ == '__main__':
    app.run(debug=True)
