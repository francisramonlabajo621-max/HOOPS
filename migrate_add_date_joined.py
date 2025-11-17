"""
Migration script to add date_joined field to existing User table.
Run this once to update your database schema.
"""
import sqlite3
import os
from datetime import datetime

def migrate_database():
    # Try different possible paths
    possible_paths = [
        'instance/blog.db',
        os.path.join(os.path.dirname(__file__), 'instance', 'blog.db'),
        'blog.db'
    ]
    
    db_path = None
    for path in possible_paths:
        if os.path.exists(path):
            db_path = path
            break
    
    if not db_path:
        print(f"Database not found. Tried: {possible_paths}")
        return
    
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get existing columns
        cursor.execute("PRAGMA table_info(user)")
        existing_columns = [row[1] for row in cursor.fetchall()]
        
        if 'date_joined' not in existing_columns:
            print("Adding date_joined field to User table...")
            cursor.execute('ALTER TABLE user ADD COLUMN date_joined DATETIME')
            conn.commit()
        
        # Set date_joined for existing users who don't have it set
        cursor.execute("SELECT id FROM user WHERE date_joined IS NULL")
        users_without_date = cursor.fetchall()
        
        if users_without_date:
            print(f"Setting date_joined for {len(users_without_date)} user(s)...")
            for user_id, in users_without_date:
                # Try to get oldest post date
                cursor.execute("SELECT MIN(date_posted) FROM post WHERE user_id = ?", (user_id,))
                result = cursor.fetchone()
                oldest_post = result[0] if result else None
                
                # Try to get oldest comment date
                cursor.execute("SELECT MIN(date_posted) FROM comment WHERE user_id = ?", (user_id,))
                result = cursor.fetchone()
                oldest_comment = result[0] if result else None
                
                # Use the oldest date available, or current date
                if oldest_post and oldest_comment:
                    date_joined = min(oldest_post, oldest_comment)
                elif oldest_post:
                    date_joined = oldest_post
                elif oldest_comment:
                    date_joined = oldest_comment
                else:
                    date_joined = datetime.utcnow().isoformat()
                
                cursor.execute("UPDATE user SET date_joined = ? WHERE id = ?", (date_joined, user_id))
            
            conn.commit()
            print(f"SUCCESS: Set date_joined for {len(users_without_date)} user(s)")
        else:
            print("SUCCESS: All users have date_joined set. No updates needed.")
        
        conn.close()
    except Exception as e:
        print(f"ERROR: Migration error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    print("Running database migration for date_joined field...\n")
    migrate_database()
    print("\nDone!")

