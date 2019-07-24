"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

INSULT = [
    'boring', 'lazy', 'plain', 'mean']


@app.route("/")
def start_here():
    """Home page."""
    
    return "<!doctype html><html>Hi! This is the home page.<br><a href=/hello>Go to Hello page</a><br><a href=/byebye>Go to Bye page</a></html>"


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""
    
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          <br>
          <select name="compliment">
            <option value="">--Please choose an compliment--</option>
            <option value="awesome">Awesome</option>
            <option value="terrific">Terrific</option>
            <option value="fantastic">Fantastic</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)

@app.route("/byebye")
def say_bye():
    """Say hello and prompt for user's name."""
    
    return """
    <!doctype html>
    <html>
      <head>
        <title>Bye There!</title>
      </head>
      <body>
        <h1>Bye There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """
@app.route("/diss")
def diss_person():
  """insult person"""
  insult = choice(INSULT)
  player = request.args.get("person")

  return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, insult)



if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
