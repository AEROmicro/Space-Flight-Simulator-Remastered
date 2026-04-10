import time
import random
import sys


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print(f"  Time on spacewalk: {int(hours)}h {int(mins)}m {sec:.1f}s")


def divider(char="-", width=60):
    print("  " + char * width)


def show_status(fuel, damage, day, score):
    divider()
    fuel_bar   = "#" * max(0, fuel  // 10) + "." * max(0, 10 - fuel  // 10)
    damage_bar = "#" * max(0, damage // 20) + "." * max(0, 10 - damage // 20)
    print(f"  Fuel   [{fuel_bar}] {fuel}%")
    print(f"  Hull   [{damage_bar}] {damage}/200")
    print(f"  Day: {day}   |   Score: {score}")
    divider()


def ask(prompt, valid=None):
    """Prompt until the user gives an accepted answer (case-insensitive)."""
    while True:
        raw = input(f"  > {prompt}: ").strip().lower()
        if valid is None or raw in valid:
            return raw
        print(f"  [!] Please enter one of: {', '.join(str(v) for v in valid)}")


def credits_screen():
    time.sleep(1)
    print()
    divider("=")
    print("  Graphics & Programming by Callum Chang")
    print("  Facts and info from nasa.gov")
    print("  Made for the Game Design merit badge")
    print()
    print("  Thanks for playing!")
    print("  Copyright 2023 AEROforge")
    divider("=")
    time.sleep(3)


def game_over(reason, flight, crew_names):
    cap, name2, name3, name4, name5 = crew_names
    print()
    divider("=")
    print("  *** MISSION FAILED ***")
    print(f"  {reason}")
    print()
    print(f"  Breaking news: The crew of {flight} are lost in space.")
    print(f"  {cap}, {name2}, {name3}, {name4}, and {name5}")
    divider("=")
    credits_screen()
    sys.exit()


def check_game_over(fuel, damage, flight, crew_names):
    if fuel <= 0:
        game_over("You ran out of fuel and were lost in space!", flight, crew_names)
    if damage <= 0:
        game_over("Hull integrity failed — catastrophic decompression!", flight, crew_names)


def countdown(from_n=10):
    for i in range(from_n, 0, -1):
        if i == 7:
            print("  Main engine start")
            time.sleep(0.3)
        elif i == 2:
            print("  Ignition")
            time.sleep(0.5)
        else:
            print(f"  {i}")
        time.sleep(1)
    print("  LIFTOFF!")
    time.sleep(0.5)


# ---------------------------------------------------------------------------
# ASCII art
# ---------------------------------------------------------------------------

AEROFORGE_LOGO = r"""
  * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * .
  . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . *

                            ___________
              _____________/           \
             /                          \________________________
            /                                                    \
           |         A  E  R  O  F  O  R  G  E                   |
           |                                                      |
            \____________________________________________________/
              |__________________________________________________|
                               |         |
                    ___________|         |___________
                   |                                 |
                   |_________________________________|
                                 \     /
                                  \___/

  * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * .
  . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . *
"""

TITLE_ART = r"""
  +==========================================================+
  |                                                          |
  |          *         *    .    *    .    *         *       |
  |       .     *   .                          .   *   .     |
  |                          /\                              |
  |                         /  \                             |
  |                        / /\ \                            |
  |                       |/|  |\|                           |
  |                       | | S| |                           |
  |                       | | F | |                          |
  |                       | | M | |                          |
  |                      /| |___| |\                         |
  |                     / |/     \| \                        |
  |                    /  /       \  \                       |
  |                   /__/ ======= \__\                      |
  |                       |  [#]  |                          |
  |                      /|       |\                         |
  |                     / |  [#]  | \                        |
  |                    (  )       (  )                       |
  |                     \/         \/                        |
  |                                                          |
  |        S P A C E   F L I G H T   M A R S                |
  |                  R E M A S T E R E D                     |
  |                                                          |
  |             Copyright 2023  AEROforge                    |
  |                                                          |
  +==========================================================+
"""


def show_map(flight, position="earth"):
    divider()
    print(f"  Flight map of {flight} mission")
    divider()
    if position == "earth":
        col_earth = "O"
        col_mars  = " "
    else:
        col_earth = " "
        col_mars  = "O"
    print(r"        ______________         /--------------------------------------------\  ")
    print(r"       /     o        \       /         (||) moon               /------\    \  ")
    print(f"       |{{  }}        ^(|      /                           mars  |  {col_mars}   |    /  ")
    print(f"       | {{   }}  {col_earth}  - - - - /                                  \\------/   /  ")
    print(r"       |   {     ^{ \|      /                                                   /  ")
    print(r"       |     \  -----------------------------------------------------------/      ")
    print(r"       |     \\   \|)| earth                                                      ")
    print(f"       \\_____________/     O = {flight}   - = flight path")
    divider()


# ---------------------------------------------------------------------------
# Mini-game: randomised spacewalk repair
# ---------------------------------------------------------------------------

def spacewalk_minigame(cap, name2, name3, name4, name5, fuel, damage, score, difficulty):
    """Randomised spacewalk repair. Returns (fuel, damage, score, bad_count)."""
    print()
    divider("=")
    print("  *** SPACEWALK MINI-GAME ***")
    print("  Guide the astronaut and repair the hydrogen tank.")
    print("  Enter the number for each command shown.")
    divider("=")
    time.sleep(1)

    # Crew selection
    print(f"  1 = {cap}")
    print(f"  2 = {name2}")
    print(f"  3 = {name3}")
    print(f"  4 = {name4}")
    print(f"  5 = {name5}")
    choice = ask("Who goes on the spacewalk? (1-5)", valid=["1","2","3","4","5"])
    crew_list = [cap, name2, name3, name4, name5]
    walker = crew_list[int(choice) - 1]
    print(f"  {walker} suits up and heads outside.")
    time.sleep(1)

    input("  Press Enter to start the spacewalk timer...")
    start_time = time.time()
    bad = 0

    dir_map    = {"left": "1", "stay": "2", "right": "3"}
    dir_prompt = "  1 = left   2 = stay   3 = right"
    n_steps    = 6 + difficulty

    # Phase 1 — navigate to the leak
    print(f"\n  {dir_prompt}")
    sequence = [random.choice(list(dir_map)) for _ in range(n_steps)]
    for cmd in sequence:
        print(f"\n  >> Go {cmd}!")
        time.sleep(0.4)
        ans = ask("Enter (1/2/3)", valid=["1","2","3"])
        if ans == dir_map[cmd]:
            print("  [OK] Correct!")
            score += 10
        else:
            print(f"  [X]  Wrong! (correct was {dir_map[cmd]})")
            fuel   -= 2
            damage -= 10
            bad    += 1
        time.sleep(0.4)

    # Phase 2 — repair tasks (shuffled every run)
    print("\n  --- Repair the hydrogen tank ---")
    task_map  = {"turn": "1", "hammer": "2", "twist": "3", "close": "4"}
    task_list = ["turn", "turn", "twist", "hammer", "twist", "close"]
    random.shuffle(task_list)
    print("  1 = turn   2 = hammer   3 = twist   4 = close")
    time.sleep(2)
    for cmd in task_list:
        print(f"\n  >> {cmd.capitalize()}!")
        time.sleep(0.4)
        ans = ask("Enter (1/2/3/4)", valid=["1","2","3","4"])
        if ans == task_map[cmd]:
            print("  [OK] Correct!")
            score += 15
        else:
            print(f"  [X]  Wrong! (correct was {task_map[cmd]})")
            fuel   -= 2
            damage -= 12
            bad    += 1
        time.sleep(0.4)

    # Phase 3 — navigate back
    print(f"\n  --- Head back to the airlock! ---")
    print(f"  {dir_prompt}")
    return_seq = [random.choice(list(dir_map)) for _ in range(n_steps)]
    for cmd in return_seq:
        print(f"\n  >> Go {cmd}!")
        time.sleep(0.4)
        ans = ask("Enter (1/2/3)", valid=["1","2","3"])
        if ans == dir_map[cmd]:
            print("  [OK] Correct!")
            score += 10
        else:
            print(f"  [X]  Wrong! (correct was {dir_map[cmd]})")
            fuel   -= 2
            damage -= 10
            bad    += 1
        time.sleep(0.4)

    input("\n  Press Enter once safely back inside...")
    time_convert(time.time() - start_time)
    print(f"\n  Spacewalk complete! Mistakes: {bad}")
    time.sleep(2)
    return fuel, damage, score, bad


# ---------------------------------------------------------------------------
# Mini-game: asteroid avoidance
# ---------------------------------------------------------------------------

def asteroid_avoidance(flight, fuel, damage, score, difficulty):
    """Grid-based asteroid dodge game. Returns (fuel, damage, score)."""
    divider("=")
    print("  *** ASTEROID FIELD — EVASIVE MANEUVERS! ***")
    print(f"  {flight}, a dense asteroid field is on the heading.")
    print("  Steer your ship to avoid incoming rocks!")
    divider("=")
    time.sleep(1)
    print("  L = move Left   R = move Right   S = Stay")
    print()
    time.sleep(1)

    n_waves  = 8 + difficulty * 2
    ship_pos = 3          # columns 1-5, start in the middle
    hits     = 0

    for wave in range(1, n_waves + 1):
        # Later waves can have two simultaneous asteroids
        n_rocks = 1 if wave <= n_waves // 2 else random.randint(1, 2)
        rock_cols = random.sample(range(1, 6), n_rocks)

        # Build grid rows
        danger_row = ["  .  "] * 5
        for col in rock_cols:
            danger_row[col - 1] = " *** "
        ship_row = ["  .  "] * 5
        ship_row[ship_pos - 1] = " /^\ "

        print(f"  Wave {wave}/{n_waves}")
        print("  " + "|".join(f"[{g}]" for g in danger_row) + "  <- incoming")
        print("  " + "|".join(f"[{s}]" for s in ship_row)   + "  <- your ship (col {ship_pos})")

        move = ask("Move (L/R/S)", valid=["l","r","s","left","right","stay"])
        move = move[0]
        if move == "l":
            ship_pos = max(1, ship_pos - 1)
        elif move == "r":
            ship_pos = min(5, ship_pos + 1)

        if ship_pos in rock_cols:
            print("  [BOOM] Asteroid hit!")
            damage -= 15
            fuel   -= 3
            score  -= 20
            hits   += 1
        else:
            print("  [OK]   Dodged! Nice flying!")
            score += 20
        print()
        time.sleep(0.6)

    divider()
    if hits == 0:
        print(f"  Outstanding! You dodged all {n_waves} asteroids! +50 bonus!")
        score += 50
    elif hits <= 2:
        print(f"  Good flying! Only {hits} hit(s).")
    else:
        print(f"  Rough ride — {hits} hit(s) sustained.")
    divider()
    time.sleep(2)
    return fuel, damage, score


# ---------------------------------------------------------------------------
# Random transit events
# ---------------------------------------------------------------------------

TRANSIT_EVENTS = [
    {"text": "A micro-meteorite shower peppers the hull.",
     "tip":  "Hull plating absorbed most of the impact.",
     "fuel": 0,  "damage": -15, "day": 0},
    {"text": "Solar flare detected! You increase shielding power.",
     "tip":  "Extra fuel burned to power the shields.",
     "fuel": -5, "damage": 0,   "day": 0},
    {"text": "The crew spots an unidentified satellite of unknown origin.",
     "tip":  "You log the sighting and report to Houston.",
     "fuel": 0,  "damage": 0,   "day": 0},
    {"text": "Navigation computer glitch — course correction required.",
     "tip":  "Two extra days added to the journey.",
     "fuel": -4, "damage": 0,   "day": 2},
    {"text": "You pick up a faint distress signal from deep space.",
     "tip":  "You log it and keep pressing on.",
     "fuel": 0,  "damage": 0,   "day": 0},
    {"text": "Crew morale soars — everyone watches a film on the laptop.",
     "tip":  "A well-rested crew makes better decisions.",
     "fuel": 0,  "damage": 0,   "day": 0},
    {"text": "A fuel line develops a small leak — quickly patched.",
     "tip":  "Quick repair prevents a much larger loss.",
     "fuel": -3, "damage": -5,  "day": 0},
    {"text": "Jupiter slides into view through the observation window. Breathtaking.",
     "tip":  "Sometimes space just rewards you with beauty.",
     "fuel": 0,  "damage": 0,   "day": 0},
    {"text": "A routine engine burn puts you three days ahead of schedule.",
     "tip":  "Burned a little extra fuel but saved travel time.",
     "fuel": -5, "damage": 0,   "day": -3},
    {"text": "A gyroscope fails — backup unit engaged immediately.",
     "tip":  "Backup systems held. That was close.",
     "fuel": -2, "damage": -10, "day": 1},
    {"text": "Unexpected solar wind gives the ship a free velocity boost.",
     "tip":  "Nature just gave you a helping hand.",
     "fuel": 0,  "damage": 0,   "day": -2},
    {"text": "A coolant pipe bursts; crew works fast to contain it.",
     "tip":  "Sealed in time, but hull absorbed some heat.",
     "fuel": -3, "damage": -8,  "day": 0},
]


def random_transit_event(fuel, damage, day, score, flight, crew_names):
    cap = crew_names[0]
    event = random.choice(TRANSIT_EVENTS)
    print()
    divider()
    print("  *** TRANSIT EVENT ***")
    print(f"  {event['text']}")
    print(f"  {event['tip']}")
    fuel   += event["fuel"]
    damage += event["damage"]
    day    += event["day"]
    fuel   = max(0, min(100, fuel))
    damage = max(0, min(200, damage))
    if event["fuel"]   < 0: print(f"  Fuel lost: {abs(event['fuel'])}%")
    if event["damage"] < 0: print(f"  Hull damage: {abs(event['damage'])}")
    if event["day"]   != 0:
        word = "increased" if event["day"] > 0 else "decreased"
        print(f"  Journey time {word} by {abs(event['day'])} day(s).")
    time.sleep(2)
    print(f"  Houston to {flight}: Copy that, {cap}.")
    divider()
    time.sleep(1)
    return fuel, damage, day, score


# ---------------------------------------------------------------------------
# Go / No-Go sequence
# ---------------------------------------------------------------------------

def go_no_go(flight):
    print()
    print(f"  Houston — requesting go/no-go for {flight} launch...")
    time.sleep(0.5)
    for station in ["CAPCOM","FDO","GPO","Booster","EECOM","INCO","MMACS","FLIGHT"]:
        time.sleep(0.5)
        print(f"  {station}: go")
    time.sleep(0.5)
    print(f"  {flight} crew: go")
    time.sleep(1)
    print("  Godspeed.")
    time.sleep(2)


# ---------------------------------------------------------------------------
# Main game
# ---------------------------------------------------------------------------

def main():
    # ── ÆROforge splash ──────────────────────────────────────────────────────
    print(AEROFORGE_LOGO)
    time.sleep(2)
    print(TITLE_ART)
    time.sleep(2)

    print("  Note: the game looks best in a fullscreen terminal.")
    input("  Press Enter to start your flight...")
    time.sleep(1)

    # ── Difficulty ────────────────────────────────────────────────────────────
    print()
    divider()
    print("  Select difficulty:")
    print("  1 = Easy   2 = Normal   3 = Hard")
    diff_choice = ask("Difficulty (1/2/3)", valid=["1","2","3"])
    difficulty  = int(diff_choice) - 1       # 0 / 1 / 2
    diff_name   = {0: "Easy", 1: "Normal", 2: "Hard"}[difficulty]
    print(f"  Difficulty set to: {diff_name}")
    time.sleep(1)

    # ── Starting resources ────────────────────────────────────────────────────
    fuel   = {0: 115, 1: 100, 2: 85}[difficulty]
    damage = 200
    day    = 375
    score  = 0
    bad    = 0

    # ── Crew setup ────────────────────────────────────────────────────────────
    print()
    print("  Building spacecraft...")
    time.sleep(1)
    print("  Gathering samples...")
    time.sleep(1)
    print("  Training crew...")
    time.sleep(1)

    name  = input("  Mission Commander's name: ").strip() or "Commander"
    n     = input("  Mars Module Pilot's name: ").strip() or "Pilot"
    n1    = input("  Command Pilot's name: ").strip()     or "Co-Pilot"
    n2    = input("  Engineer's name: ").strip()           or "Engineer"
    n3    = input("  Civilian's name: ").strip()           or "Civilian"

    cap   = f"Mission Commander {name}"
    name2 = f"Mars Module Pilot {n}"
    name3 = f"Command Pilot {n1}"
    name4 = f"Engineer {n2}"
    name5 = f"Civilian {n3}"
    crew_names = [cap, name2, name3, name4, name5]

    print(f"\n  Your mission starts now, {cap}!")
    time.sleep(1)

    flight = input("  Name your space mission: ").strip() or "Apollo X"
    ship   = input("  Name your recovery ship: ").strip() or "USS Recovery"
    time.sleep(1)

    # ── Mission map (outbound) ────────────────────────────────────────────────
    show_map(flight, "earth")
    time.sleep(3)

    # ── Go / No-Go ────────────────────────────────────────────────────────────
    go_no_go(flight)

    # ── Launch code ───────────────────────────────────────────────────────────
    launch_code = input("  Set your personal launch code: ").strip()
    print()
    print("  We are go for launch in T-minus...")
    time.sleep(1)
    entered = input("  Enter launch code to confirm: ").strip()
    while entered != launch_code:
        print("  [!] Incorrect launch code.")
        entered = input("  Re-enter launch code: ").strip()
    print("  Launch code confirmed.")
    time.sleep(1)

    countdown()
    fuel -= 9
    time.sleep(1)
    print(f"  And we have liftoff of the {flight} mission!")
    time.sleep(3)
    print("  Pressure looks stable.")
    time.sleep(2)
    print(f"  Houston to {flight}: you are exiting Earth's atmosphere.")
    time.sleep(2)

    # ── Fuel boost ────────────────────────────────────────────────────────────
    print("  Do you want to burn extra fuel to accelerate?")
    if ask("yes or no", valid=["yes","no","y","n"]) in ["yes", "y"]:
        fuel -= 5
        day  -= 5
        print("  Fuel burned — you will arrive 5 days sooner.")
    else:
        print("  Conserving fuel — the journey will take a little longer.")
        day += 3
    time.sleep(2)

    # ── Radio contact ─────────────────────────────────────────────────────────
    print(f"\n  Houston to {flight}: please copy.")
    msg = input("  What do you want to say? ").strip()
    print(f"  {flight} to Houston: {msg}")
    time.sleep(1)
    print(f"  Houston to {flight}: thank you for advising.")
    time.sleep(2)

    # ── ISS stop ──────────────────────────────────────────────────────────────
    print(f"\n  Houston to {flight}: do you want to stop at the ISS for rest?")
    if ask("yes or no", valid=["yes","no","y","n"]) in ["yes", "y"]:
        day    += 4
        damage  = min(200, damage + 10)
        print("  Docking with the ISS... the crew rests for 3 days.")
        time.sleep(2)
        print("  Crew is rested. Hull systems inspected.")
    else:
        print("  Continuing to Mars — saving time.")
    time.sleep(2)

    day  += 1
    fuel -= 3
    show_status(fuel, damage, day, score)
    check_game_over(fuel, damage, flight, crew_names)

    # ── Random transit events (outbound) ─────────────────────────────────────
    n_events = 2 + difficulty
    for _ in range(n_events):
        print(f"\n  [Transit — Day {day}]  Traveling to Mars...")
        time.sleep(2)
        fuel, damage, day, score = random_transit_event(
            fuel, damage, day, score, flight, crew_names)
        check_game_over(fuel, damage, flight, crew_names)
        day += random.randint(20, 40)
        show_status(fuel, damage, day, score)

    # ── Asteroid avoidance mini-game ──────────────────────────────────────────
    print(f"\n  Houston to {flight}: asteroid field detected on current heading!")
    time.sleep(2)
    fuel, damage, score = asteroid_avoidance(flight, fuel, damage, score, difficulty)
    check_game_over(fuel, damage, flight, crew_names)
    show_status(fuel, damage, day, score)

    # ── Hydrogen leak / spacewalk ─────────────────────────────────────────────
    print()
    divider("=")
    print("  *** WARNING ***")
    time.sleep(0.5)
    print("  *** WARNING ***")
    time.sleep(0.5)
    print(f"  Collision detected — {name3} takes over!")
    time.sleep(2)
    print(f"  Hydrogen leak in Tank 2!  A spacewalk is required.")
    time.sleep(2)

    fuel, damage, score, bad = spacewalk_minigame(
        cap, name2, name3, name4, name5,
        fuel, damage, score, difficulty)
    day += 2
    check_game_over(fuel, damage, flight, crew_names)
    show_status(fuel, damage, day, score)
    print("  Ship repaired! Continuing to Mars...")
    time.sleep(3)

    # ── Mars orbit entry ──────────────────────────────────────────────────────
    print("  You are now entering Mars orbit.")
    time.sleep(2)
    print(f"  {cap} takes charge.")
    time.sleep(2)
    print("  Beginning the Seven Minutes of Terror...")
    input("  Press Enter to begin Mars entry...")

    # ── Seven minutes of terror ───────────────────────────────────────────────
    print("  Heat shield activated.")
    time.sleep(1)
    for alt in [10000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 700, 500, 200, 100, 50, 25]:
        if alt == 7000:
            input("  Press Enter to deploy parachute...")
            print("  Parachute deployed!")
        if alt == 1000:
            print("  Thrusters engaged!")
        print(f"  {alt} feet")
        time.sleep(0.8 if alt > 1000 else 1)

    time.sleep(3)
    print(f"  *** TOUCHDOWN of the {flight} mission! ***")
    time.sleep(2)
    show_map(flight, "mars")
    time.sleep(1)

    # ── Mars surface ──────────────────────────────────────────────────────────
    msg2 = input("  What do you want to say to Houston? ").strip()
    print(f"  {flight} to Houston: {msg2}")
    time.sleep(1)
    print(f"  Houston to {flight}: thank you for advising.")
    time.sleep(2)
    print("  You suit up and step onto the Martian surface.")
    time.sleep(3)
    print('  "One small step for man, one giant leap for mankind."')
    time.sleep(4)
    print("  You collect samples and plant the flag.")
    time.sleep(2)
    print("  You step back into the rocket.")
    time.sleep(1)
    print(f"  {name4} reports mission status:")
    show_status(fuel, damage, day, score)

    # ── Mars launch ───────────────────────────────────────────────────────────
    input("  Press Enter to launch from Mars...")
    print("  Houston, we are go for Mars launch in T-minus...")
    time.sleep(1)
    countdown()
    fuel -= 10
    time.sleep(1)
    print(f"  The {flight} is leaving Mars and heading home!")
    time.sleep(3)

    # ── Return journey ────────────────────────────────────────────────────────
    day  += 175
    fuel -= 25
    print(f"\n  [Return journey — Day {day}]")
    time.sleep(1)

    for _ in range(1 + (difficulty // 2)):
        fuel, damage, day, score = random_transit_event(
            fuel, damage, day, score, flight, crew_names)
        check_game_over(fuel, damage, flight, crew_names)
        show_status(fuel, damage, day, score)

    check_game_over(fuel, damage, flight, crew_names)

    # ── Earth re-entry ────────────────────────────────────────────────────────
    print(f"\n  You are now approaching Earth.")
    print(f"  {name5} takes over.")
    time.sleep(1)
    print("  Approaching the blackout zone...")
    time.sleep(1)
    print("  We expect ----------------------------")
    for _ in range(5):
        print("  ---------------------------------------")
        time.sleep(0.3)
    print("  You are in the blackout zone — all comms cut.")
    time.sleep(2)
    print("  Deploying heat shield.")
    time.sleep(1)

    for alt in [10000, 8000, 6000, 4000, 3000, 2500, 2000, 1000, 500, 250, 100, 50]:
        if alt == 6000:
            print("  Parachute deployed!")
        if alt == 2000:
            print("  Buoy inflating!")
        print(f"  {alt} feet")
        time.sleep(0.8)

    time.sleep(4)
    print("  *** Water landing successful! ***")
    time.sleep(2)
    print(f"  The {ship} has recovered all five astronauts.")
    time.sleep(3)

    # ── Final summary ─────────────────────────────────────────────────────────
    if bad == 0:
        score += 200
    elif bad <= 3:
        score += 100

    divider("=")
    print(f"  *** MISSION COMPLETE — {flight} ***")
    print()
    print(f"  {cap}, {name2}, {name3}, {name4}, and {name5}")
    print(f"  are safe after the {flight} mission.")
    print()
    print(f"  Mission duration : {day} days")
    print(f"  Fuel remaining   : {fuel}%")
    print(f"  Hull integrity   : {damage}/200")
    print(f"  Spacewalk errors : {bad}")
    print(f"  Final score      : {score}")
    print()

    if   score >= 500: rating = "S  — Outstanding Mission!"
    elif score >= 350: rating = "A  — Excellent Mission"
    elif score >= 200: rating = "B  — Good Mission"
    elif score >= 100: rating = "C  — Mission Accomplished"
    else:              rating = "D  — Rough Mission"
    print(f"  Rating: {rating}")
    divider("=")

    time.sleep(3)
    print(f"\n  Breaking news: All five astronauts safe after {flight} mission!")
    time.sleep(3)
    credits_screen()


if __name__ == "__main__":
    main()
