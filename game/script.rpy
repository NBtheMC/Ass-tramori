﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define to = Character("Tony", who_color="#769c69")
define ti = Character("Tina")

define audio.masks = "audio/MasksRequired.mp3"
define audio.tsunderion = "audio/Tsunderion_v2.mp3"

image tina normal = "images/Tina_1.png"
image tina upset = "images/Tina_2.png"
image tina blush = "images/Tina_3.png"
image tina inactive_normal = im.MatrixColor(
    "images/Tina_1.png",
    im.matrix.tint(0.45, 0.45, 0.75)
    *im.matrix.brightness(-0.07))
image tina inactive_upset = im.MatrixColor(
    "images/Tina_2.png",
    im.matrix.tint(0.45, 0.45, 0.75)
    *im.matrix.brightness(-0.07))
image tina inactive_blush = im.MatrixColor(
    "images/Tina_3.png",
    im.matrix.tint(0.45, 0.45, 0.75)
    *im.matrix.brightness(-0.07))

image tony up = "images/Tony_1.png"
image tony down = "images/Tony_2.png"
image tony normal = "images/Tony_3.png"
image tony inactive_up = im.MatrixColor(
    "images/Tony_1.png",
    im.matrix.tint(0.45, 0.45, 0.75)
    *im.matrix.brightness(-0.07))
image tony inactive_down = im.MatrixColor(
    "images/Tony_2.png",
    im.matrix.tint(0.45, 0.45, 0.75)
    *im.matrix.brightness(-0.07))
image tony inactive_normal = im.MatrixColor(
    "images/Tony_3.png",
    im.matrix.tint(0.45, 0.45, 0.75)
    *im.matrix.brightness(-0.07))

define pc = Character("Me")

transform midright:
    xcenter .66

transform midleft:
    xcenter .33


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play music masks

    "It’s only been a few days since I moved to the city, but I’d be lying if I said I was enjoying it."

    "After spending all of my time being bored out of my mind in my room, I reluctantly decided to check out the area looking for something interesting."

    scene bg arcade nofilter
    with fade

    "After some stumbling around, I came across this neat arcade. I look through the window. Pink neon lights, fuzzy carpeting, and a shadowy, harrowing atmosphere. Perfect vibe for an arcade."

    "I check out some of the cool cabinets littered around the room. Some fast-paced game about… elevators? This one here is about throwing little green creatures around. Oh, what’s this one? Assterion?"

    "It’s a classic retro game from the looks of it. The demo shows a small ship frantically weaving between a fleet of alien ships. And also some pink squares. Not sure what those do."

    "The screen changes to a large, blinking “INSERT COIN,” so I head over to the coin machine on the other side of the room. I insert a dollar and get some quarters."

    show tina normal at midleft
    with dissolve

    ti "Hm, what’s this? Oh great, someone found their way in here. Well, it’ll be fun scaring them outta here at least. {p}{i}ehehe{/i}"

    hide tina normal
    show tina inactive_normal at midleft

    show tony down at midright
    with dissolve

    to "Tina, what the hell is that noise? Don’t tell me… another guest? {w} {i}Sigh{/i}. {w} It’s been a few years since the last one. Can’t people give me some privacy? I just need to think of a way to get them out of here…"

    hide tony down
    show tony inactive_down at midright

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

    scene bg arcade nofilter
    with fade

    pc "Gosh dangit!"

    to "Jeez, how many quarters is that now?"

    ti "I don’t know. I lost count."

    to "It’s a bit concerning, ain’t it? This person looks like they’re in college. That’s probably ramen money they've been pouring into the machine all this time."

    to "And to be honest, I’m kind of getting annoyed seeing them die at the same spot every time. You’d think they’d learn by now."

    ti "Should we stop them?"

    to "Maybe… Wait, I have an idea!"

    ti "Oh?"

    to "Check this out!"

    pc "H-Huh? What’s going on?"

    pc "WHY ARE THE CONTROLS SUDDENLY INVERTED!?"

    "Narrator" "While in the middle of your game, you suddenly find that the game’s controls aren’t responding the way they’re supposed to. Left has become right, up has become down, and vice versa."

    "Narrator" "Naturally, this led to a lot of swearing and frustration."

    pc "How the fuck am I supposed to-"

    pc "Aaaand I died."

    pc "{i}*sigh*{/i} Maybe I should take a break. There’s a bunch of other games I haven’t tried yet."

    ti "Guess that was the final nail in the coffin for them, huh."

    to "Heh heh, that was kinda fun actually."

    ti "Should we follow them? I kind of want to mess around with them a bit."

    to "You read my mind. Come on, let’s see where they scurried off to."

    pc "Let’s see… Oh hey, this one looks kinda cute!"

    "Narrator" "Having spotted from the corner of your eye some sort of farming inspired rhythm game, you find yourself drawing quarters from your pockets once again."

    pc "Ah, this is a nice change of pace. No bullshit inverted controls to fuck me over this time."

    ti "Oh, you poor soul…"

    to "Care to do the honors?"

    ti "Mhm, I already have something in mind for this one."

    pc "Looks like the level is almost, and I haven’t missed a single note."

    pc "Heh, guess i’m just that much of a ga-"

    pc "W-Wha? Did the game just freeze?"

    pc "Come on! I was so close to the finish!"

    "Narrator" "You frantically mash the buttons on the arcade machine, but to no avail. But then, something strange suddenly starts happening."

    pc "T-The notes… they’re moving backwards! And the music..."

    "Narrator" "Taking a step back from the machine, you stare in horror at the screen as the eerie sound of music being played in reverse fills their ears."

    to "Not bad, but I think we can take it a step further."

    pc "God, what is it with all the games in this arcade? Are they all haunted or something?"

    ti "Uh oh, I think they’re onto us."

    to "Nah, don’t worry. They’ll never suspect that there are two funny little dudes living in a bunch of arcade machines."

    ti "True. Afterall, it’s been quite a while since we’ve last made our presence known to a person."

    to "Here, let’s turn off the lights. That’ll really send ‘em."

    ti "Oh, I don’t know, I think that might be going a bit too-"

    pc "EEK!"

    pc "W-WHY DID THE LIGHTS TURN OFF!?"

    pc "OH GOD OH FUCK THIS PLACE REALLY IS A CREEPYPASTA AINT IT."

    ti "What’s a creepypasta?"

    to "Some kind of halloween themed pasta i’m sure."

    pc "AAAAGHGGHOIARNGAAOPSEHRN"

    ti "Oh dear, they seem to be in quite a frenzy."

    to "Yeah."

    to "…Huh, maybe we went a bit too far."

    pc "I WANT TO GO HOME. I WANT TO GO GO HOME. I WANT TO HOME."

    ti "Oh no, I think they’re on the verge of crying."

    to "Oops."

    ti "Here, I’ll turn the lights back on."

    pc "Oh… oh thank god, the lights are back…"

    pc "I-I’m getting out of this place! I’m filing a complaint first thing in the morning."

    to "Gee, I kind of feel bad now…"

    ti "Perhaps we should apologize?"

    to "Won’t that make things worse? I’m sure they might just pass out from the shock."

    to "I mean… look at us."

    ti "Oh I’m sure it’ll be fine. They’ll get over it once we explain ourselves."

    show tina inactive_normal at midright

    "..."

    ti "Hello!"

    pc "{i}*Incomprehensible screaming*{/i}"

    show tony inactive_down at midleft

    to "Hey hey, relax! We’re not out here to hurt you."

    pc "What the hell is wrong with this town!?"

    ti "Now now, I’m sure we aren’t the type of creatures you’re used to looking at, but I assure you, we mean no harm."

    pc "R-Really?"

    to "Indeed, we usually don’t make our presence known, but we felt the need to apologize."

    pc "Apologize? Apologize for what?"

    ti "All the weird glitches you noticed earlier? Well… that was our doing."

    pc "I… I see."

    pc "..."

    pc "Well, in hindsight, I guess it was kinda funny."

    ti "Oh that’s so good to hear? We were worried you might’ve been traumatized."

    pc "Well, you were certainly getting there."

    to "We might have gone a bit too far there at the end. Sorry about that."

    ti "Yeah, can we make it up to you somehow?"

    pc "Hm…"

    pc "How about a date?"

    to "…Huh?"

    ti "Excuse me?"

    pc "Sorry, weird question. Forget I asked."

    to "Um…"

    ti "What’s a date?"

    pc "What?"

    to "By date, you’re not talking about the thing used to mark time, right?"

    pc "Oh."

    pc "You two really don’t know what a date is?"

    ti "Not the date you’re speaking of, it seems."

    pc "…Huh. Didn’t think I would ever have to explain this but…"

    pc "…"

    pc "Well, it’s basically when two people hang out together and… do stuff."

    ti "What kind of stuff?"

    pc "Anything, really. So long as the two of you bond over it and get to know each other somehow."

    to "I see. I’m afraid neither of us can leave the arcade though."

    pc "That’s fine. We can just… check out the games I guess."

    ti "But, you said that a date is an act between two people, correct?"

    to "Then that means…"

    ti "There can only be one…"

    pc "Uh, yeah. Although when you say it like that, it sounds a bit ominous."

    to "So, which one of us will it be?"

menu:

    "Tina. Tina. Tina? I pick Tina. Tinnaaaaaaa":
        pc "Tina, I guess…"

        ti "Yay! This is going to be so much fun."

        to "Ah well, have fun you two. I’m going to find some other players to mess with."

        hide tony inactive_down
        with dissolve

        show tina inactive_normal at center
        with moveinright

        $ c = ti

        $ tina = True

        ti "Bye!"

        pc "{i}As if today couldn’t get any weirder… and now i’m here taking a funny moth woman on a date…{/i}"

        jump act3


    "Tony. Yiss, Tony. Tony is good. Tony is life.":
        pc "Tony, I guess…"

        to "Heck yeah! We’re gonna have a great time together, I promise you."

        ti "Ah well, have fun you two. I’m going to find some other players to mess with."

        hide tina inactive_normal
        with dissolve

        show tony inactive_down at center
        with moveinleft

        $ tina = False

        $ c = to

        to "Have fun!"

        pc "{i}As if today couldn’t get any weirder… and now i’m here taking a funny skeleton man on a date…{/i}"

        jump act3

label act3:

    pc "Well, you mind showing me around? I bet you know all kinds of cool secrets about this place, right?"

    c "Oh uhm…yeah sure. There’s no reason to hide from you anymore, so…"

    if tina:
        pc "Oh my…your antennae are lovely…"
    else:
        pc "Oh my…your antlers are lovely…"

    c "Ah…th-thanks…"

    pc "Hey, now that I can see you more clearly…do I know you from somewhere?"

    pc "Wait a minute…you’re in that game that I was playing just now, right? Assterion?"

    if tina:
        ti "Well, I was going to be…but I dipped out of it! I don’t really have the stomach for horror stuff, you know? …Guess that’s a little strange, huh?"
    else:
        to "Yeah…that was just an acting gig though. There’s not a lot of work out there for someone like me, so I take what I can get. I promise, I’m really not that scary of a guy."

    pc "That makes sense. You don’t really strike me as that kind of…person? Monster…?"

    c "Monster is just fine!"

    pc "Cool! Thanks for letting me know."

    c "Hm…so you wanted to see some secrets, yeah? There’s a hidden hall down this way with a few machines at the end. Want me to show you the way?"

    pc "Yeah! That sounds cool."

    c "Alright! Here, take my hand. It’s dark in there, so I just want to make sure you don’t fall and hurt yourself."

    pc "Th…thanks…"

    scene bg claw
    if tina:
        show tina inactive_blush
    else:
        show tony inactive_up
    with fade

    pc "Oh wow! These claw machines are awesome!"

    c "Ah yeah…I’m no good at these ones though. I’ve never been able to get any of the big prizes."

    pc "Well, do you want one?"

    c "Oh I mean…sure! But how?"

    pc "I wouldn’t say I’m too good at these either, but if it’s for you, I’ll definitely try my best to win you something! Which prize would you like?"

    if tina:
        ti "Gosh, you’re so sweet! Hm…how about those stuffed animals over there?"
    else:
        to "Ah, I’m usually not that picky…maybe one of those stuffed animals?"

    pc "Sure! Let’s see…"

    if tina:
        "You insert a quarter into the claw machine. Aiming for the stuffed animal, you press the button, the claw descending upon a pile of prizes."

        "Tina leans close to you, as you both watch the claw grab onto your desired prize! By some miracle, it doesn’t let go, and the celebratory lights fill the room, reflecting in Tina’s twinkling eyes."

        ti "WHAAAT? How did you get it on the first try!?"
    else:
        "You insert a quarter into the claw machine. Aiming for the stuffed animal, you press the button, the claw descending upon a pile of prizes."

        "Tony leans close to you, as you both watch the claw grab onto your desired prize! By some miracle, it doesn’t let go, and the celebratory lights fill the room, reflecting in Tony’s twinkling eyes."

        to "Dang, you got it on the first try? Guess I’m not much of a gamer…"

    pc "Heh, it’s just beginner's luck."

    c "Wow…well, thank you!"

    pc "No problem! I barely noticed while having all this fun with you, but it’s getting pretty late. I should get going soon."

    c "You know…usually I don’t enjoy visitors, so I try and scare them away…but you’re free to come back whenever you’d like."

    pc "In that case, I think you’ll be seeing a lot of me. I’ll stop by again tomorrow, see you then!"

    if tina:
        ti "Hehe, I had a lot of fun today! I gotta get this place cleaned up before the human comes tomorrow!"

        ti "…it’s not like I like them or anything though…"
        hide tina inactive_blush
    else:
        to "Hm…that human wasn’t half bad. I hope they come by often…"
        hide tony inactive_down

    scene black
    with fade

    show text "Nik Thomas, Parmpreet Gill, Stevie Rodriguez - Writing \n Annie Zhang, Tiana Chamsi - Character Art \n Andrew Dunne - Background Art \n Joshua Augenstein - Programming \n Autumn Moulios - Music" at truecenter

    "Thank you for playing!"

    return
