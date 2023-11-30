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

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bot copy.html')

@app.route('/process_voice', methods=['POST'])
def process_voice():
    user_message = request.form['user_message']
    bot_response = generate_response(user_message)  # Implement your bot logic here
    return jsonify({'response': bot_response})

def generate_response(user_message):
    res=solution(user_message)
    return res

if __name__ == '__main__':
    app.run(debug=True)



