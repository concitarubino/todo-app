from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
        except json.JSONDecodeError:
            pass
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


@app.get("/")
def home():
    all_tasks = load_tasks()

    current_filter = request.args.get("filter", "all")

    if current_filter == "active":
        tasks = [t for t in all_tasks if not t["done"]]
    elif current_filter == "completed":
        tasks = [t for t in all_tasks if t["done"]]
    else:
        tasks = all_tasks

    total_count = len(all_tasks)
    completed_count = sum(1 for t in all_tasks if t["done"])
    active_count = total_count - completed_count

    return render_template(
        "index.html",
        tasks=tasks,
        current_filter=current_filter,
        total_count=total_count,
        completed_count=completed_count,
        active_count=active_count,
    )


@app.post("/add")
def add():
    tasks = load_tasks()
    task_text = request.form.get("task", "").strip()

    if task_text:
        exists = any(t["text"].lower() == task_text.lower() for t in tasks)
        if not exists:
            tasks.append({"text": task_text, "done": False})
            save_tasks(tasks)

    return redirect(url_for("home"))


@app.get("/delete/<int:idx>")
def delete(idx):
    tasks = load_tasks()

    if 0 <= idx < len(tasks):
        tasks.pop(idx)
        save_tasks(tasks)

    return redirect(url_for("home"))


@app.post("/toggle/<int:idx>")
def toggle(idx):
    tasks = load_tasks()

    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = not tasks[idx]["done"]
        save_tasks(tasks)

    return redirect(url_for("home"))


@app.post("/clear-completed")
def clear_completed():
    tasks = load_tasks()
    tasks = [t for t in tasks if not t["done"]]
    save_tasks(tasks)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
