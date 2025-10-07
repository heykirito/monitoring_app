import psutil
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent
    msg = None
    if cpu_usage > 80 or mem_usage > 80:
        msg = "High CPU or memory usgae detected"
    return render_template(
        "index.html", cpu_usage=cpu_usage, mem_usage=mem_usage, message=msg
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
