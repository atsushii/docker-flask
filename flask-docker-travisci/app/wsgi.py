from app import create_app

app = create_app()

# do some production specific things to the app
app.config['DEBUG'] = False