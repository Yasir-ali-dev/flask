from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapped_column, Mapped

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
db = SQLAlchemy(app)


class Item (db.Model):
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(nullable=False, unique=False)
    price: Mapped[int] = mapped_column(nullable=False)
    barcode: Mapped[str] = mapped_column(nullable=False, unique=True)


@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)


@app.route('/dynamic/<params>')
def dynamicParams(params):
    return f'<h1>Here is a dynamic route with passing params = {params}</h1>'


@app.route("/<dynamicParams>")
def handleParams(dynamicParams):
    return f'<h2> here {dynamicParams}</h2>'


if __name__ == "__main__":
    app.run(debug=True)
