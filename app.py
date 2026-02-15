from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []  # store tasks in memory


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_name = request.form["task"]
        priority = request.form["priority"]

        tasks.append({
            "name": task_name,
            "priority": priority,
            "completed": False
        })

        return redirect("/")

    return render_template("index.html", tasks=tasks)


@app.route("/complete/<int:task_id>")
def complete(task_id):
    tasks[task_id]["completed"] = True
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
