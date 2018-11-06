from App import app, db
from App.models.user import User
from App.models.post import Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}