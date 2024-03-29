from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import openai

app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.environ.get('app_secret_key')
openai.api_key = os.environ.get('open_ai_api_key')


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            prompt = request.form['prompt']
            resp = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=3300,
                temperature=0.9,
            )
            resp["choices"][0]["text"] = resp["choices"][0]["text"].replace('\n', '<br>')
            return render_template('index.html', response=resp["choices"][0]["text"])
        except:
            return render_template('index.html', response="Oops! Looks like the AI taking too much time te respond. Please retry.")

    return render_template("index.html", response="")

if __name__ == '__main__':
    app.run(debug=True)
