

from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config["DEBUG"] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: lightgrey;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                fond: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
               margin: 10px 0;
               width: 540px;
               height: 120px;
            }}  
        </style>
    </head>
    <body>
        <form action="/encrypt" method="post">
            <div> 
                <label>Rotate by:</label>               
                <input type="text"  name = "rot" value = "0">
                 <p class="Error"> </p>
            </div>  
            <p>              
                <textarea name = "text" required>{}</textarea>   
            </p>
            <div>                 
              <input type="submit"  value = "Submit query"/>
             </div>  
        </form>
    </body>
        """
@app.route ("/", methods=['GET'])
def index():
    return form.format(0)  

@app.route ("/encrypt", methods=['POST'])
def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]
    rot_int = int(rot)
    encrypt = rotate_string(text, rot_int)
    content = encrypt
    error = rot_int <0
    return form.format(content)
app.run()




