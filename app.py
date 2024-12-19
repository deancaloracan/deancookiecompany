from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    embed_url = "https://app.powerbi.com/reportEmbed?reportId=b430017f-1856-4596-98af-38a7b22a9602&autoAuth=true&ctid=4da98571-dcea-4839-8fb1-0bdd5dc969f9"
    return render_template("dashboard.html", embed_url=embed_url)

if __name__ == "__main__":
    app.run(debug=True)
