from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-this-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 1000 * 1024 * 1024  # 100MB max file size (for videos)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'

# Allowed file extensions
ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
ALLOWED_VIDEO_EXTENSIONS = {'mp4', 'webm', 'ogg', 'mov', 'avi'}

def allowed_file(filename, file_type='image'):
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    if file_type == 'image':
        return ext in ALLOWED_IMAGE_EXTENSIONS
    elif file_type == 'video':
        return ext in ALLOWED_VIDEO_EXTENSIONS
    return False

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    profile_picture = db.Column(db.String(200), nullable=True)
    cover_photo = db.Column(db.String(200), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(100), nullable=True)
    website = db.Column(db.String(200), nullable=True)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=True, index=True)
    image_filename = db.Column(db.String(200), nullable=True)
    video_url = db.Column('video_filename', db.String(500), nullable=True)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True, cascade='all, delete-orphan')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    search_query = request.args.get('search', '')
    selected_category = request.args.get('category', '').strip()
    view_filter = request.args.get('view', '').strip()
    
    query = Post.query
    
    if search_query:
        query = query.filter(
            db.or_(
                Post.title.contains(search_query),
                Post.content.contains(search_query)
            )
        )
    
    if selected_category:
        query = query.filter(Post.category == selected_category)

    if view_filter == 'videos':
        query = query.filter(Post.video_url.isnot(None))
    elif view_filter == 'stories':
        query = query.filter(Post.video_url.is_(None))
    
    posts = query.order_by(Post.date_posted.desc()).all()
    
    total_posts = Post.query.count()
    total_users = User.query.count()
    
    categories = [
        row[0] for row in db.session.query(Post.category)
        .filter(Post.category.isnot(None), Post.category != '')
        .distinct()
        .order_by(Post.category.asc())
        .all()
    ]
    
    return render_template(
        'index.html',
        posts=posts,
        search_query=search_query,
        categories=categories,
        selected_category=selected_category,
        total_posts=total_posts,
        total_users=total_users,
        selected_view=view_filter
    )

@app.route('/explore')
def explore():
    # Get all posts grouped by some criteria or show featured posts
    all_posts = Post.query.order_by(Post.date_posted.desc()).all()
    featured_posts = Post.query.order_by(Post.date_posted.desc()).limit(6).all()
    
    # Get post counts by author
    authors = {}
    for post in all_posts:
        if post.author.username not in authors:
            authors[post.author.username] = 0
        authors[post.author.username] += 1
    
    return render_template('explore.html', featured_posts=featured_posts, all_posts=all_posts, authors=authors)

@app.route('/about')
def about():
    total_posts = Post.query.count()
    total_users = User.query.count()
    total_comments = Comment.query.count()
    return render_template('about.html', total_posts=total_posts, total_users=total_users, total_comments=total_comments)

@app.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', post=post)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form.get('category', '').strip()
        video_url = request.form.get('video_url', '').strip()
        image_filename = None
        
        # Handle image upload
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename != '' and allowed_file(file.filename, 'image'):
                filename = secure_filename(file.filename)
                # Add timestamp to make filename unique
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
                filename = timestamp + filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                image_filename = filename
        
        new_post = Post(
            title=title,
            content=content,
            category=category or None,
            image_filename=image_filename,
            video_url=video_url or None,
            user_id=current_user.id
        )
        db.session.add(new_post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('index'))
    
    categories = [
        row[0] for row in db.session.query(Post.category)
        .filter(Post.category.isnot(None), Post.category != '')
        .distinct()
        .order_by(Post.category.asc())
        .all()
    ]
    return render_template('add_post.html', categories=categories)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    post = Post.query.get_or_404(id)
    
    # Check if user owns the post
    if post.user_id != current_user.id:
        flash('You can only edit your own posts!', 'danger')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        category = request.form.get('category', '').strip()
        post.category = category or None
        video_url = request.form.get('video_url', '').strip()
        post.video_url = video_url or None
        
        # Handle image upload
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename != '' and allowed_file(file.filename, 'image'):
                # Delete old image if exists
                if post.image_filename:
                    old_filepath = os.path.join(app.config['UPLOAD_FOLDER'], post.image_filename)
                    if os.path.exists(old_filepath):
                        os.remove(old_filepath)
                
                filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
                filename = timestamp + filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                post.image_filename = filename
        
        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('post', id=post.id))
    
    categories = [
        row[0] for row in db.session.query(Post.category)
        .filter(Post.category.isnot(None), Post.category != '')
        .distinct()
        .order_by(Post.category.asc())
        .all()
    ]
    return render_template('edit_post.html', post=post, categories=categories)

@app.route('/delete/<int:id>')
@login_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    
    # Check if user owns the post
    if post.user_id != current_user.id:
        flash('You can only delete your own posts!', 'danger')
        return redirect(url_for('index'))
    
    # Delete associated image if exists
    if post.image_filename:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], post.image_filename)
        if os.path.exists(filepath):
            os.remove(filepath)
    
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/comment/<int:post_id>', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    content = request.form['content']
    
    if content.strip():
        new_comment = Comment(content=content, user_id=current_user.id, post_id=post_id)
        db.session.add(new_comment)
        db.session.commit()
        flash('Comment added successfully!', 'success')
    else:
        flash('Comment cannot be empty!', 'danger')
    
    return redirect(url_for('post', id=post_id))

@app.route('/delete_comment/<int:comment_id>')
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    post_id = comment.post_id
    
    # Check if user owns the comment
    if comment.user_id != current_user.id:
        flash('You can only delete your own comments!', 'danger')
        return redirect(url_for('post', id=post_id))
    
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted successfully!', 'success')
    return redirect(url_for('post', id=post_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        # Validation
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return render_template('register.html')
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash(f'Username "{username}" already exists! Please choose a different username or login with your existing account.', 'danger')
            return render_template('register.html')
        
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash(f'Email "{email}" is already registered! Please use a different email or login with your existing account.', 'danger')
            return render_template('register.html')
        
        # Create new user
        password_hash = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=password_hash, date_joined=datetime.utcnow())
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            next_page = request.args.get('next')
            flash(f'Welcome back, {username}!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Invalid username or password!', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/profile')
@app.route('/profile/<int:user_id>')
@login_required
def profile(user_id=None):
    if user_id:
        user = User.query.get_or_404(user_id)
    else:
        user = current_user
    
    # Get member since date - use date_joined if available, otherwise use oldest post or comment
    member_since = user.date_joined
    if not member_since:
        # Fallback: use oldest post date
        oldest_post = Post.query.filter_by(user_id=user.id).order_by(Post.date_posted.asc()).first()
        if oldest_post:
            member_since = oldest_post.date_posted
        else:
            # Fallback: use oldest comment date
            oldest_comment = Comment.query.filter_by(user_id=user.id).order_by(Comment.date_posted.asc()).first()
            if oldest_comment:
                member_since = oldest_comment.date_posted
            else:
                # Default to current date if nothing found
                member_since = datetime.utcnow()
    
    user_posts = Post.query.filter_by(user_id=user.id).order_by(Post.date_posted.desc()).all()
    return render_template('profile.html', user=user, user_posts=user_posts, is_own_profile=(user.id == current_user.id), member_since=member_since)

@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        user = current_user
        
        # Update basic info
        user.email = request.form.get('email', user.email)
        user.bio = request.form.get('bio', user.bio)
        user.location = request.form.get('location', user.location)
        user.website = request.form.get('website', user.website)
        
        # Handle profile picture upload
        if 'profile_picture' in request.files:
            file = request.files['profile_picture']
            if file and file.filename != '' and allowed_file(file.filename, 'image'):
                # Delete old profile picture if exists
                if user.profile_picture:
                    old_filepath = os.path.join(app.config['UPLOAD_FOLDER'], user.profile_picture)
                    if os.path.exists(old_filepath):
                        os.remove(old_filepath)
                
                filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
                filename = 'profile_' + timestamp + filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                user.profile_picture = filename
        
        # Handle cover photo upload
        if 'cover_photo' in request.files:
            file = request.files['cover_photo']
            if file and file.filename != '' and allowed_file(file.filename, 'image'):
                # Delete old cover photo if exists
                if user.cover_photo:
                    old_filepath = os.path.join(app.config['UPLOAD_FOLDER'], user.cover_photo)
                    if os.path.exists(old_filepath):
                        os.remove(old_filepath)
                
                filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
                filename = 'cover_' + timestamp + filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                user.cover_photo = filename
        
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))
    
    return render_template('edit_profile.html', user=current_user)

# Initialize database
with app.app_context():
    db.create_all()
    
    # Create default admin user if it doesn't exist
    if not User.query.filter_by(username='admin').first():
        admin = User(
            username='admin',
            email='admin@blog.com',
            password_hash=generate_password_hash('admin123')
        )
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)

