from app import app, db, User, Post
from datetime import datetime, timedelta

def populate_blog():
    with app.app_context():
        # Get or create admin user
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            print("Admin user not found. Please run the app first to create the admin user.")
            return
        
        # Personal hoops blog posts
        posts_data = [
            {
                'title': 'My Journey with Basketball: Why I Love This Game',
                'content': '''Basketball has been a part of my life for as long as I can remember. From shooting hoops in my driveway as a kid to watching NBA games late into the night, this sport has shaped who I am today.

**The Early Days:**
I remember my first basketball - it was orange and white, and I could barely get it to the rim. But something about that sound of the ball bouncing, the swish of the net, it hooked me instantly. I spent countless hours practicing my shot, imagining I was hitting game-winning shots like my heroes.

**What Makes Basketball Special:**
There's something magical about basketball. It's a game of skill, strategy, and heart. Every possession matters. Every shot counts. The teamwork, the individual brilliance, the moments of pure athleticism - it all comes together to create something beautiful.

**My Favorite Moments:**
- Watching Michael Jordan's "Flu Game" - pure determination
- Kobe's 81-point game - absolute mastery
- The Warriors' 73-win season - team basketball at its finest
- Every buzzer-beater that makes you jump out of your seat

Basketball teaches you about life: hard work, teamwork, resilience, and never giving up. Whether you're playing pickup at the local court or watching the NBA Finals, basketball brings people together.

What's your basketball story? Share it in the comments! 🏀''',
                'category': 'Personal',
                'date_posted': datetime.utcnow() - timedelta(days=10)
            },
            {
                'title': 'The Art of the Crossover: Breaking Down Ankles',
                'content': '''There's nothing quite like a killer crossover. When done right, it's poetry in motion - a moment where skill, timing, and deception come together to create something beautiful (and devastating for the defender).

**What Makes a Great Crossover:**
A great crossover isn't just about speed. It's about:
- **Change of pace:** Slow to fast, fast to slow
- **Body control:** Keeping your center of gravity low
- **Ball control:** Tight handle, quick direction change
- **Deception:** Making the defender think you're going one way

**My Favorite Crossover Artists:**
1. **Allen Iverson** - The Answer had the most iconic crossover in NBA history. That move on Michael Jordan? Legendary.
2. **Kyrie Irving** - The handles are unreal. He can break anyone down with his combination of speed and skill.
3. **Jamal Crawford** - The behind-the-back, between-the-legs combinations are pure artistry.
4. **Stephen Curry** - His hesitation and quick bursts leave defenders in the dust.

**How to Practice:**
Start slow. Master the basics:
- Between the legs dribble
- Behind the back
- Hesitation moves
- Quick direction changes

Then combine them. Practice in front of a mirror, then on the court. The key is repetition until it becomes second nature.

Remember: A great crossover isn't about showing off - it's about creating space to score or make a play. Use it wisely!

What's your go-to move? Drop it in the comments! 🔥''',
                'category': 'Skills',
                'date_posted': datetime.utcnow() - timedelta(days=9)
            },
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
                'date_posted': datetime.utcnow() - timedelta(days=8),
                'category': 'Games'
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
                'date_posted': datetime.utcnow() - timedelta(days=7),
                'category': 'Training'
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
                'date_posted': datetime.utcnow() - timedelta(days=6),
                'category': 'Players'
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
                'date_posted': datetime.utcnow() - timedelta(days=5),
                'category': 'Strategy'
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
                'date_posted': datetime.utcnow() - timedelta(days=4),
                'category': 'Analysis'
            },
            {
                'title': 'Building a Basketball Community: Why We Need Each Other',
                'content': '''Basketball is more than just a game - it's a community. Whether you're playing pickup at the local court, watching games with friends, or discussing plays online, basketball brings people together.

**The Pickup Game Culture:**
There's something special about walking onto a court and finding a game. No matter where you are, the language of basketball is universal. A nod, a point, and you're in. The respect for the game, the competition, the camaraderie - it's all there.

**Online Basketball Communities:**
Platforms like this one allow us to share our passion, debate, learn, and connect with fellow basketball fans from around the world. We can discuss:
- Game strategies
- Player performances
- Training tips
- Our own experiences on the court

**Why Community Matters:**
- **Learning:** We learn from each other's experiences and insights
- **Motivation:** Seeing others work hard pushes us to do the same
- **Connection:** Shared passion creates lasting friendships
- **Growth:** Different perspectives help us see the game in new ways

**How to Build Your Basketball Community:**
1. Join local leagues or pickup games
2. Engage in online discussions (like this blog!)
3. Share your knowledge and experiences
4. Support others in their basketball journey
5. Stay open to learning from everyone

Basketball is better together. Whether you're a player, coach, or fan, we're all part of this amazing community.

How has basketball connected you with others? Share your story! 🤝''',
                'category': 'Community',
                'date_posted': datetime.utcnow() - timedelta(days=3)
            },
            {
                'title': 'Defense Wins Championships: My Take on Lockdown Defense',
                'content': '''Everyone loves a highlight dunk or a deep three, but defense wins championships. There's something beautiful about great defense - the anticipation, the positioning, the effort. It's the foundation of every great team.

**The Mindset:**
Great defense starts with mindset. You have to WANT to play defense. It's not glamorous, but it's essential. Every possession matters, every stop counts. Defense is about pride, effort, and intelligence.

**Key Defensive Principles:**

**1. On-Ball Defense:**
- Stay low, stay balanced
- Keep your eyes on the opponent's chest (not the ball)
- Use your feet, not your hands
- Force them to their weak hand

**2. Help Defense:**
- Always be aware of where the ball is
- Be ready to help your teammate
- Communicate constantly
- Rotate quickly when needed

**3. Rebounding:**
- Box out every time
- Go after the ball aggressively
- Secure the ball before looking to push
- It's not over until you have the ball

**My Favorite Defensive Players:**
- **Kawhi Leonard** - The Claw's hands and instincts are unmatched
- **Rudy Gobert** - A defensive anchor who changes everything
- **Marcus Smart** - Heart, hustle, and defensive IQ
- **Draymond Green** - The ultimate defensive communicator

**Defensive Drills to Practice:**
- Closeout drills
- Defensive slides
- One-on-one defense
- Help and recover
- Defensive rebounding

Remember: Offense sells tickets, but defense wins games. Put in the work on the defensive end, and your team will thank you.

What's your favorite defensive play or moment? Let's talk defense! 🛡️''',
                'category': 'Defense',
                'date_posted': datetime.utcnow() - timedelta(days=2)
            },
            {
                'title': 'The Mental Game: Basketball Psychology',
                'content': '''Basketball is as much a mental game as it is physical. The best players aren't just skilled - they're mentally tough, focused, and confident. Let's talk about the mental side of the game.

**Confidence:**
Confidence comes from preparation. When you've put in the work, you trust your abilities. Miss a shot? Shoot the next one with confidence. Make a mistake? Learn from it and move on. Confidence is built through:
- Consistent practice
- Preparation
- Positive self-talk
- Visualization

**Focus:**
The game moves fast. You need to stay present, stay focused. Don't dwell on past mistakes. Don't worry about future plays. Focus on the current possession, the current moment. This is where mindfulness meets basketball.

**Resilience:**
You're going to miss shots. You're going to make mistakes. The great players bounce back. They have short memories for failures and long memories for successes. Resilience is:
- Getting back up after falling
- Learning from losses
- Staying positive
- Never giving up

**Pressure Situations:**
Some players thrive under pressure, others crumble. The difference? Preparation and mindset. When the game is on the line:
- Trust your training
- Stay calm
- Focus on the process, not the outcome
- Breathe

**My Mental Game Routine:**
1. Visualization before games
2. Positive affirmations
3. Focus on what I can control
4. Learn from every game
5. Stay present in the moment

The mental game separates good players from great ones. Work on your mind as much as you work on your body.

How do you stay mentally strong on the court? Share your strategies! 🧠''',
                'category': 'Mental Game',
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
                    date_posted=post_data['date_posted'],
                    category=post_data.get('category')
                )
                db.session.add(post)
                created_count += 1
                print(f"[+] Created post: {post_data['title']}")
            else:
                print(f"[~] Skipped existing post: {post_data['title']}")
        
        db.session.commit()
        print(f"\n[SUCCESS] Successfully created {created_count} blog posts!")
        print(f"[INFO] Total posts in database: {Post.query.count()}")

if __name__ == '__main__':
    print("Populating basketball blog posts...\n")
    populate_blog()







