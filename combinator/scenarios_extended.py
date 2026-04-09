"""Extended scenario settings — loaded by scenario_generator.py"""

EXTENDED_SETTINGS = [
    # ==================================================================
    # WORKPLACE (12)
    # ==================================================================

    # ------------------------------------------------------------------
    # 1. hospital_night — Night shift nurse, empty ward
    # ------------------------------------------------------------------
    {
        "key": "hospital_night",
        "titles": ["Night Shift", "Code Blue", "Visiting Hours Over", "Bedside Manner"],
        "description": "Empty hospital ward at 3am. The monitors beep softly.",
        "time": "night",
        "location": "hospital ward",
        "furniture": ["hospital bed", "rolling medical cart", "privacy curtain", "visitor chair", "supply cabinet"],
        "lighting": ["cold fluorescent hallway spill", "blue monitor glow", "dim bedside lamp", "green heart monitor light"],
        "atmosphere": ["sterile", "quiet", "clinical"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "leaning against hospital hallway wall, scrubs slightly wrinkled, stethoscope around neck, hair in messy bun, fluorescent light casting long shadows down empty corridor, clipboard in one hand",
                "positive_extra": "hospital hallway, scrubs, stethoscope, messy bun, fluorescent light, shadows, clipboard",
                "shot": "medium",
                "caption": "3:14 AM. The ward had been empty for hours.",
            },
            {
                "scene": "standing at nurses station, leaning over counter checking charts, pen between teeth, monitor screens glowing blue behind, dim overhead light, empty coffee cup beside her",
                "positive_extra": "nurses station, leaning over counter, pen in mouth, monitor glow, dim light, coffee cup",
                "shot": "medium_close",
            },
            {
                "scene": "turning around in hospital corridor, surprised expression, hand on chest, stethoscope swaying, privacy curtains lining both sides, green exit sign glowing at end of hall",
                "positive_extra": "hospital corridor, turning around, surprised, hand on chest, stethoscope, privacy curtains, exit sign",
                "shot": "full_body",
                "dialogue": "You scared me. Nobody's supposed to be on this floor.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on edge of hospital bed, legs dangling, pulling stethoscope off neck slowly, looking up with curious expression, privacy curtain half drawn behind, blue monitor light on face",
                "positive_extra": "hospital bed, legs dangling, removing stethoscope, curious look, privacy curtain, blue light",
                "shot": "medium",
                "dialogue": "Visiting hours ended at nine.",
            },
            {
                "scene": "standing in supply closet doorway, one hand on door frame, head tilted, shelves of medical supplies behind, fluorescent light flickering above, slight smirk",
                "positive_extra": "supply closet doorway, hand on frame, head tilted, medical supplies, flickering light, smirk",
                "shot": "medium_close",
            },
            {
                "scene": "pulling privacy curtain closed around hospital bed, fingers gripping fabric edge, looking back over shoulder, dim blue light filtering through thin curtain material",
                "positive_extra": "pulling curtain, gripping fabric, looking back, dim blue light, hospital bed, curtain material",
                "shot": "close_up",
                "caption": "She pulled the curtain like she'd done it before.",
            },
            {
                "scene": "pressed against cold hospital wall, head back, eyes closed, scrubs askew, privacy curtain billowing slightly, heart monitor casting green glow across her neck",
                "positive_extra": "against wall, head back, eyes closed, scrubs askew, curtain billowing, green glow, neck",
                "shot": "close_up",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting in visitor chair beside hospital bed, fixing hair back into bun, scrubs straightened, stethoscope back on, fluorescent hall light visible through cracked door",
                "positive_extra": "visitor chair, fixing hair, scrubs neat, stethoscope on, hallway light, cracked door",
                "shot": "medium",
            },
            {
                "scene": "close-up of hospital pager on bedside table buzzing, screen lit up with new alert, stethoscope coiled beside it, wrinkled pillow in background",
                "positive_extra": "pager buzzing, screen lit, stethoscope, wrinkled pillow, bedside table",
                "shot": "close_up",
                "caption": "The pager buzzed. She was already gone.",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 2. therapy_session — Therapist's office, leather couch
    # ------------------------------------------------------------------
    {
        "key": "therapy_session",
        "titles": ["The Session", "Fifty Minutes", "Transference", "On the Couch"],
        "description": "The session ran over. Neither of them noticed the clock.",
        "time": "afternoon",
        "location": "therapist office",
        "furniture": ["leather therapy couch", "wingback armchair", "side table with tissues", "bookshelf wall", "analog clock"],
        "lighting": ["warm afternoon through blinds", "soft desk lamp", "golden stripe shadows from venetian blinds"],
        "atmosphere": ["quiet", "warm", "private"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "lying on leather therapy couch, one arm behind head, staring at ceiling, legs crossed at ankle, afternoon light striping through venetian blinds across body, bookshelves lining walls",
                "positive_extra": "therapy couch, arm behind head, ceiling stare, venetian blind stripes, afternoon light, bookshelves",
                "shot": "full_body",
                "caption": "Session twelve. She'd stopped filtering.",
            },
            {
                "scene": "sitting up on leather couch, hugging knees to chest, looking sideways at wingback chair, vulnerable expression, tissue box on side table, warm lamp light",
                "positive_extra": "sitting up, hugging knees, looking sideways, vulnerable, tissue box, warm lamp light, leather couch",
                "shot": "medium",
                "dialogue": "You always ask what I want. Nobody else does that.",
            },
            {
                "scene": "standing at office window, pulling venetian blind slat down with one finger, peering out, afternoon sun on face, silhouette from behind, analog clock on wall showing past the hour",
                "positive_extra": "window, blind slat, peering out, afternoon sun, silhouette, clock, past the hour",
                "shot": "medium_close",
            },
        ],

        "tension": [
            {
                "scene": "sitting on edge of leather couch, leaning forward toward camera, elbows on knees, chin on clasped hands, intense eye contact, venetian blind shadows across face",
                "positive_extra": "couch edge, leaning forward, elbows on knees, chin on hands, intense eyes, blind shadows",
                "shot": "medium_close",
                "dialogue": "Tell me. Professionally. What's happening right now?",
            },
            {
                "scene": "standing beside wingback armchair, fingers trailing along leather armrest, looking down at seated perspective, slight knowing smile, warm light from desk lamp",
                "positive_extra": "beside armchair, fingers on armrest, looking down, knowing smile, desk lamp, warm light",
                "shot": "medium",
            },
            {
                "scene": "leaning against bookshelf, one arm overhead gripping shelf edge, books askew behind, head tilted, lips parted, golden afternoon light on collarbone",
                "positive_extra": "against bookshelf, arm overhead, books askew, head tilted, parted lips, golden light, collarbone",
                "shot": "close_up",
                "caption": "The clock ticked past the hour. Neither moved to stop it.",
            },
            {
                "scene": "close-up face resting sideways on leather couch cushion, eyes half-open looking at viewer, hair fanned across brown leather, venetian blind light on cheek, flushed",
                "positive_extra": "face on leather, half-open eyes, hair fanned, blind light stripe, flushed, looking at viewer",
                "shot": "close_up",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting in wingback armchair now, legs crossed, adjusting collar, composed expression, tissue box knocked off side table on floor, clock visible showing one hour past",
                "positive_extra": "wingback chair, legs crossed, adjusting collar, composed, tissue box on floor, clock past hour",
                "shot": "medium",
            },
            {
                "scene": "close-up of notepad on desk, pen lying across it, single line of handwriting visible, leather couch impression visible in background, afternoon light fading",
                "positive_extra": "notepad, pen, handwriting, couch impression, fading light, desk",
                "shot": "close_up",
                "caption": "She scheduled next week's appointment before leaving.",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 3. restaurant_kitchen — After closing, stainless steel
    # ------------------------------------------------------------------
    {
        "key": "restaurant_kitchen",
        "titles": ["After Service", "Back of House", "Heat Check", "Kitchen Closed"],
        "description": "The dining room emptied. The kitchen didn't.",
        "time": "night",
        "location": "restaurant kitchen",
        "furniture": ["stainless steel prep counter", "walk-in cooler door", "hanging pot rack", "commercial stove", "dish station"],
        "lighting": ["harsh overhead kitchen fluorescent", "blue pilot light glow", "warm heat lamp over pass", "stainless steel reflections"],
        "atmosphere": ["hot", "steam", "industrial"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "leaning against stainless steel prep counter, chef coat unbuttoned at top, wiping forehead with back of hand, steam rising from pots behind, fluorescent light above, tired but alert expression",
                "positive_extra": "steel counter, chef coat open, wiping forehead, steam, fluorescent, tired, kitchen",
                "shot": "medium",
                "caption": "Last ticket cleared at 11:47. Clean-down could wait.",
            },
            {
                "scene": "sitting on overturned milk crate in kitchen corner, legs stretched out, untying apron strings, hanging copper pots above, stainless steel everywhere reflecting light",
                "positive_extra": "milk crate, legs out, untying apron, copper pots, stainless steel, kitchen corner",
                "shot": "full_body",
            },
            {
                "scene": "turning from dish station, wet hands, soap suds on forearms, surprised look, kitchen towel over shoulder, blue pilot lights from stove behind, steam in air",
                "positive_extra": "wet hands, soap suds, forearms, surprised, towel on shoulder, pilot lights, steam",
                "shot": "medium_close",
                "dialogue": "I thought everyone left already.",
            },
        ],

        "tension": [
            {
                "scene": "hoisted up sitting on stainless steel prep counter, legs swinging, hands gripping counter edge, chef coat open revealing undershirt, hanging pots framing shot from above",
                "positive_extra": "on counter, legs swinging, gripping edge, chef coat open, undershirt, hanging pots above",
                "shot": "medium",
                "dialogue": "The walk-in's right there if we need to cool down.",
            },
            {
                "scene": "standing at commercial stove, one hand on burner knob, looking back over shoulder, blue gas flame reflecting in eyes, steam rising, heat shimmer visible",
                "positive_extra": "stove, hand on knob, looking back, blue flame, eyes reflecting, steam, heat shimmer",
                "shot": "medium_close",
            },
            {
                "scene": "pressed against walk-in cooler heavy metal door, cold condensation visible, goosebumps on arms, breath visible in cold air, warm kitchen light behind",
                "positive_extra": "cooler door, condensation, goosebumps, visible breath, cold, warm light behind",
                "shot": "close_up",
            },
            {
                "scene": "face close-up, flour dusted on cheek, parted lips, eyes looking up, warm overhead heat lamp casting orange glow, stainless steel blurred behind, flushed from heat",
                "positive_extra": "flour on cheek, parted lips, looking up, heat lamp orange, stainless steel blur, flushed",
                "shot": "close_up",
                "caption": "The kitchen had never felt this hot after close.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on kitchen floor against walk-in door, apron bunched in lap, one knee up, disheveled hair, eating something from a ramekin with fingers, satisfied grin",
                "positive_extra": "kitchen floor, against cooler door, knee up, disheveled, eating from ramekin, satisfied grin",
                "shot": "full_body",
            },
            {
                "scene": "close-up of handprint in flour dust on stainless steel counter, kitchen lights still on, clean dishes stacked in background, no people in frame",
                "positive_extra": "handprint, flour dust, steel counter, kitchen lights, clean dishes, empty",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 4. mechanic_shop — Garage, car on lift
    # ------------------------------------------------------------------
    {
        "key": "mechanic_shop",
        "titles": ["Under the Hood", "Grease Monkey", "Tune-Up", "Full Service"],
        "description": "Her car's on the lift. The garage door is down.",
        "time": "evening",
        "location": "auto mechanic garage",
        "furniture": ["car on hydraulic lift", "rolling tool chest", "mechanic creeper", "workbench with vise", "oil drum seat"],
        "lighting": ["harsh overhead shop fluorescent", "orange trouble light on cord", "sunset through garage windows", "welding spark glow"],
        "atmosphere": ["grimy", "industrial", "oil-stained"],
        "phase_structure": "all_phase2",

        "setup": [
            {
                "scene": "standing in garage doorway, silhouette against sunset, car visible on hydraulic lift behind, tool chest to the side, oil-stained concrete floor, hand shielding eyes from sun",
                "positive_extra": "garage doorway, silhouette, sunset, car on lift, tool chest, oil-stained floor",
                "shot": "full_body",
                "caption": "The estimate said two hours. That was four hours ago.",
            },
            {
                "scene": "sitting on oil drum in mechanic garage, legs crossed, scrolling phone, bored expression, car elevated on lift above and behind, fluorescent shop lights, tire marks on floor",
                "positive_extra": "oil drum seat, legs crossed, phone, bored, car on lift, fluorescent, tire marks",
                "shot": "medium",
                "dialogue": "Is it going to be much longer?",
            },
            {
                "scene": "leaning over open car hood from the side, peering at engine, orange trouble light dangling, grease smudge on forearm, curious expression, tools scattered on workbench behind",
                "positive_extra": "car hood, peering at engine, trouble light, grease smudge, forearm, curious, tools, workbench",
                "shot": "medium_close",
            },
        ],

        "tension": [
            {
                "scene": "sitting on mechanic creeper, rolling slightly, legs visible from under car, looking up at camera angle from low position, fluorescent light above, oil-stained floor",
                "positive_extra": "mechanic creeper, low angle, looking up, fluorescent above, oil-stained floor, under car",
                "shot": "medium",
            },
            {
                "scene": "leaning against tool chest, arms crossed under chest, one hip cocked, grease streak on collarbone, defiant smirk, car lift hydraulic arm in background",
                "positive_extra": "tool chest, arms crossed, hip cocked, grease streak, collarbone, smirk, hydraulic lift",
                "shot": "medium_close",
                "dialogue": "I don't usually let customers back here.",
            },
            {
                "scene": "hoisted up on workbench, sitting on edge, feet off ground, vise visible beside her, tool pegboard behind, orange work light swinging casting moving shadows",
                "positive_extra": "workbench edge, feet dangling, vise, pegboard, orange light swinging, shadows",
                "shot": "full_body",
            },
            {
                "scene": "close-up face, grease smudge on cheek and jawline, parted lips, eyes wide, orange trouble light illuminating from below, car undercarriage blurred above",
                "positive_extra": "grease on cheek, parted lips, wide eyes, orange light from below, car undercarriage",
                "shot": "close_up",
                "caption": "She found the problem. It wasn't the car.",
            },
        ],

        "aftermath": [
            {
                "scene": "standing at garage utility sink, washing grease off hands and forearms, looking at own reflection in small dirty mirror, hair completely messed, satisfied half-smile",
                "positive_extra": "utility sink, washing hands, grease, dirty mirror, reflection, messed hair, half-smile",
                "shot": "medium",
            },
            {
                "scene": "close-up of car key on workbench next to greasy wrench, shop rag draped over both, fluorescent light overhead, no people visible",
                "positive_extra": "car key, workbench, greasy wrench, shop rag, fluorescent light, empty",
                "shot": "close_up",
                "caption": "The car was ready. Had been for an hour.",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 5. tattoo_parlor — After hours, ink and neon
    # ------------------------------------------------------------------
    {
        "key": "tattoo_parlor",
        "titles": ["Permanent", "Under the Needle", "Skin Deep", "Fresh Ink"],
        "description": "After-hours session. The neon OPEN sign is off, but the door isn't locked.",
        "time": "night",
        "location": "tattoo parlor",
        "furniture": ["tattoo reclining chair", "ink station tray", "leather stool", "flash art wall", "autoclave counter"],
        "lighting": ["neon sign glow red and blue", "adjustable tattoo lamp", "dim overhead track lighting", "LED strip under counter"],
        "atmosphere": ["edgy", "intimate", "buzzing"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "reclining in tattoo chair, one arm extended on armrest, looking at fresh bandage on inner wrist, neon art on walls glowing, tattoo lamp angled down, flash art sheets pinned everywhere",
                "positive_extra": "tattoo chair, arm extended, bandage on wrist, neon walls, tattoo lamp, flash art",
                "shot": "medium",
                "caption": "She said the design needed one more session. He believed her.",
            },
            {
                "scene": "standing at flash art wall, back to camera, pointing at design on wall, tank top showing shoulder blades, ink station visible to the side, neon red glow from window sign",
                "positive_extra": "flash art wall, back to camera, pointing, tank top, shoulder blades, ink station, neon red",
                "shot": "full_body",
            },
            {
                "scene": "sitting sideways in tattoo chair, legs over armrest, playful grin, pulling shirt collar to the side showing collarbone, neon blue light on skin, ink bottles in background",
                "positive_extra": "tattoo chair sideways, legs over armrest, playful grin, pulling collar, collarbone, neon blue, ink bottles",
                "shot": "medium_close",
                "dialogue": "I was thinking... maybe somewhere less visible this time.",
            },
        ],

        "tension": [
            {
                "scene": "lying back in tattoo chair, arms above head gripping chair back, stomach exposed, tattoo lamp aimed down creating spotlight effect, neon purple glow from walls",
                "positive_extra": "lying back, arms above head, stomach exposed, spotlight, tattoo lamp, neon purple",
                "shot": "medium",
            },
            {
                "scene": "close-up of fingers tracing along hip bone, goosebumps visible on skin, tattoo ink residue on fingertips, purple neon light, leather chair texture beneath",
                "positive_extra": "fingers tracing hip, goosebumps, ink on fingertips, neon purple, leather texture",
                "shot": "close_up",
                "dialogue": "Right there. That's where I want it.",
            },
            {
                "scene": "arching back in tattoo chair, one hand gripping armrest, eyes closed, biting lip, neon signs reflecting on sweat-sheened skin, buzzing tattoo machine on tray nearby",
                "positive_extra": "arching back, gripping armrest, eyes closed, biting lip, neon on skin, tattoo machine, tray",
                "shot": "medium_close",
            },
            {
                "scene": "pulling herself up by chair arms, face very close to camera, heavy-lidded eyes, lips parted, neon red on one side neon blue on other side of face, tattoo flash art blurred behind",
                "positive_extra": "pulling up, close face, heavy-lidded, parted lips, neon red blue split, flash art blur",
                "shot": "close_up",
                "caption": "Some things mark you deeper than ink.",
            },
        ],

        "aftermath": [
            {
                "scene": "standing at parlor mirror, turning to look at lower back in reflection, tracing fresh tattoo bandage with fingertip, shirt gathered up, neon signs dimmed, hair disheveled",
                "positive_extra": "mirror, turning, lower back, tattoo bandage, fingertip, shirt up, neon dim, disheveled",
                "shot": "medium",
            },
            {
                "scene": "close-up of turned-off neon OPEN sign in tattoo parlor window, street visible outside, rain starting, two coffee cups on counter inside, one with lipstick mark",
                "positive_extra": "neon sign off, window, street, rain, coffee cups, lipstick mark, empty parlor",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 6. bakery_dawn — Before opening, flour dust, warm ovens
    # ------------------------------------------------------------------
    {
        "key": "bakery_dawn",
        "titles": ["Before First Light", "Rising", "Proof", "Kneading Time"],
        "description": "4am. The ovens are warm. The doors don't open until seven.",
        "time": "morning",
        "location": "bakery kitchen",
        "furniture": ["marble prep counter", "commercial bread oven", "proofing rack", "flour sack pile", "wooden kneading table"],
        "lighting": ["warm oven glow", "blue pre-dawn through window", "pendant light over counter", "golden interior warmth"],
        "atmosphere": ["warm", "flour-dusted", "cozy", "dawn"],
        "phase_structure": "all_phase1",

        "setup": [
            {
                "scene": "kneading dough on marble counter, flour dust in air catching pre-dawn blue window light, apron tied tight, sleeves rolled up showing flour-dusted forearms, warm pendant light above",
                "positive_extra": "kneading dough, marble counter, flour dust, pre-dawn blue, apron, flour forearms, pendant light",
                "shot": "medium",
                "caption": "4:12 AM. Three hours before the doors open.",
            },
            {
                "scene": "opening commercial oven door, wave of heat and golden light flooding out, squinting against warmth, steam rising, hair escaping from tied-back style, dark bakery behind",
                "positive_extra": "oven door open, golden heat light, squinting, steam rising, hair escaping, dark bakery",
                "shot": "medium_close",
            },
            {
                "scene": "turning from proofing rack startled, flour handprint on cheek, holding risen dough ball, early morning light just starting through window, warm oven glow behind",
                "positive_extra": "startled turn, flour handprint cheek, dough ball, morning light starting, oven glow",
                "shot": "medium_close",
                "dialogue": "You're early. I haven't even started the pastries.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on flour sack pile in bakery corner, knees together, dusting flour off thighs, looking up through lashes, warm oven light painting her golden, proofing racks beside",
                "positive_extra": "flour sacks, knees together, dusting flour, looking up, oven light golden, proofing racks",
                "shot": "medium",
                "dialogue": "The dough needs twenty minutes to rise anyway.",
            },
            {
                "scene": "leaning back against wooden kneading table, hands gripping table edge behind, flour dust on bare arms and collar, head tilted back, warm bakery light, pre-dawn blue window behind",
                "positive_extra": "kneading table, hands gripping edge, flour on arms, head back, warm light, blue window",
                "shot": "full_body",
            },
            {
                "scene": "close-up of hand leaving flour fingerprints on skin of neck, warm golden light, flour particles floating in air, blurred oven glow behind",
                "positive_extra": "flour fingerprints, neck, golden light, flour particles, floating, oven glow blur",
                "shot": "close_up",
            },
            {
                "scene": "face resting against forearm on marble counter surface, eyes half-closed, lips parted, flour dusted across cheekbone, warm pendant light directly above, marble cold beneath",
                "positive_extra": "face on marble, half-closed eyes, parted lips, flour on cheekbone, pendant light, marble surface",
                "shot": "close_up",
                "caption": "The timer still had twelve minutes.",
            },
        ],

        "aftermath": [
            {
                "scene": "standing at oven pulling out tray of golden bread, composed again, apron re-tied, but flour handprints visible on back of apron, dawn light now orange through window",
                "positive_extra": "pulling bread tray, composed, apron retied, flour handprints on back, dawn orange light",
                "shot": "full_body",
            },
            {
                "scene": "close-up of fresh bread loaf on cooling rack, steam rising from crust, flour handprint visible on marble counter beside it, morning light through window, no people",
                "positive_extra": "bread loaf, cooling rack, steam, flour handprint, marble counter, morning light",
                "shot": "close_up",
                "caption": "The bread came out perfect. Best batch in weeks.",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 7. teachers_lounge — After school, empty building
    # ------------------------------------------------------------------
    {
        "key": "teachers_lounge",
        "titles": ["After the Bell", "Faculty Meeting", "Teacher's Pet", "Detention"],
        "description": "The last bus left twenty minutes ago. The building is empty.",
        "time": "afternoon",
        "location": "teachers lounge",
        "furniture": ["worn vinyl couch", "vending machine", "laminate table", "rolling office chair", "mini fridge"],
        "lighting": ["afternoon sun through high windows", "buzzing fluorescent tubes", "vending machine glow", "warm golden hour"],
        "atmosphere": ["institutional", "empty", "quiet", "golden hour"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on worn vinyl couch in teachers lounge, shoes kicked off beside couch, rubbing temples, stack of papers on lap, afternoon sun through high narrow windows, vending machine humming",
                "positive_extra": "vinyl couch, shoes off, rubbing temples, papers, afternoon sun, high windows, vending machine",
                "shot": "medium",
                "caption": "Everyone else left at the bell. She had papers to grade.",
            },
            {
                "scene": "standing at vending machine, bending slightly to retrieve drink from slot, looking sideways at door, empty teachers lounge behind, laminate table covered in folders, afternoon light",
                "positive_extra": "vending machine, bending, retrieving drink, looking at door, empty lounge, folders, afternoon",
                "shot": "full_body",
            },
            {
                "scene": "leaning in doorway of teachers lounge, arms crossed, one eyebrow raised, blouse slightly untucked, pencil still behind ear, hallway visible behind stretching empty",
                "positive_extra": "doorway, arms crossed, eyebrow raised, blouse untucked, pencil behind ear, empty hallway",
                "shot": "medium_close",
                "dialogue": "The building's supposed to be locked by now.",
            },
        ],

        "tension": [
            {
                "scene": "perched on edge of laminate table, one leg swinging, papers pushed aside, holding coffee cup with both hands, looking over rim at camera, golden hour light across face",
                "positive_extra": "table edge, leg swinging, papers aside, coffee cup, looking over rim, golden hour",
                "shot": "medium",
                "dialogue": "I'll just say I was grading if anyone asks.",
            },
            {
                "scene": "leaning against door frame pulling door shut with one hand, other hand undoing top button of blouse, determined expression, fluorescent light behind, empty hallway closing off",
                "positive_extra": "pulling door shut, undoing button, blouse, determined, fluorescent, hallway closing",
                "shot": "medium_close",
            },
            {
                "scene": "pushed back in rolling office chair, one foot on chair seat knee up, the other leg extended, leaning back with arms on rests, head tilted, warm afternoon light on body",
                "positive_extra": "office chair, knee up, leaning back, arms on rests, head tilted, afternoon light",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face with reading glasses pushed up into hair, flushed cheeks, eyes half-lidded looking upward, golden light catching in pushed-up glasses, lips parted",
                "positive_extra": "reading glasses in hair, flushed, half-lidded, looking up, golden light, glasses catching light, parted lips",
                "shot": "close_up",
                "caption": "The empty building felt enormous around them.",
            },
        ],

        "aftermath": [
            {
                "scene": "standing at lounge mirror adjusting blouse and hair, papers re-stacked on table behind, coffee cup emptied, vending machine glow only light source now, twilight through windows",
                "positive_extra": "mirror, adjusting blouse, hair fix, papers stacked, empty cup, vending glow, twilight",
                "shot": "medium",
            },
            {
                "scene": "close-up of red pen lying across half-graded paper on laminate table, large A+ circled on paper, rolling chair still spinning slowly, empty room, dusk light",
                "positive_extra": "red pen, graded paper, A+, spinning chair, empty room, dusk light",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 8. firehouse_bunk — Between calls, dormitory
    # ------------------------------------------------------------------
    {
        "key": "firehouse_bunk",
        "titles": ["Between Alarms", "The Bunk", "False Alarm", "Five-Alarm"],
        "description": "Quiet shift. The alarm could ring any second. Or not at all.",
        "time": "night",
        "location": "firehouse bunkroom",
        "furniture": ["metal bunk bed", "locker row", "bench", "emergency pole opening", "turnout gear rack"],
        "lighting": ["red emergency strip light", "dim overhead bunk light", "moonlight through high window", "locker room fluorescent"],
        "atmosphere": ["tense", "quiet", "ready", "masculine"],
        "phase_structure": "reversed",

        "setup": [
            {
                "scene": "sitting on lower bunk bed, elbows on knees, hands clasped, looking at floor, red emergency strip light casting glow across face, turnout gear hanging on rack beside bed, metal frame visible",
                "positive_extra": "bunk bed, elbows on knees, hands clasped, red strip light, turnout gear rack, metal frame",
                "shot": "medium",
                "caption": "Hour six of a twelve-hour shift. Nothing but silence.",
            },
            {
                "scene": "standing at locker pulling shirt over head, back muscles visible, open locker door with mirror, dim bunkroom behind, other bunks empty and made, red safety light along baseboard",
                "positive_extra": "locker, pulling shirt, back muscles, mirror in locker, dim bunkroom, empty bunks, red light",
                "shot": "full_body",
            },
            {
                "scene": "leaning against firehouse pole opening railing, arms crossed, looking at someone approaching, surprised, dim overhead light, pole descending into darkness below, metal railing",
                "positive_extra": "pole opening, railing, arms crossed, surprised, dim light, pole into darkness, metal",
                "shot": "medium_close",
                "dialogue": "You're not supposed to be up here.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on bench between locker rows, legs apart, leaning back against closed locker, one arm resting on knee, challenging stare, red emergency light creating dramatic shadows",
                "positive_extra": "bench, lockers, leaning back, arm on knee, challenging stare, red light, dramatic shadows",
                "shot": "medium",
                "dialogue": "Alarm could go off any second.",
            },
            {
                "scene": "standing with back pressed against cold metal locker, head tilted back, throat exposed, dim light from above, locker handle pressing into hip, eyes closed tight",
                "positive_extra": "against locker, head back, throat exposed, dim light, locker handle, eyes closed",
                "shot": "medium_close",
            },
            {
                "scene": "gripping top rail of bunk bed frame from below, knuckles white on metal, face in shadow with red strip light catching jaw and lips, bedspring visible above",
                "positive_extra": "gripping bunk rail, white knuckles, shadow face, red light on jaw, lips, bedspring",
                "shot": "close_up",
            },
            {
                "scene": "lying on narrow bunk mattress, thin sheet bunched at waist, one arm draped over edge, face turned toward camera, flushed, red emergency glow painting skin, pillow askew",
                "positive_extra": "narrow bunk, sheet at waist, arm over edge, flushed, red glow, pillow askew",
                "shot": "close_up",
                "caption": "The alarm stayed silent.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on bunk edge pulling on boots quickly, shirt half-buttoned, hair wild, alarm light now flashing amber, turnout gear rack in motion beside, urgent posture",
                "positive_extra": "pulling on boots, half-buttoned, hair wild, amber flash, turnout gear, urgent",
                "shot": "full_body",
            },
            {
                "scene": "close-up of firehouse alarm box on wall, amber light flashing, bunk sheets visible tangled and messy in background, empty room, boots left behind on floor",
                "positive_extra": "alarm box, amber flash, tangled sheets, empty room, boots on floor",
                "shot": "close_up",
                "caption": "The alarm chose its moment perfectly.",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 9. bookstore_indie — Closing time, indie shop
    # ------------------------------------------------------------------
    {
        "key": "bookstore_indie",
        "titles": ["Shelf Life", "After Browse", "First Edition", "Bookmark"],
        "description": "Indie bookshop. Closing time. The last customer won't leave.",
        "time": "evening",
        "location": "indie bookstore",
        "furniture": ["overstuffed reading chair", "tall wooden bookshelves", "checkout counter", "window display bench", "step stool"],
        "lighting": ["warm string lights along shelves", "desk lamp at register", "golden evening through shopfront", "reading nook floor lamp"],
        "atmosphere": ["cozy", "warm", "paper-scented"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing behind checkout counter, chin resting on palm, staring at empty shop, warm string lights twinkling along wooden shelves, hand-lettered OPEN sign in window, golden evening light through glass door",
                "positive_extra": "checkout counter, chin on palm, string lights, wooden shelves, OPEN sign, golden evening, glass door",
                "shot": "medium",
                "caption": "Ten minutes to close. One customer left.",
            },
            {
                "scene": "kneeling between tall bookshelves, restacking fallen books from bottom shelf, skirt riding up slightly, warm overhead light, narrow aisle, spine titles visible on shelves",
                "positive_extra": "kneeling, bookshelves, restacking, bottom shelf, warm light, narrow aisle, book spines",
                "shot": "full_body",
            },
            {
                "scene": "looking up from step stool while reaching for high shelf, one hand on shelf for balance, surprised expression, string lights casting warm dots across face, narrow bookshop aisle",
                "positive_extra": "step stool, reaching up, hand on shelf, surprised, string lights dots, narrow aisle",
                "shot": "medium_close",
                "dialogue": "We're closing in five. Can I help you find something?",
            },
        ],

        "tension": [
            {
                "scene": "sitting in overstuffed reading chair with book open, legs tucked beside her, looking up from pages with sly expression, floor lamp casting warm pool of light, bookshelves framing her",
                "positive_extra": "reading chair, book open, legs tucked, sly expression, floor lamp, warm light, bookshelves framing",
                "shot": "medium",
                "dialogue": "I found what I was looking for. It's not a book.",
            },
            {
                "scene": "leaning against checkout counter from customer side, elbows on counter, chin on hands, looking up at standing perspective, string lights reflecting in eyes, books stacked beside her",
                "positive_extra": "leaning on counter, elbows, chin on hands, looking up, string light reflections, stacked books",
                "shot": "medium_close",
            },
            {
                "scene": "pressed into corner between two tall bookshelves, hands flat against book spines on either side, head back against shelf, warm light from above, narrow trapped space",
                "positive_extra": "corner between shelves, hands on spines, head back, warm light, narrow space, trapped",
                "shot": "close_up",
            },
            {
                "scene": "sitting on window display bench, back to glass storefront, evening street lights behind creating silhouette, inside lit warmly, string lights haloing head, lips parted, looking at viewer",
                "positive_extra": "window bench, storefront glass, street lights, silhouette, string lights halo, parted lips",
                "shot": "close_up",
                "caption": "She flipped the OPEN sign to CLOSED without looking.",
            },
        ],

        "aftermath": [
            {
                "scene": "lying in overstuffed chair, knees over armrest, open book tented on stomach, eyes closed, peaceful smile, string lights still on, darkened street visible through shop window",
                "positive_extra": "chair, knees over armrest, book on stomach, eyes closed, peaceful, string lights, dark street",
                "shot": "medium",
            },
            {
                "scene": "close-up of receipt paper from register with phone number handwritten on back, pen beside it, checkout counter surface, warm lamp glow, stack of unshelved books",
                "positive_extra": "receipt paper, phone number, handwritten, pen, counter, warm lamp, unshelved books",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 10. coffee_shop_closing — Last customer, espresso machine
    # ------------------------------------------------------------------
    {
        "key": "coffee_shop_closing",
        "titles": ["Last Pour", "Grounds", "Double Shot", "Closing Time"],
        "description": "The espresso machine needs cleaning. He needs a refill.",
        "time": "evening",
        "location": "coffee shop",
        "furniture": ["espresso machine counter", "small round cafe table", "bar stool", "pastry display case", "window booth seat"],
        "lighting": ["warm pendant lights over counter", "chalkboard menu spotlight", "evening amber through windows", "under-counter LED strip"],
        "atmosphere": ["warm", "coffee-scented", "intimate"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "wiping down espresso machine with cloth, barista apron on, hair tied back, steam still rising from group head, warm pendant light above, empty cafe behind, chairs stacked on tables",
                "positive_extra": "espresso machine, wiping, apron, hair tied, steam, pendant light, empty cafe, stacked chairs",
                "shot": "medium",
                "caption": "Everyone cleared out by 8. Except him.",
            },
            {
                "scene": "carrying stack of ceramic mugs to counter, balancing carefully, tongue peeking out in concentration, pastry display case dark and empty, chalkboard menu above, evening light from windows",
                "positive_extra": "stack of mugs, carrying, concentration, empty pastry case, chalkboard menu, evening light",
                "shot": "full_body",
            },
            {
                "scene": "leaning across counter toward seated customer perspective, both hands flat on counter, amused expression, espresso machine chrome behind reflecting her face, pendant light between them",
                "positive_extra": "leaning across counter, hands flat, amused, espresso chrome, reflection, pendant light",
                "shot": "medium_close",
                "dialogue": "Kitchen's closed. But I could do one more cup.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on counter next to espresso machine, legs dangling, holding small espresso cup between both hands, steam rising from cup, looking over rim, warm overhead light, empty shop dark behind",
                "positive_extra": "on counter, legs dangling, espresso cup, steam, looking over rim, warm light, dark shop",
                "shot": "medium",
            },
            {
                "scene": "standing between cafe table and wall, untying apron strings behind back, pulling apron over head, hair falling free, bar stool visible, amber window light",
                "positive_extra": "untying apron, pulling over head, hair falling free, bar stool, amber light",
                "shot": "medium_close",
                "dialogue": "I'm officially off the clock now.",
            },
            {
                "scene": "pressed against pastry display case glass, cold glass against back, arms up gripping the case top, pendant light creating warm spotlight, empty cake shelves behind glass",
                "positive_extra": "pastry case glass, back against glass, arms up, gripping case top, pendant spotlight, empty shelves",
                "shot": "full_body",
            },
            {
                "scene": "close-up face reflected in espresso machine chrome, distorted and warm, parted lips, eyes focused, steam blurring edges of reflection, copper tubing visible",
                "positive_extra": "reflection in chrome, distorted, parted lips, focused eyes, steam blur, copper tubing",
                "shot": "close_up",
                "caption": "The espresso machine still hadn't been cleaned.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting in window booth, legs up on seat, sipping from large mug, looking out at empty evening street, relaxed posture, apron balled up on table, pendant lights off except one",
                "positive_extra": "window booth, legs up, sipping mug, evening street, relaxed, apron balled, one light",
                "shot": "medium",
            },
            {
                "scene": "close-up of two espresso cups on saucer, one with lipstick mark on rim, both empty, small biscotti crumbs, bar counter surface, all other lights off",
                "positive_extra": "two espresso cups, lipstick mark, empty, biscotti crumbs, counter, lights off",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 11. warehouse_inventory — Late stock count, industrial shelves
    # ------------------------------------------------------------------
    {
        "key": "warehouse_inventory",
        "titles": ["Stock Take", "Inventory Night", "Aisle Seven", "Counted"],
        "description": "Midnight inventory. Two people. A thousand shelves.",
        "time": "night",
        "location": "warehouse",
        "furniture": ["tall industrial shelving", "pallet jack", "cardboard box stack", "folding table", "clipboard station"],
        "lighting": ["harsh overhead bay lights", "motion sensor light sections", "loading dock moonlight", "phone flashlight beam"],
        "atmosphere": ["industrial", "echoing", "vast", "cold"],
        "phase_structure": "all_phase1",

        "setup": [
            {
                "scene": "walking down warehouse aisle between tall industrial shelves, clipboard in hand, pen behind ear, harsh overhead bay light illuminating row, vast dark space beyond, boxes stacked high on both sides",
                "positive_extra": "warehouse aisle, industrial shelves, clipboard, pen behind ear, bay light, vast dark, boxes",
                "shot": "full_body",
                "caption": "Midnight. Row 47 of 200. The math wasn't encouraging.",
            },
            {
                "scene": "sitting on stacked boxes, legs crossed, scanning barcode with handheld device, bored expression, motion sensor light flickering on above, dark warehouse stretching behind",
                "positive_extra": "stacked boxes, legs crossed, scanner, bored, motion sensor light, dark warehouse",
                "shot": "medium",
            },
            {
                "scene": "turning around at end of aisle, flashlight beam from phone illuminating face, startled, other person's shadow stretched long on concrete floor, shelving towering on both sides",
                "positive_extra": "turning around, phone flashlight, startled, shadow on floor, towering shelves, aisle end",
                "shot": "medium_close",
                "dialogue": "Jesus. I thought I was the only one still here.",
            },
        ],

        "tension": [
            {
                "scene": "leaning against pallet jack handle, one hip resting on metal, clipboard dangling from one hand, tired half-smile, overhead light buzzing above, concrete floor, warehouse shelves behind",
                "positive_extra": "pallet jack, hip on metal, clipboard dangling, tired smile, buzzing light, concrete, shelves",
                "shot": "medium",
                "dialogue": "We could skip the back rows. Nobody checks those.",
            },
            {
                "scene": "sitting on folding table that wobbles slightly, legs dangling, leaning back on hands, looking up at towering dark shelves, single bay light above creating spotlight, boxes framing either side",
                "positive_extra": "folding table, legs dangling, leaning back, dark shelves above, spotlight, boxes framing",
                "shot": "full_body",
            },
            {
                "scene": "pressed between cardboard box wall and industrial shelf support beam, metal against shoulder, looking sideways at camera, dim section with motion light off, only phone glow on face",
                "positive_extra": "between boxes and beam, metal against shoulder, looking sideways, dim, phone glow, industrial",
                "shot": "medium_close",
            },
            {
                "scene": "close-up of face lit by phone screen from below, casting dramatic upward shadows, lips slightly parted, eyes reflecting blue screen light, warehouse dark behind",
                "positive_extra": "phone light from below, dramatic shadows, parted lips, blue screen reflection, warehouse dark",
                "shot": "close_up",
                "caption": "The motion sensor lights clicked off. Neither reached for the switch.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on concrete floor leaning against box stack, clipboard across lap, pen dropped beside her, hair messed, looking at phone screen showing 3am, motion light just triggered back on",
                "positive_extra": "concrete floor, against boxes, clipboard in lap, dropped pen, messy hair, phone showing 3am, light on",
                "shot": "medium",
            },
            {
                "scene": "close-up of clipboard on folding table, inventory sheet half-completed, pen line trailing off mid-word where she stopped writing, harsh bay light overhead",
                "positive_extra": "clipboard, inventory sheet, half-completed, pen trail, stopped mid-word, bay light",
                "shot": "close_up",
                "caption": "The inventory report was filed late. No explanation given.",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 12. office_copy_room — Small room, nowhere to hide
    # ------------------------------------------------------------------
    {
        "key": "office_copy_room",
        "titles": ["Paper Jam", "Copies", "Collated", "The Small Room"],
        "description": "The copy room. Barely big enough for two. The machine is running.",
        "time": "evening",
        "location": "office copy room",
        "furniture": ["large copier machine", "paper supply shelf", "narrow counter", "filing cabinet", "recycling bin"],
        "lighting": ["copier scan light sweeping", "harsh fluorescent overhead", "green copier status LED", "hallway light under door"],
        "atmosphere": ["cramped", "humming", "warm from machine"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing at large copy machine feeding papers, one hand on lid pressing it down, other hand on hip, bored expression, fluorescent light above, narrow room with shelves of paper reams",
                "positive_extra": "copy machine, feeding papers, hand on lid, hand on hip, bored, fluorescent, paper shelves, narrow room",
                "shot": "medium",
                "caption": "200 copies. Double-sided. The machine was slow.",
            },
            {
                "scene": "reaching up to high paper shelf, standing on tiptoes, one hand on shelf edge for balance, blouse pulling taut, copy machine humming behind, cramped room, warm air",
                "positive_extra": "reaching up, tiptoes, hand on shelf, blouse taut, copier humming, cramped room",
                "shot": "full_body",
            },
            {
                "scene": "turning in cramped copy room to face door, someone blocking exit, limited space between copier and shelf, slightly alarmed then amused expression, copier scan light sweeping across wall",
                "positive_extra": "turning, cramped room, door blocked, copier, shelf, amused, scan light sweep",
                "shot": "medium_close",
                "dialogue": "There's barely room for the copier in here, let alone both of us.",
            },
        ],

        "tension": [
            {
                "scene": "perched on narrow counter beside copier, knees together, palms flat on counter surface, leaning slightly forward, copier rhythmically flashing scan light, close quarters, warm air visible",
                "positive_extra": "narrow counter, beside copier, knees together, palms flat, leaning forward, scan flash, close quarters",
                "shot": "medium",
                "dialogue": "Close the door. The copies are loud enough to cover.",
            },
            {
                "scene": "pressed against filing cabinet, metal handle pressing into lower back, one hand flat on cabinet face, other hand reaching behind to brace, copier light strobing across face periodically",
                "positive_extra": "filing cabinet, handle in back, hand flat, bracing, copier strobe, periodic light",
                "shot": "medium_close",
            },
            {
                "scene": "hands gripping copier machine lid while it runs, copier light sweeping underneath hands periodically, knuckles tight, paper stacking in output tray behind",
                "positive_extra": "gripping copier lid, scan light under hands, knuckles tight, paper stacking, output tray",
                "shot": "close_up",
            },
            {
                "scene": "close-up of face lit by copier scan light passing, green-white light stripe moving across features, eyes squeezed shut, biting lower lip, paper reams behind in shadow",
                "positive_extra": "copier scan light, stripe across face, eyes shut, biting lip, paper reams, shadow",
                "shot": "close_up",
                "caption": "The copier kept printing. Nobody touched the stop button.",
            },
        ],

        "aftermath": [
            {
                "scene": "gathering scattered papers from floor of copy room on hands and knees, pages everywhere, copier out of paper and blinking error, hair hanging down hiding face, amused",
                "positive_extra": "gathering papers, floor, hands and knees, pages everywhere, copier error, hair hiding face",
                "shot": "medium",
            },
            {
                "scene": "close-up of copier output tray overflowing with printed pages, paper spilling onto floor, green status light blinking, empty room, door ajar showing dark hallway",
                "positive_extra": "output tray overflowing, paper spilling, green light blinking, empty room, door ajar, dark hallway",
                "shot": "close_up",
                "caption": "She took one copy. Left the other 199.",
            },
        ],
    },

    # ==================================================================
    # SOCIAL/NIGHTLIFE (12)
    # ==================================================================

    # ------------------------------------------------------------------
    # 13. nightclub_vip — VIP booth, bass vibration
    # ------------------------------------------------------------------
    {
        "key": "nightclub_vip",
        "titles": ["VIP", "Bottle Service", "Velvet Rope", "Last Set"],
        "description": "VIP booth. The bass shakes the leather. Nobody's watching.",
        "time": "night",
        "location": "nightclub VIP booth",
        "furniture": ["curved leather booth seat", "low glass table", "champagne bucket", "velvet rope barrier", "DJ booth visible"],
        "lighting": ["purple UV blacklight", "laser beams cutting smoke", "LED strip under table", "strobe flashes"],
        "atmosphere": ["loud bass", "smoky", "pulsing", "exclusive"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting in curved VIP booth, one arm stretched along leather backrest, champagne glass in other hand, purple UV light making white clothing glow, dance floor crowd blurred below, laser beams through smoke above",
                "positive_extra": "VIP booth, arm on backrest, champagne, UV light, glowing, dance floor blur, lasers, smoke",
                "shot": "medium",
                "caption": "VIP meant Very Isolated Privacy.",
            },
            {
                "scene": "standing at velvet rope looking back into VIP area, hip cocked, drink in hand, UV light catching teeth in smile, bass visible as vibration in glass table surface, strobe cutting through dark",
                "positive_extra": "velvet rope, looking back, hip cocked, drink, UV glow, bass vibration glass, strobe",
                "shot": "full_body",
            },
            {
                "scene": "leaning across low glass VIP table, face close to camera, shouting over music expression, hand cupped near mouth, purple and blue light shifting across skin, champagne bubbles visible in foreground glass",
                "positive_extra": "leaning across table, close face, shouting, hand cupped, purple blue shifting light, champagne bubbles",
                "shot": "medium_close",
                "dialogue": "I can't hear you. Come closer.",
            },
        ],

        "tension": [
            {
                "scene": "pulled into VIP booth corner, back against leather, knees up on seat, holding champagne glass against collarbone, purple UV making skin glow, private alcove, bass vibrating everything",
                "positive_extra": "booth corner, back on leather, knees up, champagne on collarbone, UV skin glow, alcove, bass",
                "shot": "medium",
            },
            {
                "scene": "standing in VIP booth area, back against privacy wall, one hand above head on wall, body swaying to bass, strobe freezing motion, smoke machine haze, purple light",
                "positive_extra": "back against wall, hand above head, swaying to bass, strobe freeze, smoke haze, purple",
                "shot": "full_body",
                "dialogue": "Nobody can see us from the floor.",
            },
            {
                "scene": "close-up of hand gripping leather booth edge, knuckles tight, champagne glass overturned on table behind spilling, purple UV light, bass vibration visible in spilled liquid ripples",
                "positive_extra": "gripping leather, knuckles, champagne overturned, spilling, UV light, bass ripples",
                "shot": "close_up",
            },
            {
                "scene": "face illuminated by alternating strobe and UV, eyes half-closed, lips parted, sweat on temple, smoke curling past, leather booth texture behind, looking at viewer through haze",
                "positive_extra": "strobe UV alternating, half-closed eyes, parted lips, sweat, smoke curl, leather, through haze",
                "shot": "close_up",
                "caption": "The DJ played one more set than scheduled.",
            },
        ],

        "aftermath": [
            {
                "scene": "slumped in VIP booth, shoes kicked off on glass table, champagne bottle empty in bucket, satisfied exhausted expression, house lights coming on washing everything in flat harsh light",
                "positive_extra": "slumped in booth, shoes on table, empty bottle, exhausted satisfied, house lights on, flat harsh",
                "shot": "medium",
            },
            {
                "scene": "close-up of champagne glass on table with lipstick kiss mark on rim, UV light off now revealing harsh house light, condensation ring on glass table, empty booth",
                "positive_extra": "champagne glass, lipstick mark, UV off, house light, condensation ring, empty booth",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 14. karaoke_private — Private room, mic and screen glow
    # ------------------------------------------------------------------
    {
        "key": "karaoke_private",
        "titles": ["Private Room", "Last Song", "Duet", "Off-Key"],
        "description": "Private karaoke room. The hour is up. She's still got the mic.",
        "time": "night",
        "location": "karaoke room",
        "furniture": ["vinyl booth seat", "karaoke screen TV", "small stage platform", "disco ball", "cocktail table"],
        "lighting": ["karaoke screen blue glow", "rotating disco ball lights", "neon wall strip", "dim overhead color-changing LED"],
        "atmosphere": ["loud", "colorful", "intimate", "playful"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing on small karaoke stage, microphone in hand held to side, screen behind displaying song lyrics in blue glow, disco ball scattering light dots across face, vinyl booth seat in foreground",
                "positive_extra": "karaoke stage, microphone, lyrics screen, blue glow, disco ball dots, vinyl booth",
                "shot": "medium",
                "caption": "She picked the song. He didn't know the words.",
            },
            {
                "scene": "collapsed on vinyl booth seat laughing, microphone abandoned on cushion beside, hand covering face, disco ball spinning colors across room, empty cocktail glasses on table, karaoke screen idle",
                "positive_extra": "booth laughing, microphone abandoned, hand on face, disco lights, empty glasses, screen idle",
                "shot": "medium_close",
            },
            {
                "scene": "holding microphone out toward camera offering it, playful dare expression, one eyebrow raised, disco ball lights moving across her outstretched arm, neon wall strip behind, karaoke room door closed",
                "positive_extra": "offering microphone, dare expression, eyebrow raised, disco lights on arm, neon strip, door closed",
                "shot": "medium_close",
                "dialogue": "Your turn. Unless you're scared.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on karaoke stage edge, legs dangling off platform, mic cord wrapped loosely around one hand, looking up at standing perspective, disco ball casting moving dots, screen showing slow ballad lyrics",
                "positive_extra": "stage edge, legs dangling, mic cord on hand, looking up, disco dots moving, ballad lyrics",
                "shot": "medium",
                "dialogue": "This next one's a duet. Get up here.",
            },
            {
                "scene": "pressed into corner of vinyl booth, mic held between them like a barrier, faces close, disco lights painting skin pink blue green rotating, cocktail table pushed aside",
                "positive_extra": "booth corner, mic between them, faces close, disco lights rotating, pink blue green, table pushed",
                "shot": "medium_close",
            },
            {
                "scene": "lying back on vinyl booth seat, microphone resting on stomach, one arm above head, disco ball lights traversing across body in slow rotation, karaoke screen blank with cursor blinking",
                "positive_extra": "lying back, mic on stomach, arm above head, disco light traverse, screen blank, cursor",
                "shot": "full_body",
            },
            {
                "scene": "close-up face lit by alternating disco colors, eyes looking up, mic pressed against lower lip, warm breath visible on metal mesh, flushed cheeks, dim room behind",
                "positive_extra": "disco colors on face, looking up, mic on lip, breath on mesh, flushed, dim room",
                "shot": "close_up",
                "caption": "The room timer hit zero. The lock didn't click.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on floor of karaoke room back against booth base, microphone hanging from cord off table above, disheveled hair, legs extended, disco ball still spinning, screen displaying TIME'S UP",
                "positive_extra": "floor, back against booth, mic dangling, disheveled, legs out, disco ball, TIME'S UP screen",
                "shot": "full_body",
            },
            {
                "scene": "close-up of karaoke screen showing song queue list, one song highlighted and marked REPLAY, disco ball reflections on screen surface, empty room",
                "positive_extra": "karaoke screen, song queue, REPLAY marked, disco reflections, empty room",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 15. house_party_upstairs — Locked bedroom at a party
    # ------------------------------------------------------------------
    {
        "key": "house_party_upstairs",
        "titles": ["Upstairs", "Coat Room", "Locked Door", "The Quiet Room"],
        "description": "Party downstairs. Locked bedroom upstairs. Muffled bass through the floor.",
        "time": "night",
        "location": "bedroom at house party",
        "furniture": ["bed with coat pile", "dresser with mirror", "window overlooking backyard", "bean bag chair", "bedside lamp"],
        "lighting": ["bedside lamp warm glow", "party lights visible from window", "hallway light under door crack", "phone screen glow"],
        "atmosphere": ["muffled bass", "private", "warm", "secret"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on bed covered in pile of winter coats, one coat held up examining it, muffled bass audible from party below making floor vibrate, bedside lamp only light, party glow visible through window",
                "positive_extra": "bed, coat pile, holding coat, muffled bass, bedside lamp, party glow window",
                "shot": "medium",
                "caption": "She came upstairs to find her coat. That was twenty minutes ago.",
            },
            {
                "scene": "standing at bedroom window looking down at backyard party below, silhouette against colored party lights outside, curtain pulled aside with one hand, bedroom dark except bedside lamp, coats piled on bed",
                "positive_extra": "window, looking down, backyard party, silhouette, party lights, curtain, dark bedroom, lamp",
                "shot": "full_body",
            },
            {
                "scene": "turning from window toward bedroom door, someone entering, hand still on curtain, surprised but not displeased expression, hallway light flooding in from cracked door, party noise getting louder briefly",
                "positive_extra": "turning from window, door opening, hand on curtain, surprised, hallway light flood, party noise",
                "shot": "medium_close",
                "dialogue": "This room's supposed to be off limits.",
            },
        ],

        "tension": [
            {
                "scene": "pushing bedroom door shut with back, reaching behind to turn lock, holding eye contact with camera, party noise muffled as door closes, hallway light disappearing, only bedside lamp remaining",
                "positive_extra": "pushing door shut, back against door, turning lock, eye contact, muffled noise, lamp only",
                "shot": "medium",
            },
            {
                "scene": "sitting on bean bag chair, sinking into it, knees up, one hand brushing hair back, coats pushed to one side of bed visible, warm lamplight, muffled bass vibrating through floor",
                "positive_extra": "bean bag, sinking, knees up, brushing hair, coats pushed aside, lamplight, floor vibration",
                "shot": "medium_close",
                "dialogue": "They won't miss us for one song.",
            },
            {
                "scene": "kneeling on bed pushing pile of coats to floor, clearing space, determined expression, bedside lamp casting warm shadows, dresser mirror reflecting the scene, party bass thumping",
                "positive_extra": "kneeling on bed, pushing coats off, determined, lamp shadows, mirror reflection, bass thumping",
                "shot": "full_body",
            },
            {
                "scene": "close-up face against pillow, eyes half-closed, lips parted, warm lamp light on one side of face, shadow on other, muffled party bass matching pulse, flushed cheeks",
                "positive_extra": "face on pillow, half-closed eyes, parted lips, lamp light half, shadow half, flushed",
                "shot": "close_up",
                "caption": "Downstairs, nobody noticed they were gone.",
            },
        ],

        "aftermath": [
            {
                "scene": "standing at dresser mirror fixing hair, reflected in mirror, door slightly open, hallway party light and sound spilling in, coats scattered on floor around bed, composed expression returning",
                "positive_extra": "dresser mirror, fixing hair, reflection, door open, party light spilling, coats on floor, composed",
                "shot": "medium",
            },
            {
                "scene": "close-up of bedroom door handle from hallway side, lock button popped to unlocked, party red cup on hallway floor beside door, muffled music, no people visible",
                "positive_extra": "door handle, lock popped, hallway, red cup on floor, muffled music, no people",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 16. wedding_reception — After the dance, empty ballroom
    # ------------------------------------------------------------------
    {
        "key": "wedding_reception",
        "titles": ["After the Last Dance", "Plus One", "Open Bar", "Table Twelve"],
        "description": "The newlyweds left. The ballroom is almost empty. The band is packing up.",
        "time": "night",
        "location": "wedding ballroom",
        "furniture": ["round reception table", "dance floor", "head table with flowers", "dessert buffet table", "coat check booth"],
        "lighting": ["string light canopy", "tea candle centerpieces dying", "disco ball remnant", "exit sign red glow"],
        "atmosphere": ["romantic aftermath", "disheveled elegance", "winding down"],
        "phase_structure": "reversed",

        "setup": [
            {
                "scene": "sitting alone at round reception table, chin on hand, formal dress, one heel kicked off under table, tea candle dying on centerpiece, scattered confetti, empty chairs around table, string light canopy above",
                "positive_extra": "reception table, formal dress, one heel off, dying candle, confetti, empty chairs, string lights",
                "shot": "medium",
                "caption": "Table twelve. Everyone else went home with someone.",
            },
            {
                "scene": "standing on empty dance floor, bare feet on polished wood, shoes dangling from one hand, formal dress slightly wrinkled, disco ball still turning slowly above, band equipment being packed in background",
                "positive_extra": "empty dance floor, bare feet, polished wood, shoes in hand, wrinkled dress, disco ball turning, packing",
                "shot": "full_body",
            },
            {
                "scene": "leaning on dessert buffet table picking at leftover cake with finger, looking sideways with caught expression, formal dress disheveled, string lights reflecting in smeared buttercream, champagne flute nearby",
                "positive_extra": "buffet table, picking cake, caught expression, disheveled dress, string lights, buttercream, champagne",
                "shot": "medium_close",
                "dialogue": "I was just getting my coat. The cake was... in the way.",
            },
        ],

        "tension": [
            {
                "scene": "slow dancing alone on empty dance floor, arms positioned as if holding invisible partner, eyes closed, swaying, string lights above creating starfield, tea candles flickering on surrounding tables",
                "positive_extra": "slow dancing alone, empty floor, eyes closed, swaying, string lights starfield, tea candles",
                "shot": "full_body",
                "dialogue": "The DJ left, but the song's still in my head.",
            },
            {
                "scene": "pulled close on dance floor, head resting against shoulder perspective, one hand gripping formal fabric at hip, string lights blurred bokeh behind, confetti on floor catching light",
                "positive_extra": "close embrace, head on shoulder, gripping fabric, string lights bokeh, confetti, floor",
                "shot": "medium_close",
            },
            {
                "scene": "pressed against head table, wedding flowers pushed aside petals scattering, back against table edge, hands gripping tablecloth, string light canopy above, champagne glasses toppled",
                "positive_extra": "head table, flowers pushed, petals, back against table, gripping cloth, string lights, toppled glasses",
                "shot": "medium",
            },
            {
                "scene": "close-up of face framed by scattered rose petals on tablecloth, eyes looking up, candlelight flickering across cheekbone, formal earring dangling, flushed, lips parted",
                "positive_extra": "rose petals, tablecloth, looking up, candlelight, cheekbone, earring dangling, flushed, parted lips",
                "shot": "close_up",
                "caption": "The bride's bouquet was still sitting there. Uncaught.",
            },
        ],

        "aftermath": [
            {
                "scene": "walking across empty ballroom toward exit, one shoe on one shoe in hand, formal dress train dragging through confetti, string lights still on, back to camera, exit sign glowing red ahead",
                "positive_extra": "walking to exit, one shoe, dress train, confetti, string lights, back to camera, exit sign red",
                "shot": "full_body",
            },
            {
                "scene": "close-up of reception place card on table reading a name, lipstick kiss mark beside it, dying tea candle about to go out, rose petal on the card, empty ballroom reflected in champagne glass",
                "positive_extra": "place card, lipstick kiss, dying candle, rose petal, empty ballroom, champagne glass reflection",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 17. concert_backstage — Post-show, dressing room
    # ------------------------------------------------------------------
    {
        "key": "concert_backstage",
        "titles": ["Backstage Pass", "Encore", "The Green Room", "After Show"],
        "description": "The crowd is still screaming. Backstage, the door is closed.",
        "time": "night",
        "location": "concert dressing room backstage",
        "furniture": ["vanity mirror with bulbs", "clothing rack", "leather couch worn", "mini fridge", "instrument case"],
        "lighting": ["vanity mirror bulb ring", "warm tungsten overhead", "neon EXIT sign visible", "stage light bleed through door crack"],
        "atmosphere": ["adrenaline", "sweaty", "electric"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting at vanity mirror with bulb ring, removing stage makeup with wipe, sweat-damp hair, backstage pass visible on lanyard around neck, clothing rack behind, muffled crowd noise",
                "positive_extra": "vanity mirror, bulbs, removing makeup, sweaty, backstage pass, lanyard, clothing rack, muffled crowd",
                "shot": "medium",
                "caption": "The crowd wanted an encore. She wanted five minutes alone.",
            },
            {
                "scene": "leaning against dressing room door from inside, water bottle pressed against forehead, eyes closed, catching breath, adrenaline sweat visible, instrument case propped against wall, neon EXIT sign",
                "positive_extra": "leaning on door, water bottle on forehead, eyes closed, catching breath, sweat, instrument case, EXIT sign",
                "shot": "full_body",
            },
            {
                "scene": "turning from vanity mirror, backstage pass swinging on lanyard, amused but guarded expression, seeing visitor in mirror reflection, hand paused mid-makeup-removal, bulb light ring creating halo",
                "positive_extra": "turning from mirror, pass swinging, amused guarded, mirror reflection, hand paused, bulb ring halo",
                "shot": "medium_close",
                "dialogue": "How did you get back here?",
            },
        ],

        "tension": [
            {
                "scene": "sitting on worn leather backstage couch, legs tucked under, pulling off stage jewelry letting it drop on couch, looking up through damp hair, vanity bulbs behind creating backlight, relaxed posture",
                "positive_extra": "leather couch, removing jewelry, looking up through hair, vanity backlight, relaxed, damp",
                "shot": "medium",
                "dialogue": "The bouncer usually catches people at the door.",
            },
            {
                "scene": "standing at clothing rack, pulling stage outfit aside on hangers, revealing less underneath, looking over shoulder at camera, warm tungsten light, instrument case in background",
                "positive_extra": "clothing rack, pulling outfit aside, hangers, looking over shoulder, tungsten light, instrument case",
                "shot": "medium_close",
            },
            {
                "scene": "pushed against vanity table, sitting on its edge, legs dangling, hands gripping table edge, mirror bulbs framing body from behind, makeup scattered, water bottles toppled",
                "positive_extra": "vanity table edge, legs dangling, gripping edge, mirror bulbs framing, makeup scattered, toppled bottles",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face reflected in vanity mirror, real face and reflection visible, eyes locked on camera, stage makeup smeared, sweat and glitter on skin, light bulbs blurred around frame",
                "positive_extra": "mirror reflection, dual face, eyes locked, smeared makeup, sweat, glitter, bulbs blurred",
                "shot": "close_up",
                "caption": "The crowd finally stopped chanting.",
            },
        ],

        "aftermath": [
            {
                "scene": "lying on backstage leather couch face-down, one arm hanging off edge, backstage pass lanyard on floor, vanity lights dimmed, clothing rack clothes pushed to one side, exhausted stillness",
                "positive_extra": "couch face-down, arm hanging, pass on floor, lights dimmed, clothes pushed, exhausted",
                "shot": "medium",
            },
            {
                "scene": "close-up of backstage pass on floor, lanyard stretched out, glitter and smeared makeup on the laminated card, venue name visible, boot print partially on it, empty dressing room",
                "positive_extra": "backstage pass, floor, lanyard, glitter, smeared, venue name, boot print, empty room",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 18. bowling_alley — Late night lanes, UV light
    # ------------------------------------------------------------------
    {
        "key": "bowling_alley",
        "titles": ["Cosmic Bowl", "Strike", "Gutter Ball", "Lane Seven"],
        "description": "Cosmic bowling. Nobody else showed. UV light turns everything electric.",
        "time": "night",
        "location": "bowling alley cosmic bowling",
        "furniture": ["bowling lane seating", "scoring console", "ball return machine", "shoe rental counter", "arcade machine"],
        "lighting": ["UV blacklight cosmic bowling", "neon lane markers", "scoring screen glow", "arcade machine colors"],
        "atmosphere": ["playful", "neon", "retro", "competitive"],
        "phase_structure": "all_phase2",

        "setup": [
            {
                "scene": "sitting in lane seating, one bowling shoe on one regular shoe still on, holding bowling ball on lap, UV blacklight making white shirt glow electric blue, neon lane markers stretching away, scoring screen behind",
                "positive_extra": "lane seating, bowling shoe, ball on lap, UV blacklight, shirt glowing, neon lanes, scoring screen",
                "shot": "medium",
                "caption": "Cosmic bowling night. Two lanes booked. One couple cancelled.",
            },
            {
                "scene": "standing at lane approach holding bowling ball at chin level, focused squinting expression, UV glow painting skin purple, lane stretching ahead to lit pins, ball return machine beside",
                "positive_extra": "lane approach, bowling ball, chin level, focused, UV purple, lane to pins, ball return",
                "shot": "full_body",
            },
            {
                "scene": "turning from lane after bowling, triumphant pose, arms up, UV light catching smile and teeth, neon floor markers visible, scoring screen showing strike behind, playful competitive joy",
                "positive_extra": "turning from lane, triumphant, arms up, UV smile, neon floor, strike on screen, joy",
                "shot": "medium_close",
                "dialogue": "That's three in a row. Pay up.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on ball return machine ledge, legs swinging, bowling ball in lap held like a crystal ball, looking at it dramatically, UV light making everything glow, empty lanes on either side",
                "positive_extra": "ball return ledge, legs swinging, ball in lap, dramatic, UV glow, empty lanes",
                "shot": "medium",
                "dialogue": "Double or nothing. But I get to pick the stakes.",
            },
            {
                "scene": "leaning against arcade machine, neon colors from screen painting face, one hand on joystick, other hand on hip, competitive smirk, UV blacklight behind turning bowling area purple",
                "positive_extra": "arcade machine, neon face paint, hand on joystick, hip, competitive smirk, UV purple",
                "shot": "medium_close",
            },
            {
                "scene": "pressed against scoring console table, UV light making clothing edges glow electric, hands flat on table surface, leaning toward camera, chain of bowling lane lights stretching behind into darkness",
                "positive_extra": "scoring console, UV clothing glow, hands flat, leaning forward, lane lights, darkness behind",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face under UV blacklight, teeth glowing white, pupils dilated, neon colors reflected in eyes, lips parted, sweat visible in UV as bright dots, competitive intensity shifted to something else",
                "positive_extra": "UV blacklight face, teeth glow, dilated pupils, neon eye reflections, parted lips, UV sweat dots",
                "shot": "close_up",
                "caption": "The scoreboard stopped mattering around frame six.",
            },
        ],

        "aftermath": [
            {
                "scene": "lying on bowling lane approach, polished wood beneath, staring up at ceiling UV lights, bowling ball rolled to a stop nearby, shoes off, satisfied exhausted expression, hair spread on lane",
                "positive_extra": "lying on lane, polished wood, ceiling UV, ball stopped nearby, shoes off, satisfied, hair spread",
                "shot": "full_body",
            },
            {
                "scene": "close-up of scoring screen showing incomplete game, last frames empty, names visible at top, UV-lit bowling alley empty behind, one bowling shoe sitting on console",
                "positive_extra": "scoring screen, incomplete game, empty frames, UV bowling alley, empty, shoe on console",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 19. movie_theater — Empty late screening
    # ------------------------------------------------------------------
    {
        "key": "movie_theater",
        "titles": ["Late Showing", "Back Row", "Credits Roll", "Rated R"],
        "description": "11pm showing. Empty theater. The movie's been on for an hour.",
        "time": "night",
        "location": "movie theater auditorium",
        "furniture": ["plush theater seats", "armrest between seats", "cup holder tray", "exit row aisle", "projection screen"],
        "lighting": ["movie projector light flicker", "floor runner lights dim", "exit sign red glow", "screen color wash changing"],
        "atmosphere": ["dark", "quiet except film", "secluded"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting in back row theater seat, feet up on seat in front, popcorn container in lap, movie projector light flickering across face changing colors, rest of theater completely empty, dim floor runner lights",
                "positive_extra": "back row, feet up, popcorn, projector flicker, empty theater, floor runner lights",
                "shot": "medium",
                "caption": "The 11pm showing. Just her and an empty theater.",
            },
            {
                "scene": "walking down theater aisle toward back row, silhouette against bright projection screen, floor lights marking path, empty rows on both sides, movie playing loudly, looking at seats choosing",
                "positive_extra": "theater aisle, silhouette, projection screen, floor lights, empty rows, movie playing, choosing seats",
                "shot": "full_body",
            },
            {
                "scene": "looking sideways from theater seat, armrest raised between seats, surprised amused expression, movie light washing face blue and white, popcorn held protectively, empty theater behind",
                "positive_extra": "sideways look, armrest raised, surprised amused, movie light blue white, popcorn, empty theater",
                "shot": "medium_close",
                "dialogue": "All these seats and you pick the one next to mine.",
            },
        ],

        "tension": [
            {
                "scene": "leaning across raised armrest, face lit by changing movie colors, sharing popcorn, hand reaching into same container, fingers touching, blue light then warm light cycling from screen, close together",
                "positive_extra": "across armrest, movie colors, sharing popcorn, fingers touching, cycling light, close together",
                "shot": "medium_close",
                "dialogue": "I stopped watching the movie twenty minutes ago.",
            },
            {
                "scene": "slid down in theater seat, knees up against seat back in front, looking up at screen but not watching, armrest gone between seats, close proximity, movie projector beam visible above in darkness",
                "positive_extra": "slid down, knees up, not watching, armrest gone, close, projector beam above, darkness",
                "shot": "medium",
            },
            {
                "scene": "pressed into theater seat corner where seat meets wall, warm movie light cycling across face, one hand gripping armrest, other hand gripping seat cushion edge, exit sign red glow behind",
                "positive_extra": "seat corner, movie light cycling, gripping armrest, gripping cushion, exit sign red",
                "shot": "close_up",
            },
            {
                "scene": "close-up face illuminated by bright action movie scene, rapid light changes, eyes wide, lips parted, reflected movie imagery visible in eyes, plush seat headrest behind, flushed",
                "positive_extra": "bright movie light, rapid changes, wide eyes, parted lips, movie in eyes, headrest, flushed",
                "shot": "close_up",
                "caption": "On screen, credits began to roll. Neither noticed.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting in theater seat as house lights slowly come on, flat harsh light replacing movie magic, disheveled hair, straightening clothing, popcorn scattered on floor, credits still scrolling on screen",
                "positive_extra": "house lights on, harsh flat, disheveled, straightening clothes, popcorn floor, credits scrolling",
                "shot": "medium",
            },
            {
                "scene": "close-up of spilled popcorn on theater floor between seats, two ticket stubs among the kernels, house lights on, empty theater, screen dark, armrest still raised",
                "positive_extra": "spilled popcorn, floor, ticket stubs, house lights, empty theater, dark screen, armrest raised",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 20. speakeasy — Hidden bar, prohibition aesthetic
    # ------------------------------------------------------------------
    {
        "key": "speakeasy",
        "titles": ["Password", "Behind the Bookshelf", "Prohibition", "The Hidden Room"],
        "description": "Behind the unmarked door. Through the bookshelf. Down the stairs.",
        "time": "night",
        "location": "speakeasy hidden bar",
        "furniture": ["tufted leather booth", "antique bar top", "crystal decanter display", "candle-lit table", "velvet curtain alcove"],
        "lighting": ["warm candle glow", "amber Edison bulb pendants", "crystal glass refractions", "deep red velvet light absorption"],
        "atmosphere": ["secretive", "luxurious", "intimate", "amber"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "descending narrow staircase into speakeasy, one hand on brick wall, other holding dress hem, amber Edison bulbs lining steps, hidden bar visible below, warm candlelight, exposed brick and velvet",
                "positive_extra": "narrow stairs, brick wall, dress hem, Edison bulbs, hidden bar below, candlelight, velvet",
                "shot": "full_body",
                "caption": "The password changed every week. She always knew it.",
            },
            {
                "scene": "sitting at antique bar top, crystal cocktail glass in hand, elbow on polished wood, looking at bartender area, amber pendant lights above, crystal decanters lined behind bar, speakeasy decor",
                "positive_extra": "antique bar, crystal glass, elbow on wood, amber pendants, decanters, speakeasy decor",
                "shot": "medium",
            },
            {
                "scene": "leaning against velvet curtain at alcove entrance, one hand pulling curtain aside revealing hidden booth, beckoning expression, candlelight from inside alcove, dim main bar behind, mysterious",
                "positive_extra": "velvet curtain, alcove entrance, pulling aside, beckoning, candlelight inside, dim bar, mysterious",
                "shot": "medium_close",
                "dialogue": "This one's private. You need a different password.",
            },
        ],

        "tension": [
            {
                "scene": "seated in tufted leather booth in velvet alcove, curtain half-drawn giving privacy, candle on small table casting warm upward light on face, crystal glass catching and scattering light, legs crossed",
                "positive_extra": "tufted booth, velvet alcove, curtain half-drawn, candle uplight, crystal scatter, legs crossed",
                "shot": "medium",
            },
            {
                "scene": "standing against exposed brick wall of speakeasy, one arm above head, drink in other hand at side, amber light pooling on face, velvet curtain visible to side, worn brick texture against bare shoulder",
                "positive_extra": "brick wall, arm above head, drink at side, amber light, velvet curtain, brick on shoulder",
                "shot": "medium_close",
                "dialogue": "Nobody knows we're here. That's the whole point.",
            },
            {
                "scene": "pulling velvet curtain fully closed around alcove booth, fingers gripping heavy fabric, candlelight now only illumination, enclosed intimate space, crystal glass on table catching flame",
                "positive_extra": "pulling curtain closed, gripping velvet, candlelight only, enclosed, crystal catching flame",
                "shot": "close_up",
            },
            {
                "scene": "close-up face lit by single candle from below, warm amber tones, eyes half-lidded looking through lashes, lips wet from drink, tufted leather visible behind head, velvet dark around",
                "positive_extra": "candle from below, amber, half-lidded, through lashes, wet lips, tufted leather, velvet dark",
                "shot": "close_up",
                "caption": "Below the city, the rules were different.",
            },
        ],

        "aftermath": [
            {
                "scene": "walking up narrow speakeasy staircase away from camera, hand trailing along brick wall, looking back over shoulder, candlelight from below illuminating from behind, street level door visible above, amber glow",
                "positive_extra": "narrow stairs up, trailing hand, brick, looking back, candlelight behind, street door above, amber",
                "shot": "full_body",
            },
            {
                "scene": "close-up of empty crystal cocktail glass on antique bar top, lipstick mark on rim, single candle still burning beside it, crystal decanter reflected in glass, no one at bar, heavy velvet curtain behind",
                "positive_extra": "empty crystal glass, lipstick mark, candle burning, decanter reflection, empty bar, velvet curtain",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 21. comedy_club_green — Green room after the set
    # ------------------------------------------------------------------
    {
        "key": "comedy_club_green",
        "titles": ["Killing It", "Green Room", "After the Set", "Tough Crowd"],
        "description": "The set killed. The adrenaline hasn't faded. The green room door is thin.",
        "time": "night",
        "location": "comedy club green room",
        "furniture": ["worn couch", "vanity counter with mirror", "mini fridge", "folding chair", "brick wall"],
        "lighting": ["bare incandescent bulb overhead", "vanity mirror light strip", "warm tungsten", "neon comedy club sign through wall crack"],
        "atmosphere": ["post-adrenaline", "cramped", "buzzing"],
        "phase_structure": "all_phase1",

        "setup": [
            {
                "scene": "collapsed on worn green room couch, limbs spread, head back, laughing at ceiling, adrenaline high visible, water bottle in one hand, bare incandescent bulb above, peeling poster on brick wall",
                "positive_extra": "green room couch, limbs spread, head back, laughing, adrenaline, water bottle, bare bulb, brick wall",
                "shot": "medium",
                "caption": "Standing ovation. First one ever. The shaking hadn't stopped.",
            },
            {
                "scene": "standing at green room vanity mirror, staring at own reflection, wiping sweat from forehead with towel, bright mirror light strip, set list taped to mirror edge, small room behind in reflection",
                "positive_extra": "vanity mirror, staring at reflection, wiping sweat, mirror light strip, set list taped, small room",
                "shot": "medium_close",
            },
            {
                "scene": "sitting on folding chair, knees together, head in hands but smiling, someone entering through green room door, crowd noise flooding in then muffled as door closes, tungsten warm light",
                "positive_extra": "folding chair, head in hands, smiling, door opening, crowd noise, tungsten light",
                "shot": "medium",
                "dialogue": "I can't believe they laughed at the last bit. That wasn't even a joke.",
            },
        ],

        "tension": [
            {
                "scene": "pacing small green room, hands running through hair, wired energy, bouncing on toes, bare bulb swinging slightly from motion, brick walls close, frenetic joy still visible",
                "positive_extra": "pacing, hands in hair, wired, bouncing, swinging bulb, brick walls close, frenetic",
                "shot": "full_body",
                "dialogue": "I'm still buzzing. I can't sit still.",
            },
            {
                "scene": "standing pressed against brick wall of green room, one hand flat on rough brick, looking at someone across the tiny room, chest still heaving from adrenaline, bare bulb light casting sharp shadows",
                "positive_extra": "brick wall, hand flat, looking across room, heaving, bare bulb, sharp shadows",
                "shot": "medium_close",
            },
            {
                "scene": "sitting on vanity counter, legs dangling, mirror bulbs framing from behind creating halo, leaning forward gripping counter edge, post-show energy redirecting, small room feeling smaller",
                "positive_extra": "vanity counter, legs dangling, mirror bulbs halo, leaning forward, gripping edge, small room",
                "shot": "medium",
            },
            {
                "scene": "close-up of face against brick wall texture, rough brick visible beside cheek, eyes squeezed shut, bare bulb light from above, sweat on temple, post-adrenaline flush, lips pressed together",
                "positive_extra": "face on brick, rough texture, eyes shut, bare bulb above, sweat, flush, lips pressed",
                "shot": "close_up",
                "caption": "The next comic's muffled set leaked through the wall. Neither heard it.",
            },
        ],

        "aftermath": [
            {
                "scene": "lying on green room couch, one arm over eyes, other arm hanging off side, completely spent, bare bulb still on, water bottle knocked over on floor, set list crumpled nearby",
                "positive_extra": "couch, arm over eyes, arm hanging, spent, bare bulb, water bottle floor, crumpled set list",
                "shot": "full_body",
            },
            {
                "scene": "close-up of crumpled set list paper on green room floor, handwritten jokes visible, water stain across it, green room door visible ajar in background, hallway light stripe on floor",
                "positive_extra": "crumpled set list, handwritten, water stain, door ajar, hallway light stripe, floor",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 22. food_truck_lot — Late night, street food, steam
    # ------------------------------------------------------------------
    {
        "key": "food_truck_lot",
        "titles": ["Late Night Eats", "Street Side", "Last Order", "Food Coma"],
        "description": "2am food truck lot. Steam and street lights. Everyone else is drunk.",
        "time": "night",
        "location": "food truck lot at night",
        "furniture": ["food truck counter window", "plastic folding table", "string light canopy", "concrete barrier seating", "order pickup shelf"],
        "lighting": ["food truck interior warm light", "string light canopy", "street lamp orange", "steam diffused glow"],
        "atmosphere": ["street food", "late night", "steamy", "urban"],
        "phase_structure": "mixed",

        "setup": [
            {
                "scene": "standing at food truck order window, leaning on counter with elbows, menu board lit up above, steam pouring out of truck window around face, string lights overhead, night street behind",
                "positive_extra": "food truck window, elbows on counter, menu board, steam pouring, string lights, night street",
                "shot": "medium",
                "caption": "2:17 AM. Nothing good happens after midnight. Except tacos.",
            },
            {
                "scene": "sitting on concrete barrier in food truck lot, paper food tray on lap, legs swinging, eating with hands, steam rising from food, orange street lamp behind, other trucks dark and closed",
                "positive_extra": "concrete barrier, food tray, legs swinging, eating, steam from food, street lamp, dark trucks",
                "shot": "full_body",
            },
            {
                "scene": "turning from food truck window holding two foil-wrapped items, offering one toward camera, sauce on chin, laughing, warm truck light behind creating glow outline, string lights above, night urban backdrop",
                "positive_extra": "holding food, offering, sauce on chin, laughing, truck glow outline, string lights, night urban",
                "shot": "medium_close",
                "dialogue": "You look like you need this more than I do.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on plastic folding table instead of chair, feet on seat, food finished, licking sauce from thumb, looking directly at camera, string lights reflected in eyes, food truck steam behind, late night quiet",
                "positive_extra": "on table, feet on seat, licking thumb, direct look, string light reflections, steam, late night",
                "shot": "medium",
            },
            {
                "scene": "leaning against side of closed food truck, metal wall cool against back, head tilted, one knee bent foot on truck, string light shadows on face, empty lot, steam dissipating",
                "positive_extra": "against food truck, metal wall, head tilted, knee bent, string light shadows, empty lot, steam",
                "shot": "full_body",
                "dialogue": "My apartment's three blocks that way. If you're still hungry.",
            },
            {
                "scene": "standing between two food trucks in narrow gap, tight space, string lights above creating corridor of light, steam from truck vents mixing overhead, urban alley feel, looking at camera from shadows",
                "positive_extra": "between trucks, narrow gap, string lights corridor, steam mixing, urban alley, shadow look",
                "shot": "medium_close",
            },
            {
                "scene": "close-up of face, street lamp orange on one side, food truck warm white on other, split lighting, sauce smudge near lip, night wind moving hair, pupils wide, urban night glow behind",
                "positive_extra": "split lighting, orange and white, sauce near lip, wind in hair, wide pupils, urban night",
                "shot": "close_up",
                "caption": "Three blocks felt like a long way. They didn't make it.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on curb beside food truck lot, knees up, wrapper balled in hand, looking at phone screen showing 3am, satisfied tired expression, food truck lights shutting off one by one",
                "positive_extra": "curb, knees up, wrapper, phone showing 3am, tired satisfied, truck lights shutting off",
                "shot": "medium",
            },
            {
                "scene": "close-up of crumpled food wrapper on concrete beside knocked-over hot sauce bottle, string lights going dark, no people, steam from last truck vent slowly dying, quiet lot",
                "positive_extra": "crumpled wrapper, hot sauce bottle, string lights dark, no people, dying steam, quiet",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 23. mall_fitting_room — Shopping trip escalation
    # ------------------------------------------------------------------
    {
        "key": "mall_fitting_room",
        "titles": ["Fitting Room", "Try This On", "Mirror Mirror", "Changing"],
        "description": "She asked for a second opinion. The fitting room door has a lock.",
        "time": "afternoon",
        "location": "clothing store fitting room",
        "furniture": ["full-length mirror", "wall hooks", "small bench", "curtain door", "pile of try-on clothes"],
        "lighting": ["overhead fitting room light flattering warm", "mirror reflection doubled light", "gap light under curtain", "store light through curtain crack"],
        "atmosphere": ["private", "warm", "mirrored"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing in fitting room looking at full-length mirror, holding dress on hanger against body, head tilted assessing, pile of clothes on small bench, curtain closed behind, warm overhead light",
                "positive_extra": "fitting room, mirror, dress on hanger, assessing, clothes pile, bench, curtain, warm light",
                "shot": "full_body",
                "caption": "Third outfit. None of them were right. Or maybe she just wanted to keep trying.",
            },
            {
                "scene": "peeking head out from fitting room curtain, holding curtain close to body, only face and bare shoulder visible, playful expression, store visible behind blurred, hangers visible inside",
                "positive_extra": "peeking from curtain, bare shoulder, playful, store blurred, hangers inside",
                "shot": "medium_close",
                "dialogue": "I need a second opinion. Get in here.",
            },
            {
                "scene": "standing in fitting room with back to mirror, looking over shoulder at reflection, new outfit half-on, zipper undone showing back, warm light, small space with clothes piled on bench and hooks",
                "positive_extra": "back to mirror, over shoulder, outfit half-on, zipper undone, back visible, warm light, small space",
                "shot": "medium",
            },
        ],

        "tension": [
            {
                "scene": "reaching behind to pull fitting room curtain shut completely, other hand on hip, direct eye contact with camera, pile of discarded outfits growing on bench, mirror doubling the image, warm enclosed light",
                "positive_extra": "pulling curtain shut, hand on hip, eye contact, discarded clothes, mirror doubling, enclosed",
                "shot": "medium",
            },
            {
                "scene": "pressed against full-length mirror, hands flat on glass behind, head tilted to side, reflection visible overlapping with real body, warm light from above, tiny fitting room space, hooks with hangers",
                "positive_extra": "against mirror, hands on glass, tilted head, reflection overlap, warm light, tiny space, hooks",
                "shot": "medium_close",
                "dialogue": "Lock the curtain.",
            },
            {
                "scene": "sitting on small fitting room bench, surrounded by discarded clothes, looking up at standing perspective, knees together, hands on bench edge, mirror beside doubling image, intimate tiny space",
                "positive_extra": "bench, discarded clothes, looking up, knees together, mirror doubling, intimate, tiny space",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face in mirror reflection, warm overhead light, eyes half-closed, curtain fabric visible at edge of mirror, reflection slightly fogged, lips parted, flushed",
                "positive_extra": "mirror reflection, warm light, half-closed eyes, curtain edge, fogged mirror, parted lips, flushed",
                "shot": "close_up",
                "caption": "The store associate knocked twice. No answer.",
            },
        ],

        "aftermath": [
            {
                "scene": "standing in fitting room pulling original clothes back on hurriedly, mirror showing rushed dressing, clothes hangers scattered, bench covered in try-on pile, slightly panicked amused expression",
                "positive_extra": "pulling clothes on, hurried, mirror, scattered hangers, try-on pile, panicked amused",
                "shot": "medium",
            },
            {
                "scene": "close-up of fitting room curtain from store side, pair of shoes visible underneath curtain gap, store announcement speaker visible on ceiling, shopping bag on floor outside curtain",
                "positive_extra": "curtain from outside, shoes under gap, store speaker, shopping bag, floor",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 24. rooftop_garden — Hidden urban oasis
    # ------------------------------------------------------------------
    {
        "key": "rooftop_garden",
        "titles": ["Above It All", "Roof Access", "Urban Garden", "Sky Garden"],
        "description": "Rooftop garden nobody knows about. The city doesn't look up.",
        "time": "evening",
        "location": "rooftop garden city",
        "furniture": ["wooden planter box bench", "hanging vine trellis", "concrete ledge with cushion", "small fountain", "potting table"],
        "lighting": ["golden hour sunset", "city glow from below", "string lights in vines", "warm twilight sky"],
        "atmosphere": ["hidden", "lush", "elevated", "twilight"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "climbing through rooftop access door onto garden, one foot still on ladder, discovering the green space, city skyline behind, golden sunset light, planter boxes overflowing with vines, string lights woven through trellis",
                "positive_extra": "rooftop door, ladder, discovering garden, city skyline, golden sunset, planter boxes, vines, string lights",
                "shot": "full_body",
                "caption": "She'd lived in the building for a year. Never tried the roof access.",
            },
            {
                "scene": "walking between planter boxes on rooftop, trailing hand through hanging vines, golden light on face, city buildings visible over garden edge, small fountain trickling nearby, lush unexpected green space",
                "positive_extra": "between planters, trailing hand, vines, golden light, city buildings, fountain, lush green",
                "shot": "medium",
            },
            {
                "scene": "turning at rooftop edge, city panorama behind, surprised to see another person, one hand still touching vine leaf, sunset backlighting hair, wind moving plants, elevated perspective",
                "positive_extra": "rooftop edge, city behind, surprised, touching vine, sunset backlight, wind, elevated",
                "shot": "medium_close",
                "dialogue": "I thought I was the only one who knew about this place.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on concrete ledge cushion at rooftop edge, city lights starting to appear below as sky darkens, legs stretched along ledge, leaning back on hands, golden and blue twilight, vines overhead",
                "positive_extra": "ledge cushion, city lights below, sky darkening, legs stretched, leaning back, twilight, vines",
                "shot": "full_body",
                "dialogue": "Nobody can see us up here. We're above everything.",
            },
            {
                "scene": "standing under hanging vine trellis, string lights woven through creating warm canopy, face dappled by leaf shadows and warm light, reaching up to touch vine, city glow behind through gaps",
                "positive_extra": "vine trellis, string lights canopy, dappled face, reaching up, city glow, through gaps",
                "shot": "medium_close",
            },
            {
                "scene": "pressed against planter box edge, wood against lower back, hands gripping rough planter rim behind, head back, city skyline visible above and behind, string lights and vines framing, twilight purple sky",
                "positive_extra": "planter box edge, wood against back, gripping rim, head back, skyline, string lights, vines, purple sky",
                "shot": "medium",
            },
            {
                "scene": "close-up face with city lights bokeh behind, wind moving hair across eyes, parted lips, string light warm dot reflected in each eye, last twilight blue on one side warm light on other",
                "positive_extra": "city lights bokeh, wind in hair, parted lips, string light in eyes, twilight blue, warm light split",
                "shot": "close_up",
                "caption": "Ten stories up, the world was nothing but wind and light.",
            },
        ],

        "aftermath": [
            {
                "scene": "lying on rooftop cushion, looking straight up at stars appearing in darkening sky, city glow at edges of vision, vines silhouetted overhead, string lights tiny suns, completely still, peaceful",
                "positive_extra": "lying back, stars appearing, dark sky, city glow edges, vine silhouettes, string lights, peaceful",
                "shot": "full_body",
            },
            {
                "scene": "close-up of rooftop access door from inside stairwell, door propped open with small potted plant, city night sky visible through gap, vine leaf caught in door hinge, stairwell light below",
                "positive_extra": "access door, stairwell, propped open, potted plant, night sky, vine leaf, stairwell light",
                "shot": "close_up",
            },
        ],
    },

    # ==================================================================
    # TRANSPORT (8)
    # ==================================================================

    # ------------------------------------------------------------------
    # 25. car_backseat — Parked somewhere dark and quiet
    # ------------------------------------------------------------------
    {
        "key": "car_backseat",
        "titles": ["Parked", "Backseat", "Steamed", "Overlooking"],
        "description": "Parked at the overlook. Engine off. Windows fogging.",
        "time": "night",
        "location": "car backseat at overlook",
        "furniture": ["leather backseat", "fogged window", "dashboard glow", "center console", "headrest"],
        "lighting": ["distant city lights through fog", "dashboard instrument glow", "dome light off", "phone screen occasional"],
        "atmosphere": ["enclosed", "fogged", "intimate", "parked"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting in passenger seat, feet up on dashboard, looking out at city lights spread below overlook, car engine off, windshield starting to fog at edges, dashboard glow on legs, seat reclined slightly",
                "positive_extra": "passenger seat, feet on dash, city lights, overlook, fog edges, dashboard glow, reclined",
                "shot": "medium",
                "caption": "He said he knew a spot. He wasn't wrong.",
            },
            {
                "scene": "leaning between front seats reaching for something in backseat, body stretched across center console, looking back at camera, hair falling forward, city lights through rear window, dark car interior",
                "positive_extra": "between seats, reaching back, stretched, center console, looking back, hair forward, city lights rear window",
                "shot": "medium_close",
            },
            {
                "scene": "climbing into backseat over center console, one knee on back seat, hand on headrest, amused determined expression, dashboard light catching face from below, fogged windows all around",
                "positive_extra": "climbing to backseat, knee on seat, hand on headrest, amused determined, dashboard light, fogged windows",
                "shot": "medium",
                "dialogue": "More room back here.",
            },
        ],

        "tension": [
            {
                "scene": "sitting in backseat, back against door, legs extended across seat, fogged windows glowing with diffused city light, intimate enclosed space, hands on seat leather, looking across at other door",
                "positive_extra": "backseat, against door, legs across, fogged windows, diffused city light, enclosed, leather",
                "shot": "full_body",
            },
            {
                "scene": "pressed against backseat door, hand reaching up to draw in fogged window glass, line visible in condensation, city lights blurred through fog, confined space, warm breath visible",
                "positive_extra": "against door, drawing in fog, condensation line, blurred city, confined, visible breath",
                "shot": "medium_close",
                "dialogue": "Windows are completely fogged now.",
            },
            {
                "scene": "hand pressed flat against fogged backseat window from inside, fingers splayed, condensation running around palm, city lights distorted through glass and fog, night outside",
                "positive_extra": "hand on fogged window, fingers splayed, condensation running, distorted city lights, night",
                "shot": "close_up",
            },
            {
                "scene": "close-up of face lit only by distant city glow through fogged glass, soft diffused light, eyes half-closed, headrest beside face, leather seat texture visible, completely fogged windows enclosing",
                "positive_extra": "city glow through fog, diffused, half-closed eyes, headrest, leather texture, fogged enclosure",
                "shot": "close_up",
                "caption": "The windows fogged until the city disappeared completely.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting in backseat, one leg extended one tucked, head leaning against fogged window, drawing idle pattern in condensation, city lights slowly becoming visible as fog clears, relaxed tired",
                "positive_extra": "backseat, against fogged window, drawing in condensation, city lights clearing, relaxed, tired",
                "shot": "medium",
            },
            {
                "scene": "close-up of handprint smeared through fogged windshield from inside, city lights panorama now visible through cleared spot, car keys dangling from ignition, no people visible, dawn starting at horizon edge",
                "positive_extra": "handprint, fogged windshield, cleared spot, city panorama, keys in ignition, dawn edge",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 26. bus_last_route — Empty late night bus
    # ------------------------------------------------------------------
    {
        "key": "bus_last_route",
        "titles": ["Last Bus", "Night Route", "Terminal", "Back of the Bus"],
        "description": "Last bus of the night. Empty except for two.",
        "time": "night",
        "location": "city bus at night",
        "furniture": ["plastic bus seats", "overhead grab rail", "rear bench seat", "window ledge", "driver partition"],
        "lighting": ["harsh interior fluorescent", "passing streetlights strobing", "destination sign glow", "city neon through windows"],
        "atmosphere": ["rumbling", "isolated", "moving", "late night"],
        "phase_structure": "all_phase1",

        "setup": [
            {
                "scene": "sitting in back of empty city bus, head leaning against vibrating window, city lights passing outside creating light streaks, fluorescent bus interior, empty seats stretching forward, overhead rails swaying",
                "positive_extra": "back of bus, head on window, vibrating, city light streaks, fluorescent, empty seats, rails swaying",
                "shot": "medium",
                "caption": "The 11:47. Last route of the night.",
            },
            {
                "scene": "standing in bus aisle holding overhead rail, body swaying with bus movement, looking toward back of bus, streetlights strobing through windows creating rhythmic shadow and light, empty bus",
                "positive_extra": "bus aisle, overhead rail, swaying, looking back, streetlight strobe, shadow light rhythm, empty",
                "shot": "full_body",
            },
            {
                "scene": "looking up from bus seat at someone approaching down aisle, hand on seat back in front, curious expression, fluorescent light above, city passing outside windows, late night exhaustion in eyes",
                "positive_extra": "looking up, approaching, hand on seat back, curious, fluorescent, city passing, tired eyes",
                "shot": "medium_close",
                "dialogue": "Whole bus to yourself and you pick here?",
            },
        ],

        "tension": [
            {
                "scene": "sitting on wide rear bench seat of bus, legs crossed, hands gripping seat edge, looking sideways at adjacent position, bus vibrating and swaying, streetlights passing rhythmically, private in back",
                "positive_extra": "rear bench, legs crossed, gripping edge, looking sideways, vibrating, streetlights rhythm, private",
                "shot": "medium",
                "dialogue": "Driver can't see past the partition.",
            },
            {
                "scene": "standing holding overhead rail with both hands, body pressed against rail as bus turns, momentum pushing her, streetlight creating brief bright flash through window, empty bus rocking",
                "positive_extra": "overhead rail, both hands, pressed against rail, bus turning, streetlight flash, rocking",
                "shot": "full_body",
            },
            {
                "scene": "pressed against bus window, cold glass against shoulder, bus vibration visible, city moving past outside, reflection in glass showing two figures, interior fluorescent, grip on seat ahead",
                "positive_extra": "against bus window, cold glass, vibration, city passing, reflection two figures, fluorescent, gripping seat",
                "shot": "medium_close",
            },
            {
                "scene": "close-up of face with passing streetlights creating rhythmic illumination, light-dark-light-dark, eyes reflecting city, bus vibration in soft focus, lips parted, window glass cold and close",
                "positive_extra": "streetlight rhythm, light dark cycle, eyes reflecting city, vibration blur, parted lips, cold glass",
                "shot": "close_up",
                "caption": "Seven more stops. Neither planned on getting off.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on rear bus bench, head on companion's shoulder perspective, watching city pass through window, bus nearly at terminal, lights getting brighter, relaxed slumped posture, streetlights slowing",
                "positive_extra": "rear bench, head on shoulder, city through window, terminal approaching, lights brighter, slumped, slowing",
                "shot": "medium",
            },
            {
                "scene": "close-up of bus STOP REQUESTED button lit up red, overhead grab rail visible, empty seats stretching ahead, bus slowing, fluorescent light, no people in frame, terminal sign visible through windshield",
                "positive_extra": "stop button red, grab rail, empty seats, slowing, fluorescent, terminal sign",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 27. train_sleeper — Overnight compartment, rhythmic motion
    # ------------------------------------------------------------------
    {
        "key": "train_sleeper",
        "titles": ["Sleeper Car", "Overnight", "Compartment", "Tracks"],
        "description": "Overnight sleeper compartment. The tracks rhythmic. The door locked from inside.",
        "time": "night",
        "location": "train sleeper compartment",
        "furniture": ["narrow fold-down bed", "small window with curtain", "overhead luggage shelf", "tiny sink and mirror", "fold-out table"],
        "lighting": ["blue reading light above bunk", "passing station lights sweeping through window", "warm compartment overhead", "corridor light under door"],
        "atmosphere": ["rhythmic motion", "confined", "nocturnal", "rocking"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on narrow train bunk bed, legs tucked under, looking out small window at dark countryside passing, blue reading light above, compartment walls close, rhythmic train motion, small curtain pulled aside",
                "positive_extra": "train bunk, legs tucked, window, dark countryside, blue reading light, close walls, rhythmic motion, curtain",
                "shot": "medium",
                "caption": "Eight hours to the coast. The compartment was smaller than advertised.",
            },
            {
                "scene": "standing in tiny sleeper compartment, barely room to turn, looking in small sink mirror, train rocking visible in unsteady posture, overhead luggage shelf, corridor light seeping under locked door",
                "positive_extra": "tiny compartment, sink mirror, train rocking, unsteady, luggage shelf, corridor light, locked door",
                "shot": "medium_close",
            },
            {
                "scene": "opening compartment door revealing corridor, surprised, robe pulled closed with one hand, passing station lights sweeping through corridor windows creating strobe effect, train rocking",
                "positive_extra": "compartment door, corridor, surprised, robe, station lights sweeping, strobe, train rocking",
                "shot": "medium",
                "dialogue": "Wrong compartment. This one's... wait. This is mine.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on fold-down bed, knees drawn up in narrow space, back against compartment wall, robe loosened, blue reading light casting shadows, window showing dark landscape rushing past, train swaying",
                "positive_extra": "fold-down bed, knees up, narrow, robe loose, blue reading light, dark landscape rushing, swaying",
                "shot": "medium",
                "dialogue": "We could pretend this is a bigger compartment. Or not.",
            },
            {
                "scene": "pressed against compartment wall, one hand on overhead luggage rail for balance as train rocks, other hand on door lock checking it, confined space, warm light, rhythmic clatter of tracks",
                "positive_extra": "against wall, luggage rail, train rocking, hand on lock, confined, warm light, track rhythm",
                "shot": "medium_close",
            },
            {
                "scene": "lying on narrow bunk, body filling the small bed completely, one hand gripping bed rail, train vibration visible, blue reading light above, passing lights intermittently sweeping through window",
                "positive_extra": "narrow bunk, filling bed, gripping rail, vibration, blue light, passing lights sweep, window",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face on thin train pillow, blue reading light above, eyes reflecting passing landscape lights, train rocking lulling, lips parted, rhythmic motion in soft blur at edges",
                "positive_extra": "face on pillow, blue light, eyes reflecting, passing landscape, rocking, parted lips, motion blur",
                "shot": "close_up",
                "caption": "The rhythmic tracks counted down the miles. Neither was sleeping.",
            },
        ],

        "aftermath": [
            {
                "scene": "curled on narrow bunk wrapped in thin blanket, looking out window at dawn breaking over passing hills, train still rocking, compartment messy, blue light off, warm golden dawn light entering",
                "positive_extra": "curled on bunk, blanket, dawn over hills, train rocking, messy compartment, golden dawn light",
                "shot": "medium",
            },
            {
                "scene": "close-up of small train window, condensation on glass, finger-drawn heart in fog, dawn landscape rushing past outside, compartment reflected faintly in glass, empty bunk behind",
                "positive_extra": "train window, condensation, finger heart in fog, dawn rushing, compartment reflection, empty bunk",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 28. parking_garage — Concrete, echoes, dim industrial
    # ------------------------------------------------------------------
    {
        "key": "parking_garage",
        "titles": ["Level 5", "Underground", "Concrete", "After Dark"],
        "description": "Top level of the parking garage. No cars. No cameras. Just concrete and stars.",
        "time": "night",
        "location": "parking garage rooftop level",
        "furniture": ["concrete pillar", "parking barrier", "stairwell door", "oil-stained floor", "ventilation grate"],
        "lighting": ["orange sodium lamp buzzing", "distant city glow", "stairwell light through door crack", "car headlight sweep from below"],
        "atmosphere": ["concrete", "echoing", "industrial", "exposed"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "walking across empty top level of parking garage, no cars anywhere, concrete stretching to edges, city skyline visible over low wall, orange sodium lamp buzzing above, shoes echoing on concrete, wind blowing hair",
                "positive_extra": "empty parking level, concrete, city skyline, sodium lamp, echoing, wind, no cars",
                "shot": "full_body",
                "caption": "Top floor. She always parked up here. Never saw another car.",
            },
            {
                "scene": "leaning against concrete pillar in parking garage, arms behind back against rough concrete, orange sodium light creating harsh shadows, empty oil-stained floor stretching behind, night sky visible at edges",
                "positive_extra": "concrete pillar, arms behind, rough concrete, sodium shadows, oil-stained floor, night sky edges",
                "shot": "medium",
            },
            {
                "scene": "turning at stairwell door entrance to parking garage top level, hand on metal door, looking back at someone following, orange light from stairwell behind, dark open garage ahead, concrete ceiling low",
                "positive_extra": "stairwell door, hand on door, looking back, orange stairwell light, dark garage, low ceiling",
                "shot": "medium_close",
                "dialogue": "Nobody comes up this far. I checked.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on concrete parking barrier at garage edge, legs dangling over ledge, city lights spread below, wind moving hair, orange sodium glow mixing with city ambiance, bold relaxed posture, night sky above",
                "positive_extra": "parking barrier edge, legs dangling, city below, wind, sodium and city light mix, bold, night sky",
                "shot": "full_body",
                "dialogue": "Best view in the city and nobody knows it.",
            },
            {
                "scene": "pressed against concrete pillar, rough texture against skin, sodium lamp creating orange hot spot and deep shadow, one hand flat on pillar surface, face half in light half in dark, garage empty around",
                "positive_extra": "concrete pillar, rough on skin, sodium hot spot, deep shadow, hand on pillar, half lit, empty garage",
                "shot": "medium_close",
            },
            {
                "scene": "knelt on oil-stained concrete, hands flat on ground, ventilation grate visible beside, orange sodium lamp overhead, shadows long and dramatic, concrete pillar beside, industrial texture everywhere",
                "positive_extra": "oil-stained concrete, hands flat, ventilation grate, sodium lamp overhead, long shadows, pillar, industrial",
                "shot": "medium",
            },
            {
                "scene": "close-up of face against rough concrete pillar, textured surface visible beside cheek, sodium light harsh and warm, eyes squeezed shut, wind moving hair across face, city glow behind in distance",
                "positive_extra": "face on concrete, rough texture, sodium harsh, eyes shut, wind hair, city glow distance",
                "shot": "close_up",
                "caption": "An echo carried across the concrete. Then silence.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting against concrete pillar on garage floor, knees up, head tipped back against rough pillar, looking up at stars through open-air top level, sodium lamp buzzing, completely still and satisfied",
                "positive_extra": "against pillar, floor, knees up, head back, stars, open-air, sodium buzzing, still, satisfied",
                "shot": "medium",
            },
            {
                "scene": "close-up of car headlights sweeping across empty parking garage level from ramp below, light catching oil stains and a single dropped earring on concrete, no people visible, night",
                "positive_extra": "headlight sweep, empty level, oil stains, dropped earring, concrete, no people, night",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 29. road_trip_motel — Middle of nowhere, neon vacancy sign
    # ------------------------------------------------------------------
    {
        "key": "road_trip_motel",
        "titles": ["Vacancy", "Mile 380", "One Night", "No-Tell Motel"],
        "description": "Middle of nowhere. Neon VACANCY sign. One room left.",
        "time": "night",
        "location": "roadside motel room",
        "furniture": ["queen bed with thin bedspread", "small TV on dresser", "bathroom door ajar", "window air conditioner", "bedside clock radio"],
        "lighting": ["neon VACANCY sign through curtain red", "flickering bedside lamp", "TV static glow", "bathroom light through crack"],
        "atmosphere": ["isolated", "neon-lit", "retro", "nowhere"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing in motel room doorway, room key in hand, looking at sparse room, queen bed with thin floral bedspread, neon VACANCY sign visible through curtain casting red glow, road trip bags on floor, tired from driving",
                "positive_extra": "motel doorway, room key, sparse room, queen bed, neon VACANCY red, bags on floor, tired",
                "shot": "full_body",
                "caption": "Six hours of highway. One room left. One bed.",
            },
            {
                "scene": "sitting on edge of motel bed, bouncing testing the mattress, amused skeptical expression, thin bedspread, small TV on dresser, neon light painting wall red through thin curtains, window AC unit humming",
                "positive_extra": "motel bed edge, bouncing, skeptical amused, thin bedspread, TV dresser, neon red wall, AC humming",
                "shot": "medium",
            },
            {
                "scene": "leaning against motel room bathroom doorframe, towel in hand, steam escaping behind, looking at someone on bed, cocked eyebrow, neon red light and bathroom white light competing, hair damp",
                "positive_extra": "bathroom doorframe, towel, steam, looking at bed, eyebrow, neon red vs bathroom white, damp hair",
                "shot": "medium_close",
                "dialogue": "You said separate beds. This is not separate beds.",
            },
        ],

        "tension": [
            {
                "scene": "lying on motel bed on stomach, chin on folded arms, feet kicked up behind, TV playing static in background, neon VACANCY light pulsing red through curtain, looking directly at camera with lazy intensity",
                "positive_extra": "on stomach, chin on arms, feet up, TV static, neon red pulse, looking at camera, lazy intensity",
                "shot": "medium",
                "dialogue": "Long drive tomorrow too. Should probably sleep.",
            },
            {
                "scene": "standing at motel window pulling curtain aside, neon VACANCY sign glowing right outside, red light flooding in, dark empty highway visible beyond, one hand on cold glass, silhouette from inside",
                "positive_extra": "motel window, pulling curtain, neon VACANCY close, red flood, dark highway, hand on glass, silhouette",
                "shot": "full_body",
            },
            {
                "scene": "sitting against motel headboard, legs extended on bed, thin bedspread bunched at waist, bedside lamp flickering creating strobe, neon red constant from window, looking at camera from pillow pile",
                "positive_extra": "against headboard, legs on bed, bunched bedspread, flickering lamp, neon red, pillow pile",
                "shot": "medium_close",
            },
            {
                "scene": "close-up of face lit by alternating neon red pulse and flickering warm lamp, motel pillow behind head, eyes heavy-lidded, watching, flushed, thin motel wall audibly vibrating from highway truck passing",
                "positive_extra": "neon red pulse, flickering lamp, motel pillow, heavy-lidded, watching, flushed, wall vibrating",
                "shot": "close_up",
                "caption": "The VACANCY sign flickered. Then stayed on.",
            },
        ],

        "aftermath": [
            {
                "scene": "lying in motel bed, sheet pulled up, looking at ceiling, clock radio showing 2:47am in red digits, neon glow softened through curtain, AC humming, room quiet, road trip bag still packed at door",
                "positive_extra": "motel bed, sheet, ceiling, clock radio 2:47, neon soft, AC humming, bag packed at door",
                "shot": "medium",
            },
            {
                "scene": "close-up of motel room key on bedside table, old-fashioned key with room number tag, clock radio red digits beside, curtain edge glowing neon, no people visible, untouched TV remote",
                "positive_extra": "room key, number tag, clock radio, curtain neon edge, no people, TV remote untouched",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 30. subway_platform — Missed the last train, empty platform
    # ------------------------------------------------------------------
    {
        "key": "subway_platform",
        "titles": ["Last Train Gone", "Platform", "Underground", "Missed Connection"],
        "description": "Last train left four minutes ago. Platform empty. Next one in five hours.",
        "time": "night",
        "location": "empty subway platform",
        "furniture": ["tiled platform bench", "track edge", "tunnel entrance", "information board", "support column"],
        "lighting": ["harsh overhead tube lights", "tunnel darkness beyond platform end", "LED departure board glow", "emergency exit green sign"],
        "atmosphere": ["underground", "echoing", "abandoned feeling", "tiled"],
        "phase_structure": "reversed",

        "setup": [
            {
                "scene": "sitting on tiled subway platform bench, looking at departure board showing SERVICE ENDED, head dropped back in frustration, empty platform stretching in both directions, tunnel darkness at ends, harsh overhead lights",
                "positive_extra": "platform bench, departure board SERVICE ENDED, frustrated, empty platform, tunnel dark, harsh lights",
                "shot": "medium",
                "caption": "11:54. The last train left at 11:50.",
            },
            {
                "scene": "standing at platform edge looking down into dark tunnel, no train coming, tile and concrete, overhead lights creating bright pool, darkness beyond platform ends, hands in pockets, alone",
                "positive_extra": "platform edge, dark tunnel, no train, tile concrete, bright pool light, darkness beyond, alone",
                "shot": "full_body",
            },
            {
                "scene": "turning on platform hearing footsteps echo, another person at far end of platform, tile walls amplifying sound, fluorescent lights buzzing, departure board blank, both stranded expression",
                "positive_extra": "turning on platform, hearing footsteps, echo, tile walls, fluorescent buzzing, blank board, stranded",
                "shot": "medium_close",
                "dialogue": "You missed it too?",
            },
        ],

        "tension": [
            {
                "scene": "sitting on platform bench together, legs extended, backs against tile wall, looking at each other, empty platform, tunnel entrances dark on either side, harsh overhead light creating pool around bench",
                "positive_extra": "bench together, legs out, tile wall, looking at each other, empty, tunnel dark, light pool around bench",
                "shot": "full_body",
                "dialogue": "First train's at 5am. That's five hours.",
            },
            {
                "scene": "standing behind platform support column, peeking around edge playfully, tile and concrete, fluorescent light on one side shadow on other, train tracks visible but empty, echoing space",
                "positive_extra": "behind column, peeking around, tile concrete, light one side shadow other, empty tracks, echoing",
                "shot": "medium_close",
            },
            {
                "scene": "pressed against cold tile wall of platform, smooth tiles against back, arms at sides palms flat on tile, overhead light directly above creating sharp downward shadows, empty platform, tunnel entrance dark behind",
                "positive_extra": "cold tile wall, smooth, palms flat, overhead light, sharp shadows, empty, tunnel dark",
                "shot": "medium",
            },
            {
                "scene": "close-up of face lit by harsh fluorescent from above, tile wall visible beside head, eyes wide, lips parted, echo suggested by composition, underground atmosphere, no escape until morning",
                "positive_extra": "fluorescent from above, tile wall, wide eyes, parted lips, echo, underground, no escape",
                "shot": "close_up",
                "caption": "Underground, time moved differently.",
            },
        ],

        "aftermath": [
            {
                "scene": "leaning against each other on platform bench sleeping, jackets as blankets, harsh lights still on, clock on wall showing 4:48am, first commuters visible at distant platform end, tile floor, peaceful",
                "positive_extra": "platform bench, sleeping against each other, jackets, harsh lights, clock 4:48, commuters distant, peaceful",
                "shot": "medium",
            },
            {
                "scene": "close-up of departure board now showing first morning train arrival 5:02am, platform light reflecting on tile, rumble vibration from approaching train visible in puddle on platform, no people in frame",
                "positive_extra": "departure board, 5:02am, tile reflection, rumble vibration, puddle vibrating, no people",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 31. ferry_night — Night crossing, ocean spray
    # ------------------------------------------------------------------
    {
        "key": "ferry_night",
        "titles": ["Night Crossing", "Starboard", "Salt Air", "Between Shores"],
        "description": "Night ferry. The deck is empty. Salt air and engine hum.",
        "time": "night",
        "location": "ferry deck at night",
        "furniture": ["deck railing", "bench bolted to deck", "lifeboat davit", "cabin door", "coiled rope"],
        "lighting": ["deck sodium lamp", "moonlight on ocean", "cabin window warm glow", "navigation light red and green"],
        "atmosphere": ["salt air", "engine hum", "isolated", "oceanic"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing at ferry deck railing, looking out at dark ocean, hair blowing in wind, salt spray catching deck sodium light, moon reflecting on water, engine vibration through deck, completely alone on outer deck",
                "positive_extra": "deck railing, dark ocean, wind hair, salt spray, sodium light, moon on water, engine vibration, alone",
                "shot": "full_body",
                "caption": "The night crossing. Everyone else stayed inside.",
            },
            {
                "scene": "sitting on bolted deck bench, knees pulled up, coat wrapped tight, salt air blowing, cabin windows behind glowing warm, deck lamp above, ocean darkness beyond railing, ferry rocking gently",
                "positive_extra": "deck bench, knees up, coat tight, salt air, cabin glow behind, deck lamp, ocean dark, rocking",
                "shot": "medium",
            },
            {
                "scene": "turning from railing surprised, coat collar pulled up against wind, ocean spray on face, navigation lights red and green on either side behind, deck wet from spray, someone approaching from cabin door",
                "positive_extra": "turning from railing, surprised, coat collar, ocean spray face, nav lights red green, wet deck, approaching",
                "shot": "medium_close",
                "dialogue": "You can't sleep either?",
            },
        ],

        "tension": [
            {
                "scene": "standing together at deck railing, close for warmth, ocean stretching dark to horizon, moon creating silver path on water, wind whipping hair and coat, deck lamp creating warm pool around them, isolated",
                "positive_extra": "railing together, close, ocean to horizon, moon silver path, wind, deck lamp pool, isolated",
                "shot": "full_body",
                "dialogue": "Three more hours until we dock. Long time to be awake.",
            },
            {
                "scene": "sheltered behind lifeboat davit from wind, pressed into alcove, coat open, less wind here, deck lamp light reaching in diagonally, ocean audible but not visible, hidden corner",
                "positive_extra": "behind davit, sheltered, alcove, coat open, less wind, diagonal light, ocean audible, hidden",
                "shot": "medium_close",
            },
            {
                "scene": "against cabin wall on deck, smooth metal behind, salt-damp hair, ocean spray misting over railing, deck lamp above creating warm cone of light, engine vibration through wall into body, eyes closing",
                "positive_extra": "cabin wall, smooth metal, salt hair, spray misting, deck lamp cone, engine vibration, eyes closing",
                "shot": "medium",
            },
            {
                "scene": "close-up of face wet with ocean spray, moonlight one side sodium light other, salt crystals on lips, eyes reflecting moonlit ocean, wind-tangled hair, ferry deck behind, flushed from cold and warmth",
                "positive_extra": "wet face, spray, moonlight and sodium, salt on lips, ocean in eyes, tangled hair, flushed",
                "shot": "close_up",
                "caption": "Between one shore and the next, nothing existed but the deck.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on deck bench wrapped in shared coat, dawn starting at horizon over ocean, ferry approaching distant shore with lights, salt-crusted railing, empty deck, peaceful exhaustion, sky turning pink",
                "positive_extra": "bench, shared coat, dawn horizon, shore lights approaching, salt railing, empty deck, pink sky",
                "shot": "medium",
            },
            {
                "scene": "close-up of coiled rope on wet ferry deck, salt crystals on fibers, dawn light catching moisture, shore visible in background through railing, empty deck, horn sounding for arrival",
                "positive_extra": "coiled rope, wet deck, salt crystals, dawn moisture, shore through railing, empty, horn",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 32. rideshare_long — Back of car, city lights passing
    # ------------------------------------------------------------------
    {
        "key": "rideshare_long",
        "titles": ["Long Ride", "Shared Trip", "Estimated Arrival", "The Route"],
        "description": "Rideshare. Long route. The driver has headphones in.",
        "time": "night",
        "location": "rideshare car backseat at night",
        "furniture": ["backseat leather", "phone mount on dash", "driver partition area", "window", "middle seat armrest"],
        "lighting": ["city lights passing through windows", "phone screen map glow", "dashboard instrument light", "intermittent streetlamp flash"],
        "atmosphere": ["moving", "city lights", "semi-private", "night drive"],
        "phase_structure": "all_phase2",

        "setup": [
            {
                "scene": "sitting in backseat of rideshare, phone in hand showing map with long route, city lights passing through window, leather seat, looking at phone screen glowing blue, driver visible through gap, dashboard glow ahead",
                "positive_extra": "backseat, phone map, long route, city lights passing, leather, phone glow blue, driver ahead, dashboard",
                "shot": "medium",
                "caption": "Estimated arrival: 47 minutes. The long way.",
            },
            {
                "scene": "looking out backseat window, city neon signs and buildings passing, reflected in glass overlaid with face, hand against cold window, moving city creating light streaks, other backseat position empty",
                "positive_extra": "window, city neon passing, reflection overlay, hand on glass, light streaks, empty seat beside",
                "shot": "medium_close",
            },
            {
                "scene": "sliding across backseat as car turns, hand catching middle armrest, looking sideways at other passenger, city light sweep across both, driver's music audible through headphones faintly, amused by the slide",
                "positive_extra": "sliding across seat, car turning, hand on armrest, looking sideways, city light sweep, music faint, amused",
                "shot": "medium",
                "dialogue": "Forty minutes is a long ride. Make it interesting.",
            },
        ],

        "tension": [
            {
                "scene": "sitting in backseat, middle armrest folded up, sitting close, city lights playing across faces in rhythm, driver oblivious with headphones, phone mount showing route, leather seat, shared warmth",
                "positive_extra": "backseat, armrest up, sitting close, city light rhythm, driver headphones, route on phone, leather",
                "shot": "medium",
            },
            {
                "scene": "leaning across backseat, one hand on opposite door handle, city lights behind creating silhouette, dashboard glow from front, eyes locked on camera, driver headphones visible in rearview gap, moving vehicle",
                "positive_extra": "leaning across, hand on door, city silhouette, dashboard glow, eyes locked, driver rearview, moving",
                "shot": "medium_close",
                "dialogue": "Keep your voice down. He has one earbud out.",
            },
            {
                "scene": "pressed against backseat door, legs on seat, city lights painting skin through window in stripes, car vibrating on highway section, dashboard far ahead, enclosed moving space, nighttime",
                "positive_extra": "against door, legs on seat, city light stripes, highway vibration, dashboard far, enclosed, night",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face, city neon signs reflecting in eyes one by one as car passes them, each light a different color, lips parted, seatbelt strap across shoulder, leather seat headrest behind, moving lights",
                "positive_extra": "city neon in eyes, changing colors, parted lips, seatbelt, headrest, moving lights",
                "shot": "close_up",
                "caption": "The app updated: 12 minutes remaining.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting in backseat at red light, car stopped, composing self, looking at phone showing ARRIVING NOW, city intersection visible outside, driver removing headphones, straightening up quickly",
                "positive_extra": "red light, stopped, composing, phone ARRIVING NOW, intersection, driver turning, straightening",
                "shot": "medium",
            },
            {
                "scene": "close-up of rideshare app rating screen showing 5 stars on phone, car door handle visible, interior light on from door ajar, night street outside, ride summary showing long route taken",
                "positive_extra": "rating screen, 5 stars, door handle, interior light, door ajar, night street, long route",
                "shot": "close_up",
            },
        ],
    },

    # ==================================================================
    # OUTDOORS (12)
    # ==================================================================

    # ------------------------------------------------------------------
    # 33. camping_tent — Under stars, dying campfire
    # ------------------------------------------------------------------
    {
        "key": "camping_tent",
        "titles": ["Under Canvas", "Campfire", "Wilderness", "Two-Person Tent"],
        "description": "Campfire dying. Tent for two. Stars through the mesh ceiling.",
        "time": "night",
        "location": "campsite tent",
        "furniture": ["two-person tent", "sleeping bag", "dying campfire", "camp lantern", "log seat"],
        "lighting": ["dying campfire orange embers", "camp lantern inside tent", "starlight through mesh", "moonlight on campsite"],
        "atmosphere": ["wilderness", "crackling", "intimate", "starlit"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on log beside dying campfire, knees up, wrapping blanket around shoulders, orange ember glow on face, sparks floating up, tent visible behind, dark forest beyond, stars filling sky above",
                "positive_extra": "log seat, campfire embers, blanket, orange glow, sparks, tent behind, dark forest, stars",
                "shot": "medium",
                "caption": "Miles from the nearest road. The fire was going out.",
            },
            {
                "scene": "crouching at tent entrance, unzipping flap, camp lantern glowing inside revealing sleeping bag, looking back over shoulder at dying fire, forest silhouette, moonlit clearing, breath visible in cold air",
                "positive_extra": "tent entrance, unzipping, lantern inside, sleeping bag, looking back, fire dying, forest, moonlit, cold breath",
                "shot": "full_body",
            },
            {
                "scene": "inside tent, sitting cross-legged on sleeping bag, camp lantern beside casting warm orange glow, tent walls close, looking at entrance where someone is climbing in, amused cramped expression, stars visible through mesh ceiling",
                "positive_extra": "inside tent, cross-legged, sleeping bag, lantern glow, close walls, someone entering, amused, mesh stars",
                "shot": "medium_close",
                "dialogue": "They said two-person tent. They were optimistic.",
            },
        ],

        "tension": [
            {
                "scene": "lying in sleeping bag inside tent, camp lantern dimmed, looking up at stars through tent mesh ceiling, one arm behind head, other hand resting on stomach, warm glow, pine trees visible through mesh as shadows",
                "positive_extra": "sleeping bag, lantern dimmed, stars through mesh, arm behind head, hand on stomach, pine shadows",
                "shot": "medium",
                "dialogue": "It's cold. Sleeping bags zip together. Just saying.",
            },
            {
                "scene": "sitting up in sleeping bag, pulling shirt over head, camp lantern casting orange shadows on tent wall making shapes, close confines, sleeping bag bunched at waist, cold air visible on skin as goosebumps",
                "positive_extra": "sitting up, pulling shirt off, lantern shadows on tent wall, close confines, bunched sleeping bag, goosebumps",
                "shot": "medium_close",
            },
            {
                "scene": "pressed against tent wall from inside, fabric taut showing body shape from outside view in silhouette, camp lantern making shadow puppet display, tent fabric thin and translucent, campsite around",
                "positive_extra": "against tent wall, taut fabric, silhouette, lantern shadow, translucent fabric, campsite",
                "shot": "full_body",
            },
            {
                "scene": "close-up face lit by dim camp lantern, stars visible through mesh above, eyes reflecting tiny lantern flame, lying on sleeping bag fabric, pine air and warmth, half-smile, relaxed and alive",
                "positive_extra": "dim lantern, stars through mesh, lantern in eyes, sleeping bag fabric, warm, half-smile, alive",
                "shot": "close_up",
                "caption": "Outside, the campfire finally died. Inside, something else caught.",
            },
        ],

        "aftermath": [
            {
                "scene": "lying in tent with sleeping bag unzipped flat as blanket, looking through mesh ceiling at slowly lightening pre-dawn sky, camp lantern dead, breath visible, peaceful exhaustion, one arm extended across tent floor",
                "positive_extra": "tent, unzipped sleeping bag, mesh ceiling, pre-dawn sky, lantern dead, breath visible, peaceful, arm extended",
                "shot": "medium",
            },
            {
                "scene": "close-up of tent mesh ceiling showing stars fading as dawn approaches, pine branch silhouette across mesh, condensation drops on tent interior, sleeping bag corner visible, camp lantern cold, silence",
                "positive_extra": "tent mesh, stars fading, dawn, pine silhouette, condensation, sleeping bag corner, cold lantern, silence",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 34. hiking_waterfall — Hidden waterfall at end of trail
    # ------------------------------------------------------------------
    {
        "key": "hiking_waterfall",
        "titles": ["Trail's End", "Hidden Falls", "Off Trail", "Cascade"],
        "description": "End of the trail. A waterfall nobody else found. Water and mist.",
        "time": "afternoon",
        "location": "hidden waterfall forest pool",
        "furniture": ["flat rock by pool", "mossy log", "pool edge boulders", "waterfall curtain", "fern bank"],
        "lighting": ["dappled forest canopy light", "waterfall mist rainbow", "golden light through trees", "water reflections dancing"],
        "atmosphere": ["mist", "forest", "hidden", "refreshing"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing at edge of hidden waterfall pool, boots on mossy rock, looking up at waterfall cascade, mist on skin and in air catching golden sunlight through canopy, ferns everywhere, nobody else around",
                "positive_extra": "waterfall pool, mossy rock, looking up, cascade, mist catching gold light, canopy, ferns, alone",
                "shot": "full_body",
                "caption": "The trail ended. Then it didn't.",
            },
            {
                "scene": "sitting on flat rock beside pool, dipping feet in water, ripples spreading, hiking boots beside on rock, waterfall visible in background throwing mist, dappled forest light, cool water visible",
                "positive_extra": "flat rock, feet in water, ripples, boots beside, waterfall mist, dappled light, cool water",
                "shot": "medium",
            },
            {
                "scene": "turning from waterfall, water mist on face and arms, hair damp, exhilarated expression, hand wiping water from eyes, golden forest light behind waterfall, pool reflecting trees, fern bank",
                "positive_extra": "turning from waterfall, mist on face, damp hair, exhilarated, wiping eyes, golden light, pool reflections",
                "shot": "medium_close",
                "dialogue": "Nobody's coming this far up the trail. It's just us.",
            },
        ],

        "tension": [
            {
                "scene": "standing at pool edge, stepping into shallow water, one foot submerged, testing temperature, looking back at camera with challenging grin, waterfall behind, moss-covered boulders, golden canopy light",
                "positive_extra": "pool edge, stepping in, foot submerged, testing, challenging grin, waterfall, mossy boulders, canopy light",
                "shot": "full_body",
                "dialogue": "Water's cold. Really cold. Coming in anyway?",
            },
            {
                "scene": "standing in shallow pool water, water at knee level, waterfall mist surrounding like fog, dappled light through mist creating golden halos, hands running through wet hair, fern wall behind, natural paradise",
                "positive_extra": "in pool, knee deep, waterfall mist fog, golden halos, wet hair, fern wall, paradise",
                "shot": "medium",
            },
            {
                "scene": "pressed against mossy boulder at pool edge, back against cool wet rock, waterfall behind creating curtain of water, mist everywhere, green moss texture visible, hair wet, forest canopy above",
                "positive_extra": "mossy boulder, back on wet rock, waterfall curtain, mist, green moss, wet hair, canopy",
                "shot": "medium_close",
            },
            {
                "scene": "close-up face with water droplets on skin everywhere, waterfall mist soft focus behind, dappled golden light catching each droplet, eyes bright, lips parted, wet hair clinging, natural light, alive",
                "positive_extra": "water droplets on skin, mist soft focus, golden light on droplets, bright eyes, wet hair clinging, natural",
                "shot": "close_up",
                "caption": "The forest kept its secrets.",
            },
        ],

        "aftermath": [
            {
                "scene": "lying on warm flat rock beside pool, sun-drying, one arm shielding eyes, waterfall sound in background, dappled light through leaves moving on skin, completely relaxed, hiking gear scattered on rock",
                "positive_extra": "flat rock, sun-drying, arm shielding eyes, waterfall sound, dappled leaf light, relaxed, scattered gear",
                "shot": "full_body",
            },
            {
                "scene": "close-up of two sets of muddy boot prints leading to and from waterfall pool on forest trail, fern fronds overlapping track marks, golden afternoon light, no people, trail continuing into forest shadow",
                "positive_extra": "boot prints, muddy, trail, fern fronds, golden afternoon, no people, forest shadow ahead",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 35. park_bench_midnight — Can't go home yet
    # ------------------------------------------------------------------
    {
        "key": "park_bench_midnight",
        "titles": ["Midnight Park", "Can't Go Home", "The Bench", "Park After Dark"],
        "description": "Midnight in the park. Can't go home yet. The bench is cold but so is the apartment.",
        "time": "night",
        "location": "city park at night",
        "furniture": ["park bench", "lamppost", "fountain", "hedge row", "trash can"],
        "lighting": ["single lamppost cone", "moonlight through trees", "city glow at horizon", "phone screen light"],
        "atmosphere": ["quiet", "lonely", "cold", "midnight"],
        "phase_structure": "all_phase2",

        "setup": [
            {
                "scene": "sitting on park bench under single lamppost cone of light, darkness all around, legs crossed, looking at phone screen, coat pulled tight, park path stretching into dark, moonlight on grass, alone",
                "positive_extra": "park bench, lamppost cone, darkness, phone screen, coat tight, path into dark, moonlight grass, alone",
                "shot": "medium",
                "caption": "She told herself she was just getting air. At midnight. In November.",
            },
            {
                "scene": "standing at park fountain turned off for season, looking at still dark water reflecting lamppost light and moon, hands in pockets, cold night, hedge rows dark behind, city glow on horizon, breath visible",
                "positive_extra": "fountain, still water, reflecting lamppost, hands in pockets, cold night, hedges, city glow, breath",
                "shot": "full_body",
            },
            {
                "scene": "looking up from bench as footsteps approach on gravel path, guarded then surprised expression, lamppost light above, dark park behind approaching figure, coat collar up, phone screen going dark",
                "positive_extra": "looking up, footsteps, guarded surprised, lamppost above, dark park, collar up, phone darkening",
                "shot": "medium_close",
                "dialogue": "Couldn't sleep either?",
            },
        ],

        "tension": [
            {
                "scene": "both sitting on park bench under lamppost, close together, looking at dark park stretching ahead, lamppost creating intimate cone of warm light around them, world dark beyond, breath visible, cold but close",
                "positive_extra": "bench together, close, lamppost cone, dark park, intimate light, dark beyond, breath, cold close",
                "shot": "medium",
                "dialogue": "I wasn't going to stay. Then you showed up.",
            },
            {
                "scene": "standing just outside lamppost light cone, at edge of dark and light, one foot in brightness one in shadow, looking at camera from half-lit position, cold night air, park bench visible in light behind",
                "positive_extra": "edge of lamppost light, half dark half light, looking at camera, cold air, bench in light behind",
                "shot": "full_body",
            },
            {
                "scene": "pressed against park lamppost, metal cold against back, arms behind gripping post, looking up at light, moths circling above, park dark around, coat falling open, determined expression",
                "positive_extra": "against lamppost, cold metal, gripping post, looking up, moths, dark park, coat open, determined",
                "shot": "medium_close",
            },
            {
                "scene": "close-up face lit by warm lamppost light from above, dark park as background, eyes shining in light, cold flush on cheeks, breath visible, lips parted, moonlight catching hair edges, looking at viewer",
                "positive_extra": "lamppost from above, dark background, shining eyes, cold flush, breath visible, moonlight on hair, viewer",
                "shot": "close_up",
                "caption": "The lamp clicked off. City power saving. Moonlight remained.",
            },
        ],

        "aftermath": [
            {
                "scene": "walking down dark park path away from bench, lamppost now dark, moonlight only light, hands in pockets, looking forward, coat buttoned, path leading toward city glow at park exit, alone but different",
                "positive_extra": "dark path, away from bench, moonlight, hands in pockets, coat buttoned, city glow exit, alone but different",
                "shot": "full_body",
            },
            {
                "scene": "close-up of park bench under dark lamppost, moonlit, scarf left behind draped on armrest, no people, gravel path visible, frost starting to form on bench slats, dawn not yet but soon",
                "positive_extra": "bench, dark lamppost, moonlit, scarf left behind, no people, frost forming, pre-dawn",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 36. abandoned_warehouse — Urban exploring gone right
    # ------------------------------------------------------------------
    {
        "key": "abandoned_warehouse",
        "titles": ["Exploring", "Urban Decay", "Trespassing", "The Find"],
        "description": "Urban exploring. The warehouse was supposed to be empty. Mostly, it was.",
        "time": "afternoon",
        "location": "abandoned warehouse interior",
        "furniture": ["rusted metal staircase", "broken window", "old workbench", "concrete pillar", "paint-peeling wall"],
        "lighting": ["shaft of light through broken roof", "golden hour through broken windows", "dust motes floating in beams", "shadowed corners"],
        "atmosphere": ["abandoned", "dusty", "cathedral-like", "decaying beauty"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "climbing through broken warehouse window, one leg over sill, afternoon sun flooding through, dust motes swirling in light beam, abandoned warehouse interior vast and cathedral-like, rusted staircase visible, concrete floor",
                "positive_extra": "broken window, climbing in, afternoon sun, dust motes, cathedral warehouse, rusted staircase, concrete",
                "shot": "full_body",
                "caption": "The sign said NO TRESPASSING. The fence said otherwise.",
            },
            {
                "scene": "walking across abandoned warehouse floor, camera in hand taking photos, shaft of golden light from broken roof cutting diagonally through dust, paint peeling walls, old workbench with rusted tools, beauty in decay",
                "positive_extra": "warehouse floor, camera, photos, golden shaft, dust, peeling paint, old workbench, decay beauty",
                "shot": "medium",
            },
            {
                "scene": "looking up at broken roof from warehouse floor, standing in pool of golden light, arms slightly outstretched, dust swirling like snow, rusted metal structure above, surprised by how beautiful it is, face lit golden",
                "positive_extra": "looking up, broken roof, pool of golden light, arms out, dust snow, rusted metal, surprised beauty, golden face",
                "shot": "medium_close",
                "dialogue": "This place is incredible. How does nobody know about this?",
            },
        ],

        "tension": [
            {
                "scene": "sitting on rusted metal staircase step, legs through railing, overlooking warehouse floor below, golden light beam crossing just above head, dust floating, adventurous energy, looking at camera descending stairs",
                "positive_extra": "metal staircase, legs through railing, warehouse below, golden beam above, dust, adventurous, camera descending",
                "shot": "medium",
                "dialogue": "We should go higher. The roof access is up there.",
            },
            {
                "scene": "standing against paint-peeling wall, afternoon light painting warm stripe across body from window, peeling paint texture visible, concrete floor, shadows deep in corners, one hand trailing along crumbling wall surface",
                "positive_extra": "peeling wall, light stripe, warm, paint texture, concrete, deep shadows, hand trailing, crumbling",
                "shot": "full_body",
            },
            {
                "scene": "pressed against concrete pillar in warehouse, pillar surface rough and industrial, golden dust-filled light behind creating silhouette edge, hands behind on pillar, face turned upward in warm light beam",
                "positive_extra": "concrete pillar, rough industrial, golden light behind, silhouette edge, hands behind, face in light beam",
                "shot": "medium_close",
            },
            {
                "scene": "close-up face in shaft of golden warehouse light, dust motes floating past like stars, eyes glowing amber in light, abandoned beauty surrounding, lips parted, warm glow, face emerging from shadow into sun",
                "positive_extra": "golden shaft, dust stars, amber eyes, abandoned beauty, parted lips, warm glow, shadow to sun",
                "shot": "close_up",
                "caption": "The light moved like a clock hand. An hour of gold. Then shadow.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on old workbench, legs dangling, looking at camera screen scrolling through photos taken, golden light now lower and redder, warehouse stretching vast behind, peaceful satisfied explorer energy",
                "positive_extra": "workbench, legs dangling, camera screen, photos, red golden light, vast warehouse, satisfied explorer",
                "shot": "medium",
            },
            {
                "scene": "close-up of fresh footprints in dust on warehouse concrete floor, two sets leading deeper in then back out, golden light beam now at extreme angle nearly gone, dust settling, empty warehouse",
                "positive_extra": "footprints in dust, two sets, concrete floor, golden beam extreme angle, dust settling, empty",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 37. garden_maze — Lost on purpose, hedge walls
    # ------------------------------------------------------------------
    {
        "key": "garden_maze",
        "titles": ["Lost", "Hedge Maze", "The Center", "Dead End"],
        "description": "They entered the maze separately. Met in the center. No rush to find the exit.",
        "time": "afternoon",
        "location": "garden hedge maze",
        "furniture": ["stone bench at center", "hedge wall tall", "gravel path", "ornamental fountain center", "iron gate entrance"],
        "lighting": ["afternoon sun above maze walls", "shadow of hedge walls", "warm golden light at center", "green filtered light through leaves"],
        "atmosphere": ["labyrinthine", "green", "hidden", "warm afternoon"],
        "phase_structure": "all_phase1",

        "setup": [
            {
                "scene": "standing in tall hedge maze corridor, green walls towering on both sides, gravel path ahead turning, afternoon sun visible above wall tops, hand trailing along leaf wall, looking ahead at intersection, alone in maze",
                "positive_extra": "hedge corridor, green walls towering, gravel path turning, afternoon sun, hand on leaves, intersection, alone",
                "shot": "full_body",
                "caption": "She said she'd find the center first. She wasn't wrong.",
            },
            {
                "scene": "peering around hedge wall corner in maze, only face and shoulder visible past green wall, checking if path is clear, playful expression, gravel underfoot, tall hedges everywhere, sun-dappled",
                "positive_extra": "peering around hedge, face past wall, checking path, playful, gravel, tall hedges, sun-dappled",
                "shot": "medium_close",
            },
            {
                "scene": "arriving at maze center with stone bench and small fountain, arms raised triumphant, open square of hedge walls around, afternoon sun flooding center with golden light, gravel crunching, then seeing someone already there",
                "positive_extra": "maze center, stone bench, fountain, arms raised, hedge walls square, golden sun flooding, someone already there",
                "shot": "medium",
                "dialogue": "Took you long enough. I've been here ten minutes.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on stone bench at maze center, legs crossed, leaning back on hands, afternoon golden light, ornamental fountain trickling beside, tall hedge walls enclosing private garden room, completely hidden from outside",
                "positive_extra": "stone bench, maze center, golden light, fountain trickling, hedge walls enclosing, private, hidden",
                "shot": "medium",
                "dialogue": "Nobody can find us in here. I couldn't find me in here.",
            },
            {
                "scene": "standing against hedge wall in maze center, back pressing into soft green leaves, hand gripping branch through hedge, face in golden light, private green room, stone bench visible, entirely enclosed",
                "positive_extra": "against hedge, pressing into leaves, gripping branch, golden face, green room, stone bench, enclosed",
                "shot": "medium_close",
            },
            {
                "scene": "sitting on maze center fountain edge, feet in shallow water, splashing lightly, looking at camera from low angle, hedge walls towering behind creating green cathedral, golden afternoon, water droplets in air",
                "positive_extra": "fountain edge, feet in water, splash, low angle, hedge cathedral, golden afternoon, water droplets",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face framed by green hedge leaves on both sides like a natural frame, golden afternoon light, eyes lidded, lips parted, green reflections on skin, warmth, hidden deep in the maze",
                "positive_extra": "face framed by leaves, hedge, golden light, lidded eyes, parted lips, green reflections, hidden deep",
                "shot": "close_up",
                "caption": "The maze had no security cameras. They'd checked.",
            },
        ],

        "aftermath": [
            {
                "scene": "walking down hedge maze corridor away from center, hand dragging along leaf wall leaving trail, gravel path, afternoon light now lower, looking back over shoulder with knowing smile, maze stretching ahead",
                "positive_extra": "hedge corridor, walking away, hand trailing, gravel, lower light, looking back, knowing smile, maze ahead",
                "shot": "full_body",
            },
            {
                "scene": "close-up of stone bench at maze center, two leaves pressed together on bench surface, fountain still trickling, golden light now at extreme angle, no people, hedge walls darkening as sun lowers, peaceful",
                "positive_extra": "stone bench, two leaves, fountain trickling, extreme golden angle, no people, hedges darkening, peaceful",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 38. lighthouse_storm — Top of lighthouse, storm outside
    # ------------------------------------------------------------------
    {
        "key": "lighthouse_storm",
        "titles": ["Storm Watch", "The Lighthouse", "Beacon", "Safe Harbor"],
        "description": "Storm outside. The lighthouse keeper's quarters. The lamp keeps turning.",
        "time": "night",
        "location": "lighthouse keeper room during storm",
        "furniture": ["iron spiral staircase", "keeper's cot", "lantern on hook", "round window", "rope coils"],
        "lighting": ["lighthouse beam sweeping past window periodically", "oil lantern warm", "lightning flashes", "storm-dark except lamp sweep"],
        "atmosphere": ["storm", "isolated", "protected inside", "dramatic"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "climbing iron spiral staircase inside lighthouse, wind howling audible, one hand on cold rail, other shielding face from draft, oil lantern hanging on wall above, rain streaming down round window, storm visible",
                "positive_extra": "spiral staircase, lighthouse, wind, cold rail, lantern, rain on round window, storm",
                "shot": "full_body",
                "caption": "The storm closed the road. The lighthouse was the only shelter for miles.",
            },
            {
                "scene": "standing at round lighthouse window, palms on glass, watching storm rage over ocean below, lightning flash illuminating scene, lighthouse beam sweeping past window outside, rain lashing, warm inside, dark dramatic sea",
                "positive_extra": "round window, palms on glass, storm ocean, lightning flash, lighthouse beam sweep, rain, warm inside, dark sea",
                "shot": "medium",
            },
            {
                "scene": "turning from window as lighthouse door below bangs open, startled, oil lantern swinging in draft casting moving shadows on curved wall, storm noise flooding up stairwell, another person entering from storm",
                "positive_extra": "turning from window, door banging, startled, swinging lantern, moving shadows, curved wall, storm noise, entering",
                "shot": "medium_close",
                "dialogue": "Get in. Shut the door. How bad is it out there?",
            },
        ],

        "tension": [
            {
                "scene": "sitting on keeper's cot in lighthouse room, blanket around shoulders, oil lantern nearby, round window showing storm, lighthouse beam sweeping past periodically, periodic lightning flashes, shivering, cold-flushed",
                "positive_extra": "keeper's cot, blanket, lantern, storm window, beam sweeping, lightning periodic, shivering, cold-flushed",
                "shot": "medium",
                "dialogue": "We're stuck here until morning. Might as well get warm.",
            },
            {
                "scene": "standing in lighthouse stairwell, one hand on spiral rail, lit from above by oil lantern, lighthouse beam sweeping through tiny window creating periodic flash, storm wind shaking walls, close confines, looking up",
                "positive_extra": "stairwell, spiral rail, lantern from above, beam sweep flash, storm shaking, close confines, looking up",
                "shot": "full_body",
            },
            {
                "scene": "pressed against curved lighthouse wall, smooth plaster cool on back, oil lantern casting warm moving shadows, lightning flash through window freezing motion, rope coils on hook beside head, storm raging",
                "positive_extra": "curved wall, smooth plaster, lantern shadows, lightning freeze, rope coils, storm raging",
                "shot": "medium_close",
            },
            {
                "scene": "close-up of face lit by oil lantern from one side and lightning flash from other, dual warm and cold light, eyes wide and alive, storm energy, lips parted, wet hair from earlier rain, curved lighthouse wall behind",
                "positive_extra": "lantern warm side, lightning cold side, wide alive eyes, storm energy, parted lips, wet hair, curved wall",
                "shot": "close_up",
                "caption": "The beam kept sweeping. The storm kept raging. Inside, a different kind of heat.",
            },
        ],

        "aftermath": [
            {
                "scene": "lying on keeper's cot, blanket shared, looking up at curved ceiling, oil lantern nearly out, storm quieting outside, rain now gentle on round window, lighthouse beam still sweeping, peaceful after the storm",
                "positive_extra": "cot, shared blanket, curved ceiling, lantern low, storm quieting, gentle rain, beam sweeping, peaceful",
                "shot": "medium",
            },
            {
                "scene": "close-up of round lighthouse window at dawn, storm cleared revealing calm ocean and sunrise, rain drops still on glass catching pink light, lighthouse beam visible sweeping, oil lantern extinguished, cot in background",
                "positive_extra": "round window, dawn, cleared storm, calm ocean, sunrise, raindrops on glass, pink light, beam, lantern out",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 39. lake_dock — Summer midnight, wooden dock
    # ------------------------------------------------------------------
    {
        "key": "lake_dock",
        "titles": ["Dock", "Midnight Swim", "Still Water", "Lakeside"],
        "description": "Summer midnight. Wooden dock. Water so still it reflects every star.",
        "time": "night",
        "location": "lake wooden dock summer night",
        "furniture": ["wooden dock planks", "dock post", "tied rowboat", "dock ladder into water", "towel on planks"],
        "lighting": ["moonlight on lake surface", "starfield reflection in water", "distant cabin light", "dock lantern"],
        "atmosphere": ["still water", "warm night", "peaceful", "summer"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on edge of wooden dock, bare feet dangling over still lake water, looking at star reflections in dark water, moonlight painting silver path across lake, distant cabin light on far shore, warm summer night air",
                "positive_extra": "wooden dock edge, bare feet, still water, star reflections, moonlight silver path, cabin light, summer night",
                "shot": "medium",
                "caption": "Summer midnight. The lake was a mirror.",
            },
            {
                "scene": "lying on wooden dock planks, arms spread, looking up at stars filling sky, towel underneath, old wooden dock texture, tied rowboat gently bumping dock post, moonlight everything, crickets chirping feeling",
                "positive_extra": "dock planks, arms spread, stars above, towel, wood texture, rowboat bumping, moonlight, crickets",
                "shot": "full_body",
            },
            {
                "scene": "standing on dock looking at water, one toe touching surface creating single ripple disrupting star reflections, moonlit, warm night, looking up at approaching footsteps on wooden planks, relaxed welcoming",
                "positive_extra": "dock, toe in water, single ripple, disrupted reflections, moonlit, footsteps, relaxed welcoming",
                "shot": "medium_close",
                "dialogue": "Water's perfect. Couldn't sleep?",
            },
        ],

        "tension": [
            {
                "scene": "standing on dock looking down at still lake below, arms crossed, considering, moonlight on water, dock ladder descending into dark lake, playful challenging expression, warm night breeze, hair moving slightly",
                "positive_extra": "dock, looking at lake, arms crossed, moonlight, dock ladder, challenging, night breeze, hair",
                "shot": "full_body",
                "dialogue": "Nobody's around for miles. Just the water and the moon.",
            },
            {
                "scene": "sitting on dock edge, just climbed out of lake, water streaming off body, moonlight catching water on skin, wooden planks wet beneath, breathless laughing, cold lake water warm night air contrast",
                "positive_extra": "dock edge, climbed out, water streaming, moonlight on wet skin, wet planks, breathless, cold warm contrast",
                "shot": "medium",
            },
            {
                "scene": "lying on dock towel, back arched slightly, hand reaching up toward stars, lake water evaporating off skin in moonlight, dock planks worn and warm from day, everything silver and black, still lake beside",
                "positive_extra": "dock towel, back arched, reaching for stars, water evaporating, moonlight, warm planks, silver black, still lake",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face wet from lake, moonlight silver on wet skin, water droplets in eyelashes, eyes reflecting stars, wooden dock planks visible beside head, hair wet and spread on wood, peaceful intensity",
                "positive_extra": "wet face, moonlight silver, droplets in lashes, stars in eyes, dock planks, wet hair on wood, peaceful intense",
                "shot": "close_up",
                "caption": "The lake went still again. Like nothing had disturbed it.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on dock wrapped in towel, feet dangling, looking at lake returned to perfect stillness, moon lower now, distant cabin light gone off, rowboat bobbing, completely still scene, satisfied peace",
                "positive_extra": "dock, towel, feet dangling, still lake, lower moon, cabin dark, rowboat, still, peaceful",
                "shot": "medium",
            },
            {
                "scene": "close-up of wet footprints on wooden dock planks leading from water to towel position, moonlight catching wet marks, dock ladder rungs wet, still lake beyond, no people, pre-dawn blue barely starting",
                "positive_extra": "wet footprints, dock planks, moonlight, wet ladder rungs, still lake, no people, pre-dawn blue",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 40. orchard_twilight — Picking ended, golden hour
    # ------------------------------------------------------------------
    {
        "key": "orchard_twilight",
        "titles": ["Golden Hour", "Harvest", "Between the Trees", "Orchard"],
        "description": "Picking's done. Golden hour. The orchard is empty and glowing.",
        "time": "evening",
        "location": "apple orchard at golden hour",
        "furniture": ["wooden crate of apples", "orchard ladder", "tree trunk", "fallen apple ground", "woven basket"],
        "lighting": ["golden hour through tree leaves", "warm sunset between trunks", "dappled orchard light", "amber sky above treeline"],
        "atmosphere": ["golden", "warm", "orchard", "harvest"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing between apple tree rows, golden hour light filtering through leaves creating warm dappled pattern on face and body, woven basket of apples at feet, looking down orchard row, trees vanishing into golden distance",
                "positive_extra": "apple tree rows, golden hour, dappled pattern, basket at feet, orchard row, golden distance",
                "shot": "full_body",
                "caption": "Everyone else left at five. She stayed for the light.",
            },
            {
                "scene": "sitting on wooden apple crate under tree, one apple in hand, taking a bite, golden light through leaves above, orchard stretching behind, bark texture on nearby trunk, warm amber atmosphere, relaxed end of day",
                "positive_extra": "apple crate, under tree, apple bite, golden light through leaves, orchard behind, bark, amber, relaxed",
                "shot": "medium",
            },
            {
                "scene": "on orchard ladder reaching for high apple, stretching up, golden sunset light between tree trunks creating long shadows, looking down at someone below, amused expression, leaves and fruit around",
                "positive_extra": "orchard ladder, reaching up, sunset between trunks, long shadows, looking down, amused, leaves fruit",
                "shot": "medium_close",
                "dialogue": "Catch me if I fall. These ladders are older than the trees.",
            },
        ],

        "tension": [
            {
                "scene": "leaning against wide apple tree trunk, bark rough against back, hands behind on bark, golden sunset light warming face, orchard rows stretching away on both sides, alone between trees, one apple on ground",
                "positive_extra": "tree trunk, bark against back, hands behind, golden face, orchard rows, alone, apple on ground",
                "shot": "full_body",
                "dialogue": "We have until the sun goes below the treeline. Then it gets dark fast.",
            },
            {
                "scene": "standing between two close apple trees, tree trunks on either side, hand on each, golden light catching in hair from behind creating glow, leaves above like a canopy, looking through tree frame at camera",
                "positive_extra": "between two trees, hand on each trunk, golden backlight, hair glow, leaf canopy, looking through frame",
                "shot": "medium_close",
            },
            {
                "scene": "sitting on ground against tree trunk, grass beneath, fallen apples around, knees up, golden sunset now very low painting everything amber-red, orchard quiet, head tilted back against bark, eyes half-closed",
                "positive_extra": "ground against trunk, grass, fallen apples, knees up, amber-red sunset, quiet, head back, bark, half-closed",
                "shot": "medium",
            },
            {
                "scene": "close-up of face with golden hour light at its most intense, amber-gold, eyes catching sunset, apple tree leaves making shadow pattern on cheek, warm peaceful intensity, lips parted, earth and fruit scent",
                "positive_extra": "golden hour intense, amber eyes, leaf shadow on cheek, warm intensity, parted lips, earth scent",
                "shot": "close_up",
                "caption": "The sun touched the treeline. The orchard turned amber, then bronze, then dark.",
            },
        ],

        "aftermath": [
            {
                "scene": "walking down orchard row in near-darkness, twilight sky visible above trees, woven basket on hip, looking back at where they'd been, fireflies beginning to appear between trees, day ending",
                "positive_extra": "orchard row, near-dark, twilight sky, basket on hip, looking back, fireflies, day ending",
                "shot": "full_body",
            },
            {
                "scene": "close-up of single apple on ground between tree roots, bite mark in it, golden light gone now replaced by blue twilight, grass dewy, no people, orchard quiet except crickets",
                "positive_extra": "apple on ground, tree roots, bite mark, blue twilight, dewy grass, no people, quiet crickets",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 41. ski_lodge_fire — After the slopes, by the hearth
    # ------------------------------------------------------------------
    {
        "key": "ski_lodge_fire",
        "titles": ["Aprés-Ski", "By the Fire", "Snow Melt", "Lodge"],
        "description": "Off the slopes. By the fire. The snow on their clothes is melting.",
        "time": "evening",
        "location": "ski lodge fireplace room",
        "furniture": ["stone fireplace", "fur-draped couch", "bear skin rug", "hot cocoa mugs on table", "ski boots drying"],
        "lighting": ["roaring fireplace orange", "window showing snow and blue dusk", "warm interior lamps", "fire reflection on wood panels"],
        "atmosphere": ["warm fire", "cold outside", "cozy", "aprés-ski"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on fur-draped couch by stone fireplace, pulling wet ski socks off, fire roaring beside, snow-damp hair, flushed cheeks from cold, hot cocoa mug on table, ski boots drying near hearth, window showing snow falling at dusk",
                "positive_extra": "fur couch, fireplace, pulling socks off, damp hair, flushed cold, cocoa mug, ski boots, snow dusk window",
                "shot": "medium",
                "caption": "Last run of the day. The lodge was almost empty.",
            },
            {
                "scene": "standing by fireplace holding hands out to warm them, back to fire, facing room, ski base layers still on, steam rising from damp clothes drying, bear skin rug below, wood paneled walls reflecting fire glow",
                "positive_extra": "by fireplace, warming hands, back to fire, base layers, steam from clothes, bear rug, wood panels, fire glow",
                "shot": "full_body",
            },
            {
                "scene": "curled up on bear skin rug in front of fire, hot cocoa held in both hands, looking up at someone, fire reflecting in eyes, warm golden on one side cool blue window light on other, hair drying in waves from snow",
                "positive_extra": "bear rug, fire, cocoa in hands, looking up, fire in eyes, golden warm, blue window, hair drying waves",
                "shot": "medium_close",
                "dialogue": "Everyone else went to the bar. Their loss.",
            },
        ],

        "tension": [
            {
                "scene": "on couch by fire, peeling off damp base layer top, fire-warmed skin visible, one arm through one arm still in, looking at camera, firelight playing across exposed skin, fur thrown over couch, intimate",
                "positive_extra": "couch, peeling off base layer, fire-warmed skin, firelight on skin, fur on couch, intimate",
                "shot": "medium",
                "dialogue": "These are still soaked. Need to dry them by the fire.",
            },
            {
                "scene": "lying on bear skin rug, propped on elbows, fire roaring beside painting body in warm dancing light, hot cocoa untouched going cold on table, head tilted, rug fur texture visible, snow falling outside window",
                "positive_extra": "bear rug, on elbows, fire dancing light, cocoa going cold, head tilted, rug fur, snow outside",
                "shot": "full_body",
            },
            {
                "scene": "pressed against stone fireplace wall beside mantle, warm stone against skin, fire heat on side, face half in firelight half in shadow, hand on rough stone surface, eyes heavy from warmth",
                "positive_extra": "stone fireplace wall, warm stone, fire heat, half firelight half shadow, hand on stone, heavy eyes",
                "shot": "medium_close",
            },
            {
                "scene": "close-up of face lit entirely by firelight, warm orange glow, fire reflected dancing in each eye, flushed from heat now not cold, bear rug fur visible at jaw, lips parted, completely warm finally",
                "positive_extra": "firelight face, warm orange, fire dancing in eyes, flushed heat, bear rug fur, parted lips, warm",
                "shot": "close_up",
                "caption": "The snow kept falling outside. Inside, everything was already melting.",
            },
        ],

        "aftermath": [
            {
                "scene": "asleep on fur couch, fire burned down to embers, orange glow dim, fur pulled up as blanket, cocoa mugs both empty, ski boots dry now, snow stopped outside window showing clear star sky, peaceful",
                "positive_extra": "sleeping on couch, embers, dim orange, fur blanket, empty mugs, dry boots, clear star sky, peaceful",
                "shot": "medium",
            },
            {
                "scene": "close-up of two pairs of ski boots by hearth, completely dry now, fire reduced to glowing embers, bear rug rumpled and pushed aside, empty cocoa mugs, dawn light beginning through snow-frosted window",
                "positive_extra": "ski boots, hearth, dry, embers, bear rug rumpled, empty mugs, dawn, frosted window",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 42. hot_spring_mountain — Natural hot spring, steam, rocks
    # ------------------------------------------------------------------
    {
        "key": "hot_spring_mountain",
        "titles": ["Hot Spring", "Mountain Steam", "Mineral", "The Source"],
        "description": "Natural mountain hot spring. Steam rising. Nobody else made the hike.",
        "time": "evening",
        "location": "mountain natural hot spring",
        "furniture": ["natural rock pool", "flat boulder", "mineral deposit edge", "overhanging rock", "mountain wildflowers"],
        "lighting": ["sunset over mountain ridge", "steam diffusing warm light", "twilight purple sky", "orange on steam clouds"],
        "atmosphere": ["steamy", "mineral", "natural", "mountain"],
        "phase_structure": "all_phase1",

        "setup": [
            {
                "scene": "standing at edge of natural hot spring pool, steam rising all around, mountain landscape behind, sunset over ridge painting sky orange and purple, flat boulders around pool, mineral deposits on rock edges, pristine wilderness",
                "positive_extra": "hot spring edge, steam, mountain, sunset over ridge, orange purple sky, boulders, mineral deposits, wilderness",
                "shot": "full_body",
                "caption": "Two hours of hiking for this. Worth every step.",
            },
            {
                "scene": "sitting on flat boulder beside hot spring, dipping hand into steaming water, testing temperature, steam rising around hand, mountain twilight, wildflowers growing between rocks, mineral-colored water, peaceful",
                "positive_extra": "boulder, dipping hand, testing water, steam, mountain twilight, wildflowers, mineral water, peaceful",
                "shot": "medium",
            },
            {
                "scene": "looking back from hot spring pool at someone arriving on the trail, steam framing body, sunset backlighting, surprised then welcoming expression, mountain ridgeline visible above, natural pool clear and steaming",
                "positive_extra": "hot spring, looking back, trail arrival, steam framing, sunset backlight, surprised welcoming, ridgeline, clear pool",
                "shot": "medium_close",
                "dialogue": "You found it too? I thought I was the only one crazy enough to hike this far.",
            },
        ],

        "tension": [
            {
                "scene": "submerged in hot spring to shoulders, arms resting on natural rock edge, steam rising around face, mountain sky turning from orange to deep blue above, mineral deposits on rocks around, heat relaxing visible in posture",
                "positive_extra": "submerged to shoulders, rock edge, steam, sky orange to blue, mineral deposits, heat relaxation",
                "shot": "medium",
                "dialogue": "The water's perfect. It's like the mountain is breathing.",
            },
            {
                "scene": "sitting on submerged rock shelf in hot spring, water at waist, steam thick, leaning back against natural rock wall, overhanging rock above creating alcove, twilight sky visible through steam, mineral water clear",
                "positive_extra": "rock shelf, water at waist, thick steam, back on rock, overhanging alcove, twilight through steam, mineral clear",
                "shot": "medium_close",
            },
            {
                "scene": "standing in shallow pool area, water at knees, steam rising from water surface, mountain silhouette against last light behind, volcanic mineral rock around feet, arms crossed over chest against cool air above water",
                "positive_extra": "shallow pool, knees, steam rising, mountain silhouette, last light, volcanic rock, arms crossed, cool air",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face surrounded by hot spring steam, skin flushed from heat, water droplets and sweat mixing, mountain twilight blue above, mineral-warm, eyes half-closed from heat pleasure, steam curling past face",
                "positive_extra": "steam surrounding, heat flush, droplets and sweat, twilight blue, mineral-warm, half-closed, steam curling",
                "shot": "close_up",
                "caption": "The mountain held its heat long after the sun dropped.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on flat boulder beside pool, wrapped in towel, looking at stars now visible above mountain, steam still rising from pool, first stars incredibly bright at altitude, mountain air cold on wet skin, content",
                "positive_extra": "boulder, towel, stars above mountain, steam rising, bright stars at altitude, cold air wet skin, content",
                "shot": "medium",
            },
            {
                "scene": "close-up of still-steaming hot spring pool surface, stars reflected in mineral-tinted water, flat boulder at edge with abandoned towel, no people, mountain ridgeline silhouette, night sky, spring eternal",
                "positive_extra": "steaming pool, stars reflected, mineral water, boulder, abandoned towel, no people, mountain night, eternal",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 43. treehouse_found — Discovered in the woods
    # ------------------------------------------------------------------
    {
        "key": "treehouse_found",
        "titles": ["Found It", "Up There", "Treehouse", "Hideout"],
        "description": "An old treehouse, deeper in the woods than it should be. Someone built it years ago.",
        "time": "afternoon",
        "location": "treehouse in forest",
        "furniture": ["plank floor", "rope ladder", "window cutout", "old blanket pile", "carved initials on wall"],
        "lighting": ["forest canopy filtered green light", "afternoon sun through plank gaps", "warm light through window cutout", "leaf shadow patterns"],
        "atmosphere": ["hidden", "childhood nostalgia", "forest", "discovery"],
        "phase_structure": "reversed",

        "setup": [
            {
                "scene": "looking up at old treehouse high in oak tree, rope ladder dangling, forest canopy green and golden around, afternoon light through leaves, hand shielding eyes from sun, surprised discovery expression, deep in woods",
                "positive_extra": "treehouse high up, rope ladder, forest canopy, golden green, afternoon leaves, hand shielding, discovered, deep woods",
                "shot": "full_body",
                "caption": "Half a mile off the trail. Built by someone who didn't want it found.",
            },
            {
                "scene": "climbing rope ladder up to treehouse, looking down at ground below, forest floor covered in leaves, tree bark rough and close, plank platform visible above, afternoon sun through canopy, adventurous energy",
                "positive_extra": "climbing rope ladder, looking down, forest floor leaves, bark texture, platform above, canopy sun, adventurous",
                "shot": "medium",
            },
            {
                "scene": "pulling self up through treehouse floor opening, head and arms appearing, looking around interior discovering old blankets and carved initials, warm afternoon light through plank gaps and window cutout, dusty but magical",
                "positive_extra": "floor opening, pulling up, discovering interior, old blankets, carved initials, light through gaps, magical",
                "shot": "medium_close",
                "dialogue": "Somebody lived up here. Look at this place.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on treehouse plank floor, old blanket around shoulders, looking out window cutout at forest canopy stretching green and golden, legs dangling through floor opening, carved names on wall beside, warm cozy",
                "positive_extra": "plank floor, blanket, window cutout, forest canopy, legs dangling, carved names, warm cozy",
                "shot": "medium",
                "dialogue": "Nobody knows we're up here. Nobody even knows this exists.",
            },
            {
                "scene": "leaning against treehouse wall, sunlight coming through plank gaps creating stripe pattern across body, old wood warm behind, looking at camera, forest sounds, leaves rustling visible through window, secret place energy",
                "positive_extra": "treehouse wall, sunlight stripes through gaps, warm wood, forest sounds, leaves rustling, secret place",
                "shot": "full_body",
            },
            {
                "scene": "lying on old blankets in treehouse, looking up through gap in roof at canopy and blue sky, green leaves framing sky, afternoon light warm, plank floor beneath blankets, enclosed elevated hidden space",
                "positive_extra": "blankets, looking up, roof gap, canopy and sky, green leaves framing, warm afternoon, enclosed elevated",
                "shot": "medium_close",
            },
            {
                "scene": "close-up of face in treehouse, dappled green-gold forest light through window, leaf shadow pattern on face moving with wind, old wood visible behind, eyes bright with discovery and something more, lips parted",
                "positive_extra": "dappled green-gold, leaf shadow pattern, moving with wind, old wood, bright eyes, discovery, parted lips",
                "shot": "close_up",
                "caption": "The treehouse creaked with the wind. It held.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting in treehouse window cutout, legs outside dangling over forest drop, looking at afternoon forest stretching forever, blanket around shoulders, peaceful elevated perspective, birds visible in canopy",
                "positive_extra": "window cutout, legs dangling outside, forest stretching, blanket, elevated peace, birds, canopy",
                "shot": "medium",
            },
            {
                "scene": "close-up of fresh carved initials in treehouse wall beside old faded ones, pocket knife resting on plank, afternoon light through gap illuminating the carving, nobody in frame, forest through window",
                "positive_extra": "fresh carved initials, beside old ones, pocket knife, light on carving, nobody, forest through window",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 44. cemetery_dare — Midnight dare, old iron gates
    # ------------------------------------------------------------------
    {
        "key": "cemetery_dare",
        "titles": ["Midnight Dare", "Iron Gates", "Among the Stones", "Graveyard Shift"],
        "description": "Midnight. A dare. Old cemetery. Turns out the only thing alive in there was them.",
        "time": "night",
        "location": "old cemetery at midnight",
        "furniture": ["old headstone", "iron cemetery gate", "stone angel statue", "cemetery bench", "mausoleum wall"],
        "lighting": ["full moon overhead", "phone flashlight beam", "moonlight on pale stone", "shadows from monuments"],
        "atmosphere": ["eerie beautiful", "moonlit", "daring", "adrenaline"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing at old iron cemetery gate, one hand on cold iron bar, full moon directly above casting sharp shadows, gravel path leading into rows of old headstones, holding phone with flashlight, nervous excited expression",
                "positive_extra": "iron gate, cold iron, full moon, sharp shadows, headstone rows, phone flashlight, nervous excited",
                "shot": "full_body",
                "caption": "The dare was simple. Spend one hour past the gate. After midnight.",
            },
            {
                "scene": "walking between old headstones, phone flashlight beam cutting through dark, full moon above making stones glow pale, long monument shadows, stone angel statue visible ahead, gravel crunching, looking around alert",
                "positive_extra": "between headstones, flashlight beam, full moon, pale stones, long shadows, angel statue, gravel, alert",
                "shot": "medium",
            },
            {
                "scene": "jumping startled, one hand grabbing nearest headstone for balance, phone light swinging wild, looking at direction of noise, heart-racing expression, moonlit cemetery around, then relieved laugh seeing another person",
                "positive_extra": "startled jump, grabbing headstone, flashlight swinging, looking at noise, heart-racing, moonlit, relieved laugh",
                "shot": "medium_close",
                "dialogue": "You absolute— I thought you were a ghost!",
            },
        ],

        "tension": [
            {
                "scene": "sitting on old cemetery bench, knees up, adrenaline laugh fading, full moon above, headstones around like a garden, surprisingly peaceful, phone light off relying on moonlight, looking at companion, rush still visible",
                "positive_extra": "cemetery bench, knees up, adrenaline fading, full moon, headstones garden, peaceful, moonlight only, rush visible",
                "shot": "medium",
                "dialogue": "My heart's still pounding. From the scare, I mean.",
            },
            {
                "scene": "standing with back against mausoleum stone wall, cool carved stone, moonlight from above painting half face bright and half shadow, cemetery stretching behind, arms crossed then uncrossing, adrenaline redirecting",
                "positive_extra": "mausoleum wall, cool stone, moonlight half-face, cemetery behind, arms uncrossing, adrenaline redirecting",
                "shot": "medium_close",
            },
            {
                "scene": "pressed against stone angel pedestal, the angel statue above, moonlight making stone glow, hand on cold stone base, ironic setting, alive among the still, looking at camera, breathless from running or from something else",
                "positive_extra": "angel pedestal, statue above, moonlight glow, hand on cold stone, alive among still, breathless",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face lit by full moon from above, silver-blue moonlight, eyes wide and alive, adrenaline flush, lips parted, headstone silhouettes behind, alive never felt so literal, the dare completely forgotten",
                "positive_extra": "full moon above, silver-blue, wide alive eyes, adrenaline flush, parted lips, headstone silhouettes, alive",
                "shot": "close_up",
                "caption": "Among the stones, they'd never felt more alive.",
            },
        ],

        "aftermath": [
            {
                "scene": "walking out through iron cemetery gate, looking back over shoulder at moonlit cemetery, hand trailing on iron bar, grass stains visible, disheveled, moon lower now, first hint of dawn at horizon, peaceful not scared",
                "positive_extra": "iron gate, looking back, moonlit cemetery, hand on iron, grass stains, disheveled, dawn hint, peaceful",
                "shot": "full_body",
            },
            {
                "scene": "close-up of iron cemetery gate, padlock hanging open, moonlight catching iron curlwork, fresh flower left on nearest headstone that wasn't there before, no people visible, cemetery peaceful and still",
                "positive_extra": "iron gate, padlock open, moonlight, iron curlwork, fresh flower on headstone, no people, peaceful still",
                "shot": "close_up",
            },
        ],
    },

    # ==================================================================
    # DOMESTIC (10)
    # ==================================================================

    # ------------------------------------------------------------------
    # 45. bathroom_steam — After her shower, fogged mirror
    # ------------------------------------------------------------------
    {
        "key": "bathroom_steam",
        "titles": ["Steamed", "After the Shower", "Fogged", "Hot Water"],
        "description": "The shower just stopped. The mirror is fogged. The door wasn't locked.",
        "time": "evening",
        "location": "bathroom after shower",
        "furniture": ["fogged mirror", "shower stall glass", "bath mat", "towel rack", "vanity counter"],
        "lighting": ["warm overhead bathroom light", "steam-diffused glow", "LED vanity mirror edge light", "water droplets refracting light"],
        "atmosphere": ["steamy", "warm", "damp", "intimate"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing at fogged bathroom mirror, towel wrapped, one hand wiping clear circle in fog to see reflection, steam still thick in air, warm overhead light diffused by moisture, water droplets running down mirror, bath mat wet",
                "positive_extra": "fogged mirror, towel wrapped, wiping circle, steam thick, diffused warm light, water droplets, wet bath mat",
                "shot": "medium",
                "caption": "The bathroom was still thick with steam when the door opened.",
            },
            {
                "scene": "stepping out of shower stall through glass door, steam pouring out, hand on glass door edge, bathroom fogged, towel just grabbed from rack, wet footprint on tile floor, warm light through steam",
                "positive_extra": "shower stall, glass door, steam pouring, hand on glass, towel grabbed, wet footprint, warm steam light",
                "shot": "full_body",
            },
            {
                "scene": "turning from mirror to face bathroom door, hand holding towel at chest, eyes wide, steam swirling behind from open shower, water on skin catching overhead light, fogged mirror behind with cleared handprint",
                "positive_extra": "turning to door, towel at chest, eyes wide, steam swirling, water on skin, fogged mirror, handprint",
                "shot": "medium_close",
                "dialogue": "I didn't hear you come in. The water was—",
            },
        ],

        "tension": [
            {
                "scene": "leaning against bathroom vanity counter, hip against edge, steam thinning but still warm, mirror behind mostly fogged with clear spot showing reflection, water droplets on collar and shoulders, looking at doorway",
                "positive_extra": "vanity counter, hip against edge, steam thinning, fogged mirror, clear spot reflection, water droplets, doorway",
                "shot": "medium",
            },
            {
                "scene": "pressed against shower stall glass from outside, glass still warm and fogged, handprint visible where she braced, steam curling around, warm light, water still dripping from showerhead visible through glass",
                "positive_extra": "shower glass, warm fogged, handprint brace, steam curling, warm light, dripping showerhead",
                "shot": "medium_close",
                "dialogue": "The hot water hasn't run out yet.",
            },
            {
                "scene": "back against cool tile bathroom wall, contrast of cool tile and steam warmth, arms at sides palms flat on tile, water droplets on skin from steam condensation, overhead light creating wet-skin glow",
                "positive_extra": "tile wall, cool tile, steam warmth contrast, palms on tile, water droplets, condensation, wet-skin glow",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face in steam, water droplets on skin everywhere, eyes looking through parting steam, mirror behind clearing revealing blurred reflection, warm light diffused, lips parted, damp hair clinging to neck",
                "positive_extra": "face in steam, water droplets, looking through steam, clearing mirror, diffused warm, parted lips, damp hair neck",
                "shot": "close_up",
                "caption": "The mirror cleared slowly. Like a secret developing.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on bathroom floor against tub, towel barely arranged, wet hair dripping, steam mostly cleared, mirror now showing clear reflection of the scene, warm light, water pooled on tile, satisfied daze",
                "positive_extra": "bathroom floor, against tub, towel, wet hair dripping, steam cleared, clear mirror reflection, water pooled, daze",
                "shot": "medium",
            },
            {
                "scene": "close-up of fogged bathroom mirror with message written in condensation by finger, two words only, water dripping from letters, no people visible, toothbrush and vanity items at base, steam fading",
                "positive_extra": "fogged mirror, message in condensation, finger-written, water dripping from letters, no people, steam fading",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 46. roommate_apartment — Roommate situation, thin walls
    # ------------------------------------------------------------------
    {
        "key": "roommate_apartment",
        "titles": ["Thin Walls", "Shared Space", "Your Turn", "Common Area"],
        "description": "The roommate is out. Supposedly until ten. It's eight-thirty.",
        "time": "evening",
        "location": "shared apartment living room",
        "furniture": ["shared couch", "coffee table", "kitchenette counter", "shoes by door pile", "laundry basket"],
        "lighting": ["warm living room lamp", "TV screen glow", "kitchen light through pass-through", "evening light through window"],
        "atmosphere": ["lived-in", "shared space", "temporary privacy", "warm"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on shared apartment couch, bowl of cereal on coffee table, oversized t-shirt and shorts, TV remote in hand, comfortable and unguarded, evening light through window, shoes piled at door, laundry basket visible",
                "positive_extra": "apartment couch, cereal, oversized shirt, remote, comfortable, evening light, shoes at door, laundry",
                "shot": "medium",
                "caption": "Roommate's out until ten. An hour and a half of freedom.",
            },
            {
                "scene": "in kitchenette, one foot up on counter stool rung, reaching up to high cabinet, t-shirt riding up showing waist, warm kitchen light, shared apartment mess visible, mugs and cereal boxes, casual domestic",
                "positive_extra": "kitchenette, foot on rung, reaching high, shirt riding up, waist, warm light, shared mess, casual domestic",
                "shot": "full_body",
            },
            {
                "scene": "turning from kitchen toward front door sound, surprised but pleased, spoon still in mouth, cereal box in hand, casual domestic disheveled, lamp light warm, shoes by door now with one more pair",
                "positive_extra": "turning to door, surprised pleased, spoon in mouth, cereal box, disheveled, lamp warm, extra shoes at door",
                "shot": "medium_close",
                "dialogue": "She said she'd be gone until ten. We have ninety minutes.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on couch with TV on but volume off, legs tucked under, turned sideways to face other end of couch, lamp light warm, coffee table pushed aside, apartment door chain visible in background locked",
                "positive_extra": "couch, TV muted, legs tucked, turned sideways, lamp warm, table pushed, door chain locked",
                "shot": "medium",
                "dialogue": "Walls are thin. We have to be quiet.",
            },
            {
                "scene": "standing between couch and coffee table, tiny space, looking down at couch perspective, hand pulling shirt hem, lamp creating intimate warm space, TV casting blue flickering light, apartment small and close",
                "positive_extra": "between couch and table, tiny space, looking down, pulling shirt, lamp warm, TV blue flicker, small close",
                "shot": "full_body",
            },
            {
                "scene": "pressed against back of apartment couch, leaning over it, TV glow from other side, lamp light from this side, split lighting, looking at viewer over couch back, one hand gripping cushion",
                "positive_extra": "couch back, leaning over, TV glow, lamp light, split lighting, looking over, gripping cushion",
                "shot": "medium_close",
            },
            {
                "scene": "close-up of face with TV light flickering blue on one side, lamp warm on other, biting lip to stay quiet, eyes intense, cushion fabric visible at edge of frame, apartment sounds audible feeling",
                "positive_extra": "TV flicker blue, lamp warm, biting lip, quiet, intense eyes, cushion fabric, apartment sounds",
                "shot": "close_up",
                "caption": "A key turned in the lock. They froze.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on couch in completely normal position, bowl of cereal back in lap, TV volume suddenly up, perfectly composed, door opening, roommate entering, nothing to see here expression, heart pounding invisible",
                "positive_extra": "couch normal, cereal in lap, TV on, composed, door opening, nothing to see here, heart pounding",
                "shot": "medium",
                "dialogue": "Oh hey. You're back early. Just watching TV.",
            },
            {
                "scene": "close-up of couch cushion slightly askew, one sock visible wedged between cushions, TV playing to nobody, cereal bowl with milk warming on coffee table, everything almost in place but not quite",
                "positive_extra": "cushion askew, sock wedged, TV playing, cereal bowl warming, almost in place, not quite",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 47. wrong_apartment — Wrong floor, door was open
    # ------------------------------------------------------------------
    {
        "key": "wrong_apartment",
        "titles": ["Wrong Floor", "Open Door", "5B Not 4B", "Mistaken"],
        "description": "Wrong apartment. Right moment. The door was open. The layout is identical.",
        "time": "night",
        "location": "apartment hallway and interior",
        "furniture": ["apartment door", "entry hallway", "unfamiliar couch", "bookshelf", "kitchen island"],
        "lighting": ["hallway fluorescent spill", "warm apartment interior light", "city lights through window", "under-cabinet kitchen LED"],
        "atmosphere": ["disoriented", "surprise", "identical but different"],
        "phase_structure": "mixed",

        "setup": [
            {
                "scene": "standing inside apartment that looks almost right but wrong, holding key that didn't work, looking around confused at unfamiliar items on familiar shelves, warm interior light, identical layout to own apartment but different belongings, slightly drunk confused",
                "positive_extra": "apartment interior, holding key, confused, unfamiliar items, familiar layout, warm light, different belongings",
                "shot": "medium",
                "caption": "5B. Not 4B. The door was open. The layout was identical. The rest was not.",
            },
            {
                "scene": "standing in apartment entry hallway, one hand still on door handle, realizing mistake, other person's shoes and coat visible, warm light from living room ahead, hallway fluorescent behind, frozen mid-entry",
                "positive_extra": "entry hallway, hand on door, realizing, other person's things, warm living room, fluorescent behind, frozen",
                "shot": "full_body",
            },
            {
                "scene": "face-to-face in hallway of wrong apartment, apologetic expression, one hand up defensively, other person blocking path in robe, narrow hallway close quarters, warm interior behind them, door still open behind",
                "positive_extra": "face to face, hallway, apologetic, hand up, robe, narrow close quarters, warm interior, door open",
                "shot": "medium_close",
                "dialogue": "I am so sorry. I thought this was my apartment. 4B. I live right below you.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on unfamiliar couch that's same model as own, deja vu expression, looking around apartment that mirrors own but different, offered water glass in hand, warm light, city lights through window, strange comfortable",
                "positive_extra": "unfamiliar couch, same model, deja vu, mirror apartment, water glass, warm light, city lights, strange comfort",
                "shot": "medium",
                "dialogue": "This is bizarre. Same couch. Same layout. Even the bookshelf is in the same spot.",
            },
            {
                "scene": "standing at apartment window looking at same view but from one floor higher, hand on glass, city at night, seeing own window below, vertigo feeling, reflection in glass showing room behind, warm light",
                "positive_extra": "window, same view higher, hand on glass, city night, own window below, vertigo, reflection, warm light",
                "shot": "medium_close",
            },
            {
                "scene": "leaning against kitchen island in wrong apartment, island identical to own but different items on it, uncanny valley domestic, looking at host, elbows on counter, face lit by under-cabinet LED, intrigued now not embarrassed",
                "positive_extra": "kitchen island, identical but different, uncanny domestic, elbows on counter, under-cabinet LED, intrigued",
                "shot": "medium",
            },
            {
                "scene": "close-up of face in warm apartment light, realization shifting from embarrassment to interest, city lights through window behind, unfamiliar familiar setting, slight smile forming, eyes searching",
                "positive_extra": "warm light, shifting expression, embarrassment to interest, city lights, unfamiliar familiar, smile forming",
                "shot": "close_up",
                "caption": "Same building. Same layout. Different everything else.",
            },
        ],

        "aftermath": [
            {
                "scene": "standing at apartment door now open, stepping into hallway, looking back into apartment, hallway fluorescent cold, apartment warm behind, hesitant departure, one foot across threshold, key to own apartment visible in hand",
                "positive_extra": "apartment door, hallway, looking back, fluorescent cold, warm behind, hesitant, threshold, own key",
                "shot": "full_body",
            },
            {
                "scene": "close-up of apartment door 5B, closed, hallway fluorescent light, apartment numbers visible, stairwell entrance nearby leading down to 4B, no people, quiet building, late night, door slightly ajar not fully closed",
                "positive_extra": "door 5B, closed hallway, apartment numbers, stairwell to 4B, no people, quiet, ajar not closed",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 48. walk_in_closet — Hiding from the party downstairs
    # ------------------------------------------------------------------
    {
        "key": "walk_in_closet",
        "titles": ["Hiding", "Walk-In", "Behind Closed Doors", "Wardrobe"],
        "description": "Party raging downstairs. She needed a minute. The walk-in closet was dark and quiet.",
        "time": "night",
        "location": "walk-in closet",
        "furniture": ["hanging clothes rows", "shoe rack", "full-length closet mirror", "storage shelf", "velvet dress visible"],
        "lighting": ["strip LED under shelf", "party light under door", "phone screen glow", "closet switch off ambient only"],
        "atmosphere": ["fabric-muffled", "dark", "hidden", "intimate enclosed"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on walk-in closet floor between shoe rack and hanging clothes, knees up, hiding from party noise, muffled bass from below, phone light only illumination, fabrics hanging all around creating tent feeling, breathing slowly",
                "positive_extra": "closet floor, shoe rack, hanging clothes, hiding, muffled bass, phone light, fabric tent, breathing",
                "shot": "medium",
                "caption": "She told them she was getting her jacket. That was fifteen minutes ago.",
            },
            {
                "scene": "standing in walk-in closet, running hand along hanging clothes, fabrics touching arm, dim LED strip under shelf providing only light, full-length mirror at end reflecting figure among clothes, door closed, quiet",
                "positive_extra": "walk-in, hand along clothes, fabric touching, LED strip, mirror reflecting, among clothes, door closed, quiet",
                "shot": "full_body",
            },
            {
                "scene": "closet door opening, light flooding in from bedroom, squinting at brightness, sitting among hanging clothes, party music louder briefly, someone stepping in and closing door again, back to dark",
                "positive_extra": "door opening, light flooding, squinting, among clothes, music louder, someone entering, door closing, dark again",
                "shot": "medium_close",
                "dialogue": "Close the door. It's quiet in here.",
            },
        ],

        "tension": [
            {
                "scene": "standing face to face in dark walk-in closet, very close, clothes hanging around them like curtains, only LED strip light below casting upward shadows, party completely muffled now, intimate forced closeness",
                "positive_extra": "face to face, dark closet, very close, clothes curtains, LED strip below, upward shadows, muffled, intimate",
                "shot": "medium_close",
                "dialogue": "It's so dark I can barely see you.",
            },
            {
                "scene": "pressed against closet wall between shelves, fabrics brushing against arms, LED glow from below, reaching up gripping shelf above, closet cramped and dark, only outlines visible, party bass vibrating through floor",
                "positive_extra": "closet wall, between shelves, fabrics brushing, LED below, gripping shelf, cramped dark, outlines, bass vibration",
                "shot": "medium",
            },
            {
                "scene": "reflected in full-length closet mirror at end of walk-in, dark silhouettes among hanging clothes, LED strip making shapes glow, mirror showing what darkness hides, party muffled through walls",
                "positive_extra": "closet mirror, dark silhouettes, hanging clothes, LED shapes, mirror revealing, party muffled",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face in near-darkness, only LED strip reflecting in eyes from below, fabric textures visible at frame edges, almost blind, relying on touch, parted lips, party completely inaudible now",
                "positive_extra": "near-darkness, LED in eyes, fabric edges, almost blind, touch, parted lips, party inaudible",
                "shot": "close_up",
                "caption": "In the dark among the clothes, the party ceased to exist.",
            },
        ],

        "aftermath": [
            {
                "scene": "closet door opening from inside, stepping out into lit bedroom, adjusting clothes, party audible again from downstairs, grabbing actual jacket from hook, looking back at dark closet with small smile, hair slightly messed",
                "positive_extra": "door opening, stepping out, adjusting clothes, party audible, grabbing jacket, looking back, small smile, messed hair",
                "shot": "medium",
            },
            {
                "scene": "close-up of velvet dress hanging in closet, slightly askew from being pressed against, fabric with creases, LED strip below, door now open showing lit room, shoe knocked on its side on rack, quiet closet",
                "positive_extra": "velvet dress, askew, creased, LED strip, door open, lit room, shoe knocked over, quiet",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 49. kitchen_midnight — Raiding the fridge at 2am
    # ------------------------------------------------------------------
    {
        "key": "kitchen_midnight",
        "titles": ["Midnight Snack", "Fridge Light", "2AM", "Hungry"],
        "description": "2am. Couldn't sleep. The fridge light is the only light in the apartment.",
        "time": "night",
        "location": "dark kitchen at night",
        "furniture": ["open refrigerator", "kitchen counter", "bar stool", "microwave", "dish rack"],
        "lighting": ["refrigerator interior light", "microwave clock green glow", "moonlight through kitchen window", "phone screen"],
        "atmosphere": ["dark except fridge", "quiet apartment", "midnight", "barefoot"],
        "phase_structure": "all_phase2",

        "setup": [
            {
                "scene": "standing at open refrigerator in dark kitchen, fridge light only illumination casting white-blue glow, barefoot on tile, oversized sleep shirt, browsing shelves, everything else in darkness, moonlight through kitchen window",
                "positive_extra": "open fridge, dark kitchen, fridge light glow, barefoot, tile, sleep shirt, browsing, moonlight window",
                "shot": "full_body",
                "caption": "2:14 AM. Insomnia tasted better with leftovers.",
            },
            {
                "scene": "sitting on kitchen counter in dark, eating directly from container, fridge still open casting light, legs dangling, bare feet, microwave clock showing 2am green digits, dark apartment, casual and unguarded",
                "positive_extra": "counter, eating from container, fridge light, legs dangling, bare feet, microwave clock 2am, dark, unguarded",
                "shot": "medium",
            },
            {
                "scene": "turning from fridge hearing footsteps in dark kitchen, container in hand, fridge door creating spotlight, surprised expression, someone in doorway silhouette, dark kitchen, bare feet on cold tile",
                "positive_extra": "turning from fridge, footsteps, container, fridge spotlight, surprised, doorway silhouette, bare feet cold tile",
                "shot": "medium_close",
                "dialogue": "I was just—it's not what it looks like. Okay, it's exactly what it looks like.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on bar stool in dark kitchen, only fridge light from open door behind, leaning back, sleep shirt riding up, one bare foot on stool rung, sharing food, fridge glow creating intimate pocket of light",
                "positive_extra": "bar stool, dark kitchen, fridge behind, leaning back, shirt riding up, bare foot, sharing food, light pocket",
                "shot": "medium",
                "dialogue": "Since we're both up. Want some?",
            },
            {
                "scene": "standing at kitchen counter, pressed against counter edge, fridge light behind creating silhouette and backlighting, dark kitchen, moonlight through window on face, contrast of fridge glow and moon",
                "positive_extra": "counter edge, fridge backlight, silhouette, dark kitchen, moonlight face, contrast glow and moon",
                "shot": "full_body",
            },
            {
                "scene": "leaning against fridge door that's slowly closing, hand holding it barely open, light shrinking, getting darker, face going from lit to shadow, kitchen completely dark apartment, last slice of light narrowing",
                "positive_extra": "fridge door closing, hand holding, light shrinking, lit to shadow, dark kitchen, light narrowing",
                "shot": "medium_close",
            },
            {
                "scene": "close-up face in almost total darkness, only microwave clock green glow and moonlight through window, eyes catching what little light exists, fridge now closed, darkness complete, lips slightly visible, intimate dark",
                "positive_extra": "total darkness, microwave green, moonlight, eyes catching light, fridge closed, dark complete, lips visible",
                "shot": "close_up",
                "caption": "The fridge door closed. Neither reached to open it again.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on kitchen floor against cabinet, bare feet extended, fridge door open again casting light, eating last of container, satisfied groggy expression, 3am on microwave, moonlight shifted position on floor",
                "positive_extra": "kitchen floor, cabinet, bare feet, fridge open again, eating, groggy satisfied, 3am, moonlight shifted",
                "shot": "medium",
            },
            {
                "scene": "close-up of empty food container on kitchen counter, fork still in it, microwave clock showing 3:17am green, fridge door closed, moonlight on counter surface, no people, dark quiet kitchen",
                "positive_extra": "empty container, fork, microwave 3:17am, fridge closed, moonlight on counter, no people, quiet",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 50. couch_thunderstorm — Power out, only the storm
    # ------------------------------------------------------------------
    {
        "key": "couch_thunderstorm",
        "titles": ["Blackout", "Thunder", "Power's Out", "Storm Inside"],
        "description": "Power's out. Thunderstorm raging. One couch. One blanket. One candle.",
        "time": "night",
        "location": "living room during thunderstorm blackout",
        "furniture": ["couch with throw blanket", "coffee table with candle", "rain-streaked window", "dead TV", "bookshelf"],
        "lighting": ["single candle on coffee table", "lightning flashes through window", "phone screen occasional", "complete darkness between flashes"],
        "atmosphere": ["thunder", "rain", "candlelit", "power outage"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on couch in completely dark living room, single candle on coffee table only light, rain hammering on windows visible streaking, lightning flash illuminating everything for one second, throw blanket around shoulders, dead TV dark",
                "positive_extra": "dark living room, single candle, rain on windows, lightning flash, throw blanket, dead TV, power out",
                "shot": "medium",
                "caption": "The power went out at nine. The storm had just begun.",
            },
            {
                "scene": "standing at rain-streaked window, pressing hand against cold glass, looking out at storm, lightning illuminating entire scene white-blue for a moment, candle on coffee table behind, dark apartment, everything silent except rain and thunder",
                "positive_extra": "rain-streaked window, hand on glass, storm, lightning white-blue, candle behind, dark apartment, rain thunder",
                "shot": "full_body",
            },
            {
                "scene": "sitting on couch looking up from phone as it dies, screen going dark, candle now truly only light, storm outside intensifying, thunder rattling windows, one last light source gone, resigned amused expression",
                "positive_extra": "couch, phone dying, screen dark, candle only light, storm intensifying, thunder rattling, resigned amused",
                "shot": "medium_close",
                "dialogue": "Phone just died. Candle's all we've got.",
            },
        ],

        "tension": [
            {
                "scene": "both on couch sharing blanket, candlelight only illumination, faces close, storm raging outside, lightning flashes periodically freezing the scene white, thunder following, candle flickering in draft, warm under blanket cold apartment",
                "positive_extra": "sharing blanket, candlelight, faces close, storm, lightning freeze, thunder, candle flicker, warm cold contrast",
                "shot": "medium_close",
                "dialogue": "It's cold. Come closer.",
            },
            {
                "scene": "pressed into couch corner, blanket pulled up, candle casting warm glow, lightning flash showing room then plunging back to candle-dark, rain intensity increasing, looking at camera in candlelight, vulnerable in the dark",
                "positive_extra": "couch corner, blanket up, candle glow, lightning show then dark, rain increasing, candlelight, vulnerable dark",
                "shot": "medium",
            },
            {
                "scene": "lying on couch, one arm extended toward coffee table candle, face lit from below by warm flame, blanket pooled at waist, rain visible streaking window behind, lightning flash mid-scene, dramatic chiaroscuro",
                "positive_extra": "lying on couch, arm toward candle, face below-lit, blanket at waist, rain window, lightning mid-scene, chiaroscuro",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face in candlelight, warm orange flicker, eyes reflecting tiny flame, thunder audible in the way cheeks vibrate, lips parted, rain sound constant, darkness beyond candle reach, completely intimate",
                "positive_extra": "candlelight close, warm orange flicker, flame in eyes, thunder vibration, parted lips, rain constant, darkness beyond",
                "shot": "close_up",
                "caption": "The candle guttered. They didn't reach for another.",
            },
        ],

        "aftermath": [
            {
                "scene": "lying together on couch under blanket, candle burned out leaving complete darkness, lightning flash revealing the scene for one instant only, rain softening, storm passing, peaceful in total dark",
                "positive_extra": "couch, blanket, candle out, complete dark, lightning one flash, rain softening, storm passing, peaceful",
                "shot": "medium",
            },
            {
                "scene": "close-up of dead candle on coffee table, wax cooled and hardened in drip pattern, blanket edge visible at couch, window no longer streaking with rain, first grey dawn light, power still out, quiet after storm",
                "positive_extra": "dead candle, wax hardened, drip pattern, blanket edge, rain stopped, grey dawn, power out, quiet",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 51. attic_boxes — Found something in the boxes
    # ------------------------------------------------------------------
    {
        "key": "attic_boxes",
        "titles": ["In the Attic", "Boxed Up", "Found", "Dust and Memories"],
        "description": "Cleaning out the attic. Found something in the boxes that changed the afternoon.",
        "time": "afternoon",
        "location": "dusty attic with boxes",
        "furniture": ["cardboard boxes stacked", "old trunk", "dormer window", "exposed beam", "dust sheet covered furniture"],
        "lighting": ["dormer window dusty light beam", "bare bulb on pull chain", "dust motes in sunbeam", "warm attic glow"],
        "atmosphere": ["dusty", "nostalgic", "hot attic", "discovery"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on attic floor surrounded by open cardboard boxes, items spread around, holding old photograph, dust motes floating in dormer window sunbeam, bare bulb on chain above, exposed wooden beams, hot stuffy attic, boxes everywhere",
                "positive_extra": "attic floor, open boxes, photograph, dust motes, dormer sunbeam, bare bulb, exposed beams, hot stuffy",
                "shot": "medium",
                "caption": "The attic hadn't been opened in years. The dust agreed.",
            },
            {
                "scene": "kneeling at old trunk, lifting heavy lid, peering inside, dormer window light falling across trunk opening, dust rising from disturbed contents, cobweb breaking, curious excited expression, attic cramped with stored boxes",
                "positive_extra": "old trunk, lifting lid, peering, dormer light on trunk, dust rising, cobweb, curious, cramped attic",
                "shot": "medium_close",
            },
            {
                "scene": "standing in attic, object held up toward dormer window light to examine it, silhouette against dusty window, exposed beams overhead, head slightly ducked for low ceiling, looking at viewer holding discovery",
                "positive_extra": "holding object to light, dormer window, silhouette, dusty, exposed beams, ducked head, low ceiling, discovery",
                "shot": "full_body",
                "dialogue": "Look what was in this trunk. This changes things.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on old trunk lid together, attic around them, dormer window light creating warm cone, dust floating like snow, boxes providing walls around private space, bare bulb off relying on window, warm closeness",
                "positive_extra": "on trunk, together, dormer cone, floating dust, boxes as walls, window light only, warm close",
                "shot": "medium",
            },
            {
                "scene": "pressed against exposed beam in attic, rough wood against back, dust caught in hair, dormer light horizontal across midsection, boxes stacked on either side creating narrow space, looking at camera, flushed from heat",
                "positive_extra": "exposed beam, rough wood, dust in hair, dormer horizontal light, boxes narrow space, flushed heat",
                "shot": "medium_close",
                "dialogue": "It's too hot up here. That's not what's making me flush.",
            },
            {
                "scene": "lying on dust sheet covering old furniture, sheet rumpled, dormer window light falling across body, attic warm and close, exposed beams above creating frame, dust motes like stars in the light, boxes around like a fort",
                "positive_extra": "dust sheet, rumpled, dormer light across body, warm close, beams framing, dust stars, box fort",
                "shot": "full_body",
            },
            {
                "scene": "close-up face lit by dormer window warm afternoon, dust motes around like gold flecks, attic wood beam visible above, heavy-lidded from heat and something else, old fabric at edge of frame, lips parted, attic warm",
                "positive_extra": "dormer warm light, dust gold flecks, beam above, heavy-lidded, old fabric, parted lips, attic warm",
                "shot": "close_up",
                "caption": "They'd come up to organize. They'd found something better.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting at dormer window in attic, looking outside at afternoon sky, dust sheet pulled around like a toga, boxes still open and spread everywhere, bare bulb swinging slightly, peaceful post-discovery atmosphere",
                "positive_extra": "dormer window, afternoon sky, dust sheet toga, boxes open, bare bulb swinging, peaceful",
                "shot": "medium",
            },
            {
                "scene": "close-up of old trunk lid closed again, dusty handprint on top, dormer light now at steep late-afternoon angle, items half-sorted around, no people, attic quiet, dust settling back down",
                "positive_extra": "trunk closed, dusty handprint, steep angle light, half-sorted items, no people, dust settling",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 52. guest_bedroom — Holiday at their parents' house
    # ------------------------------------------------------------------
    {
        "key": "guest_bedroom",
        "titles": ["Guest Room", "Be Quiet", "Holiday Visit", "Down the Hall"],
        "description": "Holiday visit. Guest bedroom. Their parents' room is down the hall.",
        "time": "night",
        "location": "guest bedroom parents house",
        "furniture": ["single guest bed with quilt", "dresser with family photos", "old wooden door", "nightstand with clock", "window with lace curtain"],
        "lighting": ["nightstand lamp dim", "hallway light under door", "moonlight through lace curtain", "phone charging LED"],
        "atmosphere": ["quiet desperation", "forbidden", "nostalgic room", "thin walls"],
        "phase_structure": "all_phase1",

        "setup": [
            {
                "scene": "sitting on edge of guest bed with quilt, looking at family photos on dresser, nightstand lamp dim, lace curtain moonlight, old house creaking, unfamiliar room familiar house, phone charging on nightstand, clock showing late",
                "positive_extra": "guest bed, quilt, family photos dresser, dim lamp, lace curtain, moonlight, creaking house, phone charging, late",
                "shot": "medium",
                "caption": "Guest bedroom. Twin bed. Parents' room twenty feet away.",
            },
            {
                "scene": "standing at guest bedroom window, pulling lace curtain aside, moonlight on face, looking down at quiet neighborhood, can't sleep, old house settling noises, guest room small and stuffy, nightstand lamp casting warm corner light",
                "positive_extra": "guest window, lace curtain, moonlight face, quiet neighborhood, can't sleep, house settling, small stuffy, warm lamp",
                "shot": "full_body",
            },
            {
                "scene": "opening guest bedroom wooden door slowly, peeking into dark hallway, hallway light off, creaking floorboard, cautious expression, nightstand lamp light spilling into hall, parents' door visible at end of hallway closed, heart-pounding quiet",
                "positive_extra": "opening door slowly, dark hallway, creaking, cautious, lamp light spilling, parents' door visible, quiet",
                "shot": "medium_close",
                "dialogue": "Everyone's asleep. The floorboards are loud.",
            },
        ],

        "tension": [
            {
                "scene": "sitting together on single guest bed, barely fits two, quilt bunched around, whispering distance close, nightstand lamp off now, only moonlight through lace, hallway light under door showing no movement, old house quiet",
                "positive_extra": "single bed, barely fits, quilt bunched, whispering close, lamp off, moonlight lace, hallway light still, quiet",
                "shot": "medium",
                "dialogue": "That floor creaks. We can't—just—stay.",
            },
            {
                "scene": "pressed against guest bedroom door from inside, one hand on old door handle checking lock, other hand palm-flat on wooden door surface, moonlight behind, listening, hallway light visible under door, tense quiet excitement",
                "positive_extra": "against door, hand on handle, palm on wood, moonlight, listening, hallway light under, tense quiet",
                "shot": "medium_close",
            },
            {
                "scene": "lying on guest bed which squeaks, hand gripping quilt, biting pillow to muffle, moonlight through lace casting pattern on skin, old nightstand with clock visible, forced silence, walls paper-thin",
                "positive_extra": "squeaky bed, gripping quilt, biting pillow, moonlight lace pattern, clock, forced silence, thin walls",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face on pillow, moonlight lace pattern across features, lips pressed together suppressing sound, eyes wide and alive, pillow gripped beside face, nightstand clock visible showing late hour, quiet intensity",
                "positive_extra": "face on pillow, lace pattern, lips pressed, suppressing, wide alive eyes, gripping pillow, clock, quiet intensity",
                "shot": "close_up",
                "caption": "A door opened somewhere in the hall. They didn't breathe.",
            },
        ],

        "aftermath": [
            {
                "scene": "lying in guest bed alone, covers up to chin, arranged innocently, staring at ceiling, moonlight through lace, door closed, hallway quiet, creaking footsteps fading back to their own room somewhere in house, trying not to smile",
                "positive_extra": "bed alone, covers up, innocent, ceiling, moonlight, door closed, footsteps fading, trying not to smile",
                "shot": "medium",
            },
            {
                "scene": "close-up of guest bedroom door from hallway side, family photos visible on hallway wall, door fully closed, nightlight at baseboard, parent's door at end of hall still closed, early morning quiet, no one awake yet",
                "positive_extra": "guest door, hallway, family photos, closed, nightlight, parents' door closed, early morning, no one awake",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 53. laundry_basement — Old building, one working machine
    # ------------------------------------------------------------------
    {
        "key": "laundry_basement",
        "titles": ["Spin Cycle", "Basement", "Last Load", "Quarters"],
        "description": "Basement laundry. One working machine. Two people waiting for the dryer.",
        "time": "night",
        "location": "basement laundry room",
        "furniture": ["washing machine", "dryer", "folding table", "plastic chair", "detergent shelf"],
        "lighting": ["harsh overhead fluorescent buzzing", "dryer window warm glow", "washer LED panel", "stairwell light from above"],
        "atmosphere": ["basement hum", "machine vibration", "institutional", "late night"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on dryer, legs dangling, machine vibrating beneath, reading magazine, laundry basket on folding table, harsh fluorescent above buzzing, concrete basement walls, one other washer running, late night laundry",
                "positive_extra": "on dryer, legs dangling, vibrating, magazine, laundry basket, fluorescent buzzing, concrete walls, late night",
                "shot": "medium",
                "caption": "11pm. The basement laundry. Where bad decisions have good lighting.",
            },
            {
                "scene": "standing at folding table sorting laundry, pulling items from basket, fluorescent light above, dryer tumbling visible through round window warm glow, concrete floor, detergent shelf behind, alone in basement",
                "positive_extra": "folding table, sorting laundry, fluorescent, dryer window glow, concrete floor, detergent shelf, alone basement",
                "shot": "full_body",
            },
            {
                "scene": "looking up from folding as laundry room door opens, stairwell light flooding in, someone with own basket entering, surprised recognition, dryer humming behind, fluorescent light harsh on both, basement late night encounter",
                "positive_extra": "looking up, door opening, stairwell light, someone entering, basket, surprised, dryer humming, fluorescent, late night",
                "shot": "medium_close",
                "dialogue": "Of course. Same building, same schedule.",
            },
        ],

        "tension": [
            {
                "scene": "both sitting on dryers, machines vibrating, facing each other, laundry forgotten on folding table between, fluorescent light above, concrete basement intimate in its ugliness, vibration constant and shared, timer counting down",
                "positive_extra": "both on dryers, vibrating, facing each other, laundry forgotten, fluorescent, concrete intimate, vibration, timer",
                "shot": "medium",
                "dialogue": "Thirty minutes left on the cycle. Got anywhere to be?",
            },
            {
                "scene": "leaning against washing machine during spin cycle, whole body vibrating with machine, hand flat on humming metal surface, looking at camera, fluorescent light, laundry basket knocked aside, basement walls close",
                "positive_extra": "against washer, spin cycle, vibrating, hand on metal, looking at camera, fluorescent, knocked basket, close walls",
                "shot": "medium_close",
            },
            {
                "scene": "pressed against folding table edge, table vibrating from machine nearby, hand gripping table edge, dryer window warm glow from one side fluorescent cold from above, laundry items pushed aside, basement isolated",
                "positive_extra": "folding table edge, vibrating from machine, gripping edge, dryer warm glow, fluorescent cold, laundry aside, isolated",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face lit by dryer window warm orange glow from one side, fluorescent from other, machines humming vibrating everything, eyes half-closed, lips parted, laundry fabric at frame edge, basement quiet except machines",
                "positive_extra": "dryer warm glow, fluorescent cold, vibrating, half-closed eyes, parted lips, fabric edge, machine hum only",
                "shot": "close_up",
                "caption": "The dryer buzzed. Cycle complete. Neither moved.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on plastic chair, laundry basket on lap warm from dryer, half-folded items, other basket still in dryer, fluorescent still buzzing, concrete walls, peaceful despite setting, alone now, small smile",
                "positive_extra": "plastic chair, warm basket, half-folded, dryer basket, fluorescent, concrete, peaceful despite, alone, smile",
                "shot": "medium",
            },
            {
                "scene": "close-up of dryer door open, single item of clothing caught in door, warm inside, timer at 0:00, folding table with neatly stacked laundry, empty laundry room, fluorescent reflecting off concrete, stairwell light visible at door",
                "positive_extra": "dryer open, caught clothing, warm, timer 0:00, neat stack, empty room, fluorescent concrete, stairwell light",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 54. neighbors_balcony — Over the divider
    # ------------------------------------------------------------------
    {
        "key": "neighbors_balcony",
        "titles": ["Over the Divider", "Next Door", "Balcony", "Adjacent"],
        "description": "Adjacent balconies. The divider is thin. The wine was strong.",
        "time": "evening",
        "location": "apartment balcony",
        "furniture": ["balcony chair", "small table", "thin partition divider", "railing", "potted plant"],
        "lighting": ["string lights on railing", "warm apartment light through sliding door", "city lights at distance", "candle on table"],
        "atmosphere": ["evening air", "urban", "adjacent", "wine-warm"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on balcony chair, wine glass in hand, feet up on railing, evening city spread below, string lights along railing, thin partition divider visible to one side, apartment warm light behind through sliding glass door, relaxed evening",
                "positive_extra": "balcony chair, wine glass, feet on railing, city below, string lights, partition divider, apartment light, relaxed",
                "shot": "medium",
                "caption": "Same view. Different balcony. Same wine, though. She could smell it.",
            },
            {
                "scene": "standing at balcony railing looking at city lights, wine glass on small table, evening breeze moving hair, thin divider partition visible, neighbor's balcony light visible on other side, string lights and candle creating warmth",
                "positive_extra": "railing, city lights, wine on table, breeze hair, divider visible, neighbor light, string lights, candle",
                "shot": "full_body",
            },
            {
                "scene": "leaning over thin balcony divider partition, resting chin on arms on divider top, looking toward neighbor's side, playful expression, wine glass balanced on divider, string lights, evening sky, casual boundary crossing",
                "positive_extra": "leaning over divider, chin on arms, looking at neighbor side, playful, wine balanced, string lights, boundary crossing",
                "shot": "medium_close",
                "dialogue": "You're drinking the same thing I am. That's either fate or the liquor store had a sale.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on divider between balconies, legs on one side body leaning other, risky balcony position, wine glass held out, city lights behind, string lights on both sides now, warm evening, breeze, bold move",
                "positive_extra": "on divider, legs one side leaning other, risky, wine glass out, city lights, string lights both sides, bold",
                "shot": "medium",
                "dialogue": "This divider is not as sturdy as it looks.",
            },
            {
                "scene": "standing on neighbor's balcony now, having climbed over, back against their sliding door, looking at own balcony visible through divider, wine glass from their side in hand, crossed over, no going back now",
                "positive_extra": "neighbor's balcony, climbed over, against sliding door, own balcony through divider, their wine, crossed over",
                "shot": "full_body",
            },
            {
                "scene": "pressed against balcony railing, city lights behind as bokeh, wine glass abandoned on divider edge, string lights framing from above, wind on skin, high up and exposed, looking at camera, thrilling vulnerability",
                "positive_extra": "against railing, city bokeh, wine on divider, string lights framing, wind on skin, high exposed, vulnerability",
                "shot": "medium_close",
            },
            {
                "scene": "close-up of face with city lights stretched behind as bokeh blur, string light reflections, wine-flushed, evening breeze, balcony night air, eyes heavy, lips wine-stained, candle flicker from table visible at edge",
                "positive_extra": "city lights bokeh, string light reflections, wine-flushed, breeze, heavy eyes, wine-stained lips, candle flicker",
                "shot": "close_up",
                "caption": "Two balconies. One evening. The divider stopped mattering.",
            },
        ],

        "aftermath": [
            {
                "scene": "climbing back over balcony divider carefully, one leg over, wine glass held up for balance, laughing quietly, city lights, string lights, late night, own apartment dark behind sliding door, neighbor's light still warm",
                "positive_extra": "climbing divider, one leg over, wine for balance, laughing quiet, city lights, late night, own apartment dark, neighbor warm",
                "shot": "medium",
            },
            {
                "scene": "close-up of wine glass left on balcony divider edge, balanced precariously, two apartments visible on either side, city lights behind, string lights, breeze moving potted plant leaves, no people, night quiet",
                "positive_extra": "wine glass on divider, precarious, two apartments, city lights, string lights, breeze, plant leaves, no people, quiet",
                "shot": "close_up",
            },
        ],
    },

    # ==================================================================
    # ACTIVITY/SITUATION (14)
    # ==================================================================

    # ------------------------------------------------------------------
    # 55. sparring_ring — Training got personal
    # ------------------------------------------------------------------
    {
        "key": "sparring_ring",
        "titles": ["Sparring", "Pinned", "Round Two", "On the Mat"],
        "description": "Training session. One-on-one. The gym closed an hour ago.",
        "time": "evening",
        "location": "boxing gym training ring",
        "furniture": ["boxing ring mat", "corner post with rope", "punching bag", "water bottle bench", "hand wraps"],
        "lighting": ["overhead ring light bright", "dark gym beyond ring", "corner shadow", "sweat catching light"],
        "atmosphere": ["sweat", "exertion", "competitive", "adrenaline"],
        "phase_structure": "all_phase2",

        "setup": [
            {
                "scene": "standing in boxing ring corner, one hand on rope, other pulling off boxing glove with teeth, sweat on forehead and arms, overhead ring light bright, dark gym beyond ropes, wrapped hands visible, post-round exhaustion, alert eyes",
                "positive_extra": "boxing ring corner, rope, pulling off glove, sweat, overhead ring light, dark gym, hand wraps, exhausted, alert",
                "shot": "medium",
                "caption": "Round four. The gym emptied an hour ago.",
            },
            {
                "scene": "sitting on ring mat in corner, knees up, water bottle pouring over head cooling down, water running over face and shoulders, ring light above, hand wraps wet, boxing ring ropes visible, catching breath, physical",
                "positive_extra": "ring mat, corner, water over head, face shoulders, ring light, wet wraps, ropes, catching breath",
                "shot": "medium_close",
            },
            {
                "scene": "standing in center of ring, guard stance dropped, hands down, looking at opponent across ring, slight challenging smile, overhead light creating shadows under cheekbones, sweat-sheened skin, ring ropes framing",
                "positive_extra": "center ring, guard dropped, hands down, looking across, challenging smile, overhead shadows, sweat-sheened, ropes",
                "shot": "full_body",
                "dialogue": "One more round. Different rules this time.",
            },
        ],

        "tension": [
            {
                "scene": "grappling on ring mat, hands locked together, face to face, very close, competitive intensity becoming something else, overhead light, sweat between them, ring mat texture visible, dark gym around",
                "positive_extra": "grappling, hands locked, face to face, close, intensity shifting, overhead light, sweat, mat texture, dark gym",
                "shot": "medium_close",
                "dialogue": "That's not a legal hold.",
            },
            {
                "scene": "pressed against ring corner post, ropes on either side, trapped in corner, looking up at standing perspective, one hand still wrapped reaching up gripping rope, sweat everywhere, overhead light, dark gym beyond",
                "positive_extra": "corner post, ropes, trapped, looking up, wrapped hand on rope, sweat, overhead light, dark",
                "shot": "medium",
            },
            {
                "scene": "on ring mat, pinned position, shoulder blades against mat, looking up at overhead ring light, one hand still gripping rope above, chest heaving from exertion, competitive fire in eyes, not giving up not wanting to",
                "positive_extra": "pinned, shoulder on mat, looking at ring light, gripping rope, chest heaving, fire in eyes, not giving up",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face, sweat running down temple, overhead ring light harsh above, eyes locked on viewer, adrenaline-flushed, exertion-parted lips, hand wrap visible at frame edge, line between fighting and something else disappeared",
                "positive_extra": "sweat on temple, ring light harsh, eyes locked, adrenaline-flushed, exertion lips, hand wrap, line disappeared",
                "shot": "close_up",
                "caption": "The bell didn't ring. Nobody was keeping score anymore.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting side by side on ring mat against ropes, legs extended, both breathing hard, water bottles between them, overhead light still on, dark gym, hand wraps being unwound, peaceful post-combat, not looking at each other",
                "positive_extra": "side by side, mat, against ropes, breathing hard, water bottles, overhead light, unwinding wraps, post-combat, not looking",
                "shot": "medium",
            },
            {
                "scene": "close-up of two pairs of boxing gloves left on ring mat, hand wraps beside them tangled together, ring light overhead, mat indent where bodies were, empty ring, dark gym, sweat marks on canvas",
                "positive_extra": "boxing gloves, mat, wraps tangled together, ring light, mat indents, empty ring, sweat marks canvas",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 56. escape_room — Time's up, still locked in
    # ------------------------------------------------------------------
    {
        "key": "escape_room",
        "titles": ["Time's Up", "Locked In", "No Exit", "Solved"],
        "description": "The timer hit zero. The door didn't open. Turns out they didn't mind.",
        "time": "evening",
        "location": "escape room",
        "furniture": ["puzzle table", "padlocked box", "wall of clues", "countdown timer screen", "themed decoration"],
        "lighting": ["red countdown timer glow", "dim atmospheric themed lighting", "UV clue light", "single spotlight on puzzle"],
        "atmosphere": ["tense", "puzzling", "locked in", "ticking"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing at escape room puzzle table, examining clue under UV light, countdown timer showing 5:00 in red on wall, dim themed room, padlocked box on table, wall of codes and clues, concentrating hard",
                "positive_extra": "puzzle table, clue under UV, countdown 5:00, red timer, dim themed room, padlocked box, clue wall, concentrating",
                "shot": "medium",
                "caption": "Five minutes left. Twelve locks solved. One remaining.",
            },
            {
                "scene": "reaching up to high shelf examining clue object, wall of hints and photos behind, red timer counting down visible, themed room decorations around, adrenaline of ticking clock, stretching on tiptoes",
                "positive_extra": "reaching high shelf, clue object, hint wall, red countdown, themed decorations, clock adrenaline, tiptoes",
                "shot": "full_body",
            },
            {
                "scene": "looking at countdown timer hitting 0:00, hands on head in disbelief, red timer now flashing, escape room door still locked, looking at companion, adrenaline still high, laughing at failure, dim atmospheric room",
                "positive_extra": "timer at 0:00, hands on head, disbelief, red flashing, door locked, adrenaline, laughing failure, dim room",
                "shot": "medium_close",
                "dialogue": "Time's up. We're still locked in. Now what?",
            },
        ],

        "tension": [
            {
                "scene": "sitting on puzzle table, legs dangling, timer screen dark now, padlocked box still closed, looking around themed room differently now, no rush, noticing the room itself, atmospheric lighting, locked in together, new energy",
                "positive_extra": "puzzle table, legs dangling, dark timer, locked box, looking around differently, no rush, atmospheric, new energy",
                "shot": "medium",
                "dialogue": "The game master usually opens the door in two minutes. That's two minutes.",
            },
            {
                "scene": "pressed against themed escape room wall, decorative chains and clue papers around, dim atmospheric light, looking at camera with shifted intensity, puzzle abandoned, timer dark, locked room new context",
                "positive_extra": "themed wall, chains, clue papers, dim light, shifted intensity, puzzle abandoned, dark timer, new context",
                "shot": "medium_close",
            },
            {
                "scene": "leaning against locked escape room door, back on door, one hand on handle testing it, looking at approaching camera, dim room behind, timer dark, red ambient light only, knowing they can't get in from outside either",
                "positive_extra": "against locked door, hand testing handle, looking at camera, dim room, dark timer, red ambient, locked both ways",
                "shot": "full_body",
            },
            {
                "scene": "close-up face in dim escape room themed light, timer dead, atmospheric red light, eyes lit up with different kind of puzzle now, excitement redirected, parted lips, clue paper at edge of frame, locked in and choosing to stay",
                "positive_extra": "dim themed light, dead timer, red ambient, eyes lit, excitement redirected, parted lips, clue paper, choosing to stay",
                "shot": "close_up",
                "caption": "The game master's voice crackled through the speaker. They pretended not to hear.",
            },
        ],

        "aftermath": [
            {
                "scene": "escape room door now open, game master's hand visible on handle, standing in room trying to look casual, puzzle table items scattered, timer reset, blinking into normal hallway light from doorway, composing quickly",
                "positive_extra": "door open, game master hand, trying casual, scattered items, timer reset, hallway light, composing",
                "shot": "medium",
            },
            {
                "scene": "close-up of escape room polaroid photo on counter, the before photo at entry, both smiling innocently, escape room name at top, time stamp, next to it the scoreboard showing FAILED, but nobody looks disappointed",
                "positive_extra": "polaroid, before photo, both smiling, escape room name, timestamp, FAILED scoreboard, nobody disappointed",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 57. theme_park_ferris — Stuck at the top
    # ------------------------------------------------------------------
    {
        "key": "theme_park_ferris",
        "titles": ["Stuck", "Top of the World", "Ferris", "The View"],
        "description": "Ferris wheel. Stuck at the top. The park is closing below them.",
        "time": "evening",
        "location": "ferris wheel gondola at top",
        "furniture": ["metal gondola bench", "safety bar", "gondola window frame", "rocking cabin"],
        "lighting": ["theme park lights below", "sunset sky", "gondola interior dim", "ride light bulbs on wheel structure"],
        "atmosphere": ["heights", "swaying", "trapped", "spectacular view"],
        "phase_structure": "reversed",

        "setup": [
            {
                "scene": "sitting in ferris wheel gondola at top, looking down at theme park lights spread below, sunset sky behind, gondola swaying gently, safety bar across lap, hand gripping seat edge, spectacular height, slight nervous excitement",
                "positive_extra": "ferris wheel top, gondola, park lights below, sunset, swaying, safety bar, gripping seat, height, nervous",
                "shot": "medium",
                "caption": "The ferris wheel stopped. They were at the top. The view was worth it.",
            },
            {
                "scene": "standing up in gondola looking out over safety rail, gondola rocking with movement, park stretched below with ride lights and crowds, sunset painting sky orange and pink, wind at height, hair blowing, exhilarated",
                "positive_extra": "standing in gondola, rocking, park below, ride lights, sunset orange pink, wind, hair blowing, exhilarated",
                "shot": "full_body",
            },
            {
                "scene": "looking at fellow rider with concerned amused expression, gondola not moving, park announcement audible faintly from below, stuck at top, sunset beautiful but wheel definitely stopped, safety bar firm across both",
                "positive_extra": "concerned amused, gondola stopped, faint announcement, stuck at top, sunset, wheel stopped, safety bar",
                "shot": "medium_close",
                "dialogue": "I think we're stuck. I think... yeah, we're stuck.",
            },
        ],

        "tension": [
            {
                "scene": "sitting in gondola at top, sunset fading to dusk, park lights getting brighter below, gondola still stopped, safety bar released and pushed up, more room now, looking at companion, time to fill, sky going purple",
                "positive_extra": "gondola top, dusk, park lights brighter, stopped, bar released, more room, sky purple",
                "shot": "medium",
                "dialogue": "Could be worse. Stuck at the top with this view. And you.",
            },
            {
                "scene": "pressed against gondola wall, metal frame behind, park lights below creating upward glow, dusk sky above, tiny swaying cabin, close quarters, looking at camera from cabin corner, wind-blown hair, intimate box in the sky",
                "positive_extra": "gondola wall, metal frame, park glow below, dusk sky, swaying, close quarters, corner, wind-blown, sky box",
                "shot": "medium_close",
            },
            {
                "scene": "lying on gondola bench seat, knees up, looking at emerging stars through gondola frame window, park lights below like city, dusk fading to night, cabin rocking gently in wind, enclosed high above everything",
                "positive_extra": "gondola bench, knees up, emerging stars, gondola frame, park lights below, dusk to night, rocking, high above",
                "shot": "full_body",
            },
            {
                "scene": "close-up face with park lights as bokeh below frame, emerging stars above, dusk purple sky, wind on face, gondola metal frame visible, eyes reflecting park lights, lips parted, suspended between earth and sky",
                "positive_extra": "park lights bokeh, stars above, purple dusk, wind, gondola frame, park in eyes, parted lips, suspended",
                "shot": "close_up",
                "caption": "The wheel jerked. Started moving. They had thirty seconds of descent left.",
            },
        ],

        "aftermath": [
            {
                "scene": "stepping off ferris wheel at bottom, hair windswept, ride operator looking annoyed, other riders waiting impatiently, park lights everywhere at ground level, looking back up at top where they'd been, flushed",
                "positive_extra": "stepping off, windswept, operator annoyed, riders waiting, park lights, looking up at top, flushed",
                "shot": "medium",
            },
            {
                "scene": "close-up of ferris wheel from below, turning again normally, their gondola cycling past at top now empty, park lights twinkling, night sky, ride running smoothly, cotton candy vendor visible at base",
                "positive_extra": "ferris wheel below, turning, empty gondola at top, park lights, night sky, smooth, vendor at base",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 58. haunted_house — Jump scare bonding
    # ------------------------------------------------------------------
    {
        "key": "haunted_house",
        "titles": ["Jump Scare", "Haunted", "Through the Dark", "Scared Close"],
        "description": "Haunted house attraction. She grabbed his arm at the first scare. Never let go.",
        "time": "night",
        "location": "haunted house attraction",
        "furniture": ["fog machine", "strobe corridor", "fake cobwebs", "emergency exit door", "dark hallway corner"],
        "lighting": ["strobe light white flash", "red emergency light", "UV blacklight", "complete darkness between effects"],
        "atmosphere": ["frightening fun", "adrenaline", "grip-tight", "dark corridors"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing at haunted house entrance, fake cobwebs overhead, dim red light inside, fog machine haze at feet, looking into dark entrance nervously excited, hands clasped together, decorations visible, other visitors ahead disappearing into dark",
                "positive_extra": "haunted entrance, cobwebs, red light, fog at feet, nervously excited, clasped hands, decorations, dark ahead",
                "shot": "full_body",
                "caption": "She said she didn't scare easily. That lasted eleven seconds.",
            },
            {
                "scene": "in dark haunted house hallway, grabbed onto companion's arm tight with both hands, wide eyes, strobe light firing behind showing scared laughing face, fake cobwebs everywhere, UV blacklight sections, adrenaline joy",
                "positive_extra": "dark hallway, grabbed arm, wide eyes, strobe, scared laughing, cobwebs, UV sections, adrenaline",
                "shot": "medium_close",
            },
            {
                "scene": "pressed against haunted house wall, hand on chest, catching breath after jump scare, laughing, fake decor around, strobe hallway behind, red emergency light glow, looking at companion with breathless expression",
                "positive_extra": "against wall, hand on chest, catching breath, laughing, fake decor, strobe behind, red light, breathless",
                "shot": "medium",
                "dialogue": "I'm not scared. I just— that one got me. Stay close.",
            },
        ],

        "tension": [
            {
                "scene": "in dark corner of haunted house where attraction turns, between scares, temporary calm, very close together, darkness complete, only faint red exit glow visible, catching breath together, adrenaline making everything heightened",
                "positive_extra": "dark corner, between scares, temporary calm, very close, darkness, faint red exit, catching breath, heightened",
                "shot": "medium_close",
                "dialogue": "I think we lost the group. I think I don't care.",
            },
            {
                "scene": "standing in strobe corridor of haunted house, light freezing motion in white flashes with total dark between, gripping companion, each flash showing them closer, fake cobwebs around, moving through together, intense",
                "positive_extra": "strobe corridor, freezing motion, white flash dark between, gripping, each flash closer, cobwebs, intense",
                "shot": "full_body",
            },
            {
                "scene": "pressed against each other in haunted house dark, found a pocket of darkness between set pieces, props visible but harmless, actors moved past, temporary hiding spot, adrenaline redirecting, UV glow from next room spilling",
                "positive_extra": "pressed together, dark pocket, between set pieces, props visible, actors past, hiding, adrenaline redirecting, UV spill",
                "shot": "medium",
            },
            {
                "scene": "close-up of face lit by single strobe flash, frozen in that instant, eyes wide and alive, adrenaline-flushed, close to another face, haunted house dark around, next flash will show something different, heart pounding visible",
                "positive_extra": "strobe flash, frozen instant, wide alive eyes, adrenaline-flushed, close, dark around, heart pounding",
                "shot": "close_up",
                "caption": "The next scare came. She jumped into him. Neither jumped apart.",
            },
        ],

        "aftermath": [
            {
                "scene": "emerging from haunted house exit into cool night air, blinking at normal light, hair messed from gripping and ducking, still holding onto arm, breathless laughing, theme park lights normal and bright, relief and disappointment mixing",
                "positive_extra": "haunted exit, cool air, blinking, messed hair, still holding arm, breathless laughing, normal lights, mixed feelings",
                "shot": "medium",
            },
            {
                "scene": "close-up of souvenir jump scare photo on screen at exit, captured at peak fright moment, both mid-scream, gripping each other, strobe-lit, haunted house logo on frame, offer to buy it for five dollars, priceless expression",
                "positive_extra": "scare photo, screen, peak fright, mid-scream, gripping, strobe-lit, logo, five dollars, priceless",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 59. yoga_private — Private session, mirrors everywhere
    # ------------------------------------------------------------------
    {
        "key": "yoga_private",
        "titles": ["Private Practice", "Breathe", "Adjusted", "Namaste"],
        "description": "Private yoga session. Studio full of mirrors. The poses are getting closer.",
        "time": "afternoon",
        "location": "yoga studio mirrors",
        "furniture": ["yoga mat", "mirror wall", "block and strap", "incense holder", "bamboo decoration"],
        "lighting": ["warm natural light through sheer curtains", "mirror-doubled light", "candle-like warm studio lighting", "soft diffused glow"],
        "atmosphere": ["calm", "focused", "warm", "body-aware"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing on yoga mat in mirror-walled studio, tree pose, one foot on inner thigh, arms above head, warm natural light through sheer curtains, reflection multiplied in mirrors on three walls, incense smoke thin in air, focused expression",
                "positive_extra": "yoga mat, mirror studio, tree pose, arms above, warm curtain light, reflections multiplied, incense smoke, focused",
                "shot": "full_body",
                "caption": "Private session. One student. One instructor. Fifteen mirrors.",
            },
            {
                "scene": "sitting cross-legged on yoga mat, eyes closed, hands on knees, meditation pose, warm diffused light, mirror behind showing back, incense burning on shelf, studio calm, bamboo decoration, breathing deeply",
                "positive_extra": "cross-legged, mat, eyes closed, meditation, warm light, mirror showing back, incense, calm, breathing deeply",
                "shot": "medium",
            },
            {
                "scene": "in warrior pose on mat, arms extended, front knee bent, back leg straight, looking at direction of front hand, mirror showing pose from side angle, warm light, yoga blocks and straps beside mat, studio quiet",
                "positive_extra": "warrior pose, arms extended, bent knee, straight leg, looking at hand, mirror side view, warm, blocks straps",
                "shot": "full_body",
                "dialogue": "Deeper into the pose. Let your hips open.",
            },
        ],

        "tension": [
            {
                "scene": "in downward dog pose on mat, hands and feet on ground, body forming inverted V, mirror in front showing face, warm light on back, yoga studio calm, muscles engaged visible, warm glow, looking at mirror reflection",
                "positive_extra": "downward dog, inverted V, mirror showing face, warm light on back, muscles engaged, looking at reflection",
                "shot": "medium",
            },
            {
                "scene": "lying on mat in resting pose, one arm extended, body open, warm studio light across body, mirror beside showing duplicate, incense smoke curling, eyes looking at standing figure beside mat, vulnerable open position",
                "positive_extra": "lying on mat, arm extended, open body, warm light, mirror duplicate, incense, looking at figure, vulnerable",
                "shot": "full_body",
                "dialogue": "I can feel the adjustment. Hold it there.",
            },
            {
                "scene": "in deep stretch on mat, body curved, every mirror showing different angle simultaneously, warm light catching sweat on skin, yoga strap on floor nearby, concentration breaking into something else, studio warm",
                "positive_extra": "deep stretch, curved body, mirrors every angle, warm sweat, strap on floor, concentration breaking, warm studio",
                "shot": "medium_close",
            },
            {
                "scene": "close-up face on yoga mat level, mat texture visible, warm side light, mirror just behind showing the scene from behind, eyes half-open focused on viewer, breath steady then not, incense smoke curling past, studio quiet except breathing",
                "positive_extra": "face at mat level, mat texture, warm side light, mirror behind view, half-open eyes, breath unsteady, incense curl, quiet",
                "shot": "close_up",
                "caption": "Namaste. The light held its pose even after they couldn't.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on yoga mat, legs stretched forward, towel around neck, drinking from water bottle, mirror showing relaxed posture, warm light now lower afternoon, studio calm restored, incense burned down to ash, mats slightly out of place",
                "positive_extra": "sitting, legs forward, towel, water, mirror relaxed, lower afternoon, calm, incense ash, mats displaced",
                "shot": "medium",
            },
            {
                "scene": "close-up of yoga mat rolled halfway, strap coiled on top, water ring on studio floor, mirror reflecting empty studio, sheer curtain moving in breeze, warm afternoon light, no people, peaceful absence",
                "positive_extra": "mat half-rolled, strap coiled, water ring, mirror empty studio, curtain breeze, afternoon light, no people",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 60. poker_night — She raised, he called
    # ------------------------------------------------------------------
    {
        "key": "poker_night",
        "titles": ["All In", "The Bluff", "High Stakes", "Poker Face"],
        "description": "Poker night. Everyone else folded hours ago. The stakes got creative.",
        "time": "night",
        "location": "poker table room",
        "furniture": ["green felt poker table", "stacked poker chips", "whiskey glass", "card deck", "overhead table lamp"],
        "lighting": ["green-shade overhead poker lamp", "dim room beyond table", "chip stack shadows", "whiskey amber glow"],
        "atmosphere": ["competitive", "smoky", "strategic", "two-player"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting at green felt poker table, fanning cards close to chest, looking over tops of cards, stacked poker chips in front, overhead green-shade lamp casting pool of light on table, dim room beyond, whiskey glass half-full, empty chairs around table",
                "positive_extra": "poker table, fanning cards, looking over, chip stacks, green lamp, dim room, whiskey, empty chairs",
                "shot": "medium",
                "caption": "The others folded at midnight. It was two now. And so were they.",
            },
            {
                "scene": "pushing stack of poker chips toward center of table, deliberate confident motion, cards face-down on felt, looking at opponent, green overhead light, chip shadows stretching, whiskey amber in glass catching light, competitive smirk",
                "positive_extra": "pushing chips, center table, confident, cards down, looking at opponent, green light, chip shadows, whiskey, smirk",
                "shot": "medium_close",
            },
            {
                "scene": "leaning back in chair, one arm draped over back, legs crossed under poker table, cards held loosely in other hand, chip stack bigger than opponent's, relaxed dominant posture, green lamp light, dark room beyond",
                "positive_extra": "leaning back, arm over chair, legs crossed, cards loose, big chip stack, dominant, green lamp, dark room",
                "shot": "full_body",
                "dialogue": "Out of chips? We could always play for something else.",
            },
        ],

        "tension": [
            {
                "scene": "leaning forward across poker table, elbows on felt, chin on clasped hands, cards fanned out face-down in front, looking at opponent with predatory focus, green overhead light catching eyes, intimate two-person game",
                "positive_extra": "leaning across table, elbows, chin on hands, cards fanned, predatory focus, green light in eyes, two-person",
                "shot": "medium_close",
                "dialogue": "I raise. Your move.",
            },
            {
                "scene": "standing at poker table, hands flat on green felt, leaning over, chip stacks scattered from bold push, cards face-down, overhead lamp swaying slightly casting moving shadows, whiskey glass empty now, all-in energy",
                "positive_extra": "standing, hands on felt, leaning over, scattered chips, lamp swaying, moving shadows, empty glass, all-in",
                "shot": "medium",
            },
            {
                "scene": "sitting on poker table edge, legs on either side of someone's chair, chip stacks knocked over, green felt beneath, overhead lamp illuminating from above, cards scattered, game transformed, dark room around",
                "positive_extra": "on table edge, legs on chair sides, chips knocked, green felt, lamp above, cards scattered, game transformed, dark",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face in green-shade poker lamp light, warm from one direction, face half in green half in shadow, eyes intense and calculating, playing card held near lips, poker chip visible at frame edge, bluffing or not",
                "positive_extra": "green lamp light, half green half shadow, intense calculating eyes, card near lips, chip at edge, bluffing",
                "shot": "close_up",
                "caption": "She showed her hand. He folded anyway.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting back in poker chair, chips gathered in front in massive pile, satisfied grin, whiskey glass refilled, cards face-up on table showing winning hand, loser's empty spot visible across table, green lamp steady",
                "positive_extra": "poker chair, massive chip pile, satisfied, whiskey refilled, winning hand shown, empty opponent spot, green lamp",
                "shot": "medium",
            },
            {
                "scene": "close-up of two cards face-up on green felt poker table, winning hand, poker chips scattered around, whiskey ring stain on felt, green lamp light, empty chairs, game over, one lipstick mark on whiskey glass",
                "positive_extra": "two cards up, green felt, winning hand, scattered chips, whiskey stain, green lamp, empty chairs, lipstick glass",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 61. truth_or_dare — Game went too far
    # ------------------------------------------------------------------
    {
        "key": "truth_or_dare",
        "titles": ["Dare", "Truth", "Your Turn", "No Backing Out"],
        "description": "Truth or dare. Two people left playing. The dares stopped being innocent three rounds ago.",
        "time": "night",
        "location": "apartment floor game night",
        "furniture": ["floor cushions", "empty bottles", "coffee table pushed aside", "blanket on floor", "phone timer"],
        "lighting": ["warm string lights", "candle on floor", "phone screen between them", "dim apartment ambient"],
        "atmosphere": ["playful dangerous", "escalating", "eye contact", "no turning back"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on floor cushion cross-legged, empty bottle lying on side between them from earlier spin, string lights above, candle on floor, apartment cozy, coffee table pushed to wall, couple empty drink bottles around, eye contact across small space",
                "positive_extra": "floor cushion, cross-legged, bottle on side, string lights, candle, apartment cozy, table pushed, eye contact",
                "shot": "medium",
                "caption": "Everyone else left at midnight. The game didn't stop.",
            },
            {
                "scene": "spinning bottle on floor between cushions, looking at it with amused apprehension, candlelight catching spinning glass, blanket on floor visible, string lights warm above, apartment intimate, phone showing dare app open",
                "positive_extra": "spinning bottle, amused apprehension, candlelight on glass, blanket, string lights, intimate, dare app phone",
                "shot": "medium_close",
            },
            {
                "scene": "leaning back on hands on floor cushion, responding to a dare, challenging defiant expression, string lights warm behind head, candle flame visible, apartment floor level view, bottle pointed right at her",
                "positive_extra": "leaning back, floor, challenging defiant, string lights behind, candle, floor level, bottle pointing at her",
                "shot": "full_body",
                "dialogue": "Dare. Obviously. When have I ever picked truth?",
            },
        ],

        "tension": [
            {
                "scene": "on hands and knees on blanket on floor, crawling forward toward camera, dare in progress, string lights above, candle flickering beside, playful dangerous expression, apartment living room turned game room, no going back",
                "positive_extra": "hands and knees, blanket, crawling forward, dare, string lights, candle, playful dangerous, no going back",
                "shot": "medium",
                "dialogue": "You didn't say how close. So I'm choosing.",
            },
            {
                "scene": "sitting on floor facing camera, pulling at clothing hem from a dare, slightly nervous laugh, candle light warm, string lights above, bottle between them, apartment quiet, phone timer visible counting something down",
                "positive_extra": "floor, pulling clothing, nervous laugh, candle warm, string lights, bottle between, quiet, timer counting",
                "shot": "medium_close",
            },
            {
                "scene": "lying on blanket on floor, completing a dare, looking up at ceiling string lights, candle beside at face level casting warm glow, floor cushion under head, apartment warm and close, game gone past the point of stopping",
                "positive_extra": "blanket, floor, completing dare, ceiling string lights, candle at face, cushion, warm close, past stopping",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face lit by candle on floor level, warm orange, eyes looking at camera with the question still hanging, dare or truth doesn't matter anymore, string light dots reflected in pupils, lips slightly parted, the game changed",
                "positive_extra": "candle floor level, warm orange, eyes with question, dare meaningless now, string dots in pupils, parted lips, game changed",
                "shot": "close_up",
                "caption": "She said truth. For the first time all night.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on floor leaning against couch base, cushions scattered around, candle burned low, string lights still on, bottle lying between them, blanket rumpled, apartment quiet, comfortable silence, game officially over",
                "positive_extra": "floor, against couch, scattered cushions, candle low, string lights, bottle between, blanket rumpled, comfortable silence",
                "shot": "medium",
            },
            {
                "scene": "close-up of bottle on floor, no longer spinning, pointing at nothing, candle nearly out, string light reflected in glass, floor cushion dented, phone face-down screen dark, no people visible, game remnants",
                "positive_extra": "bottle still, pointing nowhere, candle nearly out, string in glass, cushion dented, phone dark, game remnants",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 62. photobooth_strip — Strip mall, curtain drawn
    # ------------------------------------------------------------------
    {
        "key": "photobooth_strip",
        "titles": ["Four Frames", "Flash", "Behind the Curtain", "Keep the Strip"],
        "description": "Photobooth. Curtain drawn. Four flashes. What happens between them is unrecorded.",
        "time": "night",
        "location": "photobooth",
        "furniture": ["photobooth bench", "curtain", "camera lens", "payment slot", "screen with timer"],
        "lighting": ["flash white bursts", "screen countdown glow", "strip mall neon through curtain", "LED strip inside"],
        "atmosphere": ["cramped", "playful", "flashing", "candid"],
        "phase_structure": "all_phase1",

        "setup": [
            {
                "scene": "pulling photobooth curtain shut from inside, hand on striped curtain, strip mall visible briefly before curtain closes, cramped bench inside, screen showing READY with countdown, LED strip along top, excited anticipation",
                "positive_extra": "pulling curtain, strip mall glimpse, cramped bench, READY screen, countdown, LED strip, anticipation",
                "shot": "medium",
                "caption": "Four frames. Three dollars. Some things are worth more than the photo.",
            },
            {
                "scene": "sitting on photobooth bench, adjusting position, screen showing face preview, cramped space, curtain closed, LED light from above, laughing at own expression on preview screen, inserting quarters",
                "positive_extra": "photobooth bench, adjusting, screen preview, cramped, curtain closed, LED, laughing at preview, quarters",
                "shot": "medium_close",
            },
            {
                "scene": "squeezing onto photobooth bench together, barely fits two, looking at camera lens, countdown showing 3, getting ready for first flash, cramped shoulder to shoulder, curtain brushing against them, screen lit up",
                "positive_extra": "squeeze on bench, barely fits, looking at lens, countdown 3, cramped shoulder to shoulder, curtain brush, screen lit",
                "shot": "medium",
                "dialogue": "Okay, first one silly. Second one serious. Third and fourth—",
            },
        ],

        "tension": [
            {
                "scene": "flash firing white-bright in photobooth, both squinting laughing from flash, afterimage moment, screen showing countdown to next flash, cramped bench, very close, temporary blindness, warm from being packed in, curtain closed tight",
                "positive_extra": "flash white, squinting laughing, afterimage, countdown to next, cramped, close, warm, curtain tight",
                "shot": "medium_close",
            },
            {
                "scene": "between flashes in photobooth, dark except LED strip and countdown screen, faces very close in tiny space, waiting for next flash, curtain cocoon, no one can see in, countdown ticking, what happens between flashes",
                "positive_extra": "between flashes, dark except LED and countdown, faces close, tiny space, curtain cocoon, hidden, countdown, between flashes",
                "shot": "close_up",
                "dialogue": "We have six seconds until the next flash.",
            },
            {
                "scene": "another flash firing capturing whatever position they're in, white-out bright, cramped photobooth, curtain billowing slightly from movement, screen flashing FLASH 3 OF 4, between posed and candid",
                "positive_extra": "flash 3 firing, white-out, cramped, curtain billowing, screen FLASH 3 OF 4, between posed and candid",
                "shot": "medium",
            },
            {
                "scene": "close-up face illuminated by countdown screen showing 3-2-1, about to get caught by final flash, not posing anymore, eyes locked on viewer not camera, LED glow from above, warm cramped photobooth, last frame",
                "positive_extra": "countdown 3-2-1, about to flash, not posing, eyes on viewer not camera, LED above, warm cramped, last frame",
                "shot": "close_up",
                "caption": "Flash four. The photo strip tells a story. But not the whole one.",
            },
        ],

        "aftermath": [
            {
                "scene": "stepping out of photobooth, pulling curtain open, strip mall light flooding in, disheveled, reaching down to grab photo strip from slot, other hand smoothing hair, blinking in normal light, transitioning from private to public",
                "positive_extra": "stepping out, curtain open, strip mall light, disheveled, grabbing photo strip, smoothing hair, blinking, transition",
                "shot": "medium",
            },
            {
                "scene": "close-up of photo strip in hand, four frames showing progression from silly to close to closer to something private, last frame slightly blurred from movement, photobooth behind, strip mall at night, evidence held",
                "positive_extra": "photo strip, four frames, progression, last frame blurred, photobooth behind, strip mall night, evidence",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 63. swimming_lesson — Private pool, patience wearing thin
    # ------------------------------------------------------------------
    {
        "key": "swimming_lesson",
        "titles": ["Deep End", "Private Lesson", "Treading Water", "The Pool"],
        "description": "Private swimming lesson. The pool echoes. Patience is wearing thin.",
        "time": "evening",
        "location": "indoor swimming pool",
        "furniture": ["pool edge tile", "lane divider", "starting block", "poolside bench", "kickboard"],
        "lighting": ["underwater pool light blue", "steam and moisture in air", "overhead fluorescent reflected in water", "water reflections dancing on ceiling"],
        "atmosphere": ["chlorine", "echoing", "water", "warm humid"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on pool edge, feet in water, creating ripples, indoor pool stretching ahead, lane dividers, underwater lights blue, steam in air, water reflections dancing on ceiling, overhead lights, quiet echoing space, evening lesson",
                "positive_extra": "pool edge, feet in water, ripples, indoor pool, lane dividers, underwater blue, steam, ceiling reflections, echoing",
                "shot": "medium",
                "caption": "Private lesson. Seventh session. She'd stopped pretending she couldn't float.",
            },
            {
                "scene": "standing in shallow end of pool, water at waist, arms out for balance, looking at instructor position, pool light blue from below, water reflections on face, steam in air, tiles visible through clear water",
                "positive_extra": "shallow end, water at waist, arms for balance, pool light from below, water on face, steam, clear tiles",
                "shot": "full_body",
            },
            {
                "scene": "emerging from underwater at pool edge, hands on tile edge, pulling up, water streaming down face and off hair, gasping slightly, pool light blue from behind, looking up at someone standing on deck, water droplets catching light",
                "positive_extra": "emerging, pool edge, hands on tile, pulling up, water streaming, gasping, pool light behind, looking up, droplets",
                "shot": "medium_close",
                "dialogue": "I think I need hands-on instruction for this part.",
            },
        ],

        "tension": [
            {
                "scene": "floating on back in pool, arms out, completely relaxed in water, overhead lights above, water reflections on ceiling, pool blue around, face serene, trust exercise, evening pool session, steam in air, vulnerable floating position",
                "positive_extra": "floating on back, arms out, relaxed, overhead lights, ceiling reflections, pool blue, serene, trust, floating vulnerable",
                "shot": "full_body",
            },
            {
                "scene": "pressed against pool wall in deep end, one arm on pool edge, other in water, looking at camera, water lapping at collar, pool light blue from below illuminating face upward, lane divider beside, treading water energy",
                "positive_extra": "pool wall, deep end, arm on edge, water at collar, pool light from below, upward illumination, lane divider, treading",
                "shot": "medium_close",
                "dialogue": "Teach me something that isn't in the lesson plan.",
            },
            {
                "scene": "sitting on pool edge, legs in water, someone in water between legs at edge, water level at waist of standing person, pool light blue, water reflections everywhere, steam in warm pool air, tiles wet, echoing space silent",
                "positive_extra": "pool edge, legs in water, water at waist, pool light blue, reflections, steam, wet tiles, echoing silent",
                "shot": "medium",
            },
            {
                "scene": "close-up of face emerging from water, water running off in streams, pool light blue from below creating upward glow on features, eyes opening, water droplets on eyelashes, lips parted with water, chlorine air, underwater to surface transition",
                "positive_extra": "emerging from water, water streams, blue upward glow, eyes opening, lash droplets, parted lips water, surface transition",
                "shot": "close_up",
                "caption": "The pool timer buzzed. The session ended. They stayed in the water.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on poolside bench wrapped in towel, feet wet on tile, pool behind now still and glowing blue, overhead lights reflecting, steam thinning, water dripping from hair, peaceful exhaustion, kickboard abandoned at pool edge",
                "positive_extra": "bench, towel, wet feet, pool still blue behind, reflections, steam thin, dripping hair, exhausted, kickboard abandoned",
                "shot": "medium",
            },
            {
                "scene": "close-up of still pool surface reflecting ceiling lights perfectly, undisturbed, kickboard floating slowly across, lane divider still, no swimmers, pool light glowing blue, wet footprints leading to locker room, silent",
                "positive_extra": "still pool, ceiling reflection, kickboard floating, lane divider, no swimmers, blue glow, wet footprints, silent",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 64. detention_room — After school, locked in together
    # ------------------------------------------------------------------
    {
        "key": "detention_room",
        "titles": ["Detention", "After Hours", "Kept Behind", "Time Served"],
        "description": "After-school detention. Two people. The proctor left for coffee twenty minutes ago.",
        "time": "afternoon",
        "location": "school classroom detention",
        "furniture": ["school desk", "chalkboard", "teacher's desk", "clock on wall", "window showing empty campus"],
        "lighting": ["afternoon sun through classroom windows", "buzzing fluorescent tubes", "chalkboard reflection", "golden hour deepening"],
        "atmosphere": ["institutional", "empty school", "afternoon quiet", "bored energy"],
        "phase_structure": "reversed",

        "setup": [
            {
                "scene": "sitting at school desk, chin on arms, staring at clock on wall showing 4:30, afternoon sun through windows making dust visible, empty classroom, chalkboard with assignment written on it, fluorescent buzzing, bored beyond measure",
                "positive_extra": "school desk, chin on arms, clock 4:30, afternoon sun, dust, empty classroom, chalkboard, buzzing, bored",
                "shot": "medium",
                "caption": "Detention. An hour left. The proctor went for coffee. That was twenty minutes ago.",
            },
            {
                "scene": "leaning back in school desk chair, feet up on desk, arms crossed, looking at window showing empty school campus, afternoon golden light, classroom door closed, teacher's desk empty, detention assignment untouched",
                "positive_extra": "leaning back, feet on desk, looking at window, empty campus, golden light, door closed, teacher desk empty, untouched",
                "shot": "full_body",
            },
            {
                "scene": "turned in desk to face other person across room, amused bored expression, pencil balanced on upper lip, afternoon light getting more golden, clock ticking visible, chalkboard behind, both stuck here",
                "positive_extra": "turned in desk, facing other, amused bored, pencil on lip, golden light, clock ticking, chalkboard, stuck",
                "shot": "medium_close",
                "dialogue": "She's not coming back. I've had this proctor before. She forgets.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on teacher's desk at front of room, legs swinging, looking back at classroom from authority position, chalkboard behind with detention rules, afternoon light through windows, clock showing 4:45, bold move",
                "positive_extra": "teacher's desk, legs swinging, looking at classroom, chalkboard rules, afternoon windows, clock 4:45, bold",
                "shot": "medium",
                "dialogue": "Might as well make detention worth it.",
            },
            {
                "scene": "standing at classroom window, looking out at empty school grounds, hand on window latch, afternoon sun golden on face, school desks behind in rows, testing if window opens, breeze coming in",
                "positive_extra": "classroom window, empty grounds, hand on latch, golden sun face, desks behind, testing window, breeze",
                "shot": "medium_close",
            },
            {
                "scene": "sitting on desk surface pushed against wall, knees together, hands gripping desk edge, classroom behind, chalkboard visible, golden hour deepening, clock approaching five, fluorescent off using natural light only",
                "positive_extra": "on desk, against wall, knees together, gripping edge, classroom, chalkboard, golden deepening, clock near five, natural light",
                "shot": "full_body",
            },
            {
                "scene": "close-up face lit by deep golden afternoon through classroom window, dust motes floating, eyes looking upward, desk surface beneath chin, warm institutional light, lips parted, time running out and running over",
                "positive_extra": "deep golden afternoon, classroom window, dust motes, eyes up, desk beneath chin, warm, parted lips, time running",
                "shot": "close_up",
                "caption": "The clock hit five. The door stayed closed. The proctor never came back.",
            },
        ],

        "aftermath": [
            {
                "scene": "walking out classroom door into empty school hallway, looking back into classroom, golden late-afternoon light through hall windows, detention room door open, desks visible inside, school silent, leaving finally",
                "positive_extra": "classroom door, empty hallway, looking back, golden late-afternoon, door open, desks visible, school silent, leaving",
                "shot": "full_body",
            },
            {
                "scene": "close-up of chalkboard with detention assignment, someone has written a reply to it in different handwriting, eraser smudge marks, chalk dust, empty classroom, golden light now almost horizontal, clock showing 5:15, desks slightly rearranged",
                "positive_extra": "chalkboard, reply written, different handwriting, chalk dust, empty, horizontal golden, clock 5:15, desks rearranged",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 65. study_session_midnight — Finals week, lost focus
    # ------------------------------------------------------------------
    {
        "key": "study_session_midnight",
        "titles": ["Cramming", "All-Nighter", "Chapter Nine", "Lost Focus"],
        "description": "Finals week. Midnight study session. The textbook is open but nobody's reading.",
        "time": "night",
        "location": "dorm room study desk",
        "furniture": ["desk piled with books", "desk lamp", "laptop open", "twin bed behind", "energy drink cans"],
        "lighting": ["warm desk lamp cone", "laptop screen glow", "dark room beyond lamp", "hallway light under door"],
        "atmosphere": ["stress", "exhaustion", "midnight oil", "close quarters"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting at desk, forehead resting on open textbook, desk lamp on, laptop open with notes, energy drink cans scattered, pen in limp hand, midnight study exhaustion, small dorm room dark beyond desk lamp cone, books piled",
                "positive_extra": "desk, forehead on textbook, desk lamp, laptop, energy drinks, pen, exhaustion, dark dorm, books piled",
                "shot": "medium",
                "caption": "Chapter nine. For the fourth time. The words stopped making sense at eleven.",
            },
            {
                "scene": "sitting cross-legged on twin bed with textbook, highlighter in hand, notes spread around, desk lamp casting warm light from nearby desk, dark dorm room, laptop with timer showing late hour, oversized study hoodie, tired focused",
                "positive_extra": "on bed, textbook, highlighter, notes spread, desk lamp, dark dorm, laptop timer, hoodie, tired focused",
                "shot": "full_body",
            },
            {
                "scene": "looking up from textbook on bed, hair messy from hours of studying, highlighter behind ear, someone at dorm door with coffee, grateful surprised expression, desk lamp light, energy drink graveyard on desk",
                "positive_extra": "looking up, messy hair, highlighter behind ear, door, coffee, grateful surprised, desk lamp, energy drink graveyard",
                "shot": "medium_close",
                "dialogue": "If that's coffee, I'll do anything. And I mean anything.",
            },
        ],

        "tension": [
            {
                "scene": "both on twin bed with books, bed barely fits studying materials and two people, textbooks open between them, desk lamp light not quite reaching, leaning close to share notes, midnight dorm, door closed",
                "positive_extra": "twin bed, books, barely fits, textbooks between, lamp not reaching, leaning close, sharing, midnight, door closed",
                "shot": "medium",
                "dialogue": "Quiz me on chapter nine. I need to stay awake.",
            },
            {
                "scene": "textbook pushed aside on bed, notes sliding to floor, desk lamp creating warm spot in dark room, energy drink forgotten, laptop screen dimming from inactivity, focus completely shifted, dorm quiet at 1am",
                "positive_extra": "textbook aside, notes sliding, desk lamp warm spot, dark room, laptop dimming, focus shifted, dorm quiet 1am",
                "shot": "medium_close",
            },
            {
                "scene": "lying on twin bed, textbook still somehow open beside, desk lamp creating dramatic side light, notes crumpled beneath, highlighter rolling to floor, dark dorm, laptop screensaver, narrow bed",
                "positive_extra": "lying on bed, textbook open beside, desk lamp side light, crumpled notes, highlighter falling, dark, screensaver, narrow bed",
                "shot": "full_body",
            },
            {
                "scene": "close-up face on dorm bed pillow, desk lamp warm on face, textbook page visible at edge of frame, eyes half-open, study stress dissolved into something else, hair spread on pillow, narrow bed warmth, 2am energy",
                "positive_extra": "face on pillow, desk lamp warm, textbook edge, half-open eyes, stress dissolved, hair on pillow, 2am",
                "shot": "close_up",
                "caption": "The exam was in six hours. They'd figure it out.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting at desk now, textbook open to new chapter, coffee in hand, surprisingly alert, twin bed messy behind, notes reorganized, dawn light starting through small dorm window, laptop open to study notes, productive energy somehow",
                "positive_extra": "desk, new chapter, coffee, alert, messy bed behind, notes organized, dawn window, laptop notes, productive",
                "shot": "medium",
            },
            {
                "scene": "close-up of textbook open to chapter nine, coffee ring stain on page, highlighter marks now covering the material completely, desk lamp still on despite dawn, energy drink cans all empty, alarm clock about to go off",
                "positive_extra": "textbook chapter nine, coffee stain, highlighted fully, lamp on, dawn, empty cans, alarm about to ring",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 66. cooking_class — Hands-on instruction
    # ------------------------------------------------------------------
    {
        "key": "cooking_class",
        "titles": ["Hands-On", "From Scratch", "Taste Test", "A Pinch More"],
        "description": "Private cooking lesson. The recipe was simple. The technique required touch.",
        "time": "evening",
        "location": "cooking class kitchen",
        "furniture": ["butcher block counter", "hanging copper pots", "stove with flame", "mixing bowls", "wine glasses on counter"],
        "lighting": ["warm kitchen pendant lights", "stove flame glow", "copper pot reflections", "wine catching light"],
        "atmosphere": ["aromatic", "hands-on", "warm kitchen", "wine-loosened"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing at butcher block counter, ingredients laid out, hands covered in flour, apron on, looking at recipe card propped against wine glass, warm pendant light above, copper pots hanging behind, private kitchen class",
                "positive_extra": "butcher block, ingredients, flour hands, apron, recipe card, wine glass, pendant light, copper pots, private class",
                "shot": "medium",
                "caption": "The recipe said thirty minutes. The class said two hours. The wine said stay.",
            },
            {
                "scene": "stirring pot on stove, steam rising, one hand on pot handle other holding wooden spoon, flame visible under pot, wine glass half-full nearby, looking over shoulder at instructor position, copper pots reflecting warm light",
                "positive_extra": "stirring pot, steam, handle and spoon, flame, wine nearby, looking over shoulder, copper reflections",
                "shot": "medium_close",
            },
            {
                "scene": "holding out wooden spoon toward camera for taste test, other hand cupped underneath to catch drip, hopeful expression, stove behind still going, apron flour-dusted, warm kitchen light, cooking class intimate feel",
                "positive_extra": "spoon toward camera, taste test, hand catching drip, hopeful, stove, flour apron, warm light, intimate",
                "shot": "medium",
                "dialogue": "Tell me if it needs more... anything.",
            },
        ],

        "tension": [
            {
                "scene": "hands being guided on dough from behind, kneading motion, flour everywhere, butcher block beneath, warm pendant light, wine glasses both less full now, cooking instruction becoming something more tactile, focused on hands",
                "positive_extra": "guided hands, dough, kneading, flour, butcher block, pendant, wine glasses, tactile instruction, focused on hands",
                "shot": "medium_close",
            },
            {
                "scene": "sitting on butcher block counter beside ingredients, legs dangling, wine glass in hand, sauce simmering on stove behind, looking at someone below, apron untied hanging, warm kitchen steam, relaxed from wine and heat",
                "positive_extra": "on counter, legs dangling, wine, sauce simmering, looking down, apron untied, steam, relaxed from wine",
                "shot": "medium",
                "dialogue": "I think the sauce is done. I'm not sure about us.",
            },
            {
                "scene": "pressed against kitchen stove side, warm metal through clothing, wooden spoon abandoned in pot, flour handprint on hip, looking at camera, pendant lights warm above, copper pots reflecting the scene, wine flush visible",
                "positive_extra": "stove side, warm metal, spoon in pot, flour handprint hip, pendant lights, copper reflection, wine flush",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face, flour smudged across cheek and forehead, wine-stained lips slightly parted, warm pendant kitchen light, steam from cooking in background, copper reflection in eyes, completely unguarded and warm",
                "positive_extra": "flour on cheek forehead, wine-stained lips, pendant light, cooking steam, copper in eyes, unguarded, warm",
                "shot": "close_up",
                "caption": "The timer went off. The food was done. They weren't.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting at butcher block eating from the pot directly, shared utensil, wine glasses empty, aprons off, flour everywhere, pendant light warm, copper pots, comfortable post-cooking mess, satisfied from food and more",
                "positive_extra": "eating from pot, shared utensil, empty glasses, aprons off, flour mess, pendant, comfortable, satisfied",
                "shot": "medium",
            },
            {
                "scene": "close-up of flour handprint on butcher block surface, wine ring stain beside, recipe card splattered, wooden spoon resting across pot, kitchen pendant light, no people visible, warm empty kitchen",
                "positive_extra": "flour handprint, butcher block, wine stain, splattered recipe, spoon on pot, pendant, no people, warm empty",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 67. self_defense_lesson — Pinned position, eye contact
    # ------------------------------------------------------------------
    {
        "key": "self_defense_lesson",
        "titles": ["Self Defense", "Escape This", "Pin", "Counter Move"],
        "description": "Self-defense lesson. She was supposed to learn to escape a pin. She stopped trying.",
        "time": "evening",
        "location": "martial arts training studio",
        "furniture": ["training mat", "mirror wall", "punching bag", "equipment rack", "water bottles"],
        "lighting": ["overhead dojo fluorescent", "mirror reflections", "evening through high windows", "mat surface reflecting light"],
        "atmosphere": ["physical", "controlled", "close combat", "breath and movement"],
        "phase_structure": "all_phase2",

        "setup": [
            {
                "scene": "standing on training mat in martial arts studio, hands wrapped, athletic stance, mirror wall behind showing rear view, overhead lights, equipment rack visible, evening light through high windows, focused ready expression",
                "positive_extra": "training mat, wrapped hands, athletic stance, mirror behind, overhead lights, equipment rack, evening, focused",
                "shot": "full_body",
                "caption": "Lesson three. Escape techniques. She was a fast learner. Too fast.",
            },
            {
                "scene": "practicing defensive pose on training mat, arms up in guard, knees slightly bent, looking at training partner through guard, mirror doubling the scene, overhead lights, mat surface, athletic focus, wrapped hands",
                "positive_extra": "defensive pose, guard up, bent knees, looking through guard, mirror doubling, overhead, mat, athletic, wrapped hands",
                "shot": "medium",
            },
            {
                "scene": "post-drill catching breath on mat, one hand on hip, other wiping sweat from forehead, looking at instructor with challenging grin, mirror showing both figures, training equipment around, evening getting darker through windows",
                "positive_extra": "catching breath, hand on hip, wiping sweat, challenging grin, mirror both figures, evening darker, windows",
                "shot": "medium_close",
                "dialogue": "Show me the pin escape again. I want to feel the right leverage.",
            },
        ],

        "tension": [
            {
                "scene": "on training mat in controlled pin position, shoulder blades on mat, looking up at overhead lights, hands positioned to attempt escape but not attempting, mirror beside showing the position, mat surface, physical closeness of technique",
                "positive_extra": "pin position, shoulder on mat, looking up, not escaping, mirror view, mat surface, physical closeness, technique",
                "shot": "medium",
                "dialogue": "I know the escape. I just... forgot. Show me again.",
            },
            {
                "scene": "executing reversal on mat, rolling into top position, pinning from above, looking down, hair falling forward, training intensity in eyes becoming something else, mirror showing the reversal, mat beneath, sweat visible",
                "positive_extra": "reversal, top position, pinning, looking down, hair forward, intensity shifting, mirror reversal, sweat",
                "shot": "medium_close",
            },
            {
                "scene": "both on mat, grappling close, legs tangled, training technique abandoned for something less structured, overhead lights, mirror showing tangled forms, mat surface, breathing hard, not from exertion",
                "positive_extra": "mat, grappling, legs tangled, technique abandoned, overhead, mirror tangled, breathing hard, not exertion",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face on training mat surface, mat texture visible beside cheek, eyes looking at viewer, training sweat and something else flushing skin, hair against mat, overhead light creating sharp shadow, pinned and staying",
                "positive_extra": "face on mat, mat texture, eyes at viewer, sweat and flush, hair on mat, sharp shadow, pinned staying",
                "shot": "close_up",
                "caption": "She knew the escape. She chose not to use it.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on mat back to back, both catching breath, water bottles between legs, mirror showing them from behind, training equipment undisturbed around room, overhead lights, evening gone to full dark through windows, companionable silence",
                "positive_extra": "back to back, catching breath, water bottles, mirror behind view, equipment, overhead, dark windows, silence",
                "shot": "medium",
            },
            {
                "scene": "close-up of two hand wraps unwound and left tangled together on training mat, water bottle knocked over beside, mat surface slightly displaced, mirror showing empty training studio, lights still on, dark outside",
                "positive_extra": "hand wraps tangled, mat, water bottle knocked, mat displaced, mirror empty studio, lights on, dark outside",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 68. dance_class_tango — Bodies too close, music still playing
    # ------------------------------------------------------------------
    {
        "key": "dance_class_tango",
        "titles": ["Tango", "Close Hold", "Last Dance", "Step by Step"],
        "description": "Tango lesson. The music is still playing. They stopped following the steps.",
        "time": "evening",
        "location": "dance studio",
        "furniture": ["polished dance floor", "mirror wall floor to ceiling", "barre", "speaker system", "folding chairs"],
        "lighting": ["warm overhead studio lights", "mirror doubled light", "evening through studio windows", "speaker LED glow"],
        "atmosphere": ["music playing", "rhythmic", "passionate", "close hold"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing at barre in dance studio, one hand on barre, warming up, mirror wall reflecting figure, polished wood dance floor, warm studio lights, speaker system visible playing tango music, folding chairs pushed to wall, evening outside",
                "positive_extra": "barre, warming up, mirror reflection, polished floor, warm lights, speaker, tango music, chairs pushed, evening",
                "shot": "full_body",
                "caption": "Private lesson. The instructor said it takes two to tango. He meant it literally.",
            },
            {
                "scene": "in dance hold position, one arm extended, other on waist, proper tango frame, looking at partner position, mirror showing the pair from behind, polished floor, studio warm light, music playing, learning the form",
                "positive_extra": "dance hold, arm extended, waist, tango frame, mirror pair behind, polished floor, warm light, music, learning",
                "shot": "medium",
            },
            {
                "scene": "mid-tango step, close body contact, looking up through lashes at lead, dance hold intimate, mirror capturing the motion, polished floor reflecting figures, music filling studio, evening light mixing with warm studio light",
                "positive_extra": "mid-step, close body, through lashes, hold intimate, mirror motion, floor reflection, music, evening warm light",
                "shot": "medium_close",
                "dialogue": "Closer. Tango isn't about distance. It's about eliminating it.",
            },
        ],

        "tension": [
            {
                "scene": "in tango dip, back arched, fully supported, looking up at studio ceiling lights, dance hold controlling the position, mirror showing the dramatic pose, polished floor, music reaching crescendo, trust in the hold",
                "positive_extra": "tango dip, arched, supported, looking up, ceiling lights, mirror dramatic pose, polished floor, crescendo, trust",
                "shot": "full_body",
            },
            {
                "scene": "standing chest to chest on dance floor, no longer in proper tango frame, just close, foreheads almost touching, mirror showing them from behind, music slower now, studio warm, hands no longer in dance position",
                "positive_extra": "chest to chest, no proper frame, just close, foreheads near, mirror behind, music slower, hands repositioned",
                "shot": "medium_close",
                "dialogue": "That's not a tango step. I don't care.",
            },
            {
                "scene": "pressed against mirror wall of studio, back against cool glass, reflection behind merging with reality, dance hold transformed, polished floor reflecting, music still playing, studio lights warm, barre at hip height beside",
                "positive_extra": "against mirror, cool glass, reflection merging, hold transformed, floor reflecting, music playing, barre beside",
                "shot": "medium",
            },
            {
                "scene": "close-up of face reflected in studio mirror, real and reflected overlapping, eyes half-closed, music rhythm audible in parted lips, sweat on collarbone, warm light, polished floor reflected, stopped dancing but still moving",
                "positive_extra": "mirror face, real and reflected, half-closed, music on lips, sweat collarbone, warm, stopped dancing still moving",
                "shot": "close_up",
                "caption": "The music ended. The speaker hissed static. Neither heard it.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on polished dance floor, legs extended, leaning against mirror wall, reflection behind, shoes kicked off beside, music stopped speaker silent, studio lights still warm, peaceful exhaustion, folding chairs along wall",
                "positive_extra": "polished floor, legs out, against mirror, shoes off, music stopped, lights warm, peaceful, folding chairs",
                "shot": "medium",
            },
            {
                "scene": "close-up of dance shoes on polished studio floor, one pair proper dance shoes one pair street shoes, speaker system with LED dark, mirror reflecting empty studio, warm lights, no people, music silence",
                "positive_extra": "dance shoes, polished floor, proper and street shoes, speaker dark, mirror empty, warm lights, no people, silence",
                "shot": "close_up",
            },
        ],
    },

    # ==================================================================
    # UNUSUAL/CREATIVE (17)
    # ==================================================================

    # ------------------------------------------------------------------
    # 69. power_outage — Apartment, only candles
    # ------------------------------------------------------------------
    {
        "key": "power_outage",
        "titles": ["Dark", "Candlelight", "Blackout", "Off the Grid"],
        "description": "Power outage across the whole block. Candles and nothing else to do.",
        "time": "night",
        "location": "apartment candlelight",
        "furniture": ["candles on every surface", "couch", "kitchen counter", "window showing dark city", "blanket pile"],
        "lighting": ["candle flames multiple warm", "complete darkness beyond candle radius", "dead city through window", "matchbook flame"],
        "atmosphere": ["candlelit", "silence", "no screens", "stripped back"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing at apartment window, looking out at completely dark city block, no streetlights no building lights, holding lit candle in hand creating reflection in glass, dark apartment behind, eerie total blackout",
                "positive_extra": "apartment window, dark city, no lights, holding candle, glass reflection, dark apartment, total blackout",
                "shot": "medium",
                "caption": "The whole block went dark. Phone at 12%. Nothing to do but wait.",
            },
            {
                "scene": "placing candles around apartment, one on coffee table one on counter one on shelf, multiple warm flames creating cave-like warm glow, everything beyond candlelight completely dark, couch visible in warm flicker, dark apartment transforming",
                "positive_extra": "placing candles, multiple surfaces, warm flames, cave-like glow, dark beyond, couch in flicker, transforming",
                "shot": "full_body",
            },
            {
                "scene": "sitting on couch in candlelit apartment, face lit by nearest candle warm orange, looking at companion in flickering light, phone face-down dead, nothing electronic working, stripped back to basics, dark and warm",
                "positive_extra": "couch, candlelit, nearest candle warm, looking at companion, phone dead, nothing electronic, stripped back, dark warm",
                "shot": "medium_close",
                "dialogue": "No TV. No internet. No lights. What did people even do before electricity?",
            },
        ],

        "tension": [
            {
                "scene": "lying on couch, candle on coffee table beside, face lit from below and side by warm flame, everything else dark, looking at viewer through candlelight, blanket half-over body, dark apartment cocooned by candle warmth",
                "positive_extra": "couch, candle on table, face lit below, warm flame, dark, looking through candlelight, blanket, cocoon",
                "shot": "medium",
                "dialogue": "Turns out I like you better by candlelight.",
            },
            {
                "scene": "standing in dark kitchen, single candle on counter, reaching across to pass something, faces close in small circle of candle warmth, dark apartment around, window showing black city, intimate forced darkness",
                "positive_extra": "dark kitchen, single candle, faces close, small warmth circle, dark apartment, black city window, forced dark",
                "shot": "medium_close",
            },
            {
                "scene": "pressed against wall near candle shelf, multiple candle flames at different heights beside face creating dimensional warm lighting, deep darkness beyond, eyes catching each flame, apartment stripped to elemental warmth",
                "positive_extra": "wall, candle shelf, multiple flames, dimensional lighting, deep dark, eyes catching flames, elemental",
                "shot": "close_up",
            },
            {
                "scene": "close-up face lit by single candle held between them, warm orange glow, candle flame reflected in both eyes, wax dripping visible, lips parted in warm light, darkness absolute beyond flame radius, primal",
                "positive_extra": "single candle between, warm orange, flame in eyes, wax dripping, parted lips, absolute dark beyond, primal",
                "shot": "close_up",
                "caption": "The candles burned lower. Neither moved to light new ones.",
            },
        ],

        "aftermath": [
            {
                "scene": "lying on couch under blanket, last candle burning very low, waxy mess on coffee table, dark apartment, window now showing first streetlight coming back on outside, power returning, last moments of dark",
                "positive_extra": "couch, blanket, last candle low, wax mess, dark, streetlight returning, power coming back, last dark moments",
                "shot": "medium",
            },
            {
                "scene": "close-up of apartment light switch being flipped, but choosing to leave it off, hand on switch visible, candle still burning nearby, streetlights back on outside window, choosing to stay in the dark a little longer",
                "positive_extra": "light switch, choosing off, hand on switch, candle burning, streetlights back, choosing dark, longer",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 70. fire_alarm_hotel — Evacuated in whatever they were wearing
    # ------------------------------------------------------------------
    {
        "key": "fire_alarm_hotel",
        "titles": ["False Alarm", "Floor 14", "Fire Drill", "Underdressed"],
        "description": "Hotel fire alarm at 3am. Evacuated in whatever they were wearing. Which wasn't much.",
        "time": "night",
        "location": "hotel hallway and stairwell",
        "furniture": ["hotel hallway carpet", "stairwell concrete", "emergency blanket", "fire exit door", "ice machine alcove"],
        "lighting": ["flashing fire alarm strobe", "emergency red strip lighting", "stairwell fluorescent", "hotel hallway dim emergency"],
        "atmosphere": ["alarm blaring", "underdressed", "displaced", "adrenaline"],
        "phase_structure": "all_phase2",

        "setup": [
            {
                "scene": "standing in hotel hallway in sleep clothes, fire alarm strobing, red emergency lights, hair disheveled from bed, one shoe on one sock only, looking confused at other evacuating guests, hotel carpet hallway stretching both ways",
                "positive_extra": "hotel hallway, sleep clothes, alarm strobe, red lights, disheveled, one shoe, confused, evacuating",
                "shot": "full_body",
                "caption": "3:07 AM. Fire alarm. Grabbed one shoe and her phone. That was it.",
            },
            {
                "scene": "in hotel stairwell descending, hand on cold metal railing, fluorescent emergency light, concrete stairs, other people above and below, fire alarm echoing in stairwell, barely dressed, cold stairwell air, adrenaline waking",
                "positive_extra": "stairwell, descending, cold railing, fluorescent, concrete, alarm echoing, barely dressed, cold air, adrenaline",
                "shot": "medium",
            },
            {
                "scene": "standing outside hotel in parking lot, arms crossed against cold, fire trucks in background, hotel guests in various states of dress, looking at someone equally underdressed, amused and shivering, alarm still faintly audible",
                "positive_extra": "hotel parking lot, arms crossed cold, fire trucks, guests underdressed, looking at someone, amused shivering, alarm faint",
                "shot": "medium_close",
                "dialogue": "Nice outfit. You always evacuate in a towel?",
            },
        ],

        "tension": [
            {
                "scene": "back inside hotel after all-clear, wrapped in emergency blanket, walking down hallway, alarm off but strobe still blinking, room key held up, looking at companion also blanketed, hotel quiet now, 4am disorientation",
                "positive_extra": "hotel hallway, emergency blanket, alarm off, strobe blinking, room key, companion blanketed, quiet, 4am",
                "shot": "full_body",
                "dialogue": "My room's on fourteen. Yours? ...Also fourteen? Of course.",
            },
            {
                "scene": "standing at hotel ice machine alcove, hidden corner, still in emergency blanket, vending machine hum, dim hotel hallway behind, adrenaline hasn't faded, post-alarm energy, looking at each other in terrible light, close alcove",
                "positive_extra": "ice machine alcove, emergency blanket, vending hum, dim hallway, adrenaline, post-alarm, terrible light, close",
                "shot": "medium_close",
            },
            {
                "scene": "in hotel room now, emergency blanket dropped at door, room dark except bathroom light spilling, hotel bed visible undisturbed, 4am adrenaline making everything sharp, fire alarm adrenaline not quite the same as the new kind",
                "positive_extra": "hotel room, blanket dropped, dark room, bathroom light, bed undisturbed, 4am sharp, adrenaline shifting",
                "shot": "medium",
            },
            {
                "scene": "close-up of face lit by fire alarm strobe still blinking in room from corridor through door crack, intermittent red light, wide awake eyes, 4am alive, hotel pillow behind, adrenaline from alarm redirected completely",
                "positive_extra": "strobe through door crack, intermittent red, wide awake, 4am, hotel pillow, adrenaline redirected",
                "shot": "close_up",
                "caption": "The all-clear sounded. Nobody went back to sleep.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on hotel bed wrapped in sheet, dawn light starting through hotel curtains, emergency blanket on floor, room service card on nightstand, alarm long silent, looking at phone showing 6am, peaceful morning after chaos",
                "positive_extra": "hotel bed, sheet, dawn curtains, emergency blanket floor, room service, alarm silent, phone 6am, peaceful",
                "shot": "medium",
            },
            {
                "scene": "close-up of hotel room door, DO NOT DISTURB sign hanging, hallway now bright with morning light, fire alarm strobe dark and silent, room number visible, emergency blanket balled up outside door, morning after the false alarm",
                "positive_extra": "hotel door, DO NOT DISTURB, morning hallway, alarm dark, room number, emergency blanket outside, morning after",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 71. wrong_hotel_room — Key card opened the wrong door
    # ------------------------------------------------------------------
    {
        "key": "wrong_hotel_room",
        "titles": ["Wrong Room", "Key Card Error", "Room 412", "Check-In"],
        "description": "Hotel key card. Wrong room. Right person inside.",
        "time": "night",
        "location": "hotel room",
        "furniture": ["king hotel bed", "minibar", "desk chair", "bathroom door", "curtain-covered window"],
        "lighting": ["warm bedside lamp", "TV glow paused", "minibar fridge light", "hallway light through closing door"],
        "atmosphere": ["hotel anonymous", "wrong room", "surprise", "sterile becomes intimate"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "stepping into hotel room, door swinging open, hallway light behind, key card in hand that shouldn't have worked, seeing occupied room with warm bedside lamp, luggage visible, someone's shoes by bed, freezing mid-step",
                "positive_extra": "hotel room entry, door open, hallway light, key card, occupied room, bedside lamp, luggage, freezing",
                "shot": "full_body",
                "caption": "Room 412. Her key card said 414. The door opened anyway.",
            },
            {
                "scene": "standing in hotel room doorway, hand still on door handle, apologetic and frozen, room warm with bedside lamp, king bed behind occupant, TV paused, minibar open, intimate domestic scene walked into, hallway light cutting in",
                "positive_extra": "doorway, hand on handle, apologetic, warm lamp, king bed, TV paused, minibar open, domestic, hallway light",
                "shot": "medium",
            },
            {
                "scene": "face-to-face in hotel room entrance, close quarters between bed and desk, key card held up as evidence, other person in robe, amused not angry, hotel room warm and anonymous, door closing on its own behind, hydraulic hiss",
                "positive_extra": "face to face, hotel entrance, key card evidence, robe, amused not angry, anonymous, door closing, hiss",
                "shot": "medium_close",
                "dialogue": "I swear this is what the desk said. 412. Unless I... oh. Oh no.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on edge of wrong hotel bed, trying to explain, key card on bedside table, warm lamp light, room looks the same as own, king bed behind, minibar drinks visible, window curtain heavy, hotel room anonymity",
                "positive_extra": "wrong bed edge, explaining, key card on table, lamp light, same look, minibar, heavy curtain, anonymity",
                "shot": "medium",
                "dialogue": "I really should go. I should definitely go. ...Should I go?",
            },
            {
                "scene": "standing at hotel window, pulling heavy curtain aside revealing city at night, someone else's room viewed from inside, warm lamp one side, city light through window other side, hotel room generic intimate, looking out but thinking in",
                "positive_extra": "hotel window, heavy curtain, city night, someone else's room, lamp warm, city light, generic intimate, thinking in",
                "shot": "full_body",
            },
            {
                "scene": "pressed against hotel room desk, chair pushed aside, minibar open casting blue fridge light from one side, bedside lamp warm from other, hotel room neutral territory, key card on desk beside, neither room is theirs now",
                "positive_extra": "desk, chair aside, minibar blue light, lamp warm other side, neutral territory, key card beside, neither room",
                "shot": "medium_close",
            },
            {
                "scene": "close-up of face on hotel pillow that isn't theirs, unfamiliar but identical, bedside lamp warm, anonymous hotel comfort, looking at viewer, the wrong room became the right one, key card mistake that wasn't",
                "positive_extra": "hotel pillow, unfamiliar identical, lamp warm, anonymous comfort, viewer, wrong became right, key mistake",
                "shot": "close_up",
                "caption": "Room 412 felt exactly like 414. Exactly the same. Completely different.",
            },
        ],

        "aftermath": [
            {
                "scene": "standing at hotel room door, hand on handle, looking back at room, key card in other hand, bedside lamp still on, bed clearly used, about to step into hallway, hesitation visible, own room two doors down",
                "positive_extra": "hotel door, handle, looking back, key card, lamp on, bed used, stepping out, hesitation, own room nearby",
                "shot": "medium",
            },
            {
                "scene": "close-up of two hotel key cards on bedside table side by side, room 412 and room 414 visible on sleeves, bedside lamp warm, hotel phone with message light blinking, no people, dawn through curtain gap",
                "positive_extra": "two key cards, 412 and 414, bedside table, lamp, phone blinking, no people, dawn curtain gap",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 72. masquerade_ball — Can't see faces, don't want to
    # ------------------------------------------------------------------
    {
        "key": "masquerade_ball",
        "titles": ["Masked", "Masquerade", "Behind the Mask", "Unmasked"],
        "description": "Masquerade ball. Can't see faces. Don't want to.",
        "time": "night",
        "location": "masquerade ballroom",
        "furniture": ["marble column", "chandelier ballroom", "balcony alcove", "ornate staircase", "velvet curtain"],
        "lighting": ["chandelier warm cascading", "candle sconce on columns", "moonlight through ballroom windows", "mask shadows on face"],
        "atmosphere": ["opulent", "mysterious", "masked", "anonymous"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing at top of ornate staircase looking down at masquerade ballroom, ornate mask covering upper face, chandelier blazing below, costumed guests dancing, marble columns, candle sconces, holding ballroom gown hem, mysterious entrance",
                "positive_extra": "ornate staircase, masquerade, mask on, chandelier below, costumed guests, marble columns, candle sconces, gown, mysterious",
                "shot": "full_body",
                "caption": "The invitation said come as anyone. She took it literally.",
            },
            {
                "scene": "standing by marble column in ballroom, half-hidden, ornate mask covering eyes and nose, watching dancers through mask eyeholes, chandelier light catching mask details, anonymous in crowd, candle sconce on column behind, mysterious",
                "positive_extra": "marble column, half-hidden, ornate mask, watching through eyeholes, chandelier on mask, anonymous, candle sconce, mysterious",
                "shot": "medium",
            },
            {
                "scene": "turning to face another masked figure at masquerade, both in elaborate masks, only lips and chin visible, chandelier light between them, ballroom behind, can't see faces, choosing not to remove masks, electric recognition without identification",
                "positive_extra": "facing masked figure, elaborate masks, only lips visible, chandelier between, choosing anonymous, electric",
                "shot": "medium_close",
                "dialogue": "Don't tell me your name. I don't want to know yet.",
            },
        ],

        "tension": [
            {
                "scene": "in ballroom balcony alcove behind velvet curtain, masks still on, close together, chandelier light filtering through curtain fabric, ballroom audible but hidden from, marble railing behind, anonymous intimacy, only lower faces visible",
                "positive_extra": "balcony alcove, velvet curtain, masks on, chandelier through fabric, hidden, marble railing, anonymous, lower faces visible",
                "shot": "medium_close",
                "dialogue": "Behind the mask, I could be anyone. That's the point.",
            },
            {
                "scene": "pressed against marble column in quieter corner of ballroom, mask slightly askew showing one eye clearly, chandelier light creating patterns through mask cutouts, candle sconce beside, ballroom spinning behind, intimate column corner",
                "positive_extra": "marble column, corner, mask askew, one eye clear, chandelier through cutouts, candle sconce, column corner",
                "shot": "medium",
            },
            {
                "scene": "on balcony overlooking ballroom, moonlight from outside mixing with chandelier from within, mask on but loosening, looking at camera, masked dancers below as backdrop, ornate railing, velvet curtain beside, beautiful and hidden",
                "positive_extra": "balcony, moonlight and chandelier mix, mask loosening, dancers below, ornate railing, velvet curtain, beautiful hidden",
                "shot": "full_body",
            },
            {
                "scene": "close-up of masked face, ornate mask edge cutting across features, only lips and jaw visible, chandelier light catching mask gold detail, one eye visible through eye hole intense and focused, anonymous desire, the mask is the permission",
                "positive_extra": "masked close-up, mask edge, lips jaw visible, chandelier on gold, one eye intense, anonymous desire, mask as permission",
                "shot": "close_up",
                "caption": "She reached for the mask. He caught her hand.",
            },
        ],

        "aftermath": [
            {
                "scene": "descending ballroom staircase alone, mask now held at side not on face, face fully visible, looking back up at ballroom still masked and dancing, chandelier above, marble stairs, revealed now, the spell broke at midnight",
                "positive_extra": "descending stairs, mask at side, face revealed, looking back, masked ball continuing, chandelier, midnight spell",
                "shot": "full_body",
            },
            {
                "scene": "close-up of ornate mask left on marble column ledge in empty ballroom, chandelier still lit but ballroom empty, candle sconces burning low, no people, mask looking out at empty dance floor, dawn through windows, anonymity discarded",
                "positive_extra": "mask on column, empty ballroom, chandelier, candles low, no people, mask facing dance floor, dawn, discarded",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 73. museum_after_dark — Night security left early
    # ------------------------------------------------------------------
    {
        "key": "museum_after_dark",
        "titles": ["After Hours", "Night at the Museum", "Gallery", "Exhibit A"],
        "description": "Museum after dark. The security guard left early. The art is watching.",
        "time": "night",
        "location": "museum gallery at night",
        "furniture": ["paintings on walls", "gallery bench", "sculpture pedestal", "rope barrier", "parquet floor"],
        "lighting": ["gallery spot lights on art", "security motion sensor light", "exit sign green", "painting illumination warm"],
        "atmosphere": ["silent gallery", "art watching", "reverent space", "after hours"],
        "phase_structure": "reversed",

        "setup": [
            {
                "scene": "standing in dark museum gallery, only painting spotlights on, surrounded by illuminated art in darkness, parquet floor reflecting spots, gallery bench center of room, rope barriers, exit sign green in distance, alone with the art",
                "positive_extra": "dark gallery, painting spotlights, illuminated art, parquet reflections, gallery bench, rope barriers, green exit, alone",
                "shot": "full_body",
                "caption": "The guard clocked out early. She had the Renaissance to herself.",
            },
            {
                "scene": "sitting on gallery bench facing painting, painted figure illuminated by spot, room otherwise dark, quiet reverent space, legs crossed, chin on hand studying art, motion sensor light triggering periodically, parquet floor",
                "positive_extra": "gallery bench, facing painting, spot illuminated, dark room, reverent, chin on hand, motion light, parquet",
                "shot": "medium",
            },
            {
                "scene": "turning from painting hearing footsteps on parquet floor echoing in gallery, surprised, gallery spotlights creating pools of light with darkness between, another person emerging from dark between pools, museum at night intimate",
                "positive_extra": "turning, footsteps echoing, parquet, gallery spots, pools of light, darkness between, figure emerging, museum night",
                "shot": "medium_close",
                "dialogue": "I didn't know anyone else was still here.",
            },
        ],

        "tension": [
            {
                "scene": "standing together before large painting, faces lit by painting spotlight, art illuminating them, dark gallery around, looking at art then at each other, painting between them, museum silence, after-hours permission",
                "positive_extra": "before painting, faces lit by art spot, art illuminating, dark gallery, looking at each other, silence, permission",
                "shot": "medium",
                "dialogue": "This painting is about desire. The curator's notes say 'longing.' Same thing.",
            },
            {
                "scene": "sitting on gallery floor against bench, legs extended on parquet, looking up at painting from below, different perspective than intended, museum dark and quiet, rope barrier pushed aside, rules already broken",
                "positive_extra": "gallery floor, against bench, parquet, looking up at painting, different angle, dark quiet, barrier pushed, rules broken",
                "shot": "full_body",
            },
            {
                "scene": "pressed against gallery wall between two paintings, spot light from each painting creating side lighting, face in warm art glow, museum dark, parquet floor, rope barriers behind, standing where the art hangs",
                "positive_extra": "between paintings, wall, spot side light, art glow face, museum dark, parquet, where art hangs",
                "shot": "medium_close",
            },
            {
                "scene": "close-up of face lit by painting spotlight, warm golden art light, museum dark behind, eyes reflecting the painting, gallery silence, parquet gleaming, face as beautiful as the art, border between audience and subject blurred",
                "positive_extra": "painting spotlight face, warm golden, dark museum, eyes reflecting art, silence, parquet, border blurred",
                "shot": "close_up",
                "caption": "The painted eyes watched. That was their purpose.",
            },
        ],

        "aftermath": [
            {
                "scene": "walking through dark museum toward exit sign, galleries stretching behind, painting spotlights still on illuminating empty rooms, parquet footsteps echoing, motion sensor lights clicking on and off as she passes, leaving the art alone again",
                "positive_extra": "walking to exit, galleries behind, spotlights on empty, parquet echoing, motion sensors clicking, leaving art alone",
                "shot": "full_body",
            },
            {
                "scene": "close-up of gallery bench, slight impression from sitting visible, painting above still illuminated and watching, rope barrier slightly displaced, security camera in corner with red light, no people, gallery holding its breath",
                "positive_extra": "bench impression, painting watching above, barrier displaced, security camera red, no people, holding breath",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 74. aquarium_tunnel — Glass tunnel, blue light, fish above
    # ------------------------------------------------------------------
    {
        "key": "aquarium_tunnel",
        "titles": ["Blue Light", "The Tunnel", "Deep Blue", "Under Glass"],
        "description": "Aquarium glass tunnel. Fish swimming above. Blue light everywhere. Alone after closing.",
        "time": "evening",
        "location": "aquarium glass tunnel",
        "furniture": ["curved glass tunnel wall", "moving walkway stopped", "information plaque", "bench in tunnel", "viewing alcove"],
        "lighting": ["deep aquarium blue from above", "tank illumination through glass", "bioluminescent glow", "fish shadows moving"],
        "atmosphere": ["underwater feeling", "blue everywhere", "silent except water", "deep sea"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing in aquarium glass tunnel, looking up at fish swimming overhead through curved glass ceiling, deep blue light everywhere, water above and around, ray swimming past casting shadow, alone in tunnel, moving walkway stopped, blue world",
                "positive_extra": "glass tunnel, looking up, fish overhead, blue everywhere, water around, ray shadow, alone, walkway stopped, blue world",
                "shot": "full_body",
                "caption": "The aquarium closed. She hadn't found the exit. Didn't try very hard.",
            },
            {
                "scene": "pressing palm against glass tunnel wall, fish gathering at her hand, blue light illuminating hand from behind glass, water world on other side, standing in dry tunnel surrounded by ocean, magical blue glow on face, mesmerized",
                "positive_extra": "palm on glass, fish gathering, blue light behind hand, water world, dry tunnel in ocean, blue glow face, mesmerized",
                "shot": "medium_close",
            },
            {
                "scene": "turning in tunnel seeing someone approaching from other end, blue light on both figures, fish swimming between overhead, tunnel stretching glass and blue, closed aquarium quiet except water hum, surprised then calm",
                "positive_extra": "turning, someone approaching, blue on both, fish between, tunnel glass blue, closed quiet, water hum, calm",
                "shot": "medium",
                "dialogue": "We're the last ones in. I think they forgot about us.",
            },
        ],

        "tension": [
            {
                "scene": "sitting on bench in glass tunnel, fish swimming above and beside, blue light from every angle, water world surrounding, looking at camera through blue-lit underwater atmosphere, tunnel intimate and vast simultaneously, alone at bottom of the sea",
                "positive_extra": "bench, glass tunnel, fish above beside, blue every angle, water world, blue-lit, intimate vast, bottom of sea",
                "shot": "medium",
                "dialogue": "It's like being underwater. Without drowning.",
            },
            {
                "scene": "standing in viewing alcove off main tunnel, deeper blue, larger fish here, pressed against curved glass, fish eye visible close through glass, blue bioluminescent glow, enclosed in glass and water, breathtaking pressure",
                "positive_extra": "viewing alcove, deeper blue, larger fish, against curved glass, fish eye close, bioluminescent, enclosed glass water",
                "shot": "medium_close",
            },
            {
                "scene": "lying on tunnel floor looking up through glass ceiling, entire ocean above, sharks and rays and schools of fish passing, blue light bathing body, tunnel glass curving around, water pressure feeling without the water, small under the sea",
                "positive_extra": "tunnel floor, looking up, ocean above, sharks rays fish, blue bathing, glass curving, feeling pressure, small",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face illuminated entirely in aquarium blue, eyes reflecting fish swimming above, blue light making skin glow, water on other side of glass so close, lips parted, underwater without water, deep blue intimacy",
                "positive_extra": "aquarium blue face, fish reflected in eyes, blue skin glow, glass close, parted lips, underwater without water, deep blue",
                "shot": "close_up",
                "caption": "Under a million gallons of ocean, the world was only blue and breathing.",
            },
        ],

        "aftermath": [
            {
                "scene": "walking out of aquarium tunnel into normal-lit gift shop area, blinking at normal light after blue immersion, looking back at tunnel entrance still glowing blue, fish still swimming, transition from underwater to surface world",
                "positive_extra": "exiting tunnel, gift shop normal light, blinking, looking back, tunnel blue, fish swimming, surface transition",
                "shot": "medium",
            },
            {
                "scene": "close-up of aquarium glass tunnel from outside looking in, blue-lit and empty, school of fish swimming through where they'd been standing, moving walkway still stopped, bench empty, blue world continuing without them",
                "positive_extra": "tunnel from outside, blue empty, fish swimming through, walkway stopped, bench empty, blue continuing",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 75. planetarium_private — Stars projected on everything
    # ------------------------------------------------------------------
    {
        "key": "planetarium_private",
        "titles": ["Starfield", "Planetarium", "Constellations", "Light Years"],
        "description": "Private planetarium showing. Stars projected on everything. Including them.",
        "time": "night",
        "location": "planetarium dome",
        "furniture": ["reclining planetarium chair", "projector pedestal center", "domed ceiling screen", "control panel", "curved wall"],
        "lighting": ["star projection filling dome", "milky way band across ceiling", "projector machine glow", "constellation lines dimly visible"],
        "atmosphere": ["cosmic", "dark with stars", "reclined", "infinite"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting in reclining planetarium chair, head back looking at star projection on domed ceiling, milky way band stretching across, stars on everything including face and body, projector pedestal center casting universe, dark room full of light years",
                "positive_extra": "planetarium chair, reclined, star dome, milky way, stars on face body, projector center, dark with stars",
                "shot": "medium",
                "caption": "Private showing. Population: two. Stars: billions.",
            },
            {
                "scene": "standing in planetarium under dome, arms outstretched, stars projected across arms and face and walls, spinning slowly, milky way across body like a sash, projector humming, cosmic light on skin, small figure under infinite sky",
                "positive_extra": "under dome, arms out, stars projected, spinning, milky way sash, projector hum, cosmic skin, infinite sky",
                "shot": "full_body",
            },
            {
                "scene": "leaning on control panel, looking at domed ceiling where constellation is changing, star light on face making it look like freckles, projector pedestal beside, other chair visible, playing with the universe controls",
                "positive_extra": "control panel, constellation changing, star light freckles, projector beside, other chair, universe controls",
                "shot": "medium_close",
                "dialogue": "I found the controls. Pick a constellation. Any sky you want.",
            },
        ],

        "tension": [
            {
                "scene": "both reclined in planetarium chairs pushed close, looking up at projected stars, galaxy spiral overhead, star projections covering both bodies in celestial light, dark room, cosmic intimacy, universe surrounding them",
                "positive_extra": "reclined chairs close, stars above, galaxy spiral, star projections on bodies, dark, cosmic intimacy, universe",
                "shot": "medium",
                "dialogue": "This is what it's like at the center of the galaxy.",
            },
            {
                "scene": "standing under dome as projection shifts to aurora display, green and purple light washing over face and body, projector creating northern lights, dome ceiling alive with color, magical transformed space, reaching up toward lights",
                "positive_extra": "aurora projection, green purple wash, projector northern lights, dome alive, magical, reaching toward lights",
                "shot": "full_body",
            },
            {
                "scene": "pressed against curved planetarium wall, stars projected across back and wall, looking at camera, cosmic light making everything ethereal, projector creating galaxy on skin, dome curving above, starfield body, universal",
                "positive_extra": "curved wall, stars on back, cosmic light, ethereal, galaxy on skin, dome curving, starfield body, universal",
                "shot": "medium_close",
            },
            {
                "scene": "close-up of face covered in projected stars, each point of light a sun, eyes looking at viewer through galaxies, constellations crossing cheekbone, milky way across lips, cosmic wonder and desire, infinite projected on intimate",
                "positive_extra": "face of stars, each point a sun, eyes through galaxies, constellations on cheek, milky way on lips, infinite on intimate",
                "shot": "close_up",
                "caption": "Every star had a name. They made up new ones.",
            },
        ],

        "aftermath": [
            {
                "scene": "lying in planetarium chairs reclined, projection now showing gentle nebula cloud, softer light, peaceful after cosmic journey, stars still on ceiling but gentle now, projector humming quietly, dome protective above",
                "positive_extra": "reclined, nebula projection, softer light, peaceful, gentle stars, projector quiet, dome protective",
                "shot": "medium",
            },
            {
                "scene": "close-up of projector pedestal still running, tiny stars emerging from machine, dome above still full of universe, chairs empty, control panel lit, private show ending, stars continuing for no audience, cosmic indifference beautiful",
                "positive_extra": "projector running, tiny stars emerging, dome universe, empty chairs, controls lit, show ending, stars continuing, beautiful indifference",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 76. empty_mall_night — Security rounds ended, echoing halls
    # ------------------------------------------------------------------
    {
        "key": "empty_mall_night",
        "titles": ["After Close", "Dead Mall", "Echoes", "Neon and Marble"],
        "description": "Empty mall after midnight. Security done. Just echoes and neon.",
        "time": "night",
        "location": "empty shopping mall at night",
        "furniture": ["escalator stopped", "fountain turned off", "mall bench", "shuttered storefront", "planter with fake plants"],
        "lighting": ["emergency lighting dim", "neon store signs still on", "skylight moonlight", "escalator strip lighting"],
        "atmosphere": ["echoing empty", "liminal", "neon in dark", "vast and vacant"],
        "phase_structure": "mixed",

        "setup": [
            {
                "scene": "standing in empty mall corridor, stores shuttered, dim emergency lighting, neon store signs still glowing, escalator stopped, vast echoing space, skylight showing night sky above, marble floor reflecting neon, alone in consumer cathedral",
                "positive_extra": "empty mall, shuttered stores, dim emergency, neon signs, escalator stopped, echoing, skylight night, marble neon, alone",
                "shot": "full_body",
                "caption": "The last security guard clocked out at midnight. She'd been hiding in the bathroom since eleven.",
            },
            {
                "scene": "sitting on mall fountain edge, fountain empty and off, looking at own reflection in shallow still water, neon store lights reflecting, mall stretching empty behind, escalators still, liminal after-hours, eerie beautiful",
                "positive_extra": "fountain edge, empty fountain, reflection in water, neon reflecting, empty mall, escalators still, liminal, eerie beautiful",
                "shot": "medium",
            },
            {
                "scene": "riding stopped escalator as stairs, looking down at mall floor below, neon lights creating colored pools, emergency lighting dim, someone at bottom of escalator looking up, vast empty space between, echoing greeting",
                "positive_extra": "stopped escalator, looking down, neon pools, emergency dim, someone below, vast empty, echoing",
                "shot": "medium_close",
                "dialogue": "How long have you been in here?",
            },
        ],

        "tension": [
            {
                "scene": "running down empty mall corridor, neon reflections streaking on polished floor, echoes bouncing, escalator strip lights, shuttered stores like audience, childlike freedom in forbidden space, looking back laughing",
                "positive_extra": "running, empty corridor, neon streaking, polished floor, echoes, strip lights, shuttered audience, freedom, laughing",
                "shot": "full_body",
                "dialogue": "Nobody's here! Listen to the echo!",
            },
            {
                "scene": "pressed against shuttered store security gate, metal lattice pattern visible, neon from nearby store sign painting face, mall corridor stretching empty, fountain audible dripping, after-hours energy, forbidden space thrilling",
                "positive_extra": "shuttered gate, metal lattice, neon painting face, empty corridor, fountain drip, after-hours, forbidden thrill",
                "shot": "medium_close",
            },
            {
                "scene": "lying on mall bench, looking up at skylight showing stars, neon signs glowing on either side, vast empty mall stretching in both directions, marble floor reflecting everything, liminal space between day and night",
                "positive_extra": "mall bench, skylight stars, neon both sides, vast empty, marble reflecting, liminal, between day and night",
                "shot": "full_body",
            },
            {
                "scene": "close-up face lit by neon store sign glow, pink and blue, empty mall dark behind, eyes wide exploring, marble reflections beneath, alone in a space meant for thousands, lips parted, exhilarated by the wrongness",
                "positive_extra": "neon glow, pink blue, dark mall, wide eyes exploring, marble beneath, alone in thousands-space, exhilarated wrong",
                "shot": "close_up",
                "caption": "A mall at midnight is a cathedral for two.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on stopped escalator steps, side by side, neon signs starting to turn off one by one, mall getting darker, eating vending machine snacks, legs dangling off escalator edge, dawn somewhere above skylight",
                "positive_extra": "escalator steps, side by side, neon turning off, getting darker, vending snacks, legs dangling, dawn above",
                "shot": "medium",
            },
            {
                "scene": "close-up of empty food court table, two vending machine wrapper balls, mall emergency exit propped open showing dawn, no people, neon all off now, just emergency lights and grey morning, the spell broken",
                "positive_extra": "food court, wrapper balls, exit propped open, dawn, no people, neon off, emergency lights grey, spell broken",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 77. stairwell_between — Between floors, echo chamber
    # ------------------------------------------------------------------
    {
        "key": "stairwell_between",
        "titles": ["Between Floors", "Stairwell", "Echo", "The Landing"],
        "description": "Between floors. Concrete echo chamber. Nobody takes the stairs.",
        "time": "evening",
        "location": "building stairwell",
        "furniture": ["concrete landing", "metal railing", "fire door", "numbered floor sign", "utility pipe"],
        "lighting": ["harsh overhead stairwell light", "emergency strip", "concrete reflecting cold light", "door gap light"],
        "atmosphere": ["echoing concrete", "between spaces", "vertical", "nobody here"],
        "phase_structure": "all_phase1",

        "setup": [
            {
                "scene": "sitting on concrete stairwell landing between floors, back against wall, legs extended across landing, staircase going up and down, harsh overhead light, metal railing, floor number sign on wall, taking a breather, echo-quiet",
                "positive_extra": "concrete landing, between floors, back against wall, staircase up down, harsh light, railing, floor sign, breather",
                "shot": "medium",
                "caption": "Nobody takes the stairs. That was the point.",
            },
            {
                "scene": "leaning over stairwell railing looking down, multiple floors visible spiraling below, overhead lights at each level creating chain of light, concrete walls, vertigo angle, hand tight on cold metal rail, dizzying depth",
                "positive_extra": "leaning over railing, floors spiraling below, chain of lights, concrete, vertigo, hand on rail, dizzying depth",
                "shot": "full_body",
            },
            {
                "scene": "looking up from stairwell landing as fire door opens above, concrete echo, someone entering stairwell, door closing heavy behind them, stairwell light creating harsh shadows, surprised to see another stair-taker, cold concrete around",
                "positive_extra": "looking up, fire door opening, echo, someone entering, door closing, harsh shadows, surprised, cold concrete",
                "shot": "medium_close",
                "dialogue": "Elevator broken too?",
            },
        ],

        "tension": [
            {
                "scene": "standing on concrete landing face to face, stairwell going up behind one going down behind other, cold overhead light, metal railing beside, floor sign between, nowhere to go but up or down, choosing neither, echo chamber",
                "positive_extra": "landing face to face, stairs up and down, cold light, railing, floor sign, nowhere to go, choosing neither, echo",
                "shot": "medium",
                "dialogue": "There's a camera in the elevator. There isn't one here.",
            },
            {
                "scene": "pressed against concrete stairwell wall, cold rough surface, harsh light from above creating sharp downward shadows, metal railing at hip, between floors, echo of every sound amplified, vertical nowhere space",
                "positive_extra": "concrete wall, cold rough, harsh above, sharp shadows, railing at hip, between floors, echo amplified, vertical nowhere",
                "shot": "medium_close",
            },
            {
                "scene": "on concrete stairs between landings, one hand on railing one on wall, stairwell stretching above and below, trapped in vertical space, overhead light harsh, every sound echoing, utilitarian space turned intimate",
                "positive_extra": "concrete stairs, between landings, hand on rail hand on wall, stretching above below, harsh light, echo, utilitarian intimate",
                "shot": "full_body",
            },
            {
                "scene": "close-up face in harsh stairwell overhead light, no flattering about it yet beautiful in the rawness, concrete wall beside face, metal railing reflection on cheek, echo chamber intimacy, parted lips, breathing audible in concrete",
                "positive_extra": "harsh overhead, raw beautiful, concrete beside face, railing reflection, echo chamber, parted lips, breathing audible",
                "shot": "close_up",
                "caption": "Between floors, they existed in a space that belonged to nobody.",
            },
        ],

        "aftermath": [
            {
                "scene": "opening fire door from stairwell into building hallway, normal light and carpet flooding in, looking back at concrete stairwell behind, transition from raw to civilized, composing expression, door slowly closing on heavy hinge",
                "positive_extra": "fire door opening, hallway light carpet, looking back at stairwell, raw to civilized, composing, door closing heavy",
                "shot": "medium",
            },
            {
                "scene": "close-up of fire door fully closed, STAIRS stenciled on it, hallway side normal and carpeted, no indication of what's behind, floor number beside door, everything proper and undisturbed from this side",
                "positive_extra": "fire door closed, STAIRS stencil, hallway normal, no indication, floor number, proper undisturbed, this side",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 78. supply_closet — Quick and hidden
    # ------------------------------------------------------------------
    {
        "key": "supply_closet",
        "titles": ["Supply Room", "Quick", "Behind the Door", "Inventory"],
        "description": "Supply closet. Mop bucket. Five minutes. It's enough.",
        "time": "afternoon",
        "location": "supply closet",
        "furniture": ["shelf of supplies", "mop bucket", "broom against wall", "small stepladder", "paper towel stacks"],
        "lighting": ["single bare bulb with pull chain", "light under door from hallway", "harsh unflattering overhead"],
        "atmosphere": ["cramped", "chemical smell", "hidden", "quick"],
        "phase_structure": "all_phase2",

        "setup": [
            {
                "scene": "opening supply closet door, looking both ways down hallway first, quick glance, hand on door handle, shelves of cleaning supplies visible inside, mop bucket, broom, single bare bulb with pull chain, small cramped space",
                "positive_extra": "supply closet door, looking both ways, hallway, handle, cleaning supplies, mop bucket, broom, bare bulb, cramped",
                "shot": "medium",
                "caption": "Three minutes between meetings. The supply closet was right there.",
            },
            {
                "scene": "standing inside supply closet, pulling someone in by wrist, door closing behind, barely room for two, shelves on every wall, bare bulb swinging from door motion, chemical cleaner smell visible as label, urgent energy",
                "positive_extra": "inside closet, pulling in, door closing, barely room, shelves everywhere, bulb swinging, chemical labels, urgent",
                "shot": "medium_close",
            },
            {
                "scene": "pressed against supply shelf, back to products, facing partner in tiny closet, mop handle between them pushed aside, bare bulb above harsh and unflattering, laughing at the absurdity, pull chain dangling, hallway light under door",
                "positive_extra": "against shelf, products, tiny closet, mop pushed aside, bare bulb harsh, laughing absurdity, chain, hallway light under door",
                "shot": "medium",
                "dialogue": "We have five minutes before anyone notices.",
            },
        ],

        "tension": [
            {
                "scene": "in supply closet, bare bulb pulled off by chain, near darkness, only hallway light under door, cramped pressed together among shelves, hand visible on supply shelf for balance, chemical bottles catching sliver of door light",
                "positive_extra": "bulb off, near dark, door light only, cramped together, shelves, hand for balance, bottles catching light",
                "shot": "medium_close",
            },
            {
                "scene": "pressed against closet door from inside, hand reaching back for door lock, mop bucket nudged aside with foot, bare bulb back on swinging, supply shelves close, urgent and hidden, five minutes counting down",
                "positive_extra": "against door, reaching for lock, mop nudged, bulb swinging, shelves close, urgent hidden, counting down",
                "shot": "medium",
            },
            {
                "scene": "hand gripping supply shelf, knuckles white, cleaning product bottles rattling, bare bulb swinging casting moving shadows in tiny space, mop against wall vibrating, contained chaos, hallway footsteps audible under door",
                "positive_extra": "gripping shelf, white knuckles, bottles rattling, bulb swinging shadows, mop vibrating, contained, footsteps audible",
                "shot": "close_up",
            },
            {
                "scene": "close-up of face in harsh bare bulb light, unflattering but real, eyes wide, lips pressed together suppressing sound, supply shelf products at edge of frame, urgent intensity, hallway right outside, the most alive five minutes",
                "positive_extra": "bare bulb harsh, unflattering real, wide eyes, suppressing sound, products at edge, urgent, hallway outside, alive",
                "shot": "close_up",
                "caption": "A mop fell. They froze. Footsteps outside. Then gone.",
            },
        ],

        "aftermath": [
            {
                "scene": "stepping out of supply closet into bright hallway, smoothing clothes, someone walking past paying no attention, composing face, supply closet door closing behind revealing EMPLOYEES ONLY sign, bare bulb visible dimming inside",
                "positive_extra": "stepping out, bright hallway, smoothing clothes, passerby oblivious, composing, EMPLOYEES ONLY, bulb dimming",
                "shot": "medium",
            },
            {
                "scene": "close-up of supply closet door closed, EMPLOYEES ONLY sign, hallway normal and bright, no indication of anything, except mop bucket visible through gap at door bottom, slightly out of position",
                "positive_extra": "door closed, EMPLOYEES ONLY, normal hallway, no indication, mop bucket gap, slightly displaced",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 79. drive_in_movie — Retro theater, backseat
    # ------------------------------------------------------------------
    {
        "key": "drive_in_movie",
        "titles": ["Drive-In", "Double Feature", "Silver Screen", "Parked"],
        "description": "Drive-in theater. Last screening. The movie's bad. The company isn't.",
        "time": "night",
        "location": "drive-in movie theater",
        "furniture": ["car hood blanket", "steering wheel", "dashboard speaker", "popcorn bag", "truck bed with blankets"],
        "lighting": ["giant projection screen glow", "dashboard light", "neighboring car headlights off", "starfield above"],
        "atmosphere": ["retro", "outdoor cinema", "summer night", "nostalgic"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on truck bed tailgate with blankets, facing giant drive-in screen, movie playing in distance, popcorn bag beside, summer night sky visible above screen, speaker attached to truck, other cars parked but distant, warm night",
                "positive_extra": "truck bed tailgate, blankets, drive-in screen, movie playing, popcorn, summer night sky, speaker, distant cars, warm",
                "shot": "medium",
                "caption": "The drive-in showed double features on Thursdays. The first movie was terrible.",
            },
            {
                "scene": "lying on blankets in truck bed, propped on elbows, watching movie screen, giant image casting changing colored light across face, popcorn scattered, stars visible above screen edge, summer night warm, crickets audible feeling",
                "positive_extra": "truck bed blankets, elbows, movie screen, colored light on face, popcorn, stars above screen, summer warm, crickets",
                "shot": "full_body",
            },
            {
                "scene": "turning from movie screen to look at companion in truck bed, movie forgotten, colored light from screen still changing across both, popcorn between them, blankets rumpled, summer night, private in public space",
                "positive_extra": "turning from screen, companion, colored movie light, popcorn between, blankets, summer night, private in public",
                "shot": "medium_close",
                "dialogue": "This movie is terrible. Want to watch something better?",
            },
        ],

        "tension": [
            {
                "scene": "sitting together in truck bed, blanket shared, movie screen casting blue light behind, nobody paying attention to film, other cars distant and dark, summer night sky full of stars, speaker crackling with bad movie dialogue, intimate outdoor theater",
                "positive_extra": "truck bed together, blanket, screen blue behind, not watching, distant dark cars, stars, speaker crackle, intimate outdoor",
                "shot": "medium",
            },
            {
                "scene": "lying in truck bed under blanket, movie screen enormous behind casting colored wash, looking at sky not screen, stars between movie frames, blankets and pillows, summer warm, speaker turned very low, truck bed cocoon",
                "positive_extra": "truck bed blanket, screen behind, colored wash, looking at sky, stars, pillows, summer warm, speaker low, cocoon",
                "shot": "full_body",
                "dialogue": "Can they see us from the other cars? ...Does it matter?",
            },
            {
                "scene": "pressed against truck cab wall in bed, blanket falling away, giant movie screen light changing from blue to warm to blue behind, intimate lit by cinema, other cars all dark, summer night, drive-in soundtrack distant and irrelevant",
                "positive_extra": "truck cab wall, blanket falling, screen light changing, cinema-lit, other cars dark, summer, soundtrack distant",
                "shot": "medium_close",
            },
            {
                "scene": "close-up of face lit entirely by drive-in movie screen changing colors, blue then warm then blue, eyes not on the screen, looking at viewer, blanket at chin, stars visible past screen edge, summer night warm air, drive-in magic",
                "positive_extra": "movie screen colors, blue warm blue, eyes not on screen, viewer, blanket at chin, stars past screen, summer magic",
                "shot": "close_up",
                "caption": "The second feature started. Neither looked up.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on truck tailgate, legs dangling, drive-in screen now showing THE END in bright white, other cars starting engines, headlights clicking on around, blankets rumpled in truck bed, summer night, popcorn empty, movie over",
                "positive_extra": "tailgate, legs dangling, THE END on screen, cars starting, headlights, blankets rumpled, summer night, movie over",
                "shot": "medium",
            },
            {
                "scene": "close-up of drive-in speaker hanging on truck window, movie over, screen dark now, other cars leaving creating headlight sweep, popcorn bag crumpled on dashboard, summer night still warm, drive-in emptying",
                "positive_extra": "speaker on window, screen dark, cars leaving, headlight sweep, crumpled popcorn, summer warm, emptying",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 80. darkroom_developing — Red light, chemicals, hanging prints
    # ------------------------------------------------------------------
    {
        "key": "darkroom_developing",
        "titles": ["Developing", "Red Light", "Exposure", "Fixed"],
        "description": "Photography darkroom. Red light. Images developing in the tray. Some things can't be un-exposed.",
        "time": "evening",
        "location": "photography darkroom",
        "furniture": ["enlarger machine", "chemical trays three", "drying line with clips", "sink", "safe light"],
        "lighting": ["red safe light only", "enlarger beam when active", "paper glow in developer tray", "complete red monochrome"],
        "atmosphere": ["red monochrome", "chemical", "developing", "emerging image"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing at enlarger in darkroom, adjusting focus, negative in carrier, red safe light only illumination, everything monochrome red, chemical trays lined up on counter, hanging prints on line with clips above, developer smell, concentrated",
                "positive_extra": "enlarger, adjusting, negative, red safe light, monochrome red, chemical trays, hanging prints, clips, concentrated",
                "shot": "medium",
                "caption": "Darkroom hours. No phones. No screens. Just chemistry and red light.",
            },
            {
                "scene": "sliding photo paper into developer tray, watching image appear, fingers in liquid, leaning over tray, red safe light making everything crimson, hanging prints dripping above, other trays beside, magical image emergence",
                "positive_extra": "developer tray, image appearing, fingers in liquid, leaning over, red crimson, dripping prints, magical emergence",
                "shot": "medium_close",
            },
            {
                "scene": "turning from enlarger startled by darkroom door opening carefully, red light flooding hallway crack briefly, someone slipping in quickly, door closing preserving darkness, red world again, close quarters chemical space",
                "positive_extra": "turning, door opening, red on hallway, someone entering, door closing, red world, close quarters, chemical",
                "shot": "medium",
                "dialogue": "Close it quick. You'll fog the paper.",
            },
        ],

        "tension": [
            {
                "scene": "both in darkroom, very close in small space, everything red safe light, standing over chemical tray watching print develop together, image slowly appearing, red-lit faces looking down, hanging prints above creating curtain of images",
                "positive_extra": "both in darkroom, close, red light, over chemical tray, print developing, image appearing, red faces, print curtain",
                "shot": "medium_close",
                "dialogue": "The image takes three minutes to develop. Watch.",
            },
            {
                "scene": "pressed against darkroom counter, chemical trays beside, red safe light only light, everything crimson and shadow, hand wet from developer gripping counter edge, prints hanging at face height creating veil",
                "positive_extra": "against counter, chemical trays, red only, crimson shadow, wet hand gripping, prints at face height, veil",
                "shot": "medium",
            },
            {
                "scene": "standing between hanging prints on drying line, photos hanging all around face like curtain, red safe light making skin glow crimson, each print showing different image, surrounded by frozen moments, looking through prints at camera",
                "positive_extra": "between hanging prints, photos as curtain, red glow crimson, different images, surrounded by moments, looking through",
                "shot": "full_body",
            },
            {
                "scene": "close-up of face in pure red safe light, monochrome crimson, eyes catching the light, developer liquid sheen on fingers near face, chemical smell almost visible, print in tray behind still developing, the image and the reality",
                "positive_extra": "pure red, monochrome crimson, eyes catching light, developer on fingers, chemical, developing print, image and reality",
                "shot": "close_up",
                "caption": "In the developer tray, the image came into focus. Everything else went soft.",
            },
        ],

        "aftermath": [
            {
                "scene": "standing at darkroom door, about to open it, looking back at red-lit room, prints hanging everywhere, chemical trays still, one final print in fixer tray, red world about to become normal light, hesitating at threshold",
                "positive_extra": "darkroom door, about to open, looking back, red-lit, prints hanging, trays still, print in fixer, hesitating, threshold",
                "shot": "medium",
            },
            {
                "scene": "close-up of fresh print hanging on line to dry, image visible in red safe light, the last exposure of the session, clips holding it, other prints beside, darkroom red, chemical droplets falling from corner, nobody in frame",
                "positive_extra": "fresh print, drying line, image in red, last exposure, clips, chemical drops, nobody, darkroom red",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 81. record_store_late — Vinyl and dim lighting
    # ------------------------------------------------------------------
    {
        "key": "record_store_late",
        "titles": ["B-Side", "Vinyl", "Late Night Spins", "Track Two"],
        "description": "Indie record store. Closing up. The turntable is still spinning.",
        "time": "night",
        "location": "record store",
        "furniture": ["vinyl crate bins", "turntable on counter", "album art wall display", "listening station", "neon OPEN sign"],
        "lighting": ["warm pendant track lighting", "neon sign glow", "turntable LED", "album art spotlights"],
        "atmosphere": ["vinyl warmth", "music playing", "analog", "curated"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "flipping through vinyl records in wooden crate, warm pendant light above, record store around with album art on walls, turntable playing on counter in background, neon OPEN sign, dim after-hours vibe, focused browsing, fingers on record edges",
                "positive_extra": "vinyl crates, flipping, pendant light, album art walls, turntable playing, neon OPEN, after-hours, focused, finger edges",
                "shot": "medium",
                "caption": "The record store closed at nine. The turntable didn't care.",
            },
            {
                "scene": "holding vinyl record up, examining album art, warm light catching sleeve, looking at it then at camera, record store shelves behind, turntable counter visible, choosing carefully, music audible in posture, warm cozy shop",
                "positive_extra": "holding vinyl, album art, warm light, looking at camera, shelves, turntable, choosing carefully, music, warm shop",
                "shot": "medium_close",
            },
            {
                "scene": "at listening station with headphones half-on one ear off one ear on, looking at someone approaching, record sleeve in hand, warm record shop, neon sign, pendant lights, albums everywhere, music in one ear conversation in other",
                "positive_extra": "listening station, headphones half-on, looking at approach, sleeve in hand, warm shop, neon, pendants, music one ear",
                "shot": "medium",
                "dialogue": "You have to hear this track. Come here.",
            },
        ],

        "tension": [
            {
                "scene": "sharing headphones at listening station, one earbud each, standing very close, turntable spinning visible, warm shop light, album art walls, nodding to music together, forced proximity, vinyl crackle intimacy",
                "positive_extra": "sharing headphones, one each, very close, turntable spinning, warm light, album art, nodding together, vinyl crackle",
                "shot": "medium_close",
                "dialogue": "Wait for the bridge. It's going to change everything.",
            },
            {
                "scene": "leaning against vinyl crate bin, headphones around neck, looking at camera, record store warm and dim, turntable still spinning, music filling space, neon OPEN sign now turned off, after hours, albums as wallpaper of a life",
                "positive_extra": "against vinyl bin, headphones around neck, warm dim, turntable spinning, music, neon off, after hours, albums wallpaper",
                "shot": "full_body",
            },
            {
                "scene": "pressed against album art display wall, colorful covers beside face, warm pendant light, record spinning on turntable visible in background, vinyl warmth, analog atmosphere, looking at viewer through music",
                "positive_extra": "album art wall, colorful covers, pendant, turntable spinning, vinyl warmth, analog, looking through music",
                "shot": "medium",
            },
            {
                "scene": "close-up face lit by turntable LED and warm pendant, vinyl record spinning reflected in eyes, music audible in expression, warm record shop after hours, album art blurred behind, lips parted listening and feeling, analog intimacy",
                "positive_extra": "turntable LED, pendant, vinyl in eyes, music in expression, after hours, album art blur, listening feeling, analog",
                "shot": "close_up",
                "caption": "The record ended. The needle clicked in the run-out groove. Neither moved to flip it.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on record store floor between vinyl crate bins, headphones on floor beside, turntable needle at end of record clicking, warm light, album they were listening to sleeve visible between them, shop dark outside, quiet after music",
                "positive_extra": "floor, between crates, headphones down, needle clicking, album sleeve between, shop dark, quiet after music",
                "shot": "medium",
            },
            {
                "scene": "close-up of turntable, record finished, needle in run-out groove turning endlessly, warm pendant light on vinyl surface, headphones draped over tone arm, record sleeve propped against turntable, no one, music ended but groove continuing",
                "positive_extra": "turntable, finished record, needle in groove, pendant on vinyl, headphones on arm, sleeve propped, music ended groove continuing",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 82. airport_layover — Red-eye delay, empty terminal
    # ------------------------------------------------------------------
    {
        "key": "airport_layover",
        "titles": ["Delayed", "Terminal", "Red-Eye", "Connecting Flight"],
        "description": "Red-eye delayed indefinitely. Terminal emptied. Just the departure board and two strangers.",
        "time": "night",
        "location": "airport terminal at night",
        "furniture": ["terminal gate seating", "departure board", "floor-to-ceiling window showing tarmac", "closed kiosk", "charging station"],
        "lighting": ["harsh terminal fluorescent", "departure board LED glow", "tarmac orange sodium lights through window", "closed shop neon"],
        "atmosphere": ["transit limbo", "delayed", "in-between", "nowhere place"],
        "phase_structure": "reversed",

        "setup": [
            {
                "scene": "sitting in terminal gate seating, legs across adjacent seats, looking at departure board showing DELAYED in red, empty terminal around, fluorescent lights, floor-to-ceiling windows showing dark tarmac with orange lights, 2am traveler exhaustion",
                "positive_extra": "gate seating, legs across, departure board DELAYED, empty terminal, fluorescent, tarmac lights, 2am exhaustion",
                "shot": "medium",
                "caption": "DELAYED. No estimated departure. The terminal emptied like a theater after the show.",
            },
            {
                "scene": "standing at floor-to-ceiling terminal window, forehead against cold glass, looking at empty tarmac below, orange sodium lights, planes parked dark, own reflection overlaid on night scene, boarding pass crumpled in hand",
                "positive_extra": "terminal window, forehead on glass, tarmac, sodium lights, dark planes, reflection overlay, crumpled boarding pass",
                "shot": "full_body",
            },
            {
                "scene": "looking up from phone at charging station, seeing only other person in terminal section, mutual recognition of shared misery, fluorescent-lit, departure board DELAYED behind both, closed kiosk shuttered, small wave",
                "positive_extra": "charging station, seeing other person, mutual misery, fluorescent, DELAYED behind, shuttered kiosk, small wave",
                "shot": "medium_close",
                "dialogue": "Same flight?",
            },
        ],

        "tension": [
            {
                "scene": "sitting across from each other at terminal gate, feet up on seats, sharing phone charger cord stretched between, departure board still DELAYED, terminal dead quiet, harsh light, tarmac visible dark, strangers becoming less so",
                "positive_extra": "facing at gate, feet up, sharing charger, DELAYED still, terminal quiet, harsh light, dark tarmac, becoming less strange",
                "shot": "medium",
                "dialogue": "Nowhere to go. Nothing to do. Nobody else in the whole terminal.",
            },
            {
                "scene": "walking together down completely empty terminal corridor, closed shops on both sides, fluorescent tube lights stretching ahead, footsteps echoing on polished floor, tarmac windows on one side, exploring the emptiness",
                "positive_extra": "empty corridor, closed shops, fluorescent stretching, footsteps echoing, polished floor, tarmac windows, exploring",
                "shot": "full_body",
            },
            {
                "scene": "pressed against terminal window, cold glass against back, looking at camera, empty gate seating behind, orange tarmac light from behind glass mixing with fluorescent, departure board glow in distance, in-between person in in-between place",
                "positive_extra": "against terminal window, cold glass, empty gates, tarmac orange, fluorescent, departure board distant, in-between",
                "shot": "medium_close",
            },
            {
                "scene": "close-up of face lit by departure board LED glow, red DELAYED text reflected in eyes, terminal fluorescent from above, tired but awake, stranger intimacy, the nowhere quality of airports at 3am making everything possible",
                "positive_extra": "departure board LED, DELAYED in eyes, fluorescent above, tired awake, stranger intimacy, 3am possibility",
                "shot": "close_up",
                "caption": "Between departures, between places, between strangers — the rules dissolve.",
            },
        ],

        "aftermath": [
            {
                "scene": "departure board changing to NOW BOARDING, both standing quickly, grabbing bags, the spell breaking, terminal coming alive with announcement, other delayed passengers appearing from nowhere, real world returning, exchanging a look",
                "positive_extra": "NOW BOARDING, standing, grabbing bags, spell breaking, announcement, passengers appearing, real world, exchanging look",
                "shot": "medium",
            },
            {
                "scene": "close-up of boarding pass with seat number visible, terminal gate now showing BOARDING, phone charger still plugged into station where they sat, no people at the station, boarding line forming in background, the in-between is over",
                "positive_extra": "boarding pass, seat number, BOARDING sign, charger still plugged, empty station, boarding line, in-between over",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 83. phone_booth — Last one in the city, glass walls
    # ------------------------------------------------------------------
    {
        "key": "phone_booth",
        "titles": ["Last Booth", "Glass Walls", "Dial Tone", "Enclosed"],
        "description": "The last phone booth in the city. Glass walls. No phone. Just walls.",
        "time": "night",
        "location": "phone booth city street",
        "furniture": ["glass phone booth walls", "small shelf", "disconnected phone cord", "metal frame", "street outside"],
        "lighting": ["phone booth interior light", "neon from nearby store", "street lamp", "passing car headlights"],
        "atmosphere": ["anachronistic", "glass cage", "visible but enclosed", "city night"],
        "phase_structure": "all_phase1",

        "setup": [
            {
                "scene": "standing inside glass phone booth on city street at night, booth light on making it glow like a lantern, disconnected phone hanging by cord, city visible through glass on all sides, looking out at street, encased in glass and light, anachronistic monument",
                "positive_extra": "glass phone booth, city night, booth light, glowing lantern, phone hanging, city through glass, encased, anachronistic",
                "shot": "full_body",
                "caption": "Last phone booth in the city. The phone's dead. The light still works.",
            },
            {
                "scene": "inside phone booth, picking up disconnected receiver, holding it to ear, no dial tone, looking at dead phone amused, glass walls reflecting city around, booth light making her visible to street, small enclosed space, city rushing past outside",
                "positive_extra": "booth, receiver to ear, dead phone, amused, glass reflecting city, visible to street, small space, city rushing",
                "shot": "medium_close",
            },
            {
                "scene": "looking out phone booth glass at someone on sidewalk, hand on glass wall, booth interior bright, city dark outside, fish-in-aquarium feeling, glass between them, the person approaching the booth door",
                "positive_extra": "looking out glass, hand on wall, bright inside, dark outside, aquarium, glass between, approaching booth door",
                "shot": "medium",
                "dialogue": "There's room for two. Barely. But there is.",
            },
        ],

        "tension": [
            {
                "scene": "two people crammed in glass phone booth, barely fitting, body to body, booth light showing everything to the city but city too busy to look, glass walls on all sides, disconnected phone between them, absurd intimacy",
                "positive_extra": "crammed in booth, body to body, booth light, visible to city, glass walls, phone between, absurd intimacy",
                "shot": "medium_close",
                "dialogue": "Anyone could see us. That's sort of the point.",
            },
            {
                "scene": "pressed against phone booth glass from inside, back on cold glass, city visible through glass around body, booth light illuminating, car headlights sweeping past outside, visible to world that isn't watching, glass cage chosen",
                "positive_extra": "against glass, cold glass, city visible around, booth light, headlights sweep, visible unwatched, glass cage chosen",
                "shot": "medium",
            },
            {
                "scene": "hand pressed flat against phone booth glass, city night visible through and around hand, booth light on, condensation starting on glass from body heat, neon sign visible through glass, enclosed open vulnerable hidden",
                "positive_extra": "hand on glass, city through hand, booth light, condensation, neon through glass, enclosed open vulnerable hidden",
                "shot": "close_up",
            },
            {
                "scene": "close-up of face in phone booth light, glass wall visible beside face with city reflected, booth harsh interior light, eyes looking at viewer, phone cord dangling past frame edge, glass walls making everything private by being completely public",
                "positive_extra": "booth light face, glass city reflection, harsh interior, phone cord, private by being public",
                "shot": "close_up",
                "caption": "The whole city could see. The whole city looked away.",
            },
        ],

        "aftermath": [
            {
                "scene": "stepping out of phone booth door onto sidewalk, cool night air, looking back at lit booth, glass walls still glowing, city flowing past, disconnected phone hanging, leaving the glass cage, normal world resuming",
                "positive_extra": "stepping out, sidewalk, cool air, looking back, booth glowing, city flowing, phone hanging, leaving cage, world resuming",
                "shot": "medium",
            },
            {
                "scene": "close-up of phone booth at night from across street, glowing empty now, glass walls showing empty interior, disconnected phone swinging slightly, city passing in front, nobody inside, a monument to something that connected people",
                "positive_extra": "phone booth from across street, glowing empty, glass empty, phone swinging, city passing, monument, connection",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 84. sauna_private — Wood bench, steam, heat
    # ------------------------------------------------------------------
    {
        "key": "sauna_private",
        "titles": ["Steam Room", "Heat", "Sauna", "Degrees"],
        "description": "Private sauna. Cedar bench. Steam. The heat strips everything down to basics.",
        "time": "evening",
        "location": "private sauna cedar room",
        "furniture": ["cedar bench upper and lower", "hot stones", "wooden bucket with ladle", "thermometer on wall", "cedar door"],
        "lighting": ["dim warm overhead sauna light", "steam diffusing light", "hot stone orange glow", "cedar wood warm tones"],
        "atmosphere": ["extreme heat", "cedar", "steam", "primal"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "sitting on upper cedar bench in sauna, head back against wooden wall, eyes closed, steam rising from hot stones below, dim warm light above, thermometer showing high temperature, wooden bucket and ladle, cedar everywhere, heat visible in the air",
                "positive_extra": "cedar bench upper, head back, eyes closed, steam, hot stones, dim light, thermometer high, bucket ladle, cedar, heat visible",
                "shot": "medium",
                "caption": "Private sauna. The kind of heat that melts pretense.",
            },
            {
                "scene": "pouring water from ladle onto hot stones, massive burst of steam erupting, face visible through steam cloud, orange glow from stones, cedar walls, dim sauna light, the ritual of making more heat, careful intentional motion",
                "positive_extra": "ladle on stones, steam eruption, face through steam, stone glow, cedar walls, dim light, ritual, intentional",
                "shot": "medium_close",
            },
            {
                "scene": "looking at sauna door opening, burst of cool air visible meeting hot air, steam swirling from temperature collision, someone entering, cedar bench visible, hot stones glowing, adjusting to another presence in the small hot room",
                "positive_extra": "door opening, cool air, hot air collision, steam swirling, someone entering, cedar bench, glowing stones, adjusting",
                "shot": "medium",
                "dialogue": "Close the door. You're letting the heat out.",
            },
        ],

        "tension": [
            {
                "scene": "both on cedar bench, steam thick, heat making everything hazy, dim light through steam, hot stones glowing below, sweat visible on skin catching warm light, cedar scent, small wooden room, heat unifying and reducing",
                "positive_extra": "cedar bench, thick steam, hazy, dim through steam, stone glow, sweat catching light, cedar, small room, heat reducing",
                "shot": "medium",
                "dialogue": "In this heat, you stop thinking. You just... are.",
            },
            {
                "scene": "lying on lower cedar bench, steam above like clouds, looking up through steam at upper bench edge, hot stones visible glowing, dim warm light, cedar planks beneath, heat pressing down like a blanket, sweat pooling",
                "positive_extra": "lower bench, steam clouds above, looking up, stone glow, dim warm, cedar planks, heat blanket, sweat pooling",
                "shot": "full_body",
            },
            {
                "scene": "pressed against cedar wall, back on warm wood, steam everywhere, face visible through steam, hot stones glow to one side, dim sauna light, wood grain visible against skin, primal heat, everything simplified by temperature",
                "positive_extra": "cedar wall, warm wood back, steam, face through steam, stone glow, wood grain on skin, primal heat, simplified",
                "shot": "medium_close",
            },
            {
                "scene": "close-up of face in sauna steam, dim warm light making skin glow through sweat, steam curling past face, eyes half-closed from heat, cedar visible at edge, hot stone orange glow reflected, everything stripped to heat and proximity",
                "positive_extra": "face in steam, warm glow through sweat, steam curling, half-closed heat, cedar edge, stone orange, stripped to heat",
                "shot": "close_up",
                "caption": "At that temperature, the body stops pretending.",
            },
        ],

        "aftermath": [
            {
                "scene": "sitting on cedar bench, door cracked open, cool air visible entering mixing with steam, relief on face, thermometer still reading high, bucket empty, sweat-drenched, cooler air touching heated skin, transition from heat to normal",
                "positive_extra": "bench, door cracked, cool air mixing, relief, thermometer high, bucket empty, sweat, cool on heated skin, transition",
                "shot": "medium",
            },
            {
                "scene": "close-up of cedar sauna door from outside, steam escaping through crack, warm dim light visible inside, wooden ladle propped against wall, no people visible, sauna continuing its heat for nobody, cedar and steam",
                "positive_extra": "cedar door, steam escaping, warm dim inside, ladle propped, no people, heat continuing, cedar steam",
                "shot": "close_up",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 85. elevator_stuck — Emergency light, close quarters
    # ------------------------------------------------------------------
    {
        "key": "elevator_stuck",
        "titles": ["Going Down", "Stuck", "Emergency Stop", "Between Floors"],
        "description": "Elevator stopped between floors. Emergency light only. Could be minutes. Could be hours.",
        "time": "night",
        "location": "stuck elevator",
        "furniture": ["elevator handrail", "mirror wall", "floor indicator panel", "emergency phone box", "metal doors"],
        "lighting": ["emergency light dim warm", "floor indicator panel glow", "phone screen glow", "mirror reflecting limited light"],
        "atmosphere": ["confined", "uncertain", "metal box", "close quarters"],
        "phase_structure": "standard",

        "setup": [
            {
                "scene": "standing in elevator that just stopped, grabbing handrail, slight jolt posture, floor indicator showing between 7 and 8, emergency light clicking on, normal lights off, mirror wall showing startled reflection, confined metal space, suddenly still",
                "positive_extra": "elevator stopped, grabbing handrail, jolt, between 7 and 8, emergency light on, mirror startled, confined, suddenly still",
                "shot": "medium",
                "caption": "Between seven and eight. The elevator chose this moment to have an opinion.",
            },
            {
                "scene": "pressing elevator buttons repeatedly, none responding, floor panel dark except emergency, looking at companion in mirror wall reflection, confined space, emergency warm light, metal doors sealed, slight concern, pressing emergency call button",
                "positive_extra": "pressing buttons, not responding, panel dark, mirror reflection, confined, emergency light, sealed doors, pressing call button",
                "shot": "medium_close",
            },
            {
                "scene": "sitting on elevator floor against mirrored wall, legs extended in small space, phone in hand checking signal (none), emergency light above, metal ceiling, handrail at head height, accepting the situation, floor indicator blank",
                "positive_extra": "elevator floor, mirror wall, legs extended, phone no signal, emergency light, metal ceiling, handrail, accepting, blank indicator",
                "shot": "full_body",
                "dialogue": "Maintenance says an hour. Maybe two. No signal down here.",
            },
        ],

        "tension": [
            {
                "scene": "both sitting on elevator floor, facing each other in small square, knees almost touching, emergency light warm above, mirror walls multiplying them infinitely, phone screens the only other light, trapped together, making the best of it",
                "positive_extra": "floor, facing, small square, knees touching, emergency light, mirrors multiplying, phone screens, trapped, best of it",
                "shot": "medium",
                "dialogue": "Of all the elevators in all the buildings. You got in mine.",
            },
            {
                "scene": "standing, pressed against elevator mirrored wall, reflection behind showing infinite regression of reflections, emergency warm light, confined space feeling smaller, handrail at lower back, looking at other person very close",
                "positive_extra": "mirror wall, infinite regression, emergency light, confined smaller, handrail at back, very close",
                "shot": "medium_close",
            },
            {
                "scene": "in elevator looking up at closed metal ceiling, confined from all sides, mirror walls reflecting body from every angle, emergency light warm, small metal room suspended between floors, intimate by force, nowhere to go",
                "positive_extra": "looking up, metal ceiling, confined, mirrors every angle, emergency warm, suspended between, intimate by force, nowhere",
                "shot": "full_body",
            },
            {
                "scene": "close-up face in elevator emergency light, mirror behind showing back of head, confined warm light, metal walls, close quarters made permanent, eyes looking at viewer, lips parted, the small space creating its own gravity",
                "positive_extra": "emergency light face, mirror behind, confined warm, metal walls, permanent close, viewer, parted lips, gravity",
                "shot": "close_up",
                "caption": "Between floors, between moments, the elevator held them in amber.",
            },
        ],

        "aftermath": [
            {
                "scene": "elevator doors opening with mechanical grind, lobby light flooding in, maintenance worker visible, both standing quickly from floor, adjusting clothes and hair, normal world rushing back, confined spell broken by hydraulics",
                "positive_extra": "doors opening, mechanical grind, lobby light, maintenance worker, standing quickly, adjusting, world rushing back, spell broken",
                "shot": "medium",
            },
            {
                "scene": "close-up of elevator floor indicator now showing L for lobby, doors open showing normal lit lobby, emergency light still on inside elevator, mirror walls showing empty car, one dropped earring on elevator floor, maintenance stepping in",
                "positive_extra": "indicator L, doors open, lobby, emergency still on, mirror empty car, dropped earring, maintenance entering",
                "shot": "close_up",
                "caption": "The elevator started working again. As if nothing had happened between seven and eight.",
            },
        ],
    },
]
