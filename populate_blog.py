from app import app, db, User, Post
from datetime import datetime, timedelta

def populate_blog():
    with app.app_context():
        # Get or create admin user
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            print("Admin user not found. Please run the app first to create the admin user.")
            return
        
        # Sample blog posts
        posts_data = [
            {
                'title': 'Top 5 NBA Games of the 2024 Season',
                'content': '''The 2024 NBA season has been nothing short of spectacular! From buzzer-beaters to overtime thrillers, we've witnessed some incredible basketball. Here are my top 5 games that had fans on the edge of their seats:

**1. Lakers vs Warriors - Game 7 Playoffs**
This game had everything: LeBron's clutch performance, Curry's three-point barrage, and a nail-biting finish that went into double overtime. The energy in the arena was electric!

**2. Celtics vs Heat - Eastern Conference Finals**
A defensive masterpiece! Both teams showed incredible resilience, with the game coming down to the final possession. The intensity was off the charts.

**3. Nuggets vs Suns - Regular Season Classic**
Jokic's triple-double against Booker's 50-point game made this an instant classic. The back-and-forth action in the fourth quarter was basketball at its finest.

**4. Mavericks vs Clippers - Rivalry Renewed**
Luka Doncic and Kawhi Leonard going head-to-head is always must-see TV. This game featured multiple lead changes and clutch shots from both superstars.

**5. Bucks vs 76ers - MVP Showdown**
Giannis vs Embiid - two of the league's best going at it. The physicality and skill on display was incredible, with both players putting up monster numbers.

Which game was your favorite? Let me know in the comments!''',
                'date_posted': datetime.utcnow() - timedelta(days=5)
            },
            {
                'title': 'How to Improve Your Jump Shot: 5 Essential Tips',
                'content': '''Whether you're a beginner or looking to refine your game, improving your jump shot is crucial. Here are 5 essential tips that will help you become a better shooter:

**1. Perfect Your Form**
Start with your feet shoulder-width apart, knees slightly bent. Your shooting hand should be under the ball with your guide hand on the side. Keep your elbow in and follow through with your wrist.

**2. Practice Your Arc**
Aim for a 45-degree angle on your shot. Too flat and it won't go in; too high and you lose power. Find that sweet spot through repetition.

**3. Use Your Legs**
Power comes from your legs, not just your arms. Bend your knees and use that upward momentum to generate force for your shot.

**4. Follow Through**
Your shooting hand should finish with a "gooseneck" follow-through, pointing toward the basket. Hold that position until the ball reaches the rim.

**5. Practice, Practice, Practice**
There's no substitute for repetition. Set up a routine: 100 shots from different spots on the court every day. Track your progress and adjust as needed.

Remember: consistency is key! Start close to the basket and gradually move back as you improve. What's your biggest challenge with shooting? Share your tips in the comments!''',
                'date_posted': datetime.utcnow() - timedelta(days=4)
            },
            {
                'title': 'Rising Stars: Top 5 Rookies to Watch',
                'content': '''The 2024 NBA Draft class is showing incredible promise! These five rookies have been turning heads and making an immediate impact on their teams:

**1. Victor Wembanyama - San Antonio Spurs**
At 7'4" with guard skills, Wemby is a generational talent. His shot-blocking ability combined with his shooting range makes him a nightmare matchup for opponents.

**2. Scoot Henderson - Portland Trail Blazers**
Explosive athleticism and court vision. Scoot's ability to get to the rim and create for teammates has been impressive. He's the future of the Blazers' backcourt.

**3. Brandon Miller - Charlotte Hornets**
A smooth scorer with NBA-ready skills. Miller's ability to create his own shot and defend multiple positions makes him a valuable two-way player.

**4. Amen Thompson - Houston Rockets**
Incredible athleticism and playmaking ability. Thompson's versatility allows him to play multiple positions and impact the game in various ways.

**5. Ausar Thompson - Detroit Pistons**
A defensive specialist with offensive upside. Ausar's length and instincts make him a disruptive force on defense, while his offensive game continues to develop.

These young players are the future of the league! Which rookie has impressed you the most this season? Drop your thoughts below!''',
                'date_posted': datetime.utcnow() - timedelta(days=3)
            },
            {
                'title': 'Basketball Strategy: Understanding the Pick and Roll',
                'content': '''The pick and roll is one of the most effective plays in basketball. Used at every level from youth leagues to the NBA, understanding this fundamental play can elevate your game.

**What is a Pick and Roll?**
A pick and roll (or screen and roll) involves two players: one sets a screen (pick) for the ball handler, then "rolls" toward the basket. It creates multiple scoring opportunities.

**Key Components:**

**The Screen:**
The screener positions themselves to block the defender. Timing and angle are crucial. Set the screen too early or at the wrong angle, and it's ineffective.

**The Roll:**
After setting the screen, the screener moves toward the basket, looking for a pass. This creates a scoring opportunity close to the rim.

**The Ball Handler:**
The player with the ball uses the screen to create space. They can drive to the basket, pull up for a shot, or pass to the rolling teammate.

**Defending the Pick and Roll:**
Teams use various strategies:
- **Switch:** Defenders trade assignments
- **Hedge:** The screener's defender briefly steps out
- **Drop:** The defender stays back to protect the paint
- **Blitz:** Both defenders trap the ball handler

**Why It Works:**
The pick and roll forces the defense to make quick decisions, often creating mismatches or open shots. It's simple to execute but difficult to defend.

Have you tried running pick and roll plays? What's your favorite variation? Let's discuss in the comments!''',
                'date_posted': datetime.utcnow() - timedelta(days=2)
            },
            {
                'title': 'NBA Playoff Predictions: Who Will Win It All?',
                'content': '''The playoffs are heating up, and it's time to make some predictions! Here's my breakdown of the top contenders and who I think will hoist the championship trophy:

**Eastern Conference Favorites:**

**Boston Celtics**
With their deep roster and balanced attack, the Celtics are built for playoff success. Their defense has been elite all season, and they have multiple scoring options.

**Milwaukee Bucks**
Giannis Antetokounmpo is a force of nature. When he's healthy and playing at his best, the Bucks are nearly unstoppable. Their experience in big games is invaluable.

**Miami Heat**
Never count out the Heat! They've proven they can flip the switch in the playoffs. Jimmy Butler's playoff performances are legendary.

**Western Conference Favorites:**

**Denver Nuggets**
The defending champions have the best player in the world in Nikola Jokic. Their chemistry and playoff experience make them dangerous.

**Phoenix Suns**
With their star-studded lineup, the Suns have the firepower to outscore anyone. Their offense is explosive when clicking.

**Los Angeles Lakers**
LeBron James and Anthony Davis are a formidable duo. When healthy, they're capable of making a deep playoff run.

**My Championship Pick:**
I'm going with the **Denver Nuggets** to repeat! Jokic's versatility, their team chemistry, and championship experience give them the edge. However, the Celtics and Bucks will push them to the limit.

What are your predictions? Who do you think will win it all? Let's debate in the comments!''',
                'date_posted': datetime.utcnow() - timedelta(days=1)
            }
        ]
        
        # Check if posts already exist
        existing_posts = Post.query.filter_by(user_id=admin.id).count()
        if existing_posts > 0:
            print(f"Found {existing_posts} existing posts. Adding new posts...")
        
        # Create posts
        created_count = 0
        for post_data in posts_data:
            # Check if post with same title already exists
            existing = Post.query.filter_by(title=post_data['title']).first()
            if not existing:
                post = Post(
                    title=post_data['title'],
                    content=post_data['content'],
                    user_id=admin.id,
                    date_posted=post_data['date_posted']
                )
                db.session.add(post)
                created_count += 1
                print(f"✅ Created post: {post_data['title']}")
            else:
                print(f"⏭️  Skipped existing post: {post_data['title']}")
        
        db.session.commit()
        print(f"\n🎉 Successfully created {created_count} blog posts!")
        print(f"📊 Total posts in database: {Post.query.count()}")

if __name__ == '__main__':
    print("🏀 Populating basketball blog posts...\n")
    populate_blog()







