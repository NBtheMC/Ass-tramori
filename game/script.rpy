# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define to = Character("Tony", who_color="#769c69")
define ti = Character("Tina")

define pc = Character("Me")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "It’s only been a few days since I moved to the city, but I’d be lying if I said I was enjoying it."

    "After spending all of my time being bored out of my mind in my room, I reluctantly decided to check out the area looking for something interesting."

    scene bg arcade

    "After some stumbling around, I came across this neat arcade. I look through the window. Pink neon lights, fuzzy carpeting, and a shadowy, harrowing atmosphere. Perfect vibe for an arcade."

    "I check out some of the cool cabinets littered around the room. Some fast-paced game about… elevators? This one here is about throwing little green creatures around. Oh, what’s this one? Assterion?"

    "It’s a classic retro game from the looks of it. The demo shows a small ship frantically weaving between a fleet of alien ships. And also some pink squares. Not sure what those do."

    "The screen changes to a large, blinking “INSERT COIN,” so I head over to the coin machine on the other side of the room. I insert a dollar and get some quarters."

    ti "Hm, what’s this? Oh great, someone found their way in here. Well, it’ll be fun scaring them outta here at least. {p}{i}ehehe{/i}"

    to "Tina, what the hell is that noise? Don’t tell me… another guest? {w} {i}Sigh{/i}. {w} It’s been a few years since the last one. Can’t people give me some privacy? I just need to think of a way to get them out of here…"

    "Okay… here we go. {w} Gamer Time."

    "I familiarize myself with the controls. Spin and shoot. Got it. I quickly boost around the screen. Oh there’s the first alien ship! {w} I blast it down, turn the corner, and - BOOM! - straight into another ship. {w} Oops."

    "I’ll give it another try."

    "Okay… a few ships are down. Now’s my chance to make it to the end and - {w} DAMMIT! - one of the larger ships shoots me from behind. {w} That’s fine. I’ll just get more quarters…"

    to "Wow… this new player is… intriguing. Just watching them makes me lost for words…"

    to "they’re just so…"

    to "Terrible at Assterion! Maybe I’ll observe them for a bit from the shadows… I could use some entertainment."

    ti "What’s that Tony? A new contender? Ooh, it will be fun to watch them try to reach the leaderboard. "

    "Narrator" "While Tony slithers away into the shadows, Tina squeezes herself underneath an arcade cabinet across from the Assterion cabinet."
    
    "Narrator" "The words “Asstramori” are scratched out at the top of the cabinet, replaced by an etching saying “TINA’S SECRET DEN.” Tina slowly watches the new player’s every movement."

    "Narrator" "Tony peeks his head around a dark corner, making sure not to be seen."

    "I open my phone. It’s fully charged. Huh, I could’ve sworn my battery was low when I got here. I ignore it, looking instead at the time."

    "What??? I got here 3 hours ago? If only felt like a few minutes! I should probably leave soon… but… There’s something special about this game. I have unfinished business here."

    "Under my breath, I mutter that I’m determined to keep playing."

    "Tony/Tina" "Oh."

    pc "And I WON’T LEAVE UNTIL I MASTER IT!"

    "Tony/Tina" "Oh no."

    # This ends the game.

    return
