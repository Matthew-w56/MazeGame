# MazeGame
 A python project where the player solves mazes
<p><br>
This project started when I was around 15.  I was just starting to code and wanted to make some kind of playable game in Python, with graphics easy enough that
I could do it without needing to do a ton of art.  So I made this little game where the player traverses a maze, and is occationally chased by an enemy.
<p><br>
As I made the project, I remember a few snags I ran into that I had to solve.<p>
<ul><li>One of which was the layout of the maze.  A year or two later, I would learn how maze generation algorithms work, and build a project that dynamically generated
mazes for the player to go through.  But for this one, I ended up settling on a tactic where I could design the maze myself, and have it built in the game without having
to hardcode wall objects for every block that I wanted.  I did this by setting up the layout in an array of strings, with different characters represeting different
objects such as the player's start position, the goal, walls, barriers, etc.  This way, I could visually see and design the maze levels without a ton of hardcoding.
 </li>
 <li>
  Another snag I hit was the player's interaction with the maze.  Designing the physics so that the player could move around, and have their movement restricted to
  the walls of a map I had designed in an array of Strings was something that took a few different attemps, as well as some research on what others had done.  I ended
  up getting it figured out and I was happy with the resulting functionality and efficiency.
 </li></ul>
 
 <p><br>
  So overall I'm pretty proud of this project.  Especially because of how early on in my coding experience I was already finding things that interested me enough to
  work out the details in a test project that I could have some fun with as I grasped how it all worked.
