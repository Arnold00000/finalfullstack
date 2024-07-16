# backend/app/database.py
from app import create_app, db

app = create_app()


@app.cli.command("init_db")
def init_db():
    db.create_all()
    print("Initialized the database!")
