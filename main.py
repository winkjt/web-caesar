from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True  

form = """
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
                
            </style>
        </head>
        <body>
        <form method="post">

            <name="rot" value="rot"> Rotate by how many digits?
            <input type="text" name="rot" value="0" id="rot">
            <textarea name="text"> {0} </textarea>
            
            <input type="submit" value="Submit Query" class="button" /> 

        </form>
        </body>
    </html>
    """

@app.route("/")
def index():

    return form.format(' ')


@app.route("/", methods=['POST'])
def encrypt():

    rot = request.form['rot']
    num = int(rot)

    user_input = request.form['text']
    user_string = str(user_input)

    encrpytion = rotate_string(user_string, num)

    content = "<h1>" + form.format(encrpytion) + "</h1>"

    return content


app.run()
