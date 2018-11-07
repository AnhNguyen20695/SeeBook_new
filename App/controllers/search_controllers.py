from flask import current_app, render_template, redirect, url_for, request, g
# from App.view.forms.SearchForm import SearchForm
from App import app
from App.models.post import Post
from flask_login import login_required

@app.route('/search')
@login_required
def search():
    if not g.search_form.validate():
        return redirect(url_for('explore'))
    page = request.args.get('page', 1, type=int)
    posts, total = Post.search(g.search_form.q.data, page, current_app.config['POSTS_PER_PAGE'])
    next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) \
        if total > page * current_app.config['POSTS_PER_PAGE'] else None
    prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    return render_template('user/search.html', title=_('Search'), posts=posts, next_url=next_url, prev_url=prev_url)