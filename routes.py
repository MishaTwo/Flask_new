from __init__ import app
from flask import Flask, render_template, request, redirect
from models.car import Car
from models.base import session

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/read')
def read_all():
    car_post = session.query(Car).all()

@app.route("/read_post_detail/<int:id>")
def read_post(id):
    post = session.query(Car).get(id)
    return render_template("post_detail.html", post=post)


@app.route("/create_post", methods=["POST", "GET"])
def create_post():
    if request.method == "POST":
        content = request.form["content"]
        title = request.form["title"]

        new_post = Car(
            title=title,
            content=content
        )

        try:
            session.add(new_post)
            session.commit()
            return redirect("/")
        except Exception as exc:
            return f"При збереженні виникла помилка: {exc}"
        finally:
            session.close()
    else:
        return render_template("create_post.html")


@app.route("/update/<int:id>", methods=["GET", "PUT"])
def update_post(id):
    post = session.query(Car).get(id)
    if request.method == "PUT":
        content = request.form["content"]
        title = request.form["title"]
        if title or content:
            try:
                post.title = title
                post.content = content
                session.commit()
                return redirect("/")
            except Exception as exc:
                return f"При оновленні поста виникла помилка: {exc}"
            finally:
                session.close()
        else:
            return "Онови поля, оскільки ти їх не змінив/-ла"
    else:
        return render_template("create_post.html", post=post)


@app.route("/delete/<int:id>")
def delete_post(id):
    post = session.query(Car).filter_by(id=id)
    session.delete(post)
    session.close()
    return redirect("/")

