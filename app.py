from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Cloud Testing App</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    <h1 id="title">Welcome to Dhyey Cloud Testing App</h1>

    <input type="text" id="name" placeholder="Enter your name" style="padding:10px;">
    <br><br>

    <button id="btn" onclick="showMessage()" style="padding:10px;">Submit</button>

    <p id="message" style="font-size:20px; color:green;"></p>

    <script>
        function showMessage() {
            let name = document.getElementById("name").value;
            document.getElementById("message").innerText = "Hello, " + name;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)