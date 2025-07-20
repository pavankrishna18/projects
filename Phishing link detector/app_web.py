from flask import Flask, render_template_string, request
from predict_url import predict_url

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Phishing URL Detector</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    <h1>Phishing URL Detector</h1>
    <form method="POST">
        <input type="text" name="url" placeholder="Enter URL" size="50" required />
        <button type="submit">Check</button>
    </form>
    {% if result is defined %}
        <h2>Result: <span style="color: {{ 'red' if result == 'Phishing' else 'green' }}">{{ result }}</span></h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        result = predict_url(url)
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)