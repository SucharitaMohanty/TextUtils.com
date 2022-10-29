from ast import Param

from click import option
from flask import Flask, render_template, request



# Initalising the app
app = Flask(__name__)


# Making Routes
@app.route('/', methods=['GET', 'POST'])
def home__page():
    formatted_string = ''
    input_str = ''
    if request.method == 'POST':
        input_str = request.form['input']
        options = request.form.get('options')
        if options == 'upper':
            formatted_string+= input_str.upper()
        elif options == 'lower':
            formatted_string+= input_str.lower()
        elif options == 'capitalise':
            formatted_string+= input_str.capitalize()
        elif options == 'remove-punctuation':
            punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            new_str = ''
            for i in input_str:
                if i not in punctuation:
                    new_str+=i
            formatted_string+= new_str
        elif options == 'remove-extraspace':
            splittedWords = input_str.split()
            new_str = " ".join(splittedWords)
            formatted_string+= new_str
        elif options == 'word-count':
            splittedWords = input_str.split()
            no_of_words = len (splittedWords)
            formatted_string+= str(no_of_words)
        elif options == 'letter-count':
            no_of_letters = len(input_str)
            formatted_string += str(no_of_letters)
    return render_template('index.html', output = formatted_string, input_str=input_str )


if __name__ == '__main__':
    app.run(debug=True)
