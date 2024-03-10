from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    colors = ['Red', 'Green', 'Blue', 'Yellow', 'Orange']
    return render_template('index.html', colors=colors)

if __name__ == '__main__':
    app.run(debug=True)
