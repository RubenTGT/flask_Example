from app import app
from routes.persons_routes import persons

app.register_blueprint(persons)

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)