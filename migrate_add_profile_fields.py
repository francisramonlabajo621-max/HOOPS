"""
Migration script to add profile fields to existing User table.
Run this once to update your database schema.
"""
import sqlite3
import os

def migrate_database():
    db_path = 'instance/blog.db'
    
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get existing columns
        cursor.execute("PRAGMA table_info(user)")
        existing_columns = [row[1] for row in cursor.fetchall()]
        
        migrations_needed = []
        
        if 'profile_picture' not in existing_columns:
            migrations_needed.append('profile_picture VARCHAR(200)')
        if 'cover_photo' not in existing_columns:
            migrations_needed.append('cover_photo VARCHAR(200)')
        if 'bio' not in existing_columns:
            migrations_needed.append('bio TEXT')
        if 'location' not in existing_columns:
            migrations_needed.append('location VARCHAR(100)')
        if 'website' not in existing_columns:
            migrations_needed.append('website VARCHAR(200)')
        
        if migrations_needed:
            print("Adding profile fields to User table...")
            for field in migrations_needed:
                field_name = field.split()[0]
                print(f"  Adding {field_name}...")
                cursor.execute(f'ALTER TABLE user ADD COLUMN {field}')
            conn.commit()
            print(f"SUCCESS: Added {len(migrations_needed)} field(s) to User table")
        else:
            print("SUCCESS: All profile fields already exist. No migration needed.")
        
        conn.close()
    except Exception as e:
        print(f"ERROR: Migration error: {e}")
        print("If you're starting fresh, you can delete blog.db and let Flask create a new one.")

if __name__ == '__main__':
    print("Running database migration for profile fields...\n")
    migrate_database()
    print("\nDone!")
