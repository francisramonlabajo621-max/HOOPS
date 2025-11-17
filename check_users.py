from app import app, db, User

def check_users():
    with app.app_context():
        users = User.query.all()
        if users:
            print("\n📋 Existing Users in Database:\n")
            print("-" * 60)
            for user in users:
                print(f"ID: {user.id}")
                print(f"Username: {user.username}")
                print(f"Email: {user.email}")
                print("-" * 60)
            print(f"\nTotal users: {len(users)}\n")
        else:
            print("\n✅ No users found in database.\n")

if __name__ == '__main__':
    check_users()







