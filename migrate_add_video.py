"""
Migration script to add video_filename column to existing Post table.
Run this once to update your database schema.
"""
from app import app, db, Post
from sqlalchemy import text

def migrate_database():
    with app.app_context():
        try:
            # Check if column already exists
            inspector = db.inspect(db.engine)
            columns = [col['name'] for col in inspector.get_columns('post')]
            
            if 'video_filename' not in columns:
                print("Adding video_filename column to Post table...")
                # Add the new column
                with db.engine.connect() as conn:
                    conn.execute(text('ALTER TABLE post ADD COLUMN video_filename VARCHAR(200)'))
                    conn.commit()
                print("SUCCESS: Migration successful! video_filename column added.")
            else:
                print("SUCCESS: video_filename column already exists. No migration needed.")
        except Exception as e:
            print(f"ERROR: Migration error: {e}")
            print("If you're starting fresh, you can delete blog.db and let Flask create a new one.")
            print("Or manually add the column using SQLite browser.")

if __name__ == '__main__':
    print("Running database migration...\n")
    migrate_database()
    print("\nDone!")

