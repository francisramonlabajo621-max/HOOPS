from app import app, db, User, Post
from datetime import datetime

def add_crossover_post():
    with app.app_context():
        # Get admin user
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            print("Admin user not found. Please run the app first to create the admin user.")
            return
        
        # Check if post already exists
        existing = Post.query.filter_by(title='THE ANKLE-BREAKER 🚨🤕 Top 10 CROSSOVERS | FIBA 3x3 2024 SEASON | 3x3 Basketball').first()
        if existing:
            print("Post already exists! Skipping...")
            return
        
        # Create the blog post
        post_content = """Get ready for the most INSANE crossover compilation of the 2024 FIBA 3x3 season! 🏀 These ankle-breaking moves will leave you speechless!

**What Makes These Crossovers Special?**

The 2024 FIBA 3x3 season has showcased some of the most incredible ball-handling skills we've ever seen. These players aren't just breaking ankles - they're breaking records and redefining what's possible on the court!

**Top 10 Crossover Highlights:**

**#10 - The Quick Step**
A lightning-fast hesitation that freezes defenders in their tracks. The speed and precision of this move is absolutely mind-blowing!

**#9 - The Behind-the-Back Special**
When a player goes behind the back in a 3x3 game, you know something special is about to happen. This one sent the defender flying!

**#8 - The Double Crossover**
Two crossovers in rapid succession that left the defender completely lost. The footwork here is absolutely incredible!

**#7 - The Spin Move Crossover**
Combining a spin move with a crossover - pure artistry on the court. This player made it look effortless!

**#6 - The Hesitation Killer**
A perfect hesitation that made the defender commit, then a lightning-quick crossover to blow past. Textbook execution!

**#5 - The Between-the-Legs Crossover**
Taking it between the legs in a high-pressure situation shows incredible confidence and skill. This one was absolutely filthy!

**#4 - The In-and-Out Special**
A deceptive in-and-out dribble followed by a crossover that broke ankles and broke the internet! The reaction from the crowd says it all!

**#3 - The Step-Back Crossover**
Creating space with a step-back, then crossing over when the defender closes in. This is next-level basketball IQ!

**#2 - The Combo Move**
Multiple moves strung together in perfect sequence. This player showed why they're considered one of the best ball handlers in 3x3!

**#1 - THE ANKLE-BREAKER**
The number one spot goes to a move so devastating that the defender literally fell to the ground! This crossover had everything - speed, deception, and pure skill. It's the kind of move that gets replayed a million times!

**Why 3x3 Basketball is Perfect for Crossovers:**

The 3x3 format creates more space and one-on-one opportunities, making it the perfect showcase for incredible ball-handling skills. With fewer players on the court, every move is magnified, and every crossover has the potential to be a game-changer.

**Key Takeaways:**

- Ball handling is an art form in 3x3 basketball
- The best crossovers combine speed, deception, and perfect timing
- These players have spent countless hours perfecting their craft
- The 2024 FIBA 3x3 season has been absolutely incredible!

**Want to Improve Your Crossover?**

Practice makes perfect! Work on your ball handling daily, focus on changing speeds, and always keep your defender guessing. Study these moves and incorporate elements into your own game!

Which crossover was your favorite? Drop a comment below and let's discuss! 🏀🔥

*Don't forget to like and share if you enjoyed this compilation!*"""
        
        post = Post(
            title='THE ANKLE-BREAKER 🚨🤕 Top 10 CROSSOVERS | FIBA 3x3 2024 SEASON | 3x3 Basketball',
            content=post_content,
            user_id=admin.id,
            date_posted=datetime.utcnow()
        )
        
        db.session.add(post)
        db.session.commit()
        print("SUCCESS: Created post: THE ANKLE-BREAKER Top 10 CROSSOVERS | FIBA 3x3 2024 SEASON | 3x3 Basketball")
        print(f"Post ID: {post.id}")

if __name__ == '__main__':
    print("Adding crossover post to blog...\n")
    add_crossover_post()
    print("\nDone!")

