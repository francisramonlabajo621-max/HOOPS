"""
Migration script to add the category column to the Post table.
Run this once after pulling the latest code if your database was created
before categories were introduced.
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

        cursor.execute("PRAGMA table_info(post)")
        existing_columns = [row[1] for row in cursor.fetchall()]

        if 'category' in existing_columns:
            print("SUCCESS: 'category' column already exists. No migration needed.")
        else:
            print("Adding 'category' column to Post table...")
            cursor.execute("ALTER TABLE post ADD COLUMN category VARCHAR(50)")
            conn.commit()
            print("SUCCESS: 'category' column added.")

        conn.close()
    except Exception as exc:
        print(f"ERROR: Migration failed: {exc}")
        print("If you're starting fresh, you can delete blog.db and let Flask create a new one.")


if __name__ == '__main__':
    print("Running database migration for Post categories...\n")
    migrate_database()
    print("\nDone!")




