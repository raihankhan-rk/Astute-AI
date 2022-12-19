from flask import Flask, render_template, redirect, request, url_for
import openai
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
openai.api_key = "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"

@app.route("/")
def home():
  return render_template("index.html", response="")

@app.route('/submit', methods=['POST'])
def submit():
    prompt = request.form['prompt']
    resp = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      max_tokens=400,
      temperature=0.9,
    )
    print(resp["choices"][0]["text"])
    resp["choices"][0]["text"] = resp["choices"][0]["text"].replace('\n', '<br>')
    return render_template('index.html', response=resp["choices"][0]["text"])


if __name__ == '__main__':
    app.run(debug=True)