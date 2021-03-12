from app import app
from flask import render_template


@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Flask Page</title>
</head>
<body>
    <h1>Welcome to my sample Flask Page</h1>
    <p>"Negative energy that comes at you in some form is energy that can be turned around — to defeat an opponent and lift you up. – 50 Cent</p>
</body>
</html>
    """
