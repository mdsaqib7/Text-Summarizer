from flask import Flask, request, render_template_string
from transformers import pipeline

app = Flask(__name__)

# Load the summarization model
summarizer = pipeline("summarization")

# HTML template for the form
HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Text Summarizer</title>
</head>
<body>
    <h1>Text Summarizer</h1>
    <form method="post" action="/">
        <textarea name="text" rows="10" cols="80" placeholder="Enter your text here...">{{ text }}</textarea><br><br>
        <input type="submit" value="Summarize">
    </form>
    {% if summary %}
        <h2>Summary:</h2>
        <p>{{ summary }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = None
    if request.method == 'POST':
        text = request.form['text']
        if text.strip():
            summary = summarizer(text, max_length=50, min_length=25, do_sample=False)[0]['summary_text']
        else:
            summary = "Text cannot be empty"
    else:
        text = ""
    return render_template_string(HTML_TEMPLATE, text=text, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)