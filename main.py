

from flask import Flask, request
from caesar import rotate_string

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                 background-color: lightgrey;
                 padding: 20px;
                 margin: 20px;
                 width: 540px;
                 font: 16px sans-serif;
                 border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/action_page.php" method="post">
            <div>
                <label for = "rot">Rotate by:</label>
                <input type = "text" id="rot" value = "0" placeholder = "0">
                 <p class = "Error"> </p>
            </div>  
            <p>
               <label for="letters"></label>
                <textarea type="text"  id="letters" required></textarea>   
            </p>
            <div>  
               <label for="new_letters"></label>
               <input type="submit" id = "new_letters" value = "Submit query"/>
            </div>
            '{letters} was rotated by {value} to get {new_letters}'.format_form(Default(letters='type', value = "type", new_letters = "submit_result"))
        </form>



@app.route ("/", methods=['POST'])
