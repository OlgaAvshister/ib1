from app import app, db, bcrypt, User, Post

# создаём контекст приложения
with app.app_context():
    db.create_all()

    if not User.query.filter_by(username='alice').first():
        pw = bcrypt.generate_password_hash('password').decode('utf-8')
        u = User(username='alice', password_hash=pw)
        db.session.add(u)
        db.session.commit()
        print('Created user alice / password')
    else:
        print('User alice already exists')

    user = User.query.filter_by(username='alice').first()
    if user and not Post.query.first():
        p1 = Post(title='Hello', content='Привет мир', author_id=user.id)
        p2 = Post(title='About', content='Текст поста', author_id=user.id)
        db.session.add_all([p1, p2])
        db.session.commit()
        print('Seeded posts')
