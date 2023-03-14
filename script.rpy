image ctc_blink:
       "GUI/arrow.png"
       linear 0.75 alpha 1.0
       linear 0.75 alpha 0.0
       repeat

define narrator = Character(ctc="ctc_blink", ctc_position="nestled")
define s = Character("{b}{font=slabfont.ttf}[slabname]{/font}{/b}", color="#18AAF6", ctc="ctc_blink", ctc_position="nestled")
define dr = Character('{font=Justly.ttf}Don Rocko{/font}', color="#c49d00", ctc="ctc_blink", ctc_position="nestled")
define sb = Character('{font=njnaruto.ttf}Slaborro{/font}', color="#B92A3D", ctc="ctc_blink", ctc_position="nestled")
define l = Character('{font=Pulang.ttf}Leif{/font}', color="#1d9e03", ctc="ctc_blink", ctc_position="nestled")
define q = Character('{font=coolvetica.otf}???{/font}', color="#575757", ctc="ctc_blink", ctc_position="nestled")
define username = Character("{font=coolvetica.otf}[username]{/font}", color="#18AAF6", ctc="ctc_blink", ctc_position="nestled")
define sc = Character("{font=coolvetica.otf}Slabcashier{/font}", color="#575757", ctc="ctc_blink", ctc_position="nestled")
define sa = Character("{font=coolvetica.otf}Slabraham{/font}", color="#575757", ctc="ctc_blink", ctc_position="nestled")
define scc = Character("{font=coolvetica.otf}Slabchef{/font}", color="#575757", ctc="ctc_blink", ctc_position="nestled")

label start:

    python:
        slabname = renpy.input("{b}What is your name?{/b}{p}", length=40)
        slabname = slabname.strip()

        if not slabname:
             slabname = "Slabname"

    scene bg starry night with fade

    "{i}\"Slabsune Miku, I...\"{/i} Sailor Slab turns to Slabsune Miku."

    "The moon and the stars fill the night sky with light, but Sailor Slab… she’s only ever had eyes for one star."

    "Her slabstar."

    "Slabsune Miku sees Sailor Slab looking at her intently, and she blushes. Could it be...?"

    "{i}\"Y-Yes?\"{/i}"

    "Sailor Slab places her Stellar Stick down beside her and cups Slabsune Miku’s face with her hands. It’s now or never."

    "{i}\"Slabsune Miku, I—\"{/i}"

    scene bg forest with fade

    "{i}*CRASH* *THUD*{/i}" with vpunch

    "I jump when a loud noise echoes through my room."

    s "Huh? What was that?"

    "I look around me. Nothing seems odd until my eyes land on—"

    s "A rock?"

    "Curious, I hop out of my slab-bed and make my way towards the rock. Picking it up, it's small but heavy. It definitely would have landed with a loud thud."

    s "How in the world?"

    "The tree hollow that I live in is high up in a very, very tall tree. Someslab definitely threw this up here."

    s "Let's see..."

    "I go back to my slabtop and save my slabfic by pressing the cute little {b}save button{/b} at the bottom of the page."

    "I don't want to lose any progress on my magnum opus!"

    "I also stop by my desk and grab my Limited Edition Sailor Slab Stellar Stick™ just in case I need to fight some bad slabs."

    "Feeling a bit braver, I walk up to the opening of the tree and peer outside: only green grass and a summer breeze greet me."

    "Something is pushing me to investigate further, so I crawl down the trunk. I take a deep breath to stop myself from shaking."

    s "I have to calm down. I can’t let anything catch me off-guard."

    "My feet touch the soft grass and any fear in my mind washes away. The sun’s out, the wind’s cool; it’s just a beautiful, sunny day. I breathe a sigh of relief."

    "What could possibly go wrong?"

    "..."

    "..."

    "..."

    "As if on cue, I hear scurrying come from all directions. A few seconds later—"

    scene bg black with fade
    window show dissolve

    "—everything goes dark—"

    "—and I get swept off my feet... but not in a good way."

    s "Hey, what the—"

    "The thing around my eyes gets tightened by someslab I can’t see. I’ve read enough mystery novels to know that it's probably a blindfold."

    s "Let me go!!! This is {i}SO{/i} rude!"

    "I hear slabs whispering amongst themselves, but they don’t do as I say. The nerve!"

    "A squeaky voice finally addresses me."

    q "Just checking, but are you [slabname]?"

menu:

    "The one and only!":

        jump name

    "And what if I am?":

        jump noname

label name:

    s "Born and raised! There isn't another slab in the world like me!"

    "Oh, I forgot to introduce myself! I'm [slabname]! Cute, isn’t it? My slabmom picked it out just for me! A pretty little slab, I would hear her call me even now..."

    jump slabnap

label noname:

    s "Who's asking, huh?"

    "This feels like a good time to introduce myself! I'm [slabname], the only slab with the name [slabname] in the whole world! Pretty cool, right?"

    jump slabnap

label slabnap:

    q "Okay. We've got the right one."

    s "What?!"

    "I feel myself get carried into the air by at least six other slabs. One slab says something to another slab in hushed tones before the slabcar takes off."

    s "Woah, wait! Where are we going?"

    "My words fall on deaf ears. The slabs are too focused on going fast, maybe because they need to get away from the scene of a {b}CRIME!!!{/b}"

    "Despite making turns every which way and speeding up and slowing down at random intervals, the ‘drive’ to wherever they're taking me is a smooth one."

    "None of the slabs dip or falter, and I simply lie there, as comfortable as I can be given the circumstances."

    "After what feels like forever, the slabcar stops. They slowly set me down."

    s "Where… where are we?"

    "I say nervously, but none of the slabs answer. Instead, one of them takes my hand and guides me further into the premises."

    "Why is my heart fluttering?!"

    "{cps=4}{i}*CREAK*{/i}{/cps}"

    "We stop at the sound of giant doors opening. I hear slabs speaking just out of earshot. I focus really hard, but the only thing I can parse is a quiet ‘mhm’."

    "With that, my slabguide continues walking, and I have no choice but to walk with them."

    "We walk down flights of stairs, saying nothing to one another. What is there to say? I {i}am{/i} getting slabnapped after all."

    "As if the air was getting agitated by the silence, the opening strains of a slabrap song begins echoing through the premises."

    "{i}As I walk through the valley of Serpent’s Lagoon,{p}I take a look at my life and realise it’s ending too soon...{/i}"

    s "Slab… {i}Slabster’s Paradise?{/i} This song is so old! Who would still be listening to this?"

    "Even though I can't see the other slab, I imagine they just shrug at my question."

    "Losing myself in the lyrics of {i}Slabster’s Paradise{/i}, I don't realise that I'm being seated down on a chair."

    "The reality of the situation I'm in comes flooding back when I feel the blindfold loosen and..."

    window hide dissolve
    pause 1.0
    scene cias with dissolve
    pause 3.0
    scene bg mansion with fade
    window show dissolve

    q "Hello there."

    "Before the blindfold falls, this… suave, dulcet voice greets me. My heart flutters in spite of the situation I'm in."

    "Who… who could it be?"

    "I wait with bated breath for the blindfold to fall. Could the slab sitting in front of me be my {i}destiny{/i}? My slab in shining armor?"

    "Light quickly floods my eyes."

    "Once they adjust, I look around for the slab with the striking voice, but the only thing I see in front of me is the surface of a large table that separates me from an empty chair."

    s "Who... Who...?"

    q "Um..."

    "I hear whispering come from under my feet. Immediately, the other slabs who were standing by the walls of the vast hall we're in run towards the table."

    "I go to speak, but they completely ignore me, focusing their attention on the empty chair opposite me instead. The slabs climb up the chair and form a neat little stack."

    q "That's better."

    "A golden slab wearing a small fedora climbs up the slabstack and sits himself right on top, like royalty on their thrones."

    "Settled, he turns to face me and grins."

    show don rocko blush at center with dissolve

    q "Hello there."

    "Tealights scattered around the table give the slab a warm, almost heavenly, glow. Is this..."

    "Could this be...?"

    q "Please allow me to introduce myself..."

    q "I am {i}Don Rocko{/i}."

    "Don Rocko tips his fedora at me and winks."

    show don rocko neutral at center with dissolve

    dr "It {i}is{/i} your pleasure to make my acquaintance."

    "This... This is {i}the{/i} Don Rocko? He's a lot smaller than I thought. Not that height matters but you know..."

    "I’m speechless, but that doesn’t seem to bother Don Rocko one bit. He continues speaking as if I wasn’t there."

    dr "It is your very lucky day—"

    "Don Rocko's eyes quickly dart down to look at a note on the table."

    dr "[slabname]!"

    "Seriously? He forgot my name?"

    "Still, he continues his speech without missing a beat."

    dr "For I, Don Rocko, have selected you to be my new—"

    "He pauses as he gestures for one of his slackeys (slab lackeys) to come over. The slackey brings over a small rose, which they hand to Don Rocko."

    show don rocko happy at center with dissolve

    dr "—slablover!"

    "With a flourish, he offers the rose to me."

    show don rocko blush at center with dissolve

    dr "Please, try to contain your excitement!"

    s "I—"

    dr "Yes, it is quite an honor."

    "Before I can take the rose from him, Don Rocko simply places it on the rim of his hat. Admittedly, it does look quite dashing on him."

    show don rocko neutral at center with dissolve

    dr "Of course, there are many perks to being my slablover other than the pleasure of being in my presence—"

    "With a wave of his hand, a slackey pushes a brown and gold box closer to him."

    dr "—such as being the first slab to hear my funny jokes—"

    "He lifts the lid off the box, revealing neat rows of what I think are little chocolates wrapped in gold foil."

    dr "—as well as all of my very important thoughts."

    "They sit snugly atop dark brown paper liners accented with golden zigzags. I squint and see that they're decorated to look like Don Rocko himself, tiny fedora and all."

    "He plucks one of the chocolates from their bed and unwraps it, promptly popping it into his mouth."

    dr "Ferrorockos!"

    "He lifts up the box to show me the label."

    dr "The best chocolate in the world! Am I right?"

    "Don Rocko turns to his slackeys and they immediately cheer to hype him up. I can’t help but wonder if they’ve actually had the chance to try it."

    dr "Now, where was I?"

    "He taps on the table to re-find his train of thought."

    dr "Ah, yes."

    "He picks up another Ferrorocko."

    dr "On top of all of the aforementioned perks, you also get to live in this {i}very{/i} grand establishment!"

    show don rocko happy at center with dissolve

    "Don Rocko, triumphant, looks around proudly at his castle."

    dr "My greatest design… So beautiful..."

    "He pretends to wipe a tear from his eye."

    dr "Rest assured, [slabname]! You will want for {i}nothing{/i}!*"

    "An... asterisk?"

    dr "And we'll be very happy together!*"

    "Another one?!"

    dr "So, what do you say?"

    s "I—"

    show don rocko neutral at center with dissolve

    dr "I'll give you some time to think about it, of course."

    "Can I {i}please{/i} get a word in?"

    dr "But you’ll need to make a decision... preferably in the next 10 minutes."

    "A slackey swiftly whispers something in Don Rocko's ear before walking back to where they were standing. Don Rocko clears his throat."

    dr "I’ve been informed that 10 minutes is an unreasonable time frame to set. Do you know how long it will take for you to decide?"

    "Talk about pressure! Any more and I might just turn into a diamond."

    s "Uh, give me until tomorrow night?"

    "Don Rocko nods slowly."

    dr "Fine, but no extensions."

    "Am I really being asked to...?"

    "But I have a life and a home already..."

    "Can I just leave that all behind?"

    s "May I be excused? I'd like to, um, freshen up."

    show don rocko angry at center with dissolve

    dr "Freshening up? You're not going to try and escape, are you?"

    "I pout and bat my eyes cutely."

    s "But I've gotta look my best... for you!"

    show don rocko blush at center with dissolve

    "Don Rocko blushes slightly before shrugging, trying to look cool and distant and totally not freaking out internally at all."

    dr "Well, there’s no chance you’re getting out anyway. The bathroom’s down the hall or, uh... somewhere, I'm sure. I trust you can find your own way there."

    q "Sir."

    hide don rocko neutral
    show slaborro shadow
    with dissolve

    "A shadowy figure approaches Don Rocko from behind, taking long, purposeful strides towards us. The more their silhouette gains definition, the more the hair on the back of my neck stand up."

    "They lean in and speak in Don Rocko's ear, but make no efforts to hide what they're saying."

    q "It's not wise for someslab we don't know to be wandering the mansion unattended."

    "The slab throws a sharp glare at me. I try my hardest to keep my eyes level with theirs."

    show slaborro neutral at center with dissolve

    "Well, one eye. An eyepatch held down by a golden slab pin covers their left eye. I focus on keeping my gaze steady, but the dents and scars that cover their body prove to be distracting."

    "What stories they must have as to how they got them...!"

    show don rocko angry at left
    show slaborro neutral at right
    with dissolve

    dr "Now, now, {i}Slaborro{/i}..."

    "Don Rocko beckons for Slaborro to stand by his side. My eyes are naturally drawn to their arms and legs, which are wrapped neatly in fresh bandages."

    "The little red flowers in their hair, quaint as they may be, do little to soften their rough and tough exterior."

    dr "Need I remind you that you work for {i}me{/i}, and you will do as I say! Have you forgotten what this—"

    "He presses his fingertip on the golden pin."

    dr "— very limited-edition, one-of-a-kind, never-to-be-sold-again-unless-I-need-money golden Don Rocko badge on your lapel means?"

    "Slaborro lets out a resigned sigh before walking back to the rest of the slackeys. Their eye, however, always seems to be fixed on me."

    hide slaborro neutral
    show don rocko neutral at center
    with dissolve

    "I avert my gaze, hoping that it'll help curb this feeling of vulnerability. "

    "Don Rocko turns back to me and laughs heartily."

    dr "Don't you worry about her! She's my bodyguard. Means well and all but you know—"

    "He feigns an exaggerated yawn."

    dr "Such a {i}buzzkill{/i} sometimes! A real pain in the slab! Sheesh!"

    "Don Rocko asks a couple of slackeys to help me down from my chair, continuing to mutter slights at Slaborro’s expense."

    dr "Definitely needs to chisel out... seriously..."

    "Weary as they look, they do their best to assist me."

    s "Thank you!"

    hide don rocko neutral with dissolve

    "Don Rocko waves his hands in a shooing gesture, and I take that as my cue to ‘go to the bathroom’ and ‘freshen up’."

    window hide dissolve
    window show dissolve

    "I find it almost amusing that Don Rocko could be so gullible… or am I just that charming?"

    "... Or good at lying?"

    "Still, I take the opportunity to ‘explore’. I could just as easily say I got lost if I got caught anyway; there are {i}so{/i} many different halls and hallways, paths and passages..."

    "Aren’t labyrinthes meant to be outdoors?"

    "I wander aimlessly until I see a particularly shadowy corner of the castle. Completely ignoring any and all of my survival instincts, I walk closer to investigate."

    "A menacing-looking door towers over me, but there doesn’t seem to be any slabguards around. The door was also left open ever so slightly, leaving just enough space for me to slip inside."

    "I take a deep breath and scoot through the opening."

    scene bg black with fade
    window show dissolve

    "It’s like I’ve been dumped into a vat of ink. Any light coming from the outside is devoured by a dark, pitch black void."

    "Mustering what’s left of my courage, I keep walking forward, sticking close to the wall so I have something to lean on, until—"

    s "Oh no."

    "The wall disappears, my foot steps on nothing but air."

    "I tumble blindly into the shadowy depths."

    "Given that my head alternates between hitting concrete and nothing whilst falling in something of a spiral motion, it’s safe to say I’m rolling down a spiral staircase."

    "After an eternity, I reach the base of the stairs, crashing hard and fast onto bitterly cold ground."

    q "Are you okay?"

    "I hear a voice call out to me."

    s "Who - where are you?"

    q "Um... open your eyes."

    "Not realizing that my eyes are closed, I open them and see..."

    scene bg dungeon with fade
    show leif neutral at center with dissolve

    "...a dungeon of some sorts. How fitting."

    q "Good, it looks like you're all okay."

    "Looking up, I see a kind-looking slab staring at me."

    "The concern in their eyes softens my heart."

    s "Thank you...!"

    "I hop up and look around, but quickly realize there’s nothing to look at. It’s cold and dismal with the only source of light coming from a high window."

    "The slab is sitting behind metal bars, huddled up in blankets and basking in sunlight. In spite of their conditions, they seem to be in reasonably high spirits."

    "The slab themself is vibrantly green, the only shot of color in this dull place. Despite that, they’re quite worse for wear."

    "Bandaids, scars and scratches cover their whole body; a ball and chain is fastened to their leg."

    "Though the leaves atop their head wilt slightly, the mustache adorning their face is suspiciously well-kempt."

    q "May I ask what you’re doing down here? I haven’t seen your face before. Did Don Rocko get new slabguards?"

    "I shake my head."

    s "No, a potential slablover..."

    "The slab nods solemnly."

    show leif happy at center with dissolve

    q "Ah, what a predicament."

    "We share a giggle."

    s "I was just snooping around and found this place..."

    "..."

    s "Yeah, let's go with that."

    "They smile sympathetically."

    show leif neutral at center with dissolve

    q "It was quite a long fall down, hm? If you're feeling a bit dizzy, you're welcome to take a seat."

    "The green slab removes a blanket from around their shoulders before walking slowly to the bars. They fold the blanket into a neat square and offer it to me."

    q "It’s not much, but it does make it a bit easier to sit on the floor."

    "What a gentleslab! I walk over and graciously accept the blanket."

    s "Thank you so much!"

    "Not wanting to drag themself back to their usual spot (the ball and chain does look quite heavy to drag around), they sit opposite me."

    "They fiddle with their mustache as they wait for me to get settled."

    "I drape the blanket on the ground and quickly take a seat. It’s quite comfortable, providing just enough of a barrier from the cold ground despite how thin the blankets look!"

    "Taking a look inside their cell, it’s hard to miss just how gigantic it is when the space is completely devoid of anything."

    "The wall behind them is covered with tally marks, as well as other engravings that hint to the previous occupants of the cell."

    s "If you, um, don’t mind me asking, what the heck did you do to get on Don Rocko’s bad books?"

    "The kind slab shrugs."

    show leif sad at center with dissolve

    q "I wish I could remember, but I’m certain it was for a very silly reason."

    "They let out a deep sigh."

    q "All I remember is my name being called out in anger, and then Don Rocko getting his goons to drag me in here. The rest, as they say, is slabstory."

    "The slab jumps as if struck by lightning."

    show leif shock at center with dissolve

    q "Where are my manners? I neglected to introduce myself!"

    "They place a hand on their chest."

    show leif happy at center with dissolve

    q "I’m {i}Leif{/i}! It’s a pleasure to meet you."

    "I happily tell them my name in turn."

    l "[slabname]... A truly lovely name!"

    "I tell my heart to be still, but it doesn’t listen. They’re just so kind!"

    show leif neutral at center with dissolve

    l "I must admit, it’s been a long time since I’ve spoken with anyslab. Don Rocko’s slackeys are all too scared of him to linger around here..."

    "Leif looks over their shoulder, their eyes trailing up to the open window above."

    show leif sad at center with dissolve

    l "Soon I will be out there, free, alongside my fellow slabs..."

    "They ball their hand into a fist."

    l "I must. I must..."

    "Before I can ask about their escape plans, I hear slabs chattering up above. Stray bits of their conversation echo down to where we are."

    s "Ah! I need to head back!"

    show leif neutral at center with dissolve

    l "Of course! Go quickly!"

    "The smile that forms on Leif’s face is bright and sincere."

    show leif happy at center with dissolve

    l "I hope to see you again, [slabname]."

    "I blush scarlet and squeak out a goodbye before I take my leave."

    scene bg black with fade
    window show dissolve

    "It’s still super dark, but I manage to fumble my way up the stairs with much less trouble than before."

    "Still hearing the slackeys hovering outside, I wait in the shadows until they leave."

    scene bg mansion with fade
    window show dissolve

    "I jet out from the dungeon and run back to the main hall. Don Rocko and the others are still there; the only thing that changed was the spread of food now on the table."

    show don rocko neutral at center with dissolve

    dr "Ah, you've returned!"

    "I slow my pace to a walk, making my way back to my chair."

    show don rocko happy at center with dissolve

    dr "The food's simply {i}exquisite{/i}."

    "I’m not sure why I thought he’d wait for me before he started eating, but luckily I’m not all that hungry anyway."

    "Don Rocko asks the slabchef to describe the banquet in front of them."

    scc "Well, we got—"

    "Don Rocko nods after every dish is described in painful, {i}excruciating{/i} detail."

    dr "I must say, the pobble jelly is really quite delicious."

    scc "Glad ya like it, sir! Perfect dessert to follow up the slabby patties, yeah?"

    "Don Rocko and the slabchef go back and forth in that same fashion for what feels like an eternity."

    s "Um..."

    "Don Rocko, perhaps feeling my eyes boring into him, remembers that I’m here and quickly shoos the slabchef away."

    show don rocko neutral at center with dissolve

    dr "So!"

    "Don Rocko clears his throat in an attempt to lighten the mood."

    dr "How was your day?"

    "A genuine question for once? It’s almost too good to be true."

    s "Other than being taken here by force, it was fine."

    "My words drip with heavy sarcasm."

    dr "That's good to hear!"

    "I stifle back a sigh."

    dr "My day was great! You see, I run this business — I’m sure you’ve heard of it, very big business, very profitable — and it was so busy today like you wouldn’t {i}believe{/i}!"

    "And there he goes again."

    dr "You see, we get a {i}lot{/i} of clients — like, a {i}lot{/i} — and people love our wares! You know how it is, supply and demand and all."

    "He continues rambling about his emporium to nobody in particular. I tune him out and realise just how... soft this chair is..."

    scene bg black with fade
    window show dissolve

    "I can’t stop myself from nodding off."

    "In the brief moments when my eyes flutter open, I see that the other slabs are also leaning on each other, half-asleep as well. Even Slaborro struggles to keep her composure."

    dr "And that’s just how you make a {i}fortune{/i}!"

    scene bg mansion
    show don rocko happy at center

    "I jolt awake when Don Rocko’s impassioned words about money boom from out of him." with vpunch

    "Everyone else jumps to attention too."

    "Don Rocko, however, doesn’t seem to notice that nobody was listening to him. Instead, he looks me up and down and squints."

    show don rocko neutral at center with dissolve

    dr "Hm! I think my slablover is in need of better clothes."

    "Don Rocko makes some vague hand gestures in our general direction—"

    dr "A bit... gauche. Only the most refined threads are fit for the slab who’ll be by my side!"

    "—calling over his slackeys to get me and him off our chairs."

    dr "It’s high time we go clothes shopping, yes?"

    "Still a bit sleepy, I nod and go along with his plans."

    dr "Splendid!"

    "The slackeys bring me to Don Rocko, and the two groups of slabs mesh into one."

    show don rocko angry at center with dissolve

    dr "Go on now! We haven’t got all day!"

    hide don rocko angry with dissolve
    scene bg forest with fade
    window show dissolve

    "Our slabcar takes us on a journey through the forests—"

    s "It’s a beautiful day today!"

    show don rocko angry with dissolve

    dr "Too sunny."

    "—and to a nearby shopping area."

    scene bg cafe with fade
    show don rocko neutral with dissolve

    "Woah..."

    "It’s so grand and sophisticated compared to the slabmalls I usually shop at. There’s boutiques and cafes close to each other?! Am I in slabheaven?"

    dr "Do you see anything you like, slablover?"

    "I look around and marvel at the different clothes on display."

    s "It's so—"

    show don rocko shock with dissolve

    dr "No WAY!" with vpunch

    "Don Rocko cuts me off mid-sentence and takes my hand. He pulls me along with him as he runs to—"

    show don rocko happy with dissolve

    dr "A new cafe just opened up and we’ve got to go RIGHT NOW!"

    "I make no protests. The aroma of freshly baked goods wafts through the air, and I grow more excited as blurry figures in the distance take the shape of glorious cakes and pastries."

    s "They look so amazing!"

    "We make it to the cafe’s display window and press our faces on the glass."

    "Pebbling-shaped strawberries dipped in chocolate, seekling lava cakes flowing with molten chocolate, crabster cake pops..."

    "Iced shortbread shaped like cervabloom, baraboa swirl cookies, critter pretzels..."

    "So many to choose from!"

    s "What are you thinking of getting?"

    "A large grin forms on Don Rocko’s face."

    show don rocko neutral with dissolve

    dr "Heh."

    "Don Rocko and a couple of his goons enter the cafe as if they own it, walking with long strides over to the register where a confused slabcashier stands."

    dr "I would like..."

    "He points to the long, {i}long{/i} menu hanging on the wall behind the slabcashier."

    show don rocko happy with dissolve

    dr "... one of everything!"

    "Don Rocko cackles, prompting his slackeys to do the same."

    "They only manage to give half-hearted laughs, too busy figuring out the semantics of how they’re going to carry everything out of the shop."

    "Visible beads of sweat form on the slabcashier’s brow."

    sc "Uh, one... one of everything?"

    "Don Rocko nods enthusiastically."

    dr "I have said so, and so it shall be!"

    "He clasps his hands together."

    show don rocko neutral with dissolve

    dr "Quickly now! We haven’t got all day!"

    "The slabcashier furiously inputs all of the different food options into the register, muttering them under their breath to keep track."

    "The two other slabservers move just as swiftly as the slabcashier’s hands; one preps up take-away boxes as the other places pastries into them with admirable precision."

    "As soon as something is packaged, Don Rocko’s slackeys take it and convey it down a slabline, where poor slabs struggle to balance box upon box on their heads."

    s "Isn't this like... a lot?"

    dr "Nonsense."

    "He places payment for the order on the countertop before walking away, leaving his slabs to do the rest. I jog to catch up with him."

    dr "A feast for tonight, yes."

    "He speaks to himself, nodding every so often."

    dr "I deserve it for a hard day’s work, yes."

    s "Uh..."

    show don rocko shock with dissolve

    "He jumps, slightly red when he realizes I’m standing right beside him."

    dr "Oh, it’s you!"

    "Don Rocko goes to fix his fedora even though it’s completely straight on his head."

    show don rocko neutral with dissolve

    dr "Now, what were we doing again?"

    s "Clothes shopping?"

    "Don Rocko stops abruptly to collect his thoughts, rubbing his chin every so often."

    dr "Clothes shopping! Of course!"

    "Don Rocko takes my hand and pulls me along to some destination unknown. We pass by many different stores where I see something that catches my eyes—"

    "Woah, that hat looks—"

    "—but we don’t stop. He seems intent on going somewhere specific."

    dr "Almost there..."

    "I sigh lovingly at the clothing we pass by; a flowery dress on a hanger, a red pair of red overalls on display..."

    "So many vibrant styles and colors in equally dazzling boutiques, and yet—"

    dr "We’ve arrived!"

    "Don Rocko flies into a rich but gloomy-looking store without hesitation. It’s completely monochrome save the occasional touches of gold."

    s "Ah..."

    "The true reason why we came here dawns on me as Don Rocko beelines for the slabstylist, calling out to them from across the store."

    dr "Slabraham!"

    "They turn around as soon as they hear Don Rocko’s voice."

    sa "Don Rocko! Looking as slabulous as ever!"

    "Don Rocko briefly introduces me to Slabraham before getting to the matter at hand."

    dr "Slabraham, we must do something about—"

    "Slabraham takes a single glance at me before turning their head away."

    sa  "Say no more, sir. I know what must be done."

    "Slabraham jets away, leaving Don Rocko and I on our own."

    show don rocko blush with dissolve

    dr "If it was not evident, Slabraham is my most trusted tailor, and now he’s yours!"

    s "Thank... thank you...?"

    "I appreciate the sediment but..."

    sa "I have found the perfect thing, sir!"

    show don rocko happy with dissolve

    "Slabraham sprints back to us, almost tripping over himself as he rounds a few racks of clothing. In his little hands, he manages to carry a mountain of different clothes and accessories."

    "From the pile, he pulls out a golden dress-shirt and offers it to me."

    sa "I hope this fits you."

    "I take it graciously. Holding it up straight, I lean in and take a closer look. It’s completely plain, but it seems to be made of a nice material."

    sa "The finest satin we have."

    dr "Try it on!"

    "Slabraham helps me put the shirt on. I button up the front as I turn to face a mirror and—"

    dr "Marvelous!"

    sa "But that’s not all, sir!"

    "He pulls out a dark brown fur stole from the pile and wraps it around my shoulders."

    sa "There. Now you are perfect."

    show don rocko sad with dissolve

    "Don Rocko takes out a gold handkerchief from under his hat and wipes a tear away."

    dr "My, my... a vast improvement indeed."

    s "But..."

    show don rocko blush with dissolve

    "Don Rocko takes my hand in his, gripping it tight."

    dr "You’re finally dressed the part."

    "But it isn’t me."

    "I look at myself in the mirror and don’t recognise the slab staring back at me."

    sa "Of course, sir—"

    "Slabraham shifts his attention to Don Rocko."

    sa "You certainly will need new clothes to match your new beau, no?"

    show don rocko happy with dissolve

    "Slabraham returns to the mountain of clothes and carefully arranges them into an almost uncountable amount of outfits for Don Rocko."

    "The palette and styles remain the same, with most of the variation being the order in which they appear."

    "Don Rocko selects the outfits that catch his eye and tries them on with Slabraham’s assistance."

    dr "I'll take this one! Just this one!"

    hide don rocko neutral with dissolve

    "One becomes two, two becomes 20, and soon enough, the moon’s out and it’s nearing the store’s closing time."

    "Slabraham brings all of Don Rocko’s purchases to the counter. Rather than placing them all together in a few bags, he places each outfit in their own separate bag."

    sa "Could you please hold some of these bags? We’re running awfully low on counter space..."

    "Begrudgingly, I hold a couple of the bags."

    sa "Ah, maybe a few more?"

    "And another four."

    sa "Well..."

    "And another ten."

    sa "If you please—"

    s "{b}NO!{/b}" with vpunch

    "I drop the bags and storm out of the shop. I am not just some slab you can re-purpose into a bag-carrier!"

    "Some ‘slablover’ Don Rocko is! How can someslab be so inconsiderate towards their potential partner?"

    "I look around the shopping area for a way out, but it’s hard to make out any paths or exits in the dark."

    "I stick as closely as I can to the lamp posts, skirting around the light they provide, but—"

    q "You're not going anywhere."

    "A golden pin that glints under the street lights."

    s "You know I don't belong here."

    show slaborro angry at center
    with dissolve

    sb "And the rest of us do?"

    "Slaborro grabs my wrist."

    sb "Come on.  You're not getting out that easy."

    hide slaborro angry
    show don rocko angry at center
    with dissolve

    "Slaborro marches me right back to an irate Don Rocko."

    "He doesn’t say anything to me, instead electing to make a few ‘hmphs!’ to express his annoyance."

    "The huffing and puffing of slabs struggling to support the weight of Don Rocko’s purchases fill the air in tandem with the sound of critters chittering away in unseen trees."

    "I definitely hope these slabs get a raise... or get paid at all."

    scene bg mansion with fade
    window show dissolve
    show don rocko neutral at center with dissolve

    "We arrive back at Don Rocko’s mansion. I help the slabs bring the bags in while Don Rocko idles by the door."

    "Once we bring everything inside, he finally says something to break the tension."

    dr "Well, it’s been a long day. It’s time to retire for the night."

    hide don rocko neutral with dissolve

    "And with that, he turns and heads to his bedroom, accompanied by two of his slackeys."

    "He really just left without saying anything meaningful."

    "I sigh. I don’t know what I can do, or what I should be doing? I didn’t even ask to be here!"

    show slaborro neutral at center with dissolve

    sb "Hey."

    "Slaborro walks up to me, thankfully crashing a pity party I never wanted to throw."

    sb "Your room. Let's go."

    "I ask the slabs if they need my help and they shake their heads, though they thank me for asking."

    "I follow Slaborro down flights of stairs and through a maze of hallways. While Slaborro seems content to listen to the sound of our footsteps, I decide to break the silence."

    s "So... why are you here?"

    "Slaborro takes a second to respond."

    sb "That’s on a need-to-know basis."

    s "You can just say he pays you, you know."

    "Slaborro runs a finger along one of the scars on her hand."

    sb "There’s a bit more to the story than that."

    s "Is there a story as to why you wear an eyepatch?"

    "To my surprise, Slaborro smiles... almost imperceptibly."

    show slaborro happy at center with dissolve

    sb "You’ll have to kill me first if you want to hear it."

    "I shrug."

    s "Well, can’t say I didn’t try to be friendly."

    show slaborro neutral at center with dissolve

    sb "Friendly or looking for blackmail material?"

    "Our back and forth quips help pass the time until we make it to my bedroom. Slaborro pushes the door open for me."

    sb "It—"

    "She turns a light shade of pink as she stumbles over her words."

    show slaborro blush at center with dissolve

    sb "It was nice to meet—"

    "I hang onto every word she says. My heart is beating fast... the anticipation...!"

    "But she shakes her head—"

    show slaborro neutral at center with dissolve

    sb "...Totally uncool..."

    "—abandoning her train of thought before it could reach the station."

    "She quickly returns to her usual stoic disposition."

    sb "Tomorrow. Don’t be late. Or else."

    hide slaborro neutral with dissolve

    "Slaborro scuttles away into the shadows before I could wish her a good evening."

    window hide dissolve
    scene bg bedroom1 with fade
    window show dissolve

    "When I step into the bedroom, my jaw hits the floor."

    "Coming from a little room in a tree hollow to {i}this{/i} place? It’s like day and night."

    "The bedroom is like a mini castle in its own right. A giant bed lies in the middle of the room, covered in a sea of gold and brown pillows and blankets."

    "To the sides of the room are golden furniture: an armchair and side table, a desk and chair, and multiple chests and drawers."

    "Fancy arched windows are hidden behind golden curtains, but I can still see moonlight pooling on the windowpane."

    "What blows me away the most is the room’s crowning jewel: a golden chandelier that shines so radiantly with bright, white light."

    "Still dazzled, I slip under the covers of the bed. It’s so soft, so..."

    scene bg bedroom2

    s "Unreal. This whole situation is just unreal."

    scene bg bedroom1

    "What has my life become? More has happened to me in one day than has happened to me in my entire life!"

    "So many new faces and places… it all comes back to me like a flood."

    show don rocko neutral at left with dissolve

    "Don Rocko, the rich business slab who deems {i}me{/i} his slablover."

    show leif neutral at center with dissolve

    "Leif, the kind-hearted slab stuck in Don Rocko’s prison for no good reason."

    show slaborro neutral at right with dissolve

    "And Slaborro, Don Rocko’s faithful bodyguard."

    "Though I’ve only known the three of them for one day, they’ve already made such a deep impression on me."

    "I don’t have the words to describe what I’m feeling, but I know I’m fascinated. I want to get to know them more even if I don’t want to admit it."

    "I can’t keep my eyes open for much longer. Waves of fatigue wash over me and I let myself sink deeper and deeper into..."

    scene bg black with fade

    "Tomorrow is a brand new day, filled with new opportunities to seize and fun to be had."

    "I can’t wait to see which strange slab I’ll get to spend a little more time with when the sun rises..."

    scene cias2 with fade
    window show dissolve

    "{b}Congratulations on completing ACT ONE!{/b}"

    python:
        username = renpy.input("{b}Please enter your username (Discord, DeviantArt etc.) to claim your prizes.{/b}", length=50)
        username = username.strip()

    "{size=18}{i}[username], thank you for completing Act One! Please take a screenshot of this page and follow the directions on the event journal to have {b}one leaf & one rock{/b} added to your inventory.{/i}{/size}"

    scene bg black with fade

    "And now, for the choice you've been waiting for..."

    "{b}WHICH SLAB WILL YOU ACCOMPANY TOMORROW?{/b}"

menu:

    "Slaborro":

        jump slaborro

    "Leif":

        jump leif

    "Don Rocko":

        jump donrocko

label slaborro:

    window hide dissolve
    scene bg bedroom1 dream with fade
    window show dissolve

    "All I see when I open my eyes is darkness."

    s "Hello?"

    "It’s cold. Really cold. I wrap my arms around myself and walk forward even though I can’t see the path ahead."

    "The only thing I can hear is the sound of my own footsteps echoing through a vast room."

    s "Is anyslab here?"

    "I break into a run, desperate, looking for any sign of life."

    "Can anyslab hear me?"

    scene bg bedroom2 dream

    "Panic strikes my heart, coursing through my body in violent waves."

    scene bg bedroom1 dream

    "Where am I?"

    "Am I trapped?"

    "Have I been left behind?"

    "Questions run rampant in my mind at speeds I can’t catch; before I can grasp one, another takes its place."

    "Just as I begin to doubt whether or not I can make it out alive, I hear a voice come from the shadows."

    "{i}[slabname]{/i}."

    "Its familiarity soothes me at once."

    s "Hello?"

    "My eyes settle on a vague silhouette in the distance, outlined by a dim red glow. I run towards it, my hands reaching out."

    "{i}[slabname]{/i}."

    "I stop when I feel fingers interlocked with mine."

    "Yet, I don’t see anyslab around me."

    s "Where are you?"

    "With my question, a gradient of color washes away the darkness, an arctic climate melted by an inexplicable heat."

    "Enveloped by a comforting warmth, I feel safe enough to close my eyes."

    "For a moment, it feels balanced; that periods of darkness are fleeting, always to be followed by a splendor of color and light."

    "I feel a hand on my cheek, a soft caress that leaves me breathless."

    "{i}[slabname], I—{/i}"

    "I open my eyes slowly and see..."

    show slaborro neutral at center
    with dissolve

    s "Slaborro?"

    scene bg bedroom1 with fade
    window show dissolve

    "I wake up with a jump, my heart racing." with vpunch

    "What the heck was that dream?!"

    "Slaborro...?"

    "The sound of birds chirping calms me down, the sight of sunlight streaming through the gap in the curtains warming my heart. It was just a dream, just a dream..."

    "Right?"

    s "Good morning slabworld, and all who inhabit it!"

    "After a little stretch, I jump out of bed and draw the curtains."

    "The chandelier reflects with golden light flooding into the room, immediately dispelling the rest of the shadows from the night before."

    "Too distracted by the chandelier glittering above me, I don’t notice the sound of someslab banging at the door, calling out for me."

    s "Coming!"

    "I run up to the door and open it, and I’m greeted by one of Don Rocko’s slackeys. They look really tired, but they do their best to appear presentable."

    s "Yes, yes... I’ll be there soon."

    "They nod before scurrying away."

    "I go into the room’s en suite to freshen up. A little rinse to wash the sleep off my eyes, a little powder for my cheeks, a little perfume just in case, and I look perfect!"

    "With a spring in my step, I make my way down to where Don Rocko is expecting me."

    scene bg mansion with fade
    window show dissolve
    show don rocko neutral with dissolve

    dr "Ah, [slabname]."

    "Don Rocko calls out to me as I walk down to the main hall. He’s seated in his usual seat, already eating breakfast."

    "On his plate, I see some sunny-slab-ups piled atop toasts slathered with slavocado and a second plate stacked with chocolate chip slabcakes in the image of Don Rocko."

    "I wonder how he manages to eat so many foods that look like himself."

    dr "Come sit."

    "I head over and sit in my chair. Slackeys crowd around and set the table up, placing a clean plate and polished silverware in front of me."

    s "Thank you!"

    "Don Rocko continues eating, occasionally grabbing the slabcake that a slabwaiter intended to bring to me."

    "They smile apologetically when they eventually succeed in fixing up a plate of slabcakes for me."

    dr "So..."

    "Awkward silence... It seems this will just be my new normal."

    "Don Rocko jabs at his food as he thinks of something to say, but judging from his expression, he still seems a bit peeved from last night."

    dr "Did you, uh... sleep well?"

    "I cut into the slabcake and go to speak, but—"

    show don rocko happy with dissolve

    dr "I, for one, slept excellently!"

    "Of course. Once he starts talking about himself, his mood immediately improves."

    "Well, no matter! I don’t have much to say anyway."

    "I nibble away at my slabcake, savoring how {i}divine{/i} it truly tastes, as I think about that weird dream I had..."

    "Slaborro..."

    "I tune Don Rocko out and look around for Slaborro. She should be somewhere here, right? Where else would she be if not by Don Rocko’s side?"

    "Out of the corner of my eye, I see slackeys congregating in the corner as another slab walks into the hall."

    hide don rocko happy
    show slaborro neutral
    with dissolve

    "Slaborro...!"

    "Be still, my heart! It was just a dream! It doesn't mean anything!"

    "Yet, it feels like a spotlight’s just been shone on her, and I can’t bear to tear my eyes away."

    "Has she always looked so cool?"

    "In hushed tones, she speaks with the other slabs. They seem to laugh and crack jokes, nudging and slapping each other playfully."

    "More than anything, I wish I could be with them rather than, you know—"

    hide slaborro neutral
    show don rocko angry
    with dissolve

    dr "Ahem!"

    "I jump to attention, focusing my attention back on Don Rocko." with vpunch

    dr "Why so distracted, hm? I was just getting to the good part of my dream!"

    s "Sorry, sorry! Please tell me more!"

    show don rocko neutral with dissolve

    dr "Ah, as you wish!"

    "Before he could start his story again, one of Don Rocko’s cronies approaches the table."

    "Oh, thank the slabgods!"

    "Don Rocko places his cutlery down so he could lean over and listen."

    show don rocko angry with dissolve

    "Judging from the way his expression changes from a pleased to an annoyed one, I’d say he wasn’t given any good news."

    dr "But I’m in the middle of a—"

    show don rocko blush with dissolve

    "He turns to look at me and rubs the back of his neck, blushing."

    dr "Can’t it wait?"

    "The slackey shakes their head. Don Rocko sighs."

    show don rocko neutral with dissolve

    dr "Well, if it can’t be helped."

    "He tips his fedora at me."

    dr "My apologies, [slabname]. It seems I’m needed at my emporium! I’m sure you’ve heard of it; it’s really quite popular, lots of business, yes..."

    "Dangerously on the edge of falling into another monologue, Don Rocko’s slackey kindly offers to help him off his chair."

    dr "Ah, yes, yes! Thank you, thank you."

    "I make my way down to meet him since it’s, uh, a little hard to speak to him from up so high."

    dr "I will return shortly, but in the mean time..."

    show don rocko neutral at left with dissolve
    show slaborro neutral at right with dissolve

    "He gestures for Slaborro to come over. My eyes are immediately drawn back to her."

    "She notices me staring at her and I avert my gaze quickly. I blush out of embarrassment and she..."

    show slaborro blush at right with dissolve

    "She's blushing too?"

    dr "Make sure [slabname] doesn’t leave, yes? We can’t have my slablover running off!"

    show slaborro neutral at right with dissolve

    sb "Understood, sir."

    "She turns to me."

    sb "[slabname] won’t be leaving my side."

    hide don rocko neutral
    show slaborro neutral at center
    with dissolve

    "Reassured, Don Rocko exits the hall with his slackeys surrounding him, leaving dust in their wake. They’re really in a hurry, huh?"

    "..."

    "It’s just me and Slaborro now, standing all alone in this large hall. It’s quiet when Don Rocko’s not around. Slaborro looks around the hall awkwardly as I twiddle my thumbs."

    "..."

    "Should I say something? But what should I say?"

    "..."

    "I definitely {i}shouldn’t{/i} tell her that I dreamed about her, right?"

    "..."

    sb "Uh, do... do you want to..."

    "She stumbles over her words, but I’m just grateful she was able to break the ice."

    s "Yes! Yes, absolutely!"

    "I freeze. She hasn’t even—"

    s "I—I’m sorry, I—"

    show slaborro happy at center with dissolve

    sb "Heh, it's okay."

    sb "Nobody’s given you a proper tour yet, right? I’ll take you around."

    sb "It’s a pretty, uh, {i}killer{/i} place!"

    show slaborro neutral at center with dissolve

    "She clears her throat and composes herself, readjusting her eyepatch."

    sb "Only if you want to."

    "Is... Is this..."

    s "I would be honored!"

    show slaborro happy at center with dissolve

    "The corner of Slaborro’s mouth curls up into a small smile."

    sb "Heh, let's go. We haven't got much time."

    show slaborro neutral at center with dissolve

    "She tilts her head, confused at her own words."

    sb "Well, we {i}do{/i} have time but, you know—"

    "She lets her sentence end before it could finish, punctuating it instead with a series of quick steps forward."

    sb "Follow me."

    hide slaborro neutral with dissolve
    window hide dissolve
    window show dissolve
    show slaborro neutral with dissolve

    "I stick close to Slaborro as she leads me through the different hallways and wings of the mansion. Occasionally, she points out different rooms of interest."

    sb "That’s the formal dining room."

    s "Weren’t we already in the formal dining hall?"

    sb "No, no. We were just in the main hall, which is different from the entrance hall..."

    s "Totally not confusing at all."

    "A few rooms over..."

    sb "And this is the game room."

    "I peer inside and see an elaborate gaming set-up, RGB tower and all, as well as arcade machines."

    s "Wow. I never would have pictured Don Rocko to be a gamer."

    sb "He’s actually quite good at {i}Slabnite{/i}. When he’s not around, I also play a little {i}Slabman 3{/i}."

    show slaborro happy with dissolve

    sb "Nobody’s managed to beat my super fast time yet for the last level, heh... My superior strats..."

    show slaborro neutral with dissolve

    sb "But I'm not a gamer... I don't play anything else..."

    "..."

    sb "Moving on."

    "Right next to the game room is—"

    sb "The sunroom. Well, it’s also the conservatory."

    "She pushes the door open and holds it until I pass through."

    "Floor-to-ceiling windows line the walls, flooding the room with warm, golden light. Skylights in the middle of the room are slightly open, allowing fresh air to circulate."

    "Flowers bloom in colorful pots, some spilling with leafy vines that cascade down the benches."

    "Tiny slabs make their home anywhere they feel comfortable, atop petals, buried in the dirt, on comfy sofas like oases in a sea of foliage..."

    sb "Don Rocko doesn’t go in here too much, but we got some gardeners who come in every so often. And well, I water the plants sometimes when they can’t come in."

    "Slaborro is so cool!"

    show slaborro blush with dissolve

    sb "But I TOTALLY don’t like flowers! That’s so uncool!"

    "I chuckle as the flowers in her hair shake with a passing breeze. She may be many things, but I don’t think Slaborro is a very good liar."

    show slaborro neutral with dissolve

    sb "Let’s keep on moving."

    "We walk past a seemingly endless amount of rooms."

    sb "The cellar."

    sb "The home theatre."

    sb "Yes, that is the third pantry."

    sb "The library. Why we have this when he definitely doesn’t use it, I don’t know."

    sb "I keep my slabhero comics in there though. {i}Licence to thrill{/i}, am I right?"

    "I tilt my head in confusion. She sighs and continues walking."

    "We pass by a very dark hallway."

    s "What's down there?"

    "Slaborro places a finger on her lips."

    sb "It’s a secret, heh."

    "Slaborro eventually takes me to one of the most beautiful places I’ve ever seen."

    sb "Here we are."

    "We stand in front of arched glass doors. On the other side is—"

    scene bg forest with fade
    window show dissolve
    show slaborro neutral with dissolve

    sb "Welcome to the courtyard."

    "Under the blue light of the sky sits a vast courtyard brimming with life. We walk down spiral staircases made of marble, flanked by columns that tower over our heads."

    "The first thing that catches my eye are trellises that support the growth of climbing roses, covering a significant portion of the mansion’s back façade."

    "In the middle of the courtyard lies a grand fountain mounted atop eight stone slab statues, as if they’re carrying it on their backs."

    "The fountain’s centerpiece is a giant marble statue of Don Rocko carrying a giant money bag from which crystal blue water flows down, pooling in the fountain’s reservoir."

    "From the fountain, the courtyard is separated into four areas by flagstone paths, with each section containing its own little garden enclosed by small trimmed shrubs."

    s "Woah, roses!"

    "I walk over to the rose bushes that comprise the first section of the courtyard, carefully maneuvering around the shrubs so I could examine one of the roses up close."

    s "I've never seen a gold one before!"

    "Gold, red, pink, black, white... How do they grow all of these different varieties?"

    show slaborro happy with dissolve

    sb "Beautiful, isn’t it?"

    "Slaborro leads me to the second section of the garden, which is filled with little white flowers. They look so delicate, so gentle, with a sweet fragrance."

    show slaborro neutral with dissolve

    sb "Have you seen these flowers before?"

    s "Can't say I have, no."

    show slaborro happy with dissolve

    sb "Heh. Let me put an {i}end{/i} to that gap in your knowledge."

    sb "They’re called lilies of the valley."

    "I stroke one with the back of my finger."

    s "How pretty!"

    show slaborro neutral with dissolve

    sb "And they’re also one of the most poisonous flowers in the world."

    "I quickly retract my hand."

    s "Uh..."

    "Slaborro smirks."

    show slaborro happy with dissolve

    sb "It’s a flower to {i}die{/i} for, huh?"

    "She scratches her chin."

    show slaborro neutral with dissolve

    sb "That one didn’t... whatever. They’re fake, so there’s no need to worry."

    "Upon closer inspection, she’s quite right! They’re just plastic. Very convincing all the same."

    s "Wait... How do you know they’re poisonous?"

    show slaborro happy with dissolve

    sb "Heh... You will never know..."

    "Slaborro walks forward, leaving me with more questions than answers."

    "But I kind of like it... the mystery... the {i}thrill{/i} of the chase."

    "Oh no. I’m beginning to speak like her."

    "We walk over to the third section, which looks more like a painting than a garden."

    s "Sunflowers! How beautiful!"

    sb "Um..."

    "I turn to Slaborro when I hear her start to speak."

    show slaborro blush with dissolve

    sb "Not as beau—"

    "I blush. Is—Is she..."

    show slaborro neutral with dissolve

    "She shakes her head."

    sb "Look at how they sway in the wind."

    "I look at them and well, they don’t seem to be doing much of anything other than looking pretty, given they’re made of plastic."

    "They look realistic though!"

    show slaborro happy with dissolve

    sb "So beautiful..."

    show slaborro neutral with dissolve

    sb "Uh, but it’s so NOT cool to like flowers though!"

    "I mask a laugh with my hand."

    sb "I’ve got a lot of, uh, cooler hobbies that will TOTALLY strike fear in your heart and DEFINITELY isn’t gardening."

    s "Such as?"

    show slaborro shock with dissolve

    sb "Um..."

    sb "..."

    show slaborro neutral with dissolve

    sb "Fighting."

    s "Fighting is a hobby?"

    sb "Knife collecting."

    s "Sounds dangerous."

    sb "Eyepatch decorating."

    s "What?"

    sb "What?"

    s "Heh... nothing."

    "We banter more as we walk over to the last section of the courtyard."

    s "It's such a nice day today, isn't it?"

    sb "It is..."

    show slaborro blush with dissolve

    sb "Even more so with..."

    hide slaborro blush with dissolve

    "I turn to face her, but before I could meet her eyes, she’s already running towards shrubs blooming with hydrangeas and chrysanthemums."

    "She hides behind their vibrant plumage."

    "Slaborro... Could she be...?"

    "I run up to the shrub she’s hiding in, but I get distracted by a balcony overlooking the courtyard."

    s "Woah..."

    "I shift gears and make my way up the staircase. The trek up to the balcony is a long one, but it’s well worth the trip. The view..."

    s "It's so beautiful."

    "I lean over the railing and reach out for the sky as if I could touch the clouds that roll by."

    "I look down at thes courtyard below and see how the sun shines down on a breathtaking vista of flora and foliage."

    show slaborro shock with dissolve

    "I see Slaborro coming out from her hiding spot and looking up at me."

    "Her eyes are wide open, her lips parted in awe."

    "And then..."

    show slaborro blush with dissolve

    sb "{i}Near, far, wherever you are,{p}I believe that the heart does go on...{/i}"

    "Is Slaborro singing?"

    "My heart is racing out of my chest, skipping beats, fluttering..."

    "I... I..."

    sb "{i}We'll stay forever this way,{p}You are safe in my heart...{/i}"

    "Do I... love...?"

    "I fly down the stairs and run to Slaborro, basically jumping with my arms out towards her."

    "Thankfully, she catches me in her very strong arms."

    show slaborro sad with dissolve

    "Slaborro, however, puts me down."

    s "What... Slaborro?"

    "She pushes me away gently, but still keeps a tight grip on my shoulders."

    "Slaborro turns her head away, a tear threatening to roll down her face."

    sb "You’ve... you’ve learned too much about me. I can’t—"

    s "But we have a connection! Can’t you feel it?"

    sb "I... you must leave me... I’m not the slab you think I am."

    "I tear up and try to turn Slaborro’s head so she would face me. She keeps resisting."

    s "But I... I—"

    sb "No, [slabname], don’t..."

    s "I..."

    sb "I’m too dangerous... my past..."

    s "But..."

    sb "I don't want to hurt you."

    s "Please... believe me when I say..."

    "Slaborro turns to face me, but she doesn’t meet my eyes."

    s "I... I live for danger."

    show slaborro shock with dissolve

    "Slaborro looks up slowly, surprise evident on her face."

    sb "I must be dreaming."

    "I press her forehead to mine."

    s "No, you're not."

    show slaborro blush with dissolve

    sb "I never thought - I never thought...!"

    s "Slaborro, you have to give our love a chance!"

    "Yes, we only met yesterday, but life’s short! I can’t live on the sidelines anymore!"

    sb "All this time, I thought I would be lonely... That nobody could accept me as I am..."

    s "Not anymore."

    sb "Oh, [slabname]..."

    show slaborro happy with dissolve

    "In spite of herself, she holds her head high and smiles."

    sb "All right, okay. Let’s give this a go!"

    "Before she can pull me into a hug, we hear footsteps coming from the entrance to the courtyard. We turn around."

    show slaborro neutral with dissolve

    s "Oh no, is it—"

    "One of Don Rocko’s slackeys comes strolling in, carrying a towering pile of purple potions."

    "Slaborro takes a step away from me."

    sb "He's here."

    hide slaborro neutral with dissolve
    show don rocko neutral with dissolve
    window show dissolve

    "Don Rocko crawls out from behind the pile. Thankfully, it seems he didn’t see me and Slaborro standing close together."

    dr "There you are! I’ve been looking all over for you, [slabname]."

    show don rocko neutral at left with dissolve
    show slaborro neutral at right with dissolve

    "Slaborro walks back to Don Rocko’s side."

    dr "I hope [slabname] didn’t give you much trouble."

    show slaborro blush at right with dissolve

    "She fails at her attempt to hide how flustered she is. Don Rocko squints at her."

    dr "Hm... You seem rather off."

    sb "What... What do you mean?"

    "Don Rocko shrugs."

    dr "No matter."

    "Don Rocko walks up and takes me by the hand."

    show don rocko blush at left with dissolve

    dr "Come with me."

    scene bg mansion with fade
    window show dissolve
    show don rocko neutral at left
    show slaborro neutral at right
    with dissolve

    "I walk with him, but I look over my shoulder every so often to check up on Slaborro."

    show slaborro happy at right with dissolve

    "She nods and smiles. I do the same."

    show slaborro neutral at right with dissolve

    dr "Have I told you about the {i}Grand Vault{/i}?"

    "I shake my head."

    dr "It’s really quite a feat of engineering, yes! Completely impossible to break into."

    "He picks up one of the potions from the pile, holding it up to the light."

    dr "It’s where I store all of these, you see. They’re the most important thing in the world!"

    show don rocko angry at left with dissolve

    dr "And other slabs definitely know this. Many have tried to break in, you understand, and well..."

    "Don Rocko sneers."

    show don rocko neutral at left with dissolve

    dr "They’ve paid the price for it."

    "We make a right turn into a long, {i}long{/i} and extremely dark corridor. This must be the same one that Slaborro and I saw before."

    "Hanging on the walls are intricate paintings of Don Rocko himself, in a variety of different poses and scenarios."

    "I marvel at them, though I’m unsure if I {i}like{/i} them or if they’re so strange it’s impossible to look away."

    dr "Ah, aren’t they splendid?"

    "I laugh nervously."

    s "Aha... yeah..."

    "Eventually, we arrive in front of an imposing vault door. Made of solid gold, I wouldn't know how to go about opening it."

    hide slaborro neutral at right with dissolve
    show don rocko happy at center with dissolve

    dr "Magnificence incarnate! Have you seen anything like it before?"

    "Has anybody?"

    "Don Rocko turns to address his company."

    dr "Please avert your eyes. I cannot have anyslab jeopardizing the safety of my vault."

    "All the slabs turn around, including Slaborro."

    "I do the same, but before I turn around completely, I see Don Rocko walk over to the right of the vault and press his palm on the wall. When he does so, a little touch panel pops out."

    show don rocko angry at center with dissolve

    "Don Rocko takes a quick glance over his shoulder before he types in the code. I look away."

    "He taps in a rather long code into the panel. Once he does so, I hear a satisfying ‘click’ followed by the sound of the vault door creaking open."

    "His slackeys turn around and rush to the door, pulling it open so Don Rocko can enter."

    "Don Rocko walks back over and locks arms with me."

    show don rocko blush at center with dissolve

    dr "Come, let me show you something truly special."

    scene bg mansion with fade
    window show dissolve

    "The vault is... as described. Stepping inside, I’m almost blinded by the light reflecting off the golden coins scattered all over the floor."

    "They spill out from money bags laid haphazardly through the vault, paper bills acting like makeshift plugs to keep the rest of their contents in."

    show don rocko neutral at center with dissolve

    dr "Place the potions over there."

    "Don Rocko directs his slackeys over to the farthest, most secure corner of the vault where piles and piles of potions are stacked in neat but fragile pyramids."

    "One wrong move could easily damage the structural integrity of this monolith. A little push, and it comes crumbling down; a rubble marooned in a sea of purple liquid..."

    "What a clean-up operation that would be!"

    "By the vault’s entrance, I see a little slabster polishing a small pile of gold coins and potions."

    "The tip of a metallic item juts out from under their little mountain, which they quickly cover up with more coins."

    "I wait a moment before giving ‘em a little wave. They wave back enthusiastically, albeit a little surprised at having been acknowledged."

    "Does Don Rocko not know they’re here?"

    dr "So, what do you think?"

    s "It's... definitely something!"

    show don rocko happy at center with dissolve

    dr "A visual representation of my hard work, all in one place! Truly astounding. Have you ever seen anything so grand? So impressive and immense?"

    dr "I dare say, it's quite like me!"

    "I nod politely. Don Rocko takes this as his cue to continue."

    dr "You see, I started off my rags to riches journey very early on in my life..."

    hide don rocko happy with dissolve
    show slaborro neutral at center with dissolve

    "I quickly tune him out, though he continues giving me a 'tour' of the vault. Slaborro walks some distance behind us."

    show slaborro blush at center with dissolve

    "There’s so much we couldn’t say to each other. For now, the best we can do is exchange loving looks, but later... maybe..."

    show slaborro neutral at center with dissolve

    "As big and impenetrable as the vault appeared from the outside, it certainly isn’t on the inside."

    "Slaborro occasionally walks over to examine points of interest that might prove handy to keep in the back of our heads."

    "Cracks in the walls, hidden slabs that linger out of Don Rocko’s sight, high windows left open to keep the place cool..."

    "Interesting indeed."

    show don rocko happy at left
    show slaborro neutral at right
    with dissolve

    dr "Annddddd that’s how I made all my riches! I’m awesome, I know."

    "He places his hands on his hips, feeling triumphant and proud of himself."

    show don rocko neutral at left with dissolve

    dr "The slackeys should be done putting the potions away by now, surely..."

    "Seeing his slackeys idling by the entrance, we walk back to meet them."

    dr "If all is in order, let us head off."

    "Don Rocko leads all of his personnel out of the vault, making sure it’s securely locked once his slackeys close the doors."

    "Satisfied, he walks the group back to the main hall, passing the time engaging in idle conversation with anyslab willing to listen."

    dr "Ah, now that that’s finished..."

    hide don rocko neutral
    show slaborro neutral at center
    with dissolve

    "With no explanation, he exits the hall with his goons, completely forgetting that Slaborro and I were there."

    "..."

    sb "Well..."

    "Slaborro takes my hand."

    sb "It's... just us now."

    s "Yes... it is..."

    sb "It was {i}killing{/i} me to be away from you..."

    s "We're here now, and that's all that matters."

    show slaborro sad at center

    sb "But what should we do now? Don Rocko will not approve of this..."

    s "Surely, there’s somewhere we can go, right? Anywhere, away from this place. You must want to do something different, right?"

    "Slaborro sighs."

    sb "Yes, but Don Rocko..."

    "I press a finger gently on her lips."

    s "Take chances, Slaborro. You don’t need to be by his side anymore."

    show slaborro blush at center

    "She caresses the back of my hand."

    sb "When I could be by yours."

    "I feel nervous, but I don’t let it show on my face. I’ve never done anything like this before. If we get caught it would be all over for us."

    show slaborro happy at center

    "But when I see Slaborro smile, I know that everything will be okay. Nothing can stop us or tear us down."

    s "We need to do something. Something bold. Something that’ll make a statement."

    "We share a knowing look, a mischievous spark glinting in her eye."

    sb "Let's do some crimes."

    s "Always."

    scene bg mansion with fade
    window show dissolve
    show slaborro neutral at center with dissolve

    "Slaborro takes us back to where the vault is, but for some strange, inexplicable reason, it isn’t a walk in the slabpark."

    "Don Rocko’s goons have stationed themselves all over the castle, standing outside every door, patrolling every hallway."

    sb "Strange. His slackeys shouldn’t be here."

    s "I don’t know, but we need to be careful."

    "We weave up and down stairs, staying close to the walls so we wouldn’t be spotted."

    "When a slabster would spot us, Slaborro marches up to them — the ground shaking with every step — and pushes them up against the wall."

    show slaborro angry at center with dissolve

    sb "Don’t ask questions. Don’t say anything. Run away and pretend you saw nothing."

    "The slab, extremely intimidated by Slaborro, does as she says. When she lets them go, they whistle a happy tune while they run for their life."

    show slaborro neutral at center with dissolve

    "After some expert maneuvering (well, a couple dozen scared-to-death slabs later), we make it to the vault in one piece."

    "Faced with the giant vault doors, we realize that a much, much bigger challenge awaits us."

    sb "Any ideas?"

    s "Hmm.. maybe."

    "Remembering what Don Rocko did before, I walk up to the section of the wall where he stood before."

    "I run my hand across its surface and feel around, my fingers landing on the ridges of something running flush with the wall."

    "Though it’s almost impossible to see, following the ridges around draws a rectangular shape."

    "I press my palm in the middle of the rectangle and—"

    s "Ah!"

    "—it gives way, flipping over to reveal a code panel."

    show slaborro shock at center with dissolve

    sb "How did you know that was there?!"

    s "Taking a little glance back when you’re not supposed to never hurt anyslab..."

    show slaborro blush at center with dissolve

    sb "So devious."

    s "All that’s left is the code. Any ideas?"

    show slaborro neutral at center with dissolve

    sb "Hmm..."

    "Slaborro examines the panel."

    sb "From the looks of things, the code isn’t super long. Allows for both numbers and letters."

    s "Are there dates or anything significant to him?"

    sb "Not that I know of."

    s "What does he care about?"

    "Slaborro considers my question for a moment, fingers resting on her lower lip."

    sb "Money... potions..."

    s "What does he care about the {i}most{/i}?"

    "Slaborro follows my train of thought."

    sb "... Himself."

    "I type in Don Rocko’s name. Incorrect."

    s "Hm..."

    sb "Maybe something he’d say about himself?"

    "I try to recall everything that Don Rocko’s said to me today. I really should have been a better listener."

    s "How can he talk so much and say nothing at all?"

label slaborrochoice:

    "My mind eventually recollects a few instances that could have the solution to our problem:"

menu:

    "'Magnificence incarnate'":

        jump slaborroMI

    "'I'm awesome'":

        jump slaborroIA

    "'Impressive and immense'":

        jump slaborroIAI

label slaborroMI:

    "I type in different variations of 'magnificence incarnate', but they all come up as incorrect."

    s "Maybe he used those words to describe the vault and not himself..."

    jump slaborrochoice

label slaborroIA:

    s "Wait..."

    scene bg mansion bw with fade
    window show dissolve
    show don rocko bw at center with dissolve

    dr "And that's how I made all my riches! I'm awesome, I know."

    scene bg mansion with fade
    window show dissolve
    show slaborro neutral at center with dissolve

    s "I got it!"

    "I type in different variations of Don Rocko’s words into the panel: ‘awesome’, 'awsum’, ‘imawesome’."

    "I know this has to be it. These were his exact words to me when we were in the vault."

    sb "Maybe it has some numbers in it too?"

    "A light bulb goes off in Slaborro’s head."

    sb "He's a gamer."

    s "And?"

    sb "Just..."

    "Slaborro types in the exact words that I do, except she changes some of the letters into numbers."

    s "1m4w50m3? What?"

    sb "Don't ask."

    "With a click, the panel flips itself over, disappearing from view. The vault opens shortly after."

    "Okay then!"

    "We quickly make our way inside, making sure to leave the door open just a little bit so we can sneak back out."

    jump slaborrotrapped

label slaborroIAI:

    "I type in different variations of 'impressive' and 'immense', but they all come up as incorrect."

    sb "Good attempt, but maybe it’s something else..."

    jump slaborrochoice

label slaborrotrapped:

    "Slaborro and I get to work on pocketing some of the riches inside Don Rocko’s vault."

    sb "Potions. And a lot of it. These sell for a ton on the outside."

    "I grab one of the money bags taking up space in the vault and open it, letting Slaborro scoop more and more potions into it."

    "Once we reach the amount of bags we could reasonably carry, we go to head out."

    "{i}*SLAM* *THUD*{/i}" with vpunch

    "... The vault door?!"

    s "Oh no."

    "Loud cackling comes from the other side."

    "It's him."

    dr "I told you, did I not? {i}No slab{/i} escapes the vault."

    "Panicking, I cling onto Slaborro, money bags falling to the wayside."

    s "What should we do?! We’re stuck here until they open the doors!!!"

    show slaborro happy at center with dissolve

    "Slaborro smirks."

    sb "{i}Nothing{/i} can keep me trapped forever."

    "Slaborro turns to console me, reassuring me that she’s got a plan."

    show slaborro neutral at center with dissolve

    sb "Think. Do you remember what we saw before?"

    "..."

    s "Oh, you're right!"

    sb "We can break out of here if we—"

    "Think of something. But what should we do?"

menu:

    "Escape through the cracks in the wall":

        jump slaborroescapewall

    "Escape through the windows":

        jump slaborroescapewindow

label slaborroescapewall:

    s "You saw the cracks in the wall, right? Maybe we could make our way out through there."

    sb "I don’t think we’d fit through there, especially with everything we’re carrying."

    s "We might not be able to, but I know a few slabs who can."

    "I ask for Slaborro’s help in rounding up the little hidden slabs around the vault. They masquerade themselves as little coins or blend in with the walls and floors."

    s "Hey, little guy."

    "Though they’re a little reserved, they walk up to me rather happily when they realize I’m friendly."

    sb "Hey, come on out."

    "It takes a little convincing, as the slabs seem skeptical of her, but she eventually coaxes them out from the shadows."

    "A sea of small slabs surrounds us. Even the little slab from before, who was polishing some of Don Rocko’s riches, tagged along!"

    "Slaborro bends down to speak to them."

    sb "Do you see the cracks in the wall? We need you to crawl through to the other side and unlock the door."

    "{i}We{/i}? My heart skips a beat. We really are a couple now!!!"

    "Slaborro spells out the exact code and the slabs get to work. They crawl into the crack in the wall one by one."

    "All we have to do is wait."

    "..."

    "..."

    "..."

    "{cps=4}{i}*CREAK*{/i}{/cps}"

    "Slaborro and I jump to our feet and cheer, but we don’t celebrate just yet."

    "We grab our loot and help pull the door open. There’s just enough room for us to slide on out."

    "We thank the slabs and urge them to follow us on our way out. Most of them agree except the one gold slab, who elects to stay."

    "We give them a farewell hug before we fly down the hallway."

    "With so many of us, it’s like we’re a tidal wave, overwhelming any and all slackeys in our path."

    "Compared to how long it took to break into the vault, it’s easy sailing back to the entrance of the castle."

    "We burst through those cursed doors and crash into the driveway. As we find our feet, I take a moment to look up at a sky I never thought I’d see again."

    "In that moment, the world has never seemed wider."

    jump slaborroescape

label slaborroescapewindow:

    s "You see the windows up there, right? Maybe we could make our way out through there."

    sb "How do we make it up there? Especially with everything we’re carrying, stacking things up will take so long with just the two of us."

    s "We might not be able to on our own, but I know a few slabs who can help."

    "I ask for Slaborro’s help in rounding up the little hidden slabs around the vault. They masquerade themselves as little coins or blend in with the walls and floors."

    s "Hey, little guy."

    "Though they’re a little reserved, they walk up to me rather happily when they realize I’m friendly."

    sb "Hey, come on out."

    "It takes a little convincing, as the slabs seem skeptical of her, but she eventually coaxes them out from the shadows."

    "A sea of small slabs surrounds us. Even the little slab from before, who was polishing some of Don Rocko’s riches, tagged along!"

    "Slaborro bends down to speak to them."

    sb "Carry whatever you can and stack it up by that wall so we can reach the window. Got it?"

    "{i}We{/i}? My heart skips a beat. We really are a couple now!!!"

    "We get to work along with our new slabfriends. They work together to carry coins and money bags and potions, forming a slowly growing pile up to the window."

    "Soon, the pile is high enough that its tip reaches the window."

    "Slaborro and I jump and cheer, but we don’t celebrate just yet. We grab our loot and make our way up the fragile mountain slowly."

    "When we make it to the window stool, we thank the slabs and urge them to follow us out of the vault. Most of them agree except the one gold slab, who elects to stay."

    "We give them a heartfelt thank you and goodbye before Slaborro pushes the window open all the way. She peers her head out and breathes a sigh of relief."

    sb "The trellises. We can climb down with no issue."

    scene bg forest with fade
    window show dissolve
    show slaborro neutral with dissolve

    "With Slaborro leading the way, we make our way down in a single file line. I comfort the tiny slabs who hate heights."

    s "I'm right under you, you see? I’ll catch you. Trust me."

    "..."

    "..."

    "..."

    "When we touch the ground, I’ve never felt more free."

    "But we’re not out of the woods just yet."

    sb "There’s no way out from the courtyard. We have to go through the mansion."

    "The tiny slabs puff their chests, ready and raring to go. Slaborro appreciates their enthusiasm."

    show slaborro happy at center with dissolve

    sb "That’s more like it."

    scene bg mansion with fade
    window show dissolve
    show slaborro neutral with dissolve

    "With so many of us, it’s like we’re a tidal wave, overwhelming any and all slackeys in our path."

    "Compared to how long it took to break into the vault, it’s easy sailing back to the entrance of the castle."

    "We burst through those cursed doors and crash into the driveway."

    jump slaborroescape

label slaborroescape:

    scene bg forest with fade
    window show dissolve
    show slaborro neutral with dissolve

    "The tiny slabs scatter in the wind once we touch grass."

    "Slaborro and I go in a different direction, running as fast as our legs can take us."

    "When we think we’re far enough away, we run up a high tree,  catching our breath on a tree branch. We huddle together so we can fight in case a slabster ambushes us."

    "We stay vigilant for a while, but we lower our defenses when we don’t hear anything but wind rustling the leaves."

    show slaborro happy at center with dissolve

    sb "We... did it."

    "Slaborro pulls me into a tight hug."

    show slaborro blush at center with dissolve

    sb "We really made it out."

    "I nestle my head on her shoulder."

    s "We're free."

    "She cups my face with her hands."

    sb "Thank you, [slabname], for making the past two days such an adventure."

    s "And we’ll have many more."

    sb "The world’s open to us now, huh?"

    "We can do anything we want to."

    sb "With you by my side?"

    "I lean my head on her chest. Her heart’s beating just as fast as mine."

    s "I'm yours."

    show slaborro neutral at center with dissolve

    "Before we run away towards our future, I look up and see a little conflict in Slaborro’s eyes."

    s "Is something wrong? I know this isn’t the usual way of getting together, but—"

    sb "No, it's not that."

    "She closes her eyes, deep in thought."

    show slaborro shock at center with dissolve

    sb "Wait a minute..."

    "She jumps up, hands curled into fists."

    show slaborro angry at center with dissolve

    sb "What the hell? Don Rocko hasn’t paid me for my services yet!"

    scene cias2 with fade
    window show dissolve
    show slaborro blush at center with dissolve

    "{i}[username], thank you for completing Act Two - {b}Slaborro{/b}! Please take a screenshot of this page and follow the directions on the event journal to have {b}one leaf OR rock (your choice){/b} added to your inventory.{/i}"

    scene bg forest with fade
    window show dissolve
    show slaborro angry at center with dissolve

    "And there we are, flying back to the very place we spent so long trying to escape from. We really don’t know how to do this whole ‘breaking out and staying out’ thing, huh?"

    s "Are you sure we should do this? We can make money elsewhere."

    sb "You underestimate how much is owed to me, [slabname]."

    s "...How much?"

    "Slaborro stops in her tracks and whispers the amount in my ear."

    s "Holy—"

    "Yeah."

    "Yeah, we're going back to get that."

    scene bg mansion with fade
    show slaborro angry at center with dissolve
    window show dissolve

    "We arrive back at Don Rocko’s castle in no time, barging through the front doors with reckless abandon."

    "Don Rocko stands up high on the second floor landing, looking down at us. The smirk on his face drips with arrogance."

    hide slaborro angry at center with dissolve
    show don rocko neutral at left with dissolve
    show slaborro angry at right with dissolve

    dr "So, have you come back to grovel at my feet?"

    "Slaborro steps forward and points at him, as if raising an invisible sword right to his head."

    sb "I would never bow down to a slab like you."

    "Don Rocko snickers as he walks down the stairs."

    show don rocko angry at left with dissolve

    dr "It would be wise to reconsider such a decision."

    "I hide behind Slaborro, doing my best not to cower."

    show don rocko blush at left with dissolve

    dr "Still, I am feeling generous today and have decided to spare you long enough to hear your demands."

    dr "That is why you came back, yes?"

    sb "Pay me what I'm due."

    show don rocko neutral at left with dissolve

    "Don Rocko strokes his chin mockingly."

    dr "Do I owe you anything?"

    sb "Don’t lie to me! I am not a slab to be made a fool of!"

    show don rocko angry at left with dissolve

    dr "If I do, do you not suppose you’ve taken enough from me?"

    "Don Rocko begins circling us. A few of his slackeys stand near us, lying in wait, ready to pounce."

    dr "You’ve taken my potions..."

    "I can’t find it in me to say anything. The best I can do is grip onto Slaborro’s arm and offer reassuring squeezes."

    show don rocko sad at left with dissolve

    dr "You’ve taken my slablover..."

    "I look away from Don Rocko’s gaze, though the slight waver in his voice makes me wonder if he did genuinely care about me."

    show don rocko neutral at left with dissolve

    dr "I'd say we're even."

    sb "No! I demand to be paid for my services! We agreed on this!"

    dr "Hm? Even after everything I’ve done for you?"

    "Slaborro scoffs."

    sb "What the hell have you done for me? You were so annoying!"

    show don rocko angry at left with dissolve

    "Don Rocko bares his teeth."

    dr "Hardly the correct answer."

    "Don Rocko turns his back on us, slowly walking up to his goons."

    dr "It seems we’re not seeing eye to eye."

    sb "So be it."

    dr "Is this how it’ll end?"

    sb "Yeah."

    show don rocko neutral at left with dissolve

    "Don Rocko sighs, looking over his shoulder to give us a smug grin."

    dr "Suit yourselves."

    show slaborro happy at right with dissolve

    "Slaborro turns to me and grins."

    sb "Stick close and dodge when you can. This won’t take long."

    show slaborro neutral at right with dissolve

    "With a wave of his hand, Don Rocko gives a simple command."

    dr "Dispose of them."

    "The slackeys, however, seem to hesitate a bit. They look at each other helplessly, waiting for someslab to make the first move."

    "Slaborro happily takes the initiative."

    "She dashes for a pair of unsuspecting slackeys and picks them up by the leg. She swings them around (gently) to knock another slab off their feet."

    "Slackeys rush towards Slaborro, but it’s too late."

    "She picks up the third slab and holds them down in her mouth."

    show slaborro happy at right with dissolve

    "A smirk forms on her face."

    "...Could it be?"

    s "It’s..."

    s "Three slab style!!!"

    "Using the three dizzy slabs like swords, she continues her relentless barrage of cuts and punches, kicks and sweeps."

    "Like dominoes, the slabs fall one by one. They lay helpless around Slaborro’s feet, groaning as they nurse their wounds."

    show don rocko shock at left with dissolve

    dr "Fools!"

    "Don Rocko’s eyes grow wide with fear Slaborro steps over the bodies of her incapacitated foes, approaching Don Rocko menacingly."

    show slaborro neutral at right with dissolve

    sb "Did you forget?"

    show don rocko sad at left with dissolve

    "Don Rocko backs away, gripping his hat as if his life depends on it."

    sb "I trained them all."

    dr "No... No!"

    hide don rocko sad at left
    show bald don rocko shock at left
    with dissolve

    "Moving too fast, Don Rocko trips over and slams into the wall behind him, his fedora falling off his head."

    "A small item tumbles over next to him. It flares a bright green light before dimming completely."

    s "What the—"

    "I run over to pick it up and—"

    dr "{size=15}No! Don't!{/size}"

    "Huh? Where’s that squeaky voice coming from?"

    show bald don rocko sad at left with dissolve
    show slaborro happy at right with dissolve

    sb "HA HA HA HA HA!!!"

    "Slaborro’s thunderous laugh fills the entire castle."

    "That’s perhaps the most emotion I’ve ever seen her show."

    sb "So this is your real voice."

    "I’m too stunned to try and stop Don Rocko from snatching the voice box away. He places it atop the very, {i}very{/i} shiny bald spot he’s trying to hide."

    "Don Rocko looks around frantically for his hat, but he freezes when he sees Slaborro toying with it."

    sb "You wouldn’t want everyslab to know your secret, right?"

    "She throws his fedora up in the air and catches it with her finger."

    dr "{size=15}Are you blackmailing me?{/size}"

    sb "Well..."

    sb "I suppose that’s one way to look at it."

    "Slaborro steps closer to Don Rocko and smirks."

    sb "You already know what I want. The pebbling is in your court."

    show bald don rocko angry at left with dissolve

    "Don Rocko growls, although it sounds less like a big, scary dog and more like a small, yapping puppy."

    dr "{size=15}Fine!{/size}"

    show don rocko angry at left with dissolve

    "He snatches his fedora from Slaborro’s hands, placing it atop his head once he turns his voice box back on."

    "He pulls out his checkbook and writes a check for Slaborro, signature and all."

    "Taking a quick glance, the check is for the exact amount Slaborro said before."

    dr "Happy? Now, get out!"

    "You don’t have to tell us twice!"

    scene bg forest with fade
    show slaborro happy at center with dissolve
    window show dissolve

    "Slaborro and I leave the same way we came in, wide smug grins on our faces. The door behind us slams shut the moment we take a step outside."

    "Pocketing Don Rocko’s check, Slaborro and I run back into the forest, still riding the high of a successful confrontation."

    "We find the tree we sat under before and crawl up into the tree hollow. It’s much bigger than the one I live in. I sit down, leaning against the trunk with my legs crossed."

    "Slaborro goes to follow suit, but one of her bandages catches on a splinter. Not expecting any resistance, she stumbles forward—"

    sb "Huh—"

    "—and crashes right into me."

    "{i}*BONK*{/i}" with vpunch

    s "Are you—"

    show slaborro blush at center with dissolve

    sb "Heh heh. Heh heh."

    "She's... giggling."

    "The sound... It's like honey to my ears."

    "I giggle with her, my heart growing lighter. She unhooks her bandage from the splinter and sits down next to me."

    s "Don't worry, I won't tell anyslab."

    sb "I'll hold you to do that."

    "Once Slaborro’s settled, I lay my head on her lap. To my surprise, she doesn’t try to push me away."

    "I look up at her; her scars like red lightning on a stormy night, her eyepatch covering wounds from a different life."

    "Yet, she sits here, stroking my hair with her free hand as the little red flowers in her hair catch the light."

    "If you told me these were the same slab, I wouldn’t believe you, but..."

    sb "[slabname]..."

    sb "I couldn’t have done this without you. Thank you."

    s "No, no, it’s okay. It was the right thing to do!"

    "She twirls a strand of my hair around her finger. She takes a deep breath in and out."

    sb "If you want, we can still go anywhere, make it out of here, you know?"

    "I stay silent."

    sb "We can travel... as sort of licensed troubleshooters."

label slaborrodecision:

    "This... this is a really big decision, huh?"

    "But I need to decide. It’s now or never."

menu:

    "Run away with Slaborro":

        s "Slaborro..."

        "I sit up and turn to her. Her eyes follow me, expectant."

        s "Anywhere you go, I'll be right by your side."

        "Slaborro breathes a sigh of relief before pulling me in close."

        sb "You believe in living dangerously. I can see that."

        s "Thrill is the spice of life, after all."

        sb "Where have you been all my life?"

        "She holds my chin."

        "She leans in."

        "Her lips linger around mine."

        "Her breath is just as hot as she is."

        "I smirk."

        s "What are you waiting for?"

        "With that, Slaborro kisses me, tender as it can be."

        "My heart swells, waves of love and warmth and happiness washing all over my body."

        "It feels right."

        "For the first time in my life, I know things will work out."

        "This is the slab I want to spend the rest of my life with."

        "I’m the one to break the kiss, flushed red."

        s "Come on, let’s get out of here."

        "We run off into the sunset, the wind at our backs, the horizon line to cross and conquer."

        "Nothing can stop us anymore, not when we’re by each other’s side."

        jump slaborroending

    "Live your own slab life":

        s "I'm... sorry."

        show slaborro sad at center with dissolve

        "I go to say more, but Slaborro raises her hand."

        "Spare her... yeah."

        "She tries her best to hide the disappointment in her voice."

        sb "I understand."

        "I sit up to let Slaborro go. She gets to her feet, her movements slow as if she's in pain."

        "She supports herself against the tree trunk, her hand balled into a fist."

        sb "Thank you all the same. Life was a little brighter with you around."

        "She's reeling. I can see it. But still, she tears herself away to plant a kiss on my cheek."

        "Such an earnest act almost makes me lose my composure."

        sb "Take care of yourself, [slabname]."

        "She stands by the tree hollow's entrance, her eyes towards the sky."

        sb "A storm's coming soon..."

        "And she leaves, just like that. I fall to my knees, clutching my chest."

        "This is for the best. This is for the best."

        "But the silence that occupies the space where she used to stand doesn't deafen me any less..."

        jump slablife

label slaborroending:

    scene bg black with fade
    window show dissolve

    sb "[slabname]! Where are you?"

    scene bg forest with fade
    window show dissolve
    show slaborro happy at center with dissolve

    "I come running out of my hiding spot, knife in one hand and a money bag in the other."

    sb "That’s my slab."

    "Slaborro pulls me in for a quick kiss, but we’re rudely cut short by a couple of angry slabs."

    "Slaborro goes to fight them, but I grip her shoulder."

    "We’ve got all the time in the world to kiss later! We got what we came for."

    "We make a break for it, blissfully ignoring the barrage of insults being thrown at us by agitated slabs who are too slow to catch us."

    "It’s been a few weeks since we left Don Rocko’s and well, we’ve been on the run ever since!"

    "Funny how slabs really don’t appreciate mercenaries and assassins in their midst."

    sb "Have I ever told you you’re a natural at this?"

    s "Yeah, but keep telling me anyway."

    sb "I’ll do anything for a slab with a knife."

    "I chuckle. It really is a surprise I haven’t done more crimes in the past!"

    "Sure, it’s not the best that we keep bouncing around the island, but that’s okay."

    "I don’t really think about my actual home anymore, that little hollow in a tall tree. It just seems like a distant memory at this point when the present has been such a thrill."

    "The most work I’ve done with my fic has been scribblings on a random piece of paper, and I’m sad to report to my two readers that it’ll probably be left unfinished."

    "I look at her, her hair rustling in the wind as we run away, tucking our knives in our pockets, holding on tight to riches we stole, her hair shining in gentle waves."

    "The sight makes me fall in love all over again."

    "Home is where Slaborro is now, and I’m so, so happy."

    "There’s nowhere else I’d rather be than by her side."

    scene cias2 with fade
    window show dissolve
    show slaborro blush at center with dissolve

    "{size=18}{i}[username], thank you for completing {b}Slaborro Good Ending - Tomorrow Never Dies!{/b} Please take a screenshot of this page and follow the directions on the event journal to receive {b}a synthetic potion{/b}!{/i}{/size}"

    jump goodending

label leif:

    window hide dissolve
    scene bg bedroom1 dream with fade
    window show dissolve

    "All I see when I open my eyes is darkness."

    s "Hello?"

    "I walk forward even though I can’t see the path ahead. The only thing I can hear is the sound of dripping water echoing through a vast room."

    s "Is anyslab here?"

    "I break into a run, desperate, looking for any sign of life."

    "A torrent of water stops me in my tracks, rising from the ground with a vengeance."

    "I hold my ground for the first wave, but a deluge comes in all four directions."

    "The flood sweeps me off my feet. I careen into the unknown with nothing but my hands to protect me."

    "In the distance, a tsunami forms. The water recedes and I can do nothing but watch as a monolith grows in front of my eyes."

    "It bows to no one as it morphs and grows, in one instant a giant wave, in another a whirlpool."

    scene bg bedroom2 dream

    "Panic strikes my heart, crashing into my body like waves on a surf."

    scene bg bedroom1 dream

    "Where am I?"

    "What did I do to deserve this?"

    "Questions run rampant in my mind at speeds I can’t catch; before I can grasp one, another takes its place."

    "Just as I begin to doubt whether or not I can make it out alive, I hear a voice come from the shadows."

    "{i}[slabname].{/i}"

    s "Hello?"

    "My eyes settle on a vague silhouette in the distance, outlined by a dim green glow."

    "{i}[slabname].{/i}"

    "Of course... the only other soul is miles away."

    s "Please..."

    "I reach out and pierce my hand through the vortex’s raging waters. It scalds my skin, but I will myself to keep it steady."

    s "Help me."

    "With my question, a gradient of color washes away the darkness. The tempest stops abruptly, leaving only a drizzle of rain to fall from the sky."

    "I feel fingers interlock with mine, a touch so soothing that I feel safe enough to close my eyes and weep."

    "For a moment, it feels balanced; that periods of darkness are fleeting, always to be followed by a splendor of color and light."

    "I feel a hand on my cheek, a soft caress that leaves me breathless."

    "{i}[slabname], I—{/i}"

    "I open my eyes slowly and see.."

    show leif neutral with dissolve

    s "Leif?"

    scene bg bedroom2 with fade
    window show dissolve

    "I wake up with a jump, my heart racing." with vpunch

    scene bg bedroom1

    "What the heck was that dream?!"

    "Leif...?"

    "The sound of birds chirping calms me down, the sight of sunlight streaming through the gap in the curtains warming my heart. It was just a dream, just a dream..."

    "Right?"

    s "Good morning slabworld, and all who inhabit it!"

    "After a little stretch, I jump out of bed and draw the curtains."

    "The chandelier reflects with golden light flooding into the room, immediately dispelling the rest of the shadows from the night before."

    "Too distracted by the chandelier glittering above me, I don’t notice the sound of someslab banging at the door, calling out for me."

    s "Coming!"

    "I run up to the door and open it, and I’m greeted by one of Don Rocko’s slackeys. They look really tired, but they do their best to appear presentable."

    s "Yes, yes... I’ll be there soon."

    "They nod before scurrying away."

    "I go into the room’s en suite to freshen up. A little rinse to wash the sleep off my eyes, a little powder for my cheeks, a little perfume just in case, and I look perfect!"

    "With a spring in my step, I make my way down to where Don Rocko is expecting me."

    scene bg mansion with fade
    window show dissolve
    show don rocko neutral with dissolve

    dr "Ah, [slabname]."

    "Don Rocko calls out to me as I walk down to the main hall. He’s seated in his usual seat, already eating breakfast."

    "On his plate, I see some sunny-slab-ups piled atop toasts slathered with slavocado and a second plate stacked with chocolate chip slabcakes in the image of Don Rocko."

    "I wonder how he manages to eat so many foods that look like himself."

    dr "Come sit."

    "I head over and sit in my chair. Slackeys crowd around and set the table up, placing a clean plate and polished silverware in front of me."

    s "Thank you!"

    "Don Rocko continues eating, occasionally grabbing the slabcake that a slabwaiter intended to bring to me."

    "They smile apologetically when they eventually succeed in fixing up a plate of slabcakes for me."

    dr "So..."

    "Awkward silence... It seems this will just be my new normal."

    "Don Rocko jabs at his food as he thinks of something to say, but judging from his expression, he still seems a bit peeved from last night."

    dr "Did you, uh... sleep well?"

    "I cut into the slabcake and go to speak, but—"

    show don rocko happy with dissolve

    dr "I, for one, slept excellently!"

    "Of course. Once he starts talking about himself, his mood immediately improves."

    "Well, no matter! I don’t have much to say anyway."

    "I nibble away at my slabcake, savoring how {i}divine{/i} it truly tastes, as I think about that weird dream I had..."

    "Leif..."

    "Looking around, it seems that I'm not the only slab with my head in the clouds."

    "Even his slackeys and his bodyguard have tuned his monologue out."

    "They speak amongst themselves, browsing through the slabweb or playing slabgames on their slabphones (Ah, I miss Geopets!), laughing, cracking jokes..."

    "More than anything, I wish I could be with them rather than, you know—"

    show don rocko angry

    dr "Ahem!"

    "I jump to attention, focusing my attention back on Don Rocko." with vpunch

    dr "Why so distracted, hm? I was just getting to the good part of my dream!"

    s "Sorry, sorry! Please tell me more!"

    show don rocko neutral with dissolve

    dr "Ah, as you wish!"

    "Before he could start his story again, one of Don Rocko’s cronies approaches the table."

    "Oh, thank the slabgods!"

    "Don Rocko places his cutlery down so he could lean over and listen."

    show don rocko angry with dissolve

    "Judging from the way his expression changes from a pleased to an annoyed one, I’d say he wasn’t given any good news."

    dr "But I’m in the middle of a—"

    show don rocko blush with dissolve

    "He turns to look at me and rubs the back of his neck, blushing."

    dr "Can’t it wait?"

    "The slackey shakes their head. Don Rocko sighs."

    show don rocko neutral with dissolve

    dr "Well, if it can’t be helped."

    "He tips his fedora at me."

    dr "My apologies, [slabname]. It seems I’m needed at my emporium! I’m sure you’ve heard of it; it’s really quite popular, lots of business, yes..."

    "Dangerously on the edge of falling into another monologue, Don Rocko’s slackey kindly offers to help him off his chair."

    dr "Ah, yes, yes! Thank you, thank you."

    "I make my way down to meet him since it’s, uh, a little hard to speak to him from up so high."

    dr "I will return shortly."

    hide don rocko neutral with dissolve

    "He asks his bodyguard and the rest of his slackeys to accompany him."

    "They exit the hall quickly, leaving dust in their wake. They’re really in a hurry, huh?"

    "That leaves me, however, all on my own... to do whatever I please. Unsupervised."

    "Luckily for Don Rocko, I don’t have much inclination to do crimes! It feels like the perfect opportunity to at least take a little look around."

    scene bg mansion with fade
    window show dissolve

    "I walk up and down long hallways and corridors. The whole castle really feels more like a maze when you’re traversing it alone."

    "It feels a bit scary really, even more so when it looks and sounds like there’s no slabs around to help me in the ever-growing chance I get lost."

    "I push a few closed doors open and take a peek inside. Every single time, the room is never what I expect it to be."

    s "Dining room, got it."

    s "Uh, second dining room? But don't we have a dining {i}hall{/i}? Or was that the main hall?"

    "A few rooms over, I peer inside and see an elaborate gaming set-up, neon tower and all, as well as arcade machines."

    s "Don Rocko is a gamer? Or his bodyguard?"

    "The light-up marquees above the machines read {i}Slab-man{/i}, {i}Slab Invaders{/i} and {i}Dance, Dance Slabolution{/i}."

    "One room comes right after another: the cellar, the home theater, a gym, a bar, a library..."

    "A bowling alley? It’s fun to imagine Don Rocko gathering his personnel to play a round or three."

    "I quickly move past a very, very dark hallway, which I am far too much of a scaredy-slab to investigate on my own."

    "My prowl through the mansion comes to a stop when I see a room that takes my breath away."

    "Hanging on the door is a small floral wreath, a prelude to the majesty that lies behind this wooden barrier I push open slowly."

    "Ceiling-to-floor windows line the walls, flooding the room with warm, golden light. Skylights in the middle of the room are slightly open, allowing fresh air to circulate."

    "Flowers bloom in colorful pots, some spilling with leafy vines that cascade down the benches."

    "Tiny slabs make their home anywhere they feel comfortable, atop petals, buried in the dirt, on comfy sofas like oases in a sea of foliage..."

    "The temptation to stay there forever is strong, to lounge and idle and pass the time by admiring the petals of countless flowers, the refraction of the light..."

    "A gentle breeze blows through the room, detaching a leaf from a plant’s stem and causing it to swirl through the air."

    "I catch it in between my fingers before it can fly out of the room."

    "Such a vibrant green..."

    "I can’t help but be reminded of..."

    "...!"

    "I peel myself away from cushions and the pillows."

    "Surely, it’s only polite to drop by and say hello, right?"

    "I slip out of the conservatory in search of that shadowy recess of the castle, eventually stumbling upon the same scary-looking door I saw before."

    "With both hands on the door’s surface, I push it open with all my might."

    "Completely overestimating my own strength, it takes a good minute to make an opening wide enough for me to walk through."

    "Puffing at the top of the stairwell, I take a second to catch my breath before (properly) making my way down the stairs."

    scene bg dungeon with fade
    window show dissolve

    "My lungs feel like they’re about to cave in when I reach the dungeon."

    "Why does it hurt just as much going down normally as it did tumbling down?!"

    "Surprisingly, Leif doesn’t hear me heaving. They continue gnawing at one of the prison’s bars with pitifully blunt cutlery."

    "When my breathing returns to normal, I walk up to the unsuspecting slab..."

    show leif neutral with dissolve

    s "Hi Leif!"

    show leif shock with dissolve

    "They jump at my greeting." with vpunch

    show leif happy with dissolve

    "But their apprehension is swiftly eased when they look up and see my smiling, apologetic face."

    l "Ah, [slabname]!"

    show leif blush with dissolve

    "They look around at their surroundings and blush."

    l "Please excuse the mess! I... I wasn’t expecting company."

    "They skitter around in an effort to ‘clean’ up, which mostly involves shoving a well-read book and empty plates to the left of their cell, and folded blankets to the right."

    l "A slight improvement."

    "After a cursory sweep of the floor for dust, they take a seat by the bars of the cell. I follow suit."

    show leif neutral with dissolve

    l "To what do I owe the pleasure, [slabname]? Surely there are more interesting places up above!"

    s "Honestly..."

    "I exhale deeply."

    s "This is the only place in the entire castle that feels normal."

    "Leif nods sympathetically, dusting their hands of dirt that gathered on their palms."

    l "You are not wrong in thinking that."

    "A little pile of dust forms in front of us."

    l "But it is bitterly cold during the winter, and uncomfortably chilly during the summer, so it is not too pleasant in that respect."

    "They feign a shiver, and I mask a giggle with my hand."

    s "I... also wanted to spend some time with you."

    show leif blush with dissolve

    "Leif flushes a gentle red, a wide smile tugging at their lips."

    s "Which is definitely much more exciting than whatever’s happening up there!"

    l "Consider me flattered!"

    show leif neutral with dissolve

    l "I do think the arcade’s a tad more exciting though, or perhaps the courtyard."

    s "You’ve explored the mansion before?"

    show leif sad with dissolve

    "Leif nods, though I see an unfathomably bittersweet expression on their face."

    l "Before all..."

    "They gesture vaguely at the bars that separate us."

    l "...this, Don Rocko and I were acquaintances, even friends depending on the day."

    l "Annoying as he is, he can be quite a riot sometimes, particularly in moments when he is not thinking about money... or himself."

    l "Still, I would suffer through his insufferable temperament for the rest of my days rather than waste away in this cell."

    "They lightly tug at the tip of their mustache, lost in thought."

    "Why are they in prison? Why are they the {i}only slab{/i} in prison for that matter?"

    s "I hope you don’t mind me asking, but why did Don Rocko put you here?"

    "Leif shrugs."

    l "I wish I knew, or remembered anyway. I know {i}something{/i} happened, but I don’t know {i}what{/i} happened. I just know that I definitely don’t deserve to be here."

    l "If there are all too many good reasons to deprive a slab of their liberty anyway..."

    show leif happy with dissolve

    "Leif shakes their head and chuckles."

    l "But that’s neither here nor there, my dear slab. I’m here and mostly alive, and that is more than many slabs can say!"

    show leif neutral with dissolve

    "Leif stands up, stroking their chin. With their face half in light and shadow, they’re a picture of what I always imagine a brooding detective to look like."

    show leif happy with dissolve

    l "Though my cell can hardly rival the majesty of a castle, would you like a tour?"

    "I jump to my feet, clenching my fists in excitement."

    s "Lead the way!"

    scene bg dungeon with fade
    window show dissolve
    show leif happy with dissolve

    "I follow Leif as they walk me to the left side of their jail cell. With a flourish, they announce:"

    l "Welcome to... the left side of my home!"

    "I marvel at the empty plates stacked up by the wall. Crumbs scattered around the pile look like little islands in a vast, concrete sea."

    show leif neutral with dissolve

    l "This is where I enjoy my daily meals—"

    "They pick up two plates, wiping them down with their palm before walking over and placing one down on their side of the cell, and sliding the other to me."

    "I sit where they placed their plate, positioning myself and my plate to be opposite them."

    l "—while re-reading the well-worn pages of a beloved book."

    "Leif carefully picks up a hefty, tattered book and tucks it under their arm."

    show leif blush with dissolve

    l "It’s normally a bit nicer than this—"

    "They take a seat by their plate, placing the book in the space between us."

    "I take a glance at its cover: {i}The Last Great White Baraboa{/i}."

    "If there’s a book to be stuck with, that’s definitely one of the better ones. 800 pages? That’d take me five years to read!"

    l "—when there’s food, that is."

    "With their back straight, hands folded in their lap, Leif closes their eyes. I do the same."

    l "If I try hard enough, even a Don Rocko-shaped bread roll could be a fancy dinner."

    l "Together, we enjoy a full course dinner. Candlelight makes polished silverware shine just as its warmth kisses our skins. Under our hands, a soft tablecloth and a satin table runner."

    l "We lose ourselves in conversation until the waft of delicious food draws our attention. One plate at a time, a slabwaiter brings over our meals."

    l "An amuse-bouche, perhaps some sliced slabbatta and cheese infused with honey from the Hissing Rift."

    l "‘Compliments of the slabchef,’ the little slabwaiter would say."

    l "The main course, well, it would assuredly be your favorite meal! What your heart desires in the moment, so it shall be."

    l "As we feast, the dulcet voice of a slab from a time gone by fills the air, but you don’t notice the music at all."

    l "The way the spices dance in your mouth, the taste so precisely quelling your hunger… that is your only consideration in that moment."

    l "Just as you think nothing could top the main course, the dessert comes."

    l "Masked by a silver cloche, the only indication of what could be underneath is a trail of white smoke that follows the platter."

    l "With a flourish, our slabwaiter lifts the cover. A sea of white clouds cloaks the dish from view, and we wait with bated breath until the veil fades."

    l "And there, in the middle of the table, is a bowl of elusive Cervabloom’s Breath."

    l "Metallic sticks in hand, we skewer one of the orbs and place it right on our tongue."

    l "We bite down. It’s so cold, but it melts immediately. Flavor flows from this tiny orbular fountain, fruity and sweet in equal measure, but not too saccharine."

    l "We laugh as white vapor escapes from our mouth and noses, a visible representation of what the dessert’s namesake suggests..."

    "I sit there in almost a trance. The way Leif can describe a scene, it’s like I’m there with them."

    "A glimpse into their imagination thaws the cold. It’s just me and them, enjoying a moment in time that only we could ever know."

    "I hear Leif force a laugh and I open my eyes. They rub the back of their head, averting their gaze to a particularly dusty corner of the cell."

    show leif shock with dissolve

    l "That’s… silly to hear out loud. I apologize for that!"

    s "No, it's okay!"

    "I wrap my hand around one of the bars."

    show leif happy with dissolve

    s "The tablecloth, the plates, the food, the atmosphere; it’s so clear in my mind. I wish you could experience that again."

    "They wrap their hand around mine. They’re so warm, like a blanket, a candle..."

    "I blush at the touch. Ah, keep your cool, [slabname]!"

    show leif blush with dissolve

    l "I wish I could experience it with you."

    "They give my hand a squeeze. I could faint at this moment. They’re so sincere, a breath of fresh air in this weird, weird world."

    l "[slabname], I—"

    "Before they can say anything more, we hear footsteps echo through the dungeon. We look at each other wide-eyed."

    s "Oh no."

    "Leif lets go of my hand and I jump to my feet."

    show leif neutral with dissolve

    l "This is unusual. He never comes here."

    hide leif neutral with dissolve

    show don rocko neutral at left
    show leif neutral at right
    with dissolve

    "There he is, the unwanted man of the hour."

    show don rocko shock at left with dissolve

    "He freezes when he sees me by the jail cell."

    dr "[slabname], what are you doing here?"

    "His eyes dart between me and Leif."

    show don rocko angry at left with dissolve

    dr "What's going on here?"

    "Leif and I look at each other, panic simmering in our eyes."

    l "Well, I—"

    show don rocko neutral at left with dissolve

    "Don Rocko chuckles."

    dr "Just as I suspected."

    "Don Rocko walks up to me and wraps an arm around my shoulder."

    dr "You truly are fit to be by my side."

    "I laugh, albeit very confused. I try not to let it show on my face."

    show don rocko happy at left with dissolve

    dr "You’re already checking up on my prisoner for me!"

    "Leif nods enthusiastically."

    l "Yes, yes! A check-up, yes. Just as you would do."

    "Don Rocko drawls as he pulls me closer to him."

    show don rocko blush at left with dissolve

    dr "You do know me so, so well."

    "I wouldn’t put it like that, but whatever makes him happy."

    show don rocko neutral at left with dissolve

    dr "Now that that’s settled, come with me. There’s something I want to show you. I’ve been waiting all—"

    "{i}*CRASH*{/i}" with vpunch

    "The three of us turn around to see what’s causing the noise,  our unspoken questions answered by a little slab rolling to a stop at Don Rocko’s feet."

    "They scramble to their feet, unharmed and simply glad that they managed to keep the small potion in their hands safe. Don Rocko frowns at the display."

    dr "Well, out with it. Why have you interrupted me?"

    "The slackey places the potion in Don Rocko’s hands before leaning in, whispering something important in Don Rocko’s ear."

    "He nods every so often, but ends the exchange with a frown on his face."

    show don rocko angry at left with dissolve

    dr "But I’m in the middle of a—"

    "He looks at me before looking back at his slackey."

    dr "Can't it wait?"

    "The slackey shakes their head. Don Rocko sighs."

    show don rocko neutral at left with dissolve

    dr "Well, if it can’t be helped."

    "He tips his fedora at me."

    dr "My apologies, [slabname]. It seems I’m needed at my emporium! I’m sure you’ve heard of it; it’s really quite popular, lots of business, yes..."

    "Dangerously on the edge of falling into another monologue, Don Rocko’s slackey kindly offers to carry the potion they just handed to him."

    dr "Thank you, of course."

    hide don rocko neutral
    show leif neutral at center
    with dissolve

    "And with nothing else said, Don Rocko and his slackey walk back up the stairs."

    "Leif and I wait, afraid to take a breath. When we hear the dungeon door thud shut, we exhale."

    show leif sad at center with dissolve

    l "That was close."

    s "He can really be so exhausting."

    "And to think he left without even inviting me! How rude! Not that I would've left with him, but it’s always nice to be asked!"

    scene bg dungeon with fade
    window show dissolve
    show leif happy with dissolve

    "Leif continues their house tour."

    l "Welcome to… the right side of my home!"

    "If the left side was a dining room, the right side looks more like a bedroom. Instead of a bed, Leif crawls over to a pile of blankets and flat pillows and drags them closer to us."

    l "Truly, I live in the lap of luxury."

    show leif neutral with dissolve

    "Leif pushes a pillow under the bars for me to sit on."

    l "Much nicer than the concrete, no?"

    "As much as the cold bites at our hands and feet, it’s warm under these blankets, like a pocket of sunlight shining over a clearing in a dark forest, or a homely cottage in the middle of a snowstorm."

    s "It is surprisingly cozy, which is a strange thing to say in a dungeon."

    show leif happy with dissolve

    "Leif smiles, a soft sort of smile that rivals the brilliance of the sun."

    l "Whenever I turn in for the night, it becomes easier with every day that passes to imagine myself sailing under a sea of stars."

    show leif sad with dissolve

    "They close their eyes, but I keep mine open."

    l "Granted, my only source of entertainment has been a novel following the treacherous journey of a sailor slab in pursuit of the fabled White Baraboa..."

    l "Still, I imagine myself as a sailor, my pillows forming the vessel, the blankets becoming the sails."

    l "Most times, I drift on soft-flowing water. The ocean takes me where she wants to go, and I am but a witness to what occurs."

    "They look so serene as they paint the picture in their mind."

    l "Sometimes, however, I become Ahslab. A tempest approaches in the distance, whipping the wind into a frenzy."

    l "The tail of my coat flutters behind me. I hold down my captain’s hat lest it flies away."

    l "Something resides in the deep, an unmistakable rumbling that strikes fear in even the most hardened of slabs."

    l "But I know these seas, these stormy waters that have felled countless sailors before me."

    l "And this creature, this beast of the depths... I must pursue it. I must, even if it means my watery end."

    l "At the end of the storm, it’s nowhere to be found, the tempest tempered as a new day breaks."

    l "And yet, there I stand, at the edge of the world, it’s only me in that vast, wide, beautiful ocean."

    show leif neutral with dissolve

    "Their face softens, a sad smile forms on their face."

    l "Trapped between the sky and the sea, accompanied only by a horizon, I await waiting for a first mate to take stead by my side."

    "..."

    "..."

    "..."

    s "How... How lonely."

    show leif shock with dissolve

    "Tears well in my eyes. Leif opens theirs and panics when they see me on the verge of weeping."

    l "Oh no! I’m very sorry, [slabname]!"

    show leif sad with dissolve

    l "I didn’t realize how depressing that would sound outside of my own head."

    s "No, no! It’s just—"

    s "I wish you weren’t stuck behind here, and you could go back to living out here, in this wide world..."

    "Leif reaches through the bars and cups my cheek, wiping the tear away from my face."

    show leif blush with dissolve

    l "And I wish I could be by your side..."

    "My heart feels as if it’s about to burst. Leif..."

    "They deserve so much more than the hand they were dealt."

    s "I—"

    "There must be something I can do."

    "I stand up, my fists clenched."

    s "I can help you get out."

    "Leif stands up to meet me."

    show leif sad with dissolve

    l "[slabname]—"

    s "I know, I know, it sounds silly but—"

    l "You’ll get in trouble. I don’t want—"

    "I grab Leif’s hands through the bars, gripping them tight."

    s "I want to."

    "Leif averts their eyes."

    l "But… but why? I’ve accepted my situation. There’s no need to go through all that trouble on my behalf."

    s "All of those vivid stories you tell yourself, and you accept your situation?"

    "I smile."

    s "I don't think so."

    "Leif shakes their head."

    l "[slabname]..."

    "I lift their chin up and look into their eyes. I see them glisten just as mine do."

    s "We’ll get you out of here. I promise."

    show leif blush with dissolve

    "Leif gently pulls me in for a hug. Awkward as it is with the bars in the way, it’s still so warm. I melt in their arms."

    l "Thank you sincerely, [slabname]… This means the world to me."

    "My heart swells, surging with waves of a feeling that I can’t place..."

    "Could it be...?"

    l "But—"

    "Leif breaks the hug just in time for me to keep my composure."

    show leif neutral with dissolve

    l "What remains is the question of how we’re going to go about doing that."

    "We? They said we! Does that mean...?"

    "I tell my heart to behave; your affairs can wait for a moment longer."

    "We have a jailbreak to mastermind."

    scene bg dungeon with fade
    window show dissolve
    show leif neutral with dissolve

    "My eyes follow the sun rays up to the open window. It’s barred, but—"

    s "Surely, you’ve tried to get out through the window, right?"

    l "Plenty of times, but I can’t stack my pillows and blankets and plates high enough."

    "I rub my chin. A debacle indeed."

    "Ah! How could I forget?"

    "Leif runs over to the corner where they were sitting when I greeted them this morning."

    l "I’ve been chipping away at this bar and well, perhaps I’ve weakened its structural integrity enough to do something with it."

    "I take a look and shake the bar a bit. It’s a bit loose for sure."

    s "Maybe I could find something to help bend it or pry it open."

    l "What are the odds that something helpful would be lying around?"

    "I shrug."

    s "There’s gotta be something in this gigantic place, right?"

    l "I do wish I could help you, but the best I can do is wish you the best."

    "Leif grasps my hands firmly before I depart."

    l "Be safe. You know where to find me."

    "They’re just! So! Sweet! I can’t wait to see them again soon..."

    "I need to get them out, no matter what it takes."

    "(Well, there are some limitations, but you know...)"

    scene bg black with fade

    "I make my way up the stairs, keeping my footsteps light to make as little noise as possible. And thankfully so!"

    "It seems that Don Rocko didn’t take the rest of his goons with him, as the place is now filled to the brim with his slackeys."

    s "Where the heck did they come from?"

    "I sit by the dungeon door, peering out every so often to see if the slackeys patrolling the hallway get distracted and walk away."

    "Whenever there’s a clearing, I scuttle out, being as stealthy as I can be."

    scene bg mansion with fade
    window show dissolve

    "I feel so cool, like a spy in a  B-movie! I imagine the red lasers, dodge rolling under and around them to avoid setting off the alarms, but of course that’s all in my head."

    "In reality, all I really do is hide behind bends in the hallways and blend in with the wall."

    "Still, if Leif could see me now!"

    "I look for and open any drawers and cabinets I see. Once I finish checking one room, I move into another, repeating this cycle until I find something that can help."

    "As I search through the arcade, I hear slackeys enter the room. I dive behind one of the cabinets."

    "They play a couple rounds of {i}Slab Fighter IV{/i} before they get bored and go back to work."

    "I breathe a sigh of relief. Stopping myself from playing a round myself, I skitter away."

    "The next bend in the hallway shows a familiar sight, that extremely dark hallway."

    "My face darkens, but..."

    s "Better now than never."

    "I round the corner and walk down a long, {i}long{/i} and extremely dark corridor."

    "Hanging on the walls are intricate paintings of Don Rocko himself, in a variety of different poses and scenarios."

    "I marvel at them, though I’m unsure if I like them or if they’re so strange it’s impossible to look away."

    "Eventually, I arrive in front of an imposing vault door. Made of solid gold, how to unlock it doesn’t seem immediately evident."

    "I examine the door up close. I really don’t have the words to describe how gigantic it is."

    "Even if I could find some way to open it, it looks like it’s one of those doors that don’t open on their own."

    s "No way I can get in there."

    "Before I turn around to leave, I see something glimmer near the vault. I look over my shoulder."

    "I walk closer and see the legs of a gold slab popping out from a crack in the wall. Barely visible, but there nonetheless."

    "After waiting a while, a little slab emerges. They jump when they see me, knocking the feather duster they had off their head."

    s "I'm sorry, I'm sorry!!!"

    "I help place the feather duster back on their head and they smile at me gratefully."

    s "Were you just in there?"

    "The little slab nods."

    "I think for a moment. I definitely can’t fit in there, but if they can get out, then—"

    s "Say... Do you think you can help me with something?"

    "They nod enthusiastically. They seem very eager to help!"

    s "There is some slab I want to help out in the dungeon downstairs. Do you know them?"

    "Their eyes sparkle at my words. They rummage through the feather duster on their head and produce an unopened bandaid. They offer it to me on an outstretched hand."

    "I take it and stash it away."

    s "I'll be sure to give it to them!"

    s "Do you think there’s anything in there that could help them out of their cell? Something to pry open the bars, anything."

    "The slab furrows their brows before crawling back through the crack in the wall."

    "I wait by the opening, kicking up dust in the corner. It seems nobody really goes here and understandably so. A place like this probably wouldn’t be visited unless you were with Don Rocko."

    "A few minutes pass and I hear the sound of something heavy being dragged across the floor come from the other side of the wall, broken up by faint panting."

    s "Did you need some help?"

    "The little slab doesn’t — or couldn’t — respond."

    "Eventually, I see something metallic sticking out from the opening. I help pull it out, revealing the little slab clutching onto the item as they pat away beads of sweat with their feather duster."

    "I see that they’ve somehow brought along—"

    s "A pry bar! Fantastic!"

    "The slab gives me a weary thumbs up as they catch their breath."

    s "Thank you so, so much."

    "I pick up the crowbar and even I struggle with it. How did they carry this all on their own?"

    "I give them a tiny fist bump as I hoist the crowbar on my shoulders. Can’t be making noise by dragging this all over the mansion, after all."

    "They wave goodbye as I walk away."

    "It’s much, much harder to be inconspicuous with this pry bar on me, but I do my best."

    "I fare mostly well for the journey back. That is, until—"

    "{i}*THUNK*{/i}" with vpunch

    "The bar slams into the ground, making a slab-shattering noise that echoes through the empty halls."

    "Uh-oh."

    "I quickly pick up the bar and grip it tight, waiting for the slackey who’ll inevitably come to investigate."

    "I shouldn’t use this for evil, but if I must—"

    "I hide behind one of the vases in the hallway and try not to make a noise, but it seems that I would not be the one betraying my location. Rather, a mere sun ray causes the metal to gleam and—"

    "Footsteps. Fast footsteps."

    "I muster up the last of my courage and jump out from my hiding spot, bar pointed towards any approaching adversaries."

    "I lock eyes with a slabster. My fingers flex around the bar."

    "The slabster, however, simply throws their hands up, exasperated, saying that they don’t get paid enough to deal with this sort of nonsense, that they don’t get paid at all."

    "They walk away grumbling, stomping their feet on their way back to their post."

    s "Well, that was easy..."

    "I quickly retrace my steps and run back to the dungeon."

    scene bg dungeon with fade
    window show dissolve
    show leif neutral with dissolve

    "When I make it back to Leif, I’m visibly puffed out. Who would’ve thought that carrying a metal bar everywhere is going to be such a workout?"

    "Leif offers me the tragically lukewarm glass of water they were given by a slabster while I was away."

    l "Are you okay, [slabname]?"

    "I nod as I take a sip of water."

    s "All good, all good."

    "I push the bar over to Leif, who takes it in their hand."

    show leif happy with dissolve

    l "This — this is fantastic!"

    l "Where in the world did you end up to find this?"

    s "Stumbled... across... the vault."

    "I give them the bandaid as I tell them about the little slab."

    l "Ah, Slabson is still there, is he?"

    "They tear open the bandaid packet and apply the adhesive on one of their scratches."

    show leif happy bandaid with dissolve

    l "Good for him! I must give him my thanks when I see him next."

    show leif angry bandaid with dissolve

    "Patched up and thinking of their kind friend, they wield the bar with more confidence, propping it up against the compromised cell bar. Taking a few deep breaths in, they pull and pull."

    "The cell bar, however, doesn’t seem to budge."

    show leif sad bandaid with dissolve

    l "I confess, I am not the strongest slab."

    "I walk over to help them, wrapping my hands around theirs."

    show leif blush bandaid with dissolve

    s "But together, perhaps...?"

    l "Together."

    "We tug on the pry bar with all our might."

    "Slowly but surely, the cell bar starts to give way, bending precisely at its weakened spot."

    s "It's working!"

    show leif happy bandaid with dissolve

    l "We can do this!"

    "Straining ourselves, we keep pulling and pulling until the bar is widened enough for Leif to leap through."

    "We let go of the bar. It drops to the floor with a resounding thunk."

    "Leif hurriedly jumps out from the opening and onto free land."

    show leif shock bandaid with dissolve

    "They freeze for a moment, as if they need to recalibrate or wrap their head around the reality of the situation."

    "..."

    "..."

    "..."

    show leif blush bandaid with dissolve

    l "[slabname]."

    "Leif starts walking up to me slowly. I swear I start to hear gentle music coming from outside."

    s "Leif...!"

    "Leif wraps their arms around me, pulling me into a tight embrace."

    "I rest my head on their chest."

    "I’ve never felt more warm, more at home, than I do in this moment."

    l "I’ve been wanting to do this for so long..."

    s "Oh, Leif...!"

    "Their steady hands travel up to the back of my head, gently running their fingers through my hair."

    "It’s such a soothing sensation."

    l "Thank you sincerely, [slabname]. I owe my freedom to you."

    "I feel so completely safe with them."

    s "You deserve it more than anyslab."

    "Leif clears their throat before breaking the hug. I giggle as I watch them dry their eyes with their mustache."

    l "Though it would be quite pleasant to stay like this forever..."

    s "Let's get out of here."

    scene bg black with fade

    "I take their hand and we run up the stairs."

    scene bg mansion with fade
    show leif blush bandaid with dissolve

    "Becoming as light as a feather when more than one slab tries to conquer it, the dungeon door flies open when the two of us burst through it."

    "It seems subtlety takes a back seat when you’re gripped by the power of {b}LOVE{/b}!"

    scene bg mansion with fade
    window show dissolve
    show leif neutral bandaid with dissolve

    "Of course, this doesn’t help us at all. Slabsters are immediately made aware of our presence."

    s "Run!!!"

    "The slabsters scramble to get us, but we maintain our distance, running as fast as our legs can carry us."

    s "We’re almost there!"

    "Of course, the palace becomes an incomprehensible mess of smoke and mirrors. Once I think I’ve made the right turn to the entrance hall, it’s just another hallway."

    dr "And where do you think you're going?"

    show leif shock bandaid with dissolve

    s "I knew I should've turned left."

    "Don Rocko’s voice comes from behind us, dripping with malice."

    dr "Was I not enough for you, hm?"

    "We keep running, but Don Rocko’s voice does not waver, nor does it seem distant."

    dr "And you settle for this..."

    "I can’t see him, but I imagine he gestures vaguely towards Leif."

    dr "...I cannot believe I ever called you a friend."

    hide leif shock bandaid with dissolve

    show don rocko neutral at left
    show leif angry bandaid at right
    with dissolve

    "Leif stops in place. They turn around. Don Rocko laughs in turn."

    dr "It seems the coward has found their backbone."

    "I turn around and see Don Rocko staring Leif down. He’s hoisted up on the backs of slackeys who do their best to carry him in between yawns."

    l "You dare call me the coward, when you are the one who cannot face your problems head on?"

    "Don Rocko feigns offense."

    dr "That cuts deep, Leif. Are you still bitter that I put you in a cell?"

    l "You denied me of my freedom for no good reason! Of course I’m bitter."

    dr "There was a good reason!"

    "Don Rocko goes to explain his reason but—"

    show don rocko shock at left with dissolve

    dr "Uh—"

    "He turns to his bodyguard and his slackeys."

    show don rocko sad at left with dissolve

    dr "Do you guys know?"

    show slaborro neutral at center with dissolve

    "The group exchanges confused looks amongst themselves. The bodyguard shrugs."

    sb "I don’t remember having a record of theirs stashed anywhere."

    hide slaborro neutral with dissolve

    "Don Rocko stands aghast."

    show don rocko shock at left with dissolve

    dr "Blasted paperwork...!"

    "He shifts his attention back on us, his face taut for a moment before returning to his usual arrogant self."

    show don rocko blush at left with dissolve

    dr "Well, semantics, semantics! A thing of the past."

    "Leif’s mustache twitches."

    l "Hardly!"

    show don rocko neutral at left with dissolve

    dr "I feel this is the time where I should let you go free, but—"

    "Don Rocko steepled his fingers."

    dr "I'm afraid it won't be that easy."

    "I grab Leif’s hands."

    s "He's stalling! We have to go!"

    "Leif grits their teeth, but they relent."

    hide don rocko neutral
    show leif neutral bandaid at center
    with dissolve

    "We rely on our feet to move us forward. It’s terrifying hearing Don Rocko’s bellowing laugh echo behind us."

    dr "Run while you can!"

    "We round a corner and see the main hall in all its splendor."

    s "There!"

    dr "Faster, faster!"

    "Don Rocko barks at his slackeys to crowd around the door just as we sprint down the stairs."

    "Waves of slabs climb on top of one another, creating a wall that blocks the door before we could cross the entrance hall."

    "I feel Leif tighten their grip around my hand."

    show leif angry bandaid at center with dissolve

    l "Keep a steady course."

    s "But we'll—"

    l "A wave will inevitably crash. The best we can do is expedite the process."

    "Leif picks up the pace."

    "We charge at the wall, bracing ourselves for impact."

    "I take a quick glance up at the slabs and see some of them starting to sweat."

    "Some begin to fidget, causing the wall to wobble."

    show leif happy bandaid at center with dissolve

    l "Bingo."

    "Before we can make contact, the wall collapses. Slabs spill out across the hall’s floor."

    "Our shoulders meet the entrance doors and force them open."

    scene bg forest with fade
    show leif happy bandaid at center with dissolve

    "We hear Don Rocko scold his slackeys before yelling out to us."

    dr "You’ll be back! Everyone always comes back!"

    "But Don Rocko’s voice tapers away the deeper we go into the woods, feeling the wind tousle our hair and the afternoon sun kiss our skin."

    "In that moment, I have never felt more free."

    scene bg forest with fade
    window show dissolve
    show leif happy bandaid at center with dissolve

    "We don’t stop running until we’re some distance enough away from the castle."

    "We look over our shoulder and thankfully see no slabsters following us."

    "After taking a second to catch our breaths, we collapse into each other’s arms."

    show leif blush bandaid at center with dissolve

    l "Finally..."

    s "You're free."

    "Leif hugs me tight, resting their head on top of mine."

    l "All because of you."

    "I feel my heart pounding. This is it."

    "This is the moment we’ve both been waiting for."

    l "[slabname], I—"

    "They shake their head."

    l "Ah, it is a most foolish thing to say..."

    "I shake my head."

    s "You’re the most level-headed slab in this whole place. You always say the right things."

    "Leif takes a deep breath before cupping my face with their hands."

    l "I have spent so long chasing something I cannot name. Like a phantom, it eludes me, showing up only in the stories I weave in my head, or the dreams that fill my evenings."

    l "After meeting you, I... realize I’ve been chasing the wrong thing. The fabled white Baraboa is just that, a myth."

    "Leif gently strokes my cheek."

    l "This feeling, it’s so strange. I don’t know how to describe it, but I know that it’s because of you I feel so happy."

    l "Freedom, yes, but there’s something more... something better to celebrate."

    "I know we’ve only known each other for a few days, but..."

    s "I feel the same."

    l "I—I—"

    "I giggle in spite of myself. I’ve never seen them so speechless!"

    l "I am... truly lost for words...!"

    "I speak for them. I gently pull them in and kiss them tenderly."

    "They respond by wrapping their arms around me."

    "It feels right, so right."

    "These days have gone by in the blink of an eye, but for now, the world stops to let us enjoy this moment."

    "We’re free. We’re really free."

    "And we’re free to do whatever we want, in love and so, completely alive."

    "When we break the kiss, we lose ourselves in each other’s eyes."

    l "A fresh start, a new world to explore, together with you."

    "They too are smiling from ear to ear, flushed red like a ripe tomato."

    "I start to think about what we should do next. Should we live together?"

    "I mean, we could make it back to my place, but would we both fit?"

    "Ah, it doesn’t matter. Wherever Leif is is where I want to be. We’ll be able to make it work, I know it!"

    "..."

    "..."

    "..."

    scene bg black with fade

    s "Night certainly came early, huh? Time just flies when you’re in love!"

    l "I don't think—"

    "Oh no. Not this again."

    l "[slabname]? Where are you?"

    "I feel slabs pulling me away from Leif."

    s "Hey, wait! Stop this!"

    "We hear the slabs snickering."

    "In all fairness, we were quite distracted."

    "Yeah... Yeah."

    "Serves us right for getting lost in each other’s eyes before actually getting away."

    "Starstruck slablovers, for better or for worse!"

    scene cias2 with fade
    window show dissolve
    show leif blush at center with dissolve

    "{size=18}{i}[username], thank you for completing Act Two - {b}Leif{/b}! Please take a screenshot of this page and follow the directions on the event journal to have {b}one leaf OR rock (your choice){/b} added to your inventory.{/i}{/size}"

    scene bg mansion with fade
    window show dissolve
    show leif sad bandaid with dissolve

    "The blindfold around our eyes fall."

    "We’re right back in the main hall. Figures."

    "Our hands are also bound, but at least they’re bound together. It’s much more comforting that way."

    hide leif sad bandaid with dissolve

    show don rocko neutral at left
    show leif sad bandaid at right
    with dissolve

    "We see Don Rocko walking up to us, as menacing as a small slab like him can be. He’s cackling like the villain he is."

    dr "Fools! Did you think you could escape so easily?"

    l "We did escape..."

    dr "Did you think you could escape so easily and stay escaped?"

    s "That—"

    "I don’t bother."

    "The way he speaks — as if what comes from his mouth are the most important words that have ever been said — means he won’t listen to corrections anyway."

    dr "Now, what shall I do with you two, hm?"

    show leif angry bandaid at right with dissolve

    "Leif tries to free us from our bindings, but it’s no use. They bare their teeth, frustrated at this golden menace."

    l "It doesn’t matter. I will always be the better slab than you, and you know it."

    "A silence falls over the crowd, but I can tell what they’re all thinking."

    "Leif really is so, so much better than Don Rocko for sure."

    "Don Rocko turns away from Leif with a huff, focusing on me instead."

    show don rocko angry at left with dissolve

    dr "And you..."

    "He walks up to me with a scowl on his face."

    dr "I can’t help but feel a bit... betrayed by your actions. You’d rather go off with a prisoner than stay with an {i}entrepreneur{/i} like me?"

    "I scoff at his words."

    s "If you hadn’t jailed them for literally no reason, they wouldn’t be a prisoner in the first place."

    dr "You’re still hung up on that, huh?"

    "Leif and I shout a resounding 'Yes!' Don Rocko simply shrugs."

    show don rocko happy at left with dissolve

    dr "Well, you’ll have plenty of time to get over it in jail."

    scene bg dungeon with fade
    window show dissolve
    show leif neutral bandaid with dissolve

    "And so ends our 10 minutes of freedom."

    "We’re back where we started, shivering in that dingy, cold dungeon. At least this time, we’re both behind bars."

    show leif happy bandaid with dissolve

    l "Better together than all alone again, I suppose."

    "We sit right under the window, where the last few moments of sunlight keep us warm."

    "I lean my head on their shoulder."

    s "I’m sorry that didn’t work out any better."

    "They lean their head on mine."

    l "It was a valiant effort all the same."

    show leif neutral bandaid with dissolve

    "Leif twirls their mustache as I look around the cell."

    "Leif and I are pretty normal-sized slabs, but this cell... You could fit 100 of us in here."

    s "This cell is, like, way, way bigger than my actual house."

    "Leif scans the cell themself."

    l "Come to think of it, it really is quite big."

    "Outside from how perpetually cold the ground is, there’s still plenty of natural light and plenty of warmth to be had by snuggling in close."

    l "Perhaps with more pillows and blankets, this could definitely be transformed into something of a home..."

label leifdecision:

    "I stay silent."

    l "It’s possible we likely won’t be able to afford anything bigger on the outside... You know how the housing market is nowadays..."

    "This... this is a really big decision, huh?"

    "But I need to decide. It’s now or never."

menu:

    "Stay with Leif":

        "I pull Leif in close."

        s "Home is wherever you are. Where we live doesn’t matter!"

        show leif blush bandaid with dissolve

        l "[slabname]...!"

        "They pull me in for a kiss that I happily reciprocate."

        "I’m in love, Mom! Are you proud of me?"

        "We resolve to spend the rest of our life in this cell. Sad as it may sound, it’s really quite comfortable."

        "When we’ve both had the chance to actually sit and get to know one another more, it turns out we’re both homebodies!"

        "This arrangement could be better, but it certainly could be worse."

        "The slackeys tend to give us what we need, from food and water to leisure items including my laptop and piles of new books for Leif! How nice of them!"

        l "{i}Les Miseraslabs{/i}? {i}War and Piece{/i}? Fantastic!"

        "I continue writing my fanfics. I actually have a beta reader this time, so my viewership is going way up!"

        "I even finished the one I started about Slabsune Miku and Sailor Slab before, but I think the ending is not what my readers are expecting..."

        "Don Rocko never checks up on us anymore. I’m sure he’s forgotten about us, and that’s totally fine."

        "We’re content in our little corner of the world, snuggling together, talking about anything and everything. As long as we’re side by side, everything will be right."

        scene cias2 with fade
        window show dissolve
        show leif blush bandaid at center with dissolve

        "{size=18}{i}[username], thank you for completing {b}Leif Good Ending - A Study in Foliage!{/b} Please take a screenshot of this page and follow the directions on the event journal to receive {b}a synthetic potion{/b}!{/i}{/size}"

        jump goodending

    "Live your own slab life":

        s "I'm... sorry."

        show leif sad bandaid at center with dissolve

        "I go to say more, but Leif stops me."

        "They try their best to hide the disappointment in their voice."

        l "I understand."

        "They back away from me before pressing a hand to their chest."

        l "I thank you for everything, [slabname]. If anything, I am glad to have lived a free life with you, as fleeting as it may have been."

        "They're blind-sided, that much is evident from their facial expression. Still, they find it within themself to plant one kiss on my cheek."

        "Such a sincere act almost makes me reconsider my decision."

        l "Take care of yourself, [slabname]."

        "They take one of the folded-up blankets and urge me to take it in case I get cold."

        l "And think of me with fondness."

        "I will my heart to stop rending as I look for a way out. The bar is no longer bent, but—"

        "Wait..."

        "Have these bars always been big enough to slide under?"

        "No matter..."

        scene bg black with fade

        "I can’t stop my knees from wobbling as I march solemnly up the stairs."

        "This is for the best. This is for the best."

        "What Leif may have been chasing, I don't know for certain... But I hope they find their Baraboa one day. They deserve as much, and so much more."

        jump slablife

label donrocko:

    scene bg bedroom1 dream with fade
    window show dissolve

    "All I see when I open my eyes is darkness."

    s "Hello?"

    "I walk forward even though I can’t see the path ahead. The sound of my footsteps meld with a medley of noises coming from every direction in this vast room."

    s "Is anyslab there?"

    "I break into a run, desperate, looking for any sign of life."

    "What I’m greeted with, however, is a wall of discordant sound. With each step I take, it grows louder by a decibel. Static, clamor, vicious, deafening..."

    "I try to cover my ears, but it helps none. The cacophony is almost too much to bear."

    "I fall to my knees, almost drilling my hands into my ears to block out the sound."

    scene bg bedroom2 dream

    "Where am I?"

    scene bg bedroom1 dream

    "Why have I been subject to this?"

    "Questions run rampant in my mind at speeds I can’t catch; before I can grasp one, another takes its place."

    "Just as I begin to doubt whether or not I can make it out in one piece, I hear a voice come from the shadows."

    "{i}Stop.{/i}"

    "It speaks with such authority that it manages to quell the chaotic sounds around me."

    "I let my hands fall."

    s "Thank—thank you..."

    "Grateful, I scan the room to try and locate the voice’s source."

    "{i}[slabname].{/i}"

    s "Hello? Where are you?"

    "My eyes settle on a vague silhouette in the distance, outlined by a dim golden glow."

    "I run towards it, my hands reaching out."

    "{i}[slabname].{/i}"

    "I stop when I feel fingers interlocked with mine."

    "Yet, I don’t see anyslab around me."

    s "Where are you?"

    "With my question, a gradient of color washes away the darkness, birdsong comes floating in on a gentle wind."

    "This sound... It's so comforting, like a warm embrace on a bad day. I feel safe enough to close my eyes."

    "For a moment, it feels balanced; that periods of darkness are fleeting, always to be followed by a splendor of color and light."

    "I feel a hand on my cheek, a caress that leaves me breathless."

    "{i}[slabname], I—{/i}"

    "I open my eyes slowly and see..."

    show don rocko blush at center with dissolve

    s "... Don Rocko?!?"

    scene bg bedroom1 with fade
    window show dissolve

    "I wake up with a jump, my heart racing." with vpunch

    "What the heck was that dream?!"

    "Don Rocko...?"

    scene bg bedroom2

    "The sound of birds chirping calms me down, the sight of sunlight streaming through the gap in the curtains warming my heart. It was just a dream, just a dream..."

    scene bg bedroom1

    "Right?"

    s "Good morning slabworld, and all who inhabit it!"

    "After a little stretch, I jump out of bed and draw the curtains."

    "The chandelier reflects with golden light flooding into the room, immediately dispelling the rest of the shadows from the night before."

    "Too distracted by the chandelier glittering above me, I don’t notice the sound of someslab banging at the door, calling out for me."

    s "Coming!"

    "I run up to the door and open it, and I’m greeted by one of Don Rocko’s slackeys. They look really tired, but they do their best to appear presentable."

    s "Yes, yes... I’ll be there soon."

    "They nod before scurrying away."

    "I go into the room’s en suite to freshen up. A little rinse to wash the sleep off my eyes, a little powder for my cheeks, a little perfume just in case, and I look perfect!"

    "With a spring in my step, I make my way down to where Don Rocko is expecting me."

    scene bg mansion with fade
    window show dissolve
    show don rocko neutral with dissolve

    dr "Ah, [slabname]."

    "Don Rocko calls out to me as I walk down to the main hall. He’s seated in his usual seat, already eating breakfast."

    "On his plate, I see some sunny-slab-ups piled atop toasts slathered with slavocado and a second plate stacked with chocolate chip slabcakes in the image of Don Rocko."

    "I... kind of appreciate the confidence he must have to eat so many foods that look like himself."

    dr "Come sit."

    "I head over and sit in my chair. Slackeys crowd around and set the table up, placing a clean plate and polished silverware in front of me."

    s "Thank you!"

    "Don Rocko continues eating, occasionally grabbing the slabcake that a slabwaiter intended to bring to me."

    "They smile apologetically when they eventually succeed in fixing up a plate of slabcakes for me."

    dr "So..."

    "Don Rocko jabs at his food as he thinks of something to say, but judging from his expression, he still seems a bit peeved from last night."

    "Awkward as it is, something about him just feels... different. Is it because of the dream I had?"

    dr "Did you, uh... sleep well?"

    "I cut into the slabcake and go to speak, but—"

    show don rocko happy with dissolve

    dr "I, for one, slept excellently!"

    "Once he starts talking about himself, his mood immediately improves."

    "Strangely enough, I don’t feel annoyed. In fact, part of me {i}wants{/i} him to keep monologuing as I nibble away at my slabcake, savoring how {i}divine{/i} it truly tastes."

    "Sure, I hear his slackeys and his bodyguards speaking amongst themselves, tapping away on their slabphones and enjoying their slabgames, but I tune them out."

    "I focus on him speaking. His voice... It's so dulcet, so smooth. I don’t even know what he’s talking about, but please! Keep speaking!"

    show don rocko blush with dissolve

    "It seems the sun also wants to listen. Rays of light come shining down from above, giving Don Rocko this almost godly glow to him."

    "Thankfully, he doesn’t seem to notice thanks to his fedora, but I can’t help but stare..."

    "Was he always so handsome?"

    show don rocko neutral with dissolve

    dr "And that’s my dream. Very cool, right?"

    "I nod dreamily. Don Rocko’s lofty pretense breaks for a moment, the confusion on his face evident."

    show don rocko shock with dissolve

    dr "You were listening?"

    s "Of course... Tell me more!"

    show don rocko neutral with dissolve

    "Don Rocko grins, as if to say, 'You don’t need to tell me twice!'"

    "Ah!!! I feel myself flush slightly, but that doesn’t stop Don Rocko from launching into another monologue."

    "Before he could get too far in, one of Don Rocko’s cronies approaches the table, rubbing their eyes."

    show don rocko angry with dissolve

    "Judging from the way his expression changes from a pleased to an annoyed one, I’d say he wasn’t given any good news."

    "He grumbles, evidently angry that they interrupted a tender moment."

    dr "Am I needed {i}now{/i}?"

    "The slackey nods. Don Rocko sighs before turning to me."

    show don rocko neutral with dissolve

    dr "It seems there has been a slight change of plans."

    "Don Rocko’s slackey kindly offers to help him off his chair."

    dr "Ah, yes, yes! Thank you, thank you."

    "Don Rocko orders another slackey to help me off my chair. I happily take their hand."

    dr "I confess, this is not how I wanted to spend my morning—"

    "They bring me to Don Rocko's side."

    dr "—but it seems I am needed at the Emporium. You know of the Emporium, I’m sure."

    s "Who doesn't?"

    show don rocko happy with dissolve

    dr "Thank you! It is most assuredly a household name by now. It’s quite a central business on the island, you see..."

    show don rocko neutral with dissolve

    "Don Rocko, to my surprise, cuts himself off."

    dr "Needless to say, if you are to be my slablover, then you must be privy to my affairs, no?"

    "Don Rocko extends his hand."

    dr "Do you trust me?"

    "I..."

    "We're - we're moving so fast!"

    show don rocko blush with dissolve

    dr "It's time, my lover, to show you the ropes."

    "I take the hand I'm offered."

    s "I am."

    scene bg forest with fade
    show don rocko neutral with dissolve
    window show dissolve

    "The Emporium is just as grand as it is said to be."

    "Gold columns give the place an air of luxury. I look up and see that the capitals were crafted to look like slabs, giving the Don Rocko statue that sat on top a little slabpedestal."

    "The back wall of the Emporium itself is filled with miscellaneous decorations. I squint and see some wanted posters depicting faces I don’t recognise and two employee awards."

    "How kind of Don Rocko to show his workers some recognition!{p}{alpha=0.3}(This is a lie. Please tell him to pay us.){/alpha}"

    "My eyes, naturally, are drawn to the large framed portrait of Don Rocko himself."

    "Surrounded in swaths of purples and piles of potions, he really does look like royalty, the Slabdonis of our times."

    "As soon as we walk into the shop, Don Rocko gets straight to work. He may have his... issues, but no slab can ever say that Don Rocko doesn’t get the job done!"

    "He takes a bundle of contracts from a chest by the storefront and places them next to him."

    "With a slight huff, Don Rocko takes a seat on his plush purple pillow and starts to whittle away at the line of customers in front of him."

    "I sit just out of the customers’ view, but close enough to Don Rocko to see his process."

    "He slaps a contract in front of a buyer and points to his right, where they walk over to the emporium’s bulletin."

    "I follow one of the customers and watch as they fill out the form with shaking hands, barely managing to pin it onto the board without pricking their fingers in the process."

    "A slackey takes the owed potions from them before handing over the item they purchased."

    "Like a slab out of hell, customers run as far away as they can from the store once the exchange is done, clutching their new item as if their life depended on it."

    "Seeing the slackey struggle to hold an ever-growing mountain of potions, I step in and offer a helping hand."

    "Their expression on their face can only be described as one of pure relief."

    "They hand over one potion, and then five, and then ten..."

    "Don Rocko doesn’t miss a beat while I become the slab struggling to keep the potions in check. He’s really a true salesman!"

    "He casts a passing glance in my direction before focusing back on his work."

    dr "I trust you’ll be careful with them."

    "The most reassurance I can offer him is a weary thumbs-up."

    s "May I ask why you need all {i}this{/i} for?"

    "Don Rocko pauses before clenching his fist, crumpling up the contract in his hands."

    show don rocko angry with dissolve

    dr "My nemesis... They must be captured, and I must fundraise a worthy bounty for such a cause."

    "He smoothens the contract once he realizes what he’s done. He pretends not to notice the worried expression on the customer’s face."

    "..."

    s "But what did they do?"

    show don rocko happy with dissolve

    "Don Rocko doesn't really seem like the type to divulge much of his past to anyslab."

    "But judging from the look in his eye, he makes a split-second judgment call that if there is any slab in this world he could be a tiny bit vulnerable with, it’s me."

    show don rocko sad with dissolve

    "He launches into an extremely epic tale, the sort filled with betrayal, sorrow and treachery."

    show don rocko blush with dissolve

    "He resists the urge to fully act out some of the scenes, as he obviously needs to be professional in front of his customers."

    "But this doesn’t stop him from doing some wild gestures to emphasize the highest highs and lowest lows of his story."

    show don rocko neutral with dissolve

    "By the time he’s finished telling his tale, my jaw is on the floor."

    "The customers don’t seem to understand what’s happening as they just see Don Rocko occasionally entertain an unseen audience with some weird… posing."

    "Thankfully, they also know better than to say anything."

    show don rocko happy with dissolve

    "I give him a little clap and he bows, beaming and elated."

    "Is there anything that Don Rocko hasn’t been through?! Is there anything that he can’t do?!"

    scene bg forest with fade
    window show dissolve
    show don rocko neutral with dissolve

    "We continue talking about anything and everything..."

    "Well, he continues talking and I continue listening."

    dr "Ah, you haven’t been around the mansion? Not to worry, I will take you on a tour myself. There is much to see! Very big place, yes, immense..."

    dr "I... indulge in a few games here and there. Who doesn’t? They’re very fun."

    dr "Gardens? Beautiful they may be, they require too much time and effort to tend. You might like the courtyard though. Very grand, very beautiful! Tomato is very fond of it, yes."

    dr "The pink guy on the wall? I can’t say I remember his name all too well. Savvy? Laffy? Something to that effect."

    dr "You know, I’m something of a musician myself..."

    show don rocko shock with dissolve

    dr "The little slab in the—"

    "He turns around and looks over at the gold-painted slab holding a little brush in their hand. They hide behind their easel and peek their head out slightly."

    show don rocko neutral with dissolve

    "Don Rocko squints but ultimately lets them off with a shrug."

    dr "Huh. Well, as long as they’re making potions..."

    "Eventually, Don Rocko tends to the last customer in line and closes up shop for the day."

    "The sun is just about to set. Time’s really just flown."

    "Having fun at {i}work{/i} of all places? That’s something new!"

    "Don Rocko stores the spare contracts in their usual place before focusing his attention on me."

    dr "Oh, my."

    "I look down and realize that my arms are overflowing with potions, shining bright like purple diamonds under the last rays of a setting sun."

    "I stagger back, now feeling the weight of them in full. Don Rocko rushes to my side and just manages to catch the potions that were about to fall."

    show don rocko blush with dissolve

    dr " Let me help you with that..."

    "The slackeys who were coming to help me stop dead in their tracks. Even I am taken aback as Don Rocko relieves me of potions until there’s more of a manageable amount."

    "I can’t help but blush at the gesture."

    s "Thank—thank you...!"

    "The slackeys stand around us, completely slack-jawed at the sight they’re seeing."

    "Could it really be..."

    show don rocko neutral with dissolve

    dr "Come. It's time to go home."

    scene bg forest with fade
    window show dissolve
    show don rocko neutral with dissolve

    "We walk back to his castle together, carrying potions in our hands. The slackeys keep their distance but I still feel their eyes boring on us just in case Don Rocko gets tired."

    "Don Rocko too keeps his distance at first, but I see him slowly nudging himself towards me."

    "He seems on the verge of saying something, but for a change, it takes him a moment to form the right words."

    show don rocko blush with dissolve

    dr "I—"

    "He stands closer to me. I can almost feel his shoulder graze mine."

    dr "I much appreciated your company today... Thank you..."

    "I see him turn away from me slightly, trying to hide the blush on his face."

    s "Thank you for inviting me...!"

    "The warmth coming from our cheeks helps stave the evening chill that’s beginning to set in."

    "If a slabseer were to say that I’d one day admit to having {i}enjoyed{/i} time spent with Don Rocko, I’d say they were joking!"

    "Don Rocko clears his throat, drawing my focus back on him."

    show don rocko neutral with dissolve

    dr "Did you want anything in particular for dinner, [slabname]?"

    dr "I have very good slabchefs, the best on this island! Anything you desire, they can certainly deliver."

    "What {i}I{/i} want? I hold back a gasp."

    "I can hardly believe my ears. Is it the case that Don Rocko cares about what {i}I{/i} want?"

    "Is it true that he {i}can{/i} think about a slab other than himself?"

    "Perhaps he’s really not so bad after all."

    s "Hm... maybe spaghetti? I haven’t had that in a while!"

    show don rocko happy with dissolve

    "Maybe it’s just a trick of the light, but I swear I see a sparkle in Don Rocko’s eyes."

    dr "How serendipitous! Spaghetti happens to be my dish of choice too."

    show don rocko neutral with dissolve

    "Don Rocko commands his slackeys to move on ahead so they can prepare dinner for us. They happily dash forward."

    "We continue speaking about our favorite types of pastas and sauces until we make it back to the mansion."

    "From this whole whirlwind of a day, just having this quiet moment with Don Rocko where we can speak about frivolous things has been so… refreshing."

    scene bg mansion with fade
    window show dissolve
    show don rocko neutral with dissolve

    "Don Rocko’s slackeys really worked overtime."

    "When we got to the mansion, the hall was already prepared with a lavish candlelight dinner."

    s "Woah...!"

    "Don Rocko takes my hand and walks us forward."

    "My eyes waver between the twinkling candles, the plush velvet tablecloth and the bouquet of cut flowers inside an ornate vase."

    s "This is beautiful!"

    "The hearty, warm smell of freshly baked bread wafts through the air, mingling with the eggy aroma of freshly cooked pasta."

    dr "It seems we’ve arrived at the perfect time."

    "Don Rocko leads me to my side of the table, pulling out the chair for me."

    "Such... such a gentleslab!"

    "I thank him, graciously taking a seat. Don Rocko sits on the opposite side."

    show don rocko happy with dissolve

    "Just as we get settled, a slabchef carries a big bowl of spaghetti to our table and places it in front of us."

    "The tangy aroma of the vivid red slabpolitan sauce covering a bed of spaghetti like a blanket makes my mouth water."

    dr "Ah, let’s dig in, shall we?"

    "Don Rocko goes to take the first scoop, but stops himself. Instead, he gestures for me to have the first taste."

    "I happily do so, shovelling some spaghetti into my mouth. I perk up as I chew."

    s "This tastes amazing!"

    "Don Rocko begins eating too, happily nodding along."

    dr "Of course! My chefs have {i}perfected{/i} this dish."

    show don rocko neutral with dissolve

    "We talk as we eat, continuing our conversation about pasta types—"

    dr "The chefs will certainly make slabaroni and cheese if that is what you desire."

    dr "Slabatoni or Slabioli?"

    "—before gravitating to different topics. Well, Don Rocko talks about whatever crosses his mind, but I do comment sometimes."

    dr "Hm… Do you think we should get more flowers in the hall?"

    s "That'd make it a bit more lively."

    "Don Rocko nods his head slowly as he chews, considering changes to his mansion."

    "He punctuates his sentences by raining cheese on top of the spaghetti on his fork before taking a bite."

    dr "Maybe new curtains, yes. Or perhaps a new room to the mansion."

    "Now that it’s just us two, he’s much more relaxed."

    dr "Are you satisfied with your room?"

    "I don’t know for certain, but he feels more like… himself, more at ease, more down to earth rather than trying to be lofty just to flaunt his money or his power."

    dr "I wonder if I plugged in my Slablet so it can charge..."

    s "Do you have the newest one?"

    "Don Rocko smirks."

    dr "Three of them. Have you tried them out yet?"

    "As I tell him about my slaptop back at home, we both lean in to grab some spaghetti."

    show don rocko shock with dissolve

    "We start chewing and quickly realize that we both got the same strand of pasta."

    "We lock eyes. I half wait for Don Rocko to cut the strand, but he doesn’t. It seems that he’s waiting for me to do the same."

    "But I keep chewing and so does he. The shortening strand forces us to lean in, and we inch closer and closer..."

    show don rocko neutral with dissolve

    "I feel my heart pounding."

    "Is... Is this it? Is this the moment?"

    "I don’t know for sure, but I let the moment sweep me off my feet..."

    "..."

    "..."

    "...!"

    show don rocko blush with dissolve

    "Our lips touch very gently, but it’s enough to make my head spin."

    "Is this real? Am I kissing Don Rocko?"

    "And it's... enjoyable?!"

    show don rocko shock with dissolve

    "It's Don Rocko who pulls away first, surprise evident on his face along with an unmistakable flush."

    "Now he’s really {i}speechless{/i}."

    dr "I—Did we—"

    "{i}We{/i}? Are we… a couple now…?"

    s "Yeah..."

    dr "And you didn’t... turn away?"

    "I shake my head."

    s "Why... Why would I? It was nice!"

    "He hops down from his chair and paces under the table for a bit. I do the same with the hopes of calming him down."

    "Lost in thought, Don Rocko strokes his chin, muttering something incomprehensible under his breath."

    "Did I do something wrong? Am I just not that good of a kisser?"

    show don rocko neutral with dissolve

    "When he sees that I’m worrying about him, he stops and takes my hand."

    dr "Ah, I apologize, [slabname]. It was very uncouth of me to leave you alone at the table."

    dr "I was just… in shock."

    s "Why shocked?"

    dr "I suppose I’m not used to… this sort of thing."

    "He strokes the back of my hand."

    show don rocko happy with dissolve

    dr "But I am truly happy… Thank you, [slabname]."

    "He retracts his hand for a moment and turns his back to me. I watch as he lifts his hat and takes something lying underneath it."

    "When he turns back around, I see exactly what he has in his hand."

    "And I almost faint at the sight."

    scene bg mansion with fade
    window show dissolve
    show don rocko blush with dissolve

    dr "[slabname], you make me the happiest slab in the world."

    "A little purple box."

    dr "Like I’m the only slab in the world."

    "He places a hand on its cover—"

    dr "And I want to be by your side—"

    "—and lifts it—"

    dr "—if you’ll have me."

    "—revealing a golden ring, topped by a sparkling diamond. It’s not too extravagant, not too demure; it’s just right."

    dr "I hope... this is to your liking..."

    "Don Rocko waits expectantly, blushing, nervous. His lips settle into an unconscious smile, a smile that’s truly {i}sincere{/i}, perhaps the first one I’ve seen him give."

    "I never could resist a slab with a smile like that."

    "Before I could even think it through properly, considering all the pros and cons, if we’re moving too fast (we did just meet a few days ago, I know, I know), my mouth speaks for me."

    s "YES!"

    show don rocko happy with dissolve

    "I take the ring and slide it on my finger, before I jump into Don Rocko’s arms. He plants a tender kiss on my forehead."

    dr "Brilliant. Let's get married."

    s "Right now? But isn’t it getting late?"

    dr "Nonsense! There is no time to delay!"

    "Don Rocko does, however, look out the window and sees that it is well and truly night-time."

    show don rocko neutral with dissolve

    dr "Hmm… If my slab-to-be says we should wait, then we shall."

    s "More time to plan the wedding!"

    "Don Rocko lifts me up in the air and swings me around. His joy is so infectious!"

    show don rocko happy with dissolve

    dr "Ah, it shall be the most extravagant on the island!"

    scene bg mansion with fade
    window show dissolve

    "Within the next few days, we plan the wedding and have the slackeys work overtime."

    "Thinking that white’s too boring and cliche, the main hall is transformed into a wedding venue with purple and gold decor."

    "Everything that can be gilded is; anything that can hold a bouquet of lavenders and chrysanthemums does."

    "The aisle runner is colored a deep purple with golden flower petals scattered over it."

    "Swathes of white fabric are draped across golden columns that were brought in temporarily from the store, forming nice little arcs that contrast the sharpness of the gold and the purple."

    "It’s picture-perfect."

    "As I wait outside for the ceremony to start, I take a peek inside."

    "Don Rocko stands at the end of the aisle with his bodyguard, waiting underneath a golden arch wrapped in vines of beautiful flowers."

    "Everyone is already seated, including Leif! They still seem to be in chains though."

    "I take a deep breath and the slackey next to me very kindly asks if I’m ready."

    s "Yeah, I think I am."

    "They push the door open for me and I walk through..."

    "{i}*GASP*{/i}"

    "{i}*AWE*{/i}"

    "{i}*AMAZING*{/i}"

    "Oohs and ahhs come from the sea of guests around me, and for good reason!"

    "I’m dressed in the finest clothes that Don Rocko’s money could buy: pearls, diamonds, silks, velvet…"

    "In this moment, I’m the star of the show, and I am LOVING it."

    "I give a polite nod to Slabraham and some tiny slabs I don’t recognise. Still, how lovely of them to show up!"

    "I wave shyly at Leif, who mouths some well-wishes."

    show don rocko neutral with dissolve

    "As I approach the altar, I see Don Rocko looking at me intently. He’s grinning, his eyes filled with stars, filled with love."

    "He looks quite dapper too, in a new suit and tie that matches my clothes."

    "He takes my hand and walks me the rest of the way."

    show don rocko blush with dissolve

    "The rest of the ceremony goes off without a hitch. We say our moving vows and exchange wedding bands, topping it all off with our 'I Do’s'."

    "With our guests sending us off to enjoy our new married life with a wild cheer, we run out of the entrance hall, practically leaping out of the doors."

    "And that’s how I ended up getting married to Don Rocko!"

    "I’m married! I’m really married! Are you proud of me now, Ma?"

    "Though I was expecting to ride a slabcar with Don Rocko to our secret honeymoon destination, I’m surprised to see that there are two slabcars idling in the driveway."

    "The slabs jump to attention when they see us."

    show don rocko happy with dissolve

    dr "Well, enjoy your honeymoon!"

    hide don rocko happy with dissolve

    "Without further explanation, Don Rocko gives me a tender peck on the lips before a slabcar whisks him away to a place unknown."

    "My slabcar walks up to me. A soft spoken slab breaks from the group and asks me where I’d like to go for my own personalized vacation."

    "…This is the best honeymoon EVER!"

    scene cias2 with fade
    window show dissolve
    show don rocko blush at center with dissolve

    "{i}[username], thank you for completing Act Two - {b}Don Rocko{/b}! Please take a screenshot of this page and follow the directions on the event journal to have {b}one leaf OR rock (your choice){/b} added to your inventory.{/i}"

    scene bg forest with fade
    window show dissolve

    "On my vacation, I decided to go to Paradise Oasis! I’ve never been to a beach before, and truly there is nothing more relaxing than the sound of waves."

    "As I catch up with some fanfic reading on Don Rocko's slablet, I find myself lost in thought, getting more and more distracted to the point where I’m unable to read the words in front of me."

    "I’m here, I’m married, but…"

    "Did I get married too soon?"

    "Did I make a mistake?"

    "Did I rush into things?"

    "A flurry of questions strikes my heart all at once. So much for a vacation if I’m just spending it doing some soul-searching! Argh!"

    "I get up from my beach chair and walk up to the ocean, standing in the surf. Water washes over my feet as they sink deeper into the sand."

    "My eyes are fixed on the horizon. There it remains, unreachable, the picture of endless freedom."

    "I’m married, and I let that sink in. I’m married, and I’m married to Don Rocko."

    "Don Rocko."

    "How did I go from disliking him to marrying him in a span of a week?"

label donrockodecision:

    "Do I... really love him?"

menu:

    "You love Don Rocko":

        "No, I married him for a reason, right? Of course I love him! Sure, he has his flaws, but who doesn’t?"

        "Now that I’ve successfully sorted out the anguish in my soul, I get back to enjoying the rest of my vacation before I head back to the mansion."

        "I can’t wait to live out the rest of my married life!"

        jump donrockoending

    "You don't love Don Rocko":

        "The spectacle of it all..."

        "I think I was just blinded by it all. I've never experienced such luxury in my life..."

        "Don Rocko improved in bounds, sure, but..."

        "I don't want to spend the rest of my life with him, I know that for sure. It's just too soon, way too soon..."

        "But how do I go back to that big mansion and tell him I don't want to be married anymore?"

        "The divorce will be so, so messy..."

        "..."

        "..."

        "..."

        "Wait."

        "I’m all alone. None of his slackeys are here, and aren’t scheduled to pick me up for another few days."

        "I don’t need to go back!"

        "I just need to go somewhere where no slab will find me!"

        jump slablife

label donrockoending:

    scene bg mansion with fade
    window show dissolve

    "Everything goes back to normal when I return to the mansion. Don Rocko tells me about his exciting vacation up at the Lonely Pebbling and I tell him about the fics I read."

    "You could say we live in something of domestic bliss, strange as it sounds."

    "We go to work, we eat, we fall into a routine that, for a little while, is really nice. It’s like I’m back at home, doing the same thing, and being content doing so."

    "But after a while, well, you know how it goes in a marriage…"

    "The little things you do together as you wither away… it’s not so exciting. It never {i}was{/i}, but it was different for a little while, you know?"

    "The more time you spend with another slab, the more time you have to just scrutinize them, {i}really{/i} see them."

    "You decide what parts you choose to look away from and just accept that it won’t change."

    "And then there’s the parts that you can’t unsee, and then it becomes a bother, the chip on your shoulder."

    "For me, that’s Don Rocko’s FRICKING HAT."

    "I’ve asked him multiple times to remove his hat at the very least indoors. It is rather strange that he would prefer to wear it when there’s a giant roof over his head."

    show don rocko neutral with dissolve

    dr "No, I like my hat."

    hide don rocko neutral with dissolve

    "That is always the reason he gives, and I never push it further than that. But I can’t help but wonder why he won’t remove it."

    "Is he afraid of doing so? Is he hiding something? He certainly keeps things under there, that’s for sure."

    scene bg forest with fade
    window show dissolve

    "We’re walking in the courtyard as Don Rocko speaks business with his bodyguard, and this one little habit of his keeps gnawing at my patience."

    "I can’t stop looking, wondering. Am I a bad slab for wanting to know? Is he just not comfortable with me even though we’re married?"

    "I stop in my tracks, my fists balled, my eyes fixed on the ground. Don Rocko turns around to check up on me."

    show don rocko sad with dissolve

    dr "Is something wrong, my slablove?"

    s "Do you not... trust me?"

    show don rocko shock with dissolve

    "Don Rocko is taken aback by my question."

    dr "Well..."

    "I look up. Anger simmers in my eyes."

    s "So that's why."

    dr "What is that supposed to mean?"

    s "That’s why you won’t take off your hat."

    show don rocko angry with dissolve

    "Don Rocko scoffs and rolls his eyes."

    dr "This again."

    s "This again?! Why won’t you just take it off? Do you know how weird it is that you never remove it? At all?"

    dr "But I—"

    s "Yes, you like your hat, I know!"

    "Don Rocko scowls. He doesn’t seem to take kindly to being cut off mid-sentence."

    dr "It’s my house. I can do what I want."

    "..."

    "..."

    "..."

    s "... Your house?"

    "I close my eyes and sigh."

    s "This was a mistake."

    show don rocko sad with dissolve

    s "We're getting a divorce."

    "Before Don Rocko can stop me or change my mind, I stomp away, leaving the rest of my anger behind me."

    scene bg mansion with fade
    show don rocko angry with dissolve
    window show dissolve

    "I find the best slablawyer on the island and take what I’m owed."

    "The divorce goes very smoothly, filed one day and finalized the next. I see Don Rocko shaking with anger during proceedings, and all I can do is grin."

    "At one point, he even goes to rush for me and my legal slabcounsel, but is held back by his bodyguard."

    hide don rocko angry
    show bald don rocko shock
    with dissolve

    "The inertia from his restraint causes his hat to come flying forward, tumbling towards and stopping in front of me."

    "When I pick up his fedora to turn it right-side up, a small little box falls out of the hat."

    "It flares a bright green light before dimming completely."

    "..."

    "..."

    "..."

    "{i}*GASP*{/i}"

    show bald don rocko sad with dissolve

    "I look up and see that everyone is looking at Don Rocko’s shiny, shiny bald head."

    "He goes to talk, but when he does, it’s not that same smooth, suave voice."

    "It’s squeaky. Super squeaky."

    hide bald don rocko sad
    show don rocko sad
    with dissolve

    "I try my hardest to suppress a giggle, as do all the other slabs in the room. Don Rocko makes a mad scramble for his hat."

    "This explains so, {i}so{/i} much."

    "The rest of the proceedings are not so comical. It seems he’s forgotten that because he didn’t listen to me when I spoke about prenups, I went ahead and organized them myself."

    "Granted, I feel that I was very fair with the terms, just a standard 50 percent of his money even though it was all ‘earned’ by him…"

    "But hey, he signed the prenup!"

    scene bg mansion with fade
    show don rocko angry with dissolve

    "I stride into his vault and, with the help of his slackeys, carry bags and bags and bags filled with gold."

    "They follow me out into the front of the mansion, where I’m met by a slablimousine to help me carry my new riches back home."

    "Don Rocko doesn’t speak to me nor comes near me. Even though he doesn’t think I can see him, I notice him peering at me from out a window high in the mansion."

    "He sneers at me when we lock eyes and I stick my tongue out at him before the slablimousine takes me home."

    scene bg forest with fade
    window show dissolve

    "Thank goodness for all of Don Rocko’s money! With it, I move out of my little, little tree hollow and into a much bigger pod!"

    "It’s not a mansion, sure, but it’s very comfortable, and I have plenty of gold left to keep me comfortable for the rest of my life."

    "I jump back into my giant bed, a sea of blankets and long pillows surround me. I drag my top of the line slabtop and get to writing my fanfics."

    "For a while, I didn’t know how I wanted to end the Slabsune Miku and Sailor Slab fic to end, but I think I’ve got an idea in my head now."

    "Whether or not it’s the ending that my readers want, I don’t know."

    "But I just wanted to change things up a bit!"

    "At the end of the day, I’m happy, I’m thriving, as single as a slab like me can be."

    "And things could not have turned out any better!"

    scene cias2 with fade
    window show dissolve
    show don rocko sad at center with dissolve

    "{size=18}{i}[username], thank you for completing {b}Don Rocko ... Ending - He Had It Coming!{/b} Please take a screenshot of this page and follow the directions on the event journal to receive {b}a synthetic potion{/b}!{/i}{/size}"

    jump goodending

label goodending:

    scene bg starry night with fade
    window show dissolve

    "{i}\"Slabsune Miku, I...\"{/i} Sailor Slab turns to Slabsune Miku."

    "The moon and the stars fill the night sky with light, but Sailor Slab… she’s only ever had eyes for one star."

    "Her slabstar."

    "Slabsune Miku sees Sailor Slab looking at her intently, and she blushes. Could it be...?"

    "{i}\"Y-Yes?\"{/i}"

    "Sailor Slab places her Stellar Stick down beside her and cups Slabsune Miku’s face. It’s now or never."

    "{i}\"Slabsune Miku, I—\"{/i}"

    "But the words Slabsune Miku wants to hear don't leave Sailor Slab’s lips."

    "Instead, Sailor Slab withdraws her hands."

    "{i}\"I'm sorry.\"{/i}"

    "Confusion almost overwhelms Slabsune Miku."

    "{i}\"What... Why? Don't you—\"{/i}"

    "{i}\"No, I can’t…\"{/i} Sailor Slab turns her face away, looking up at the moon, but not before Slabsune Miku sees a single tear roll down her cheek."

    "It glistens in the moonlight."

    "{i}\"We live in two different worlds, Slabsune Miku.\"{/i}"

    "Slabsune Miku tries to reach out, to wipe the tear off her face, to see her smile and reassure her that this is just a joke."

    "But every word that Sailor Slab says breaks Slabsune Miku’s heart, piece by piece."

    "{i}\"It can’t work, it won’t ever work…\"{/i}"

    "Sailor Slab picks up her wand. She stands still, her hand gripping it so tightly that the handle threatens to crumble."

    "With one last glance back at her love, Sailor Slab locks eyes with Slabsune Miku."

    "{i}\"I'm sorry...\"{/i}"

    "Sailor Slab climbs onto the balcony’s railings and hops to an adjacent building."

    "Slabsune Miku clutches her chest, eyes welling with tears as she watches the only slab she ever loved loses herself to the cold, cold night..."

    window hide dissolve
    scene cggoodend with fade
    pause 3.0
    window show dissolve

    "{b}FIN.{/b}"

    label goodendmenu:

    "Thank you for playing {i}Caught in a (Slab)Romance!{/i}"

    $ MainMenu(confirm=True)()
    jump goodendmenu

label slablife:

    scene bg forest with fade
    window show dissolve

    "That was a wild couple of days, huh?"

    "It’s easy to see things more clearly once the dust settles. There’s no loud noises, no loud voices; just birdsong and a slabpop song at a low volume."

    scene bg mansion with fade

    "I miss the mansion sometimes, the luxury and the mystery of it all. The halls, the courtyard, the prison..."

    scene bg bedroom2 with fade

    "That bedroom in particular was something out of a storybook!"

    scene bg mansion with fade

    "There’s something about the place that draws you in and is determined to keep you in if you’re not careful."

    "And the slabs I met along the way..."

    show don rocko neutral at left with dissolve

    "Don Rocko..."

    show leif neutral at center with dissolve

    "Leif..."

    show slaborro neutral at right with dissolve

    "Slaborro..."

    "Their little quirks and idiosyncrasies made them so compelling and fascinating that I definitely couldn’t blame anyslab who would stay by their side until the end of time."

    "Indeed, the time I spent with them are times that I can’t and won’t ever forget for as long as I live."

    "But that lifestyle isn’t for me. I’m my own slab, I want to live my own life, no matter how boring it may seem."

    "As long as I’ve got a roof over my head, some blankets by my side, and a slabtop on my lap, I’m thriving as any high roller would be."

    "Heh, that’s enough of my monologue. I’ve got a slabfic to finish!"

    jump trueending

label trueending:

    scene bg starry night with fade
    window show dissolve

    "{i}\"Slabsune Miku, I...\"{/i} Sailor Slab turns to Slabsune Miku."

    "The moon and the stars fill the night sky with light, but Sailor Slab… she’s only ever had eyes for one star."

    "Her slabstar."

    "Slabsune Miku sees Sailor Slab looking at her intently, and she blushes. Could it be...?"

    "{i}\"Y-Yes?\"{/i}"

    "Sailor Slab places her Stellar Stick down beside her and cups Slabsune Miku’s face. It’s now or never."

    "{i}\"Slabsune Miku, I—\"{/i}"

    "Unable to say the words that so desperately wants to leave her lips, Sailor Slab turns her head away, cheeks flushed with embarrassment and unspoken affection."

    "{i}\"No, I can't...\"{/i}"

    "Sailor Slab withdraws her hands."

    "{i}\"We live in two different worlds…\"{/i}"

    "She looks up at the moon, hoping that it could give her the strength to be honest with her feelings just as it gives her the power to fight crime."

    "But Sailor Slab knows that there is nothing more the moon can give her; this is a battle she must win on her own terms."

    "Slabsune Miku feels her heart sink when Sailor Slab walks away to lean on the balcony’s railings… even more so when she lets her do so."

    "She could have grabbed her hand to stop her, encourage her to keep going…"

    "But the tides ebbed before she could pull her back, an ocean of glitter separating her from the slab who holds her heart."

    "Sailor Slab looks down at the city below. From up so high, lit windows from distant skyscrapers look like little pinpricks of light."

    "For Slabsune Miku, it’s rare to see Sailor Slab like this; with her wand down, her silhouette framed by moonlight."

    "She can’t remember the last time she’s seen Sailor Slab just taking in the sights of a city she spends so much time protecting."

    "And she could only see Sailor Slab when she too was away from her stage, closer to the earth, closer to a world where she could simply be… her, with the slab that she—"

    "..."

    "Slabsune Miku takes a deep breath; just as tides ebb, so too it must flow."

    "She runs to Sailor Slab, her heart leading the way."

    "Sailor Slab hears footsteps coming from behind her and turns, seeing Slabsune Miku with her arms outstretched.  Needing no explanation, she catches Slabsune Miku in her own."

    "{i}\"Slabsune Miku…? But I'm just—\"{/i}"

    "Slabsune Miku presses a finger to Sailor Slab’s lips, her eyes bright like stars, a smile filled with love."

    "{i}\"Just kiss me already!!!\"{/i}"

    window hide dissolve
    scene cgtrueend with fade
    pause 3.0
    window show dissolve

    "{b}FIN.{/b}"

    "{size=18}{i}[username], thank you for completing {b}True Ending - It's a Slab's Life For Me!{/b} Please take a screenshot of this page and follow the directions on the event journal to receive {b}a synthetic potion{/b}!{/i}{/size}"

    label trueendmenu:

    "Thank you for playing {i}Caught in a (Slab)Romance!{/i}"

    $ MainMenu(confirm=True)()
    jump trueendmenu
