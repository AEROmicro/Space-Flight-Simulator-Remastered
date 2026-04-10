import time
import random
import sys


# ═══════════════════════════════════════════════════════════════════════════════
#  STATIC DATA
# ═══════════════════════════════════════════════════════════════════════════════

SHIP_CLASSES = {
    "1": {
        "name": "Ares-1 Heavy Lifter",
        "fuel": 120, "hull": 220, "day_bonus": 12,
        "desc": "Massive fuel capacity and reinforced hull plates. Slow but unstoppable.",
    },
    "2": {
        "name": "Hermes Explorer",
        "fuel": 100, "hull": 200, "day_bonus": 0,
        "desc": "The classic deep-space explorer. Balanced in every way.",
    },
    "3": {
        "name": "Falcon Sprint",
        "fuel": 82, "hull": 170, "day_bonus": -22,
        "desc": "Lightweight and lightning-fast. Fragile, but arrives 22 days sooner.",
    },
}

MISSION_TYPES = [
    {
        "name": "First Crewed Landing",
        "briefing": (
            "You are part of the historic first crewed mission to Mars.\n"
            "  The entire world is watching. Every decision counts."
        ),
        "bonus": 100, "day_limit": None,
    },
    {
        "name": "Rescue Mission",
        "briefing": (
            "A crew on Mars is stranded after a dust storm destroyed their base power.\n"
            "  Their oxygen reserves run out at day 550. You must reach them in time."
        ),
        "bonus": 150, "day_limit": 550,
    },
    {
        "name": "Supply Run",
        "briefing": (
            "The Mars colony is critically low on food and medicine.\n"
            "  Your cargo hold is packed. Deliver it safely or the colony starves."
        ),
        "bonus": 120, "day_limit": None,
    },
    {
        "name": "Scientific Survey",
        "briefing": (
            "Survey three candidate sites for a permanent Mars colony.\n"
            "  Science teams on Earth are counting on your data."
        ),
        "bonus": 110, "day_limit": None,
    },
    {
        "name": "Emergency Evacuation",
        "briefing": (
            "A volcanic vent opened beneath the Mars habitat -- it must be abandoned.\n"
            "  You have until day 530 to reach the crew and bring them home alive."
        ),
        "bonus": 130, "day_limit": 530,
    },
]

SPACE_FACTS = [
    "Mars has the largest volcano in the solar system -- Olympus Mons stands 22 km high.",
    "A Martian day (a 'sol') lasts 24 hours and 37 minutes.",
    "Mars has two small moons: Phobos and Deimos, both believed to be captured asteroids.",
    "The average surface temperature on Mars is around -63 degrees Celsius.",
    "Mars dust storms can engulf the entire planet for months at a time.",
    "The Martian atmosphere is 95% carbon dioxide.",
    "Mars is roughly half the diameter of Earth.",
    "Sunlight takes about 13 minutes to reach Mars.",
    "The first Mars landing was NASA's Viking 1 lander in July 1976.",
    "Mars has seasons similar to Earth due to its 25-degree axial tilt.",
    "Water once flowed on Mars -- ancient riverbeds and lake floors are still visible today.",
    "Gravity on Mars is about 38% of Earth's.",
    "The Valles Marineris canyon system stretches over 4,000 km across Mars.",
    "Perseverance rover produced breathable oxygen from Martian CO2 in 2021.",
    "Mars polar ice caps contain both water ice and dry ice (frozen CO2).",
    "The Martian sky appears butterscotch/pink during the day due to suspended dust.",
    "A Martian year lasts 687 Earth days.",
    "It takes around 7-9 months to travel to Mars with current propulsion technology.",
    "The pressure on Mars is less than 1% of Earth's.",
    "Methane has been detected in the Martian atmosphere, and its source remains a mystery.",
]

# Event type legend:
#   "auto"   -- effects apply automatically
#   "choice" -- player picks an option; each option has different effects
#   "crew"   -- references a random crew member via {crew} placeholder
TRANSIT_EVENTS = [
    # -- auto / bad ----------------------------------------------------------
    {"type":"auto",
     "text":"A micro-meteorite shower peppers the outer hull.",
     "detail":"Hull plating absorbed most of the impact.",
     "fuel":0,"damage":-15,"day":0,"score":0},
    {"type":"auto",
     "text":"A solar flare erupts. You divert power to the radiation shield.",
     "detail":"Crew protected, but the shields cost fuel.",
     "fuel":-6,"damage":0,"day":0,"score":0},
    {"type":"auto",
     "text":"Navigation computer glitch -- course correction required.",
     "detail":"Two extra days added to the journey.",
     "fuel":-4,"damage":0,"day":2,"score":0},
    {"type":"auto",
     "text":"A fuel line develops a slow leak and is quickly patched.",
     "detail":"Quick fix prevents a much larger loss.",
     "fuel":-5,"damage":-4,"day":0,"score":0},
    {"type":"auto",
     "text":"A coolant pipe bursts. Crew scrambles to contain it.",
     "detail":"Sealed in time, but the hull absorbed heat stress.",
     "fuel":-3,"damage":-10,"day":0,"score":0},
    {"type":"auto",
     "text":"A gyroscope fails -- the backup unit engages.",
     "detail":"Backup held. That was uncomfortably close.",
     "fuel":-2,"damage":-8,"day":1,"score":0},
    {"type":"auto",
     "text":"A microimpact damages the communication antenna.",
     "detail":"Auto-repair took several hours.",
     "fuel":0,"damage":-6,"day":0,"score":0},
    {"type":"auto",
     "text":"The water recycler seizes up. Manual override required.",
     "detail":"Fixed, but morale took a hit.",
     "fuel":0,"damage":-5,"day":1,"score":0},
    {"type":"auto",
     "text":"A pressure wave from a distant stellar event rattles the ship.",
     "detail":"Structural integrity slightly compromised.",
     "fuel":0,"damage":-12,"day":0,"score":0},
    {"type":"auto",
     "text":"An ion storm forces a course deviation.",
     "detail":"Longer path. Extra days added.",
     "fuel":-3,"damage":0,"day":3,"score":0},
    {"type":"auto",
     "text":"A cosmic ray burst disrupts on-board computers.",
     "detail":"Rebooted. Lost some time.",
     "fuel":0,"damage":0,"day":2,"score":0},
    {"type":"auto",
     "text":"A loose component causes vibration damage in the engine bay.",
     "detail":"Located and secured before major harm.",
     "fuel":0,"damage":-8,"day":0,"score":0},
    {"type":"auto",
     "text":"A debris field forces you to slow down and navigate carefully.",
     "detail":"Safe passage, but at the cost of extra time.",
     "fuel":-4,"damage":0,"day":2,"score":0},
    {"type":"auto",
     "text":"Unexpected gravitational variance from a nearby asteroid.",
     "detail":"Course correction expended extra fuel.",
     "fuel":-5,"damage":0,"day":0,"score":0},
    {"type":"auto",
     "text":"A sudden temperature drop causes stress fractures in the outer hull.",
     "detail":"Inner hull intact. Outer layer needs attention on return.",
     "fuel":0,"damage":-10,"day":0,"score":0},
    {"type":"auto",
     "text":"A power surge trips the main circuit breaker.",
     "detail":"Backup power held. Full systems restored after 30 minutes.",
     "fuel":-2,"damage":-5,"day":0,"score":0},
    {"type":"auto",
     "text":"A thruster nozzle partially clogs with debris.",
     "detail":"Efficiency drops until cleared. Costs extra fuel.",
     "fuel":-7,"damage":0,"day":0,"score":0},
    {"type":"auto",
     "text":"An oxygen sensor gives a false alarm at 3 a.m., waking the entire crew.",
     "detail":"False alarm confirmed. Crew is exhausted for 24 hours.",
     "fuel":0,"damage":0,"day":1,"score":0},
    # -- auto / good ---------------------------------------------------------
    {"type":"auto",
     "text":"Solar wind gives you an unexpected velocity boost.",
     "detail":"Nature just gave you a free ride.",
     "fuel":0,"damage":0,"day":-3,"score":20},
    {"type":"auto",
     "text":"A more efficient trajectory is calculated mid-flight.",
     "detail":"Burned a little extra fuel, but cut travel time significantly.",
     "fuel":-3,"damage":0,"day":-5,"score":30},
    {"type":"auto",
     "text":"The crew watches a film together. Morale soars.",
     "detail":"A well-rested crew is a better crew.",
     "fuel":0,"damage":0,"day":0,"score":15},
    {"type":"auto",
     "text":"Jupiter comes into view through the observation window.",
     "detail":"The crew spends a quiet hour watching in silence.",
     "fuel":0,"damage":0,"day":0,"score":10},
    {"type":"auto",
     "text":"An early self-diagnosis catches a minor fault before it worsens.",
     "detail":"Saved what could have been a real problem.",
     "fuel":0,"damage":5,"day":0,"score":20},
    {"type":"auto",
     "text":"You pass through the edge of a comet tail -- spectacular visuals.",
     "detail":"Crew morale at an all-time high.",
     "fuel":0,"damage":0,"day":0,"score":15},
    {"type":"auto",
     "text":"Engine efficiency exceeds projections.",
     "detail":"Ahead of the fuel consumption curve.",
     "fuel":5,"damage":0,"day":0,"score":20},
    {"type":"auto",
     "text":"NASA sends a micro-supply drone to your position.",
     "detail":"Small resupply received. Every drop counts.",
     "fuel":7,"damage":0,"day":0,"score":25},
    {"type":"auto",
     "text":"You spot an unidentified satellite of unknown origin.",
     "detail":"Logged and relayed to Houston for analysis.",
     "fuel":0,"damage":0,"day":0,"score":25},
    {"type":"auto",
     "text":"An unusual repeating radio signal is detected and recorded.",
     "detail":"Scientists on Earth will study it for years.",
     "fuel":0,"damage":0,"day":0,"score":30},
    {"type":"auto",
     "text":"A perfect alignment gives a stunning view of Saturn's rings.",
     "detail":"Photographed extensively. A once-in-a-lifetime sight.",
     "fuel":0,"damage":0,"day":0,"score":20},
    {"type":"auto",
     "text":"The crew runs a successful full-ship emergency drill.",
     "detail":"Emergency readiness is now at peak.",
     "fuel":0,"damage":5,"day":0,"score":20},
    {"type":"auto",
     "text":"A minor hull weld is found to be stronger than the spec required.",
     "detail":"Manufacturing quality bonus -- hull integrity improved.",
     "fuel":0,"damage":8,"day":0,"score":15},
    # -- choice --------------------------------------------------------------
    {"type":"choice",
     "text":"A fuel line is leaking. Two repair options are available.",
     "options":[
         {"text":"1. Emergency weld -- fast, imperfect",
          "detail":"Holds mostly. Minor seepage continues.","fuel":-3,"damage":-8,"day":0,"score":10},
         {"text":"2. Full pipe replacement -- safe, costs time",
          "detail":"Solid fix. No further leakage.","fuel":-10,"damage":0,"day":1,"score":15},
     ]},
    {"type":"choice",
     "text":"A derelict spacecraft is detected on the same heading. Investigate?",
     "options":[
         {"text":"1. Yes -- alter course to inspect it",
          "detail":"The derelict yields spare hull material and parts!","fuel":-5,"damage":12,"day":2,"score":50},
         {"text":"2. No -- stay on mission profile",
          "detail":"Prudent call. You stay on schedule.","fuel":0,"damage":0,"day":0,"score":10},
     ]},
    {"type":"choice",
     "text":"Houston requests a detour to deploy a relay satellite.",
     "options":[
         {"text":"1. Accept -- deploy the satellite",
          "detail":"Satellite deployed. Houston sends congratulations.","fuel":-8,"damage":0,"day":3,"score":60},
         {"text":"2. Decline -- mission schedule takes priority",
          "detail":"Houston understands.","fuel":0,"damage":0,"day":0,"score":5},
     ]},
    {"type":"choice",
     "text":"A remarkable stellar phenomenon is nearby. Divert for data?",
     "options":[
         {"text":"1. Yes -- collect unique scientific readings",
          "detail":"Extraordinary data. Science teams ecstatic.","fuel":-6,"damage":0,"day":2,"score":70},
         {"text":"2. No -- not worth the detour",
          "detail":"You stay on course.","fuel":0,"damage":0,"day":0,"score":0},
     ]},
    {"type":"choice",
     "text":"The engine is running hotter than expected.",
     "options":[
         {"text":"1. Throttle back and let it cool (adds days)",
          "detail":"Temperature normalises. Safe and steady.","fuel":0,"damage":0,"day":3,"score":10},
         {"text":"2. Push through it (faster, but stresses the hull)",
          "detail":"You push through. Hull takes the punishment.","fuel":5,"damage":-15,"day":0,"score":5},
     ]},
    {"type":"choice",
     "text":"A small asteroid is on a near-intercept course.",
     "options":[
         {"text":"1. Burn fuel to avoid it completely",
          "detail":"Clean avoidance. No damage at all.","fuel":-8,"damage":0,"day":0,"score":20},
         {"text":"2. Hold course and brace -- save the fuel",
          "detail":"Glancing blow. Hull takes a hit.","fuel":0,"damage":-18,"day":0,"score":5},
     ]},
    {"type":"choice",
     "text":"You can attempt a fuel-scooping manoeuvre near a gas cloud.",
     "options":[
         {"text":"1. Attempt the scoop (risky -- hull exposure)",
          "detail":"Success! Significant fuel recovered.","fuel":14,"damage":-10,"day":1,"score":40},
         {"text":"2. Skip it -- too dangerous",
          "detail":"You play it safe and continue.","fuel":0,"damage":0,"day":0,"score":5},
     ]},
    {"type":"choice",
     "text":"The crew is showing signs of exhaustion. Force rest or push on?",
     "options":[
         {"text":"1. Enforce a mandatory rest period (costs a day)",
          "detail":"Crew fully recovered. Performance improves.","fuel":0,"damage":5,"day":1,"score":15},
         {"text":"2. Push on -- mission schedule first",
          "detail":"You maintain pace but efficiency drops.","fuel":-3,"damage":-5,"day":0,"score":5},
     ]},
    {"type":"choice",
     "text":"Sensors detect an unusual metallic signature on a passing asteroid.",
     "options":[
         {"text":"1. Match velocity and probe it",
          "detail":"Extraordinary -- evidence of processed metal. Not natural.","fuel":-7,"damage":0,"day":2,"score":80},
         {"text":"2. Log it and continue",
          "detail":"Logged for future investigation.","fuel":0,"damage":0,"day":0,"score":10},
     ]},
    {"type":"choice",
     "text":"A microcrack is found in the observation window.",
     "options":[
         {"text":"1. Seal it immediately with a precautionary EVA",
          "detail":"Window reinforced. No further risk.","fuel":-4,"damage":5,"day":1,"score":20},
         {"text":"2. Monitor it -- act only if it grows",
          "detail":"Crack holds, but the crew is nervous.","fuel":0,"damage":-8,"day":0,"score":5},
     ]},
    {"type":"choice",
     "text":"A short-cut passes through a high-radiation belt -- cuts 8 days off the trip.",
     "options":[
         {"text":"1. Take the short-cut -- risk the radiation",
          "detail":"Radiation absorbed by hull. Days saved!","fuel":0,"damage":-12,"day":-8,"score":30},
         {"text":"2. Stay on the safe path",
          "detail":"All systems nominal. No radiation risk.","fuel":0,"damage":0,"day":0,"score":10},
     ]},
    {"type":"choice",
     "text":"You receive a distress beacon from an unmanned probe. Salvage it?",
     "options":[
         {"text":"1. Yes -- rendez-vous and recover it",
          "detail":"Probe data recovered! Immense scientific value.","fuel":-6,"damage":0,"day":1,"score":65},
         {"text":"2. No -- too far off course",
          "detail":"You relay the beacon coordinates to Houston.","fuel":0,"damage":0,"day":0,"score":10},
     ]},
    {"type":"choice",
     "text":"Two routes present themselves. The northern route is shorter but rocky.",
     "options":[
         {"text":"1. Northern route -- faster but rougher",
          "detail":"You make good time, but the hull takes some stress.","fuel":-2,"damage":-10,"day":-4,"score":20},
         {"text":"2. Southern route -- longer but smooth",
          "detail":"Smooth sailing. Nothing remarkable.","fuel":0,"damage":0,"day":3,"score":5},
     ]},
    # -- crew ----------------------------------------------------------------
    {"type":"crew",
     "text":"{crew} develops a mild fever. Rest is prescribed.",
     "detail":"{crew} recovers within 48 hours. All systems normal.",
     "fuel":0,"damage":0,"day":1,"score":0},
    {"type":"crew",
     "text":"Today is {crew}'s birthday! The whole crew celebrates.",
     "detail":"Morale boost across the board.",
     "fuel":0,"damage":5,"day":0,"score":15},
    {"type":"crew",
     "text":"{crew} notices an anomalous pressure reading and investigates.",
     "detail":"Good catch -- a valve was misaligned. Fixed before any damage.",
     "fuel":0,"damage":8,"day":0,"score":25},
    {"type":"crew",
     "text":"{crew} accidentally vents a small amount of propellant during a routine check.",
     "detail":"Minor loss. {crew} is mortified.",
     "fuel":-4,"damage":0,"day":0,"score":0},
    {"type":"crew",
     "text":"{crew} and another crew member have a heated argument. Tension rises.",
     "detail":"You mediate. Things settle slowly.",
     "fuel":0,"damage":-5,"day":1,"score":-10},
    {"type":"crew",
     "text":"{crew} photographs an unusual formation on a passing asteroid.",
     "detail":"Invaluable data for Earth's geologists.",
     "fuel":0,"damage":0,"day":0,"score":30},
    {"type":"crew",
     "text":"{crew} discovers a more efficient engine timing sequence.",
     "detail":"Fuel efficiency improves for the rest of the journey.",
     "fuel":6,"damage":0,"day":-2,"score":35},
    {"type":"crew",
     "text":"{crew} organises a zero-gravity exercise session. Everyone joins in.",
     "detail":"Physical health and morale both improve.",
     "fuel":0,"damage":5,"day":0,"score":20},
    {"type":"crew",
     "text":"{crew} writes a song about the mission and performs it for the crew.",
     "detail":"Unexpected morale boost. Everyone laughs and claps.",
     "fuel":0,"damage":0,"day":0,"score":15},
    {"type":"crew",
     "text":"{crew} stays up all night recalibrating the navigation sensors.",
     "detail":"Accuracy improved. Small time saving.",
     "fuel":0,"damage":0,"day":-1,"score":20},
    {"type":"crew",
     "text":"{crew} finds an old care package hidden in the cargo bay by mission control.",
     "detail":"Snacks, letters from home, and a morale video from NASA leadership.",
     "fuel":0,"damage":0,"day":0,"score":25},
    {"type":"crew",
     "text":"{crew} runs a full diagnostic and finds a fuel valve only 60% open.",
     "detail":"Valve fully opened. Fuel flow improves immediately.",
     "fuel":5,"damage":0,"day":0,"score":20},
]

SURFACE_EVENTS = [
    {"text":"A dust storm rolls in from the north.",
     "detail":"You shelter in the ship. The storm passes in a few hours.",
     "fuel":-3,"damage":-8,"day":1,"score":0},
    {"text":"The landing site sits on solid bedrock -- perfect conditions!",
     "detail":"Ideal stability. The crew moves with precision.",
     "fuel":0,"damage":0,"day":0,"score":40},
    {"text":"An exposed ice deposit is discovered just 200 metres away!",
     "detail":"Breakthrough find. Houston erupts with excitement.",
     "fuel":0,"damage":0,"day":0,"score":80},
    {"text":"A soil sample reveals unusually complex organic chemistry.",
     "detail":"Not life -- but the building blocks of it. Enormous implications.",
     "fuel":0,"damage":0,"day":0,"score":70},
    {"text":"A meteorite strikes 500 metres away. The shockwave rattles the ship.",
     "detail":"No direct damage, but nerves are shattered.",
     "fuel":0,"damage":-10,"day":0,"score":0},
    {"text":"Perfect stillness and low winds -- ideal EVA conditions.",
     "detail":"You extend the surface mission by a day. Worth every minute.",
     "fuel":0,"damage":0,"day":1,"score":50},
    {"text":"The drill bit snaps on an unexpectedly hard rock layer.",
     "detail":"Backup drill deployed. Minor delay.",
     "fuel":0,"damage":0,"day":1,"score":0},
    {"text":"A faint, regular radio signal is detected repeating from underground.",
     "detail":"Non-geological pattern. Houston wants full analysis immediately.",
     "fuel":0,"damage":0,"day":0,"score":90},
    {"text":"A Martian sunrise paints the sky in ribbons of blue and pink.",
     "detail":"The crew stops to watch in silence. A moment none will forget.",
     "fuel":0,"damage":0,"day":0,"score":20},
    {"text":"You find old rover tracks in the dust -- a reminder of those who came before.",
     "detail":"Photographed and logged. Another piece of history.",
     "fuel":0,"damage":0,"day":0,"score":25},
]


# ===============================================================================
#  ASCII ART
# ===============================================================================

AEROFORGE_LOGO = """
  * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . *
  . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * .

                                ___________
                  _____________/           \\
                 /                          \\________________________
                /                                                    \\
               |          A  E  R  O  F  O  R  G  E                  |
               |               Established  2023                     |
                \\____________________________________________________/
                  |__________________________________________________|
                                   |         |
                        ___________|         |___________
                       |                                 |
                       |_________________________________|
                                     \\     /
                                      \\___/

  * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . *
  . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * .
"""

TITLE_ART = """
  +==========================================================================+
  |                                                                          |
  |       *         *    .    *    .   *    .    *    .    *         *       |
  |    .     *   .     *    .     *    .     *    .     *    .   *     .     |
  |                                                                          |
  |                              /\\                                          |
  |                             /  \\                                         |
  |                            / /\\ \\                                        |
  |                           |/|  |\\|                                       |
  |                           | | SF| |                                      |
  |                           | | M | |                                      |
  |                          /| |___| |\\                                     |
  |                         / |/     \\| \\                                    |
  |                        /  /  [ ]  \\  \\                                   |
  |                       /__/ ======= \\__\\                                  |
  |                           |  [ ]  |                                      |
  |                          /|       |\\                                     |
  |                         / |  [ ]  | \\                                    |
  |                        (  )       (  )                                   |
  |                         \\/         \\/                                    |
  |                                                                          |
  |          S P A C E   F L I G H T   M A R S   -- R e m a s t e r e d    |
  |                                                                          |
  |                   Copyright 2023  A E R O f o r g e                     |
  |                                                                          |
  +==========================================================================+
"""


# ===============================================================================
#  UTILITY HELPERS
# ===============================================================================

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print(f"  Time on spacewalk: {int(hours)}h {int(mins)}m {sec:.1f}s")


def divider(char="-", width=62):
    print("  " + char * width)


def show_status(fuel, damage, day, score, max_fuel=100, max_hull=200):
    divider()
    f10 = max(0, min(10, fuel   * 10 // max(1, max_fuel)))
    h10 = max(0, min(10, damage * 10 // max(1, max_hull)))
    print(f"  Fuel   [{'#'*f10}{'.'*(10-f10)}] {fuel}/{max_fuel}")
    print(f"  Hull   [{'#'*h10}{'.'*(10-h10)}] {damage}/{max_hull}")
    print(f"  Day: {day}   |   Score: {score}")
    divider()


def ask(prompt, valid=None):
    """Prompt until the user gives an accepted answer (case-insensitive)."""
    while True:
        raw = input(f"  > {prompt}: ").strip().lower()
        if valid is None or raw in valid:
            return raw
        print(f"  [!] Please enter one of: {', '.join(str(v) for v in valid)}")


def space_fact():
    print(f"\n  [Space Fact]  {random.choice(SPACE_FACTS)}\n")


def credits_screen():
    time.sleep(1)
    print()
    divider("=")
    print("  Graphics & Programming by Callum Chang")
    print("  Facts and info from nasa.gov")
    print("  Made for the Game Design merit badge")
    print()
    print("  Thanks for playing!")
    print("  Copyright 2023  AEROforge")
    divider("=")
    time.sleep(3)


def game_over(reason, flight, crew_names):
    print()
    divider("=")
    print("  *** MISSION FAILED ***")
    print(f"  {reason}")
    print()
    print(f"  Breaking news: The crew of the {flight} mission are lost.")
    print(f"  {', '.join(crew_names)}")
    divider("=")
    credits_screen()
    sys.exit()


def check_game_over(fuel, damage, day, mission, flight, crew_names):
    if fuel <= 0:
        game_over("You ran out of fuel and were lost in space!", flight, crew_names)
    if damage <= 0:
        game_over("Hull integrity failed -- catastrophic decompression!", flight, crew_names)
    if mission["day_limit"] and day > mission["day_limit"]:
        game_over(
            f"Mission time limit exceeded on day {day}. "
            "The crew you were sent to rescue did not survive.",
            flight, crew_names,
        )


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


def show_map(flight, position="earth"):
    divider()
    print(f"  Flight map of {flight} mission")
    divider()
    e = "O" if position == "earth" else " "
    m = "O" if position == "mars"  else " "
    print(r"        ______________         /----------------------------------------------\  ")
    print(r"       /     o        \       /         (||) moon               /------\      \  ")
    print(f"       |{{  }}        ^(|      /                           mars  |  {m}   |      /  ")
    print(f"       | {{   }}  {e}  - - - /                                   \\------/     /  ")
    print(r"       |   {     ^{ \|      /                                                /  ")
    print(r"       |     \  ---------------------------------------------------------------/")
    print(r"       |     \\   \|)| earth")
    print(f"       \\_____________/     O = {flight}   - = flight path")
    divider()


def go_no_go(flight):
    print()
    print(f"  Houston -- requesting go/no-go for {flight} launch...")
    time.sleep(0.5)
    for station in ["CAPCOM", "FDO", "GPO", "Booster", "EECOM", "INCO", "MMACS", "FLIGHT"]:
        time.sleep(0.5)
        print(f"  {station}: go")
    time.sleep(0.5)
    print(f"  {flight} crew: go")
    time.sleep(1)
    print("  Godspeed.")
    time.sleep(2)


# ===============================================================================
#  EVENT ENGINE
# ===============================================================================

def fire_event(event, fuel, damage, day, score, flight, crew_names, max_fuel, max_hull):
    """Fire a single transit event and return updated (fuel, damage, day, score)."""
    cap = crew_names[0]
    print()
    divider()

    if event["type"] == "auto":
        print("  *** TRANSIT EVENT ***")
        print(f"  {event['text']}")
        space_fact()
        print(f"  {event['detail']}")
        eff = event

    elif event["type"] == "choice":
        print("  *** DECISION REQUIRED ***")
        print(f"  {event['text']}")
        print()
        for opt in event["options"]:
            print(f"  {opt['text']}")
        choice = ask(f"Choose (1-{len(event['options'])})",
                     valid=[str(i) for i in range(1, len(event["options"]) + 1)])
        eff = event["options"][int(choice) - 1]
        print(f"  {eff['detail']}")

    else:  # crew
        member = random.choice(crew_names)
        print("  *** CREW EVENT ***")
        print(f"  {event['text'].format(crew=member, cap=cap, flight=flight)}")
        space_fact()
        print(f"  {event['detail'].format(crew=member, cap=cap)}")
        eff = event

    fuel   = max(0, min(max_fuel,  fuel   + eff.get("fuel",   0)))
    damage = max(0, min(max_hull,  damage + eff.get("damage", 0)))
    day   += eff.get("day",   0)
    score += eff.get("score", 0)

    if eff.get("fuel",   0) < 0: print(f"  Fuel lost     : {abs(eff['fuel'])} units")
    if eff.get("fuel",   0) > 0: print(f"  Fuel gained   : {eff['fuel']} units")
    if eff.get("damage", 0) < 0: print(f"  Hull damage   : {abs(eff['damage'])} points")
    if eff.get("damage", 0) > 0: print(f"  Hull restored : {eff['damage']} points")
    if eff.get("day",    0) > 0: print(f"  Journey time increased by {eff['day']} day(s).")
    if eff.get("day",    0) < 0: print(f"  Journey time cut by {abs(eff['day'])} day(s)!")

    time.sleep(2)
    print(f"  Houston to {flight}: Copy that, {cap}.")
    divider()
    time.sleep(1)
    return fuel, damage, day, score


def run_event_phase(n, fuel, damage, day, score,
                    flight, crew_names, max_fuel, max_hull, mission, label="Transit"):
    """Fire n random non-repeating events, checking game-over after each."""
    pool = TRANSIT_EVENTS.copy()
    random.shuffle(pool)
    used = set()
    fired = 0
    idx = 0
    while fired < n and idx < len(pool):
        ev = pool[idx]
        idx += 1
        key = ev["text"][:40]
        if key in used:
            continue
        used.add(key)
        print(f"\n  [{label} -- Day {day}]  Traveling...")
        time.sleep(2)
        fuel, damage, day, score = fire_event(
            ev, fuel, damage, day, score, flight, crew_names, max_fuel, max_hull)
        check_game_over(fuel, damage, day, mission, flight, crew_names)
        day += random.randint(18, 35)
        show_status(fuel, damage, day, score, max_fuel, max_hull)
        fired += 1
    return fuel, damage, day, score


# ===============================================================================
#  MINI-GAMES  (8 total)
# ===============================================================================

# ── 1. Asteroid Avoidance ────────────────────────────────────────────────────
def asteroid_avoidance(flight, fuel, damage, score, difficulty, max_fuel, max_hull):
    """5-column grid dodge game. Returns (fuel, damage, score)."""
    divider("=")
    print("  *** ASTEROID FIELD -- EVASIVE MANEUVERS! ***")
    print(f"  {flight}: a dense asteroid field is dead ahead.")
    print("  Steer your ship to avoid incoming rocks!")
    divider("=")
    time.sleep(1)
    print("  L = move Left   R = move Right   S = Stay\n")
    time.sleep(1)

    n_waves  = 8 + difficulty * 2
    ship_pos = 3
    hits     = 0

    for wave in range(1, n_waves + 1):
        n_rocks   = 1 if wave <= n_waves // 2 else random.randint(1, 2)
        rock_cols = random.sample(range(1, 6), n_rocks)

        danger = ["  .  "] * 5
        for c in rock_cols:
            danger[c - 1] = " *** "
        ship = ["  .  "] * 5
        ship[ship_pos - 1] = " /^\\ "

        print(f"  Wave {wave}/{n_waves}")
        print("  " + "|".join(f"[{g}]" for g in danger) + "  <- incoming")
        print("  " + "|".join(f"[{s}]" for s in ship)   + f"  <- your ship (col {ship_pos})")

        mv = ask("Move (L/R/S)", valid=["l","r","s","left","right","stay"])[0]
        if mv == "l": ship_pos = max(1, ship_pos - 1)
        elif mv == "r": ship_pos = min(5, ship_pos + 1)

        if ship_pos in rock_cols:
            print("  [BOOM] Asteroid hit!")
            damage = max(0, damage - 15)
            fuel   = max(0, fuel   - 3)
            score -= 20
            hits  += 1
        else:
            print("  [OK]   Dodged!")
            score += 20
        print()
        time.sleep(0.6)

    divider()
    if hits == 0:
        print(f"  Outstanding! All {n_waves} asteroids dodged! +60 bonus!")
        score += 60
    elif hits <= 2:
        print(f"  Good flying! Only {hits} hit(s).")
    else:
        print(f"  Rough ride -- {hits} hit(s) sustained.")
    divider()
    time.sleep(2)
    return fuel, damage, score


# ── 2. Spacewalk ─────────────────────────────────────────────────────────────
def spacewalk_minigame(crew_names, fuel, damage, score, difficulty, max_fuel, max_hull):
    """Randomised 3-phase spacewalk. Returns (fuel, damage, score, bad_count)."""
    cap, name2, name3, name4, name5 = crew_names
    print()
    divider("=")
    print("  *** SPACEWALK -- HYDROGEN TANK REPAIR ***")
    print("  Guide the astronaut outside and repair the tank.")
    divider("=")
    time.sleep(1)

    for i, nm in enumerate(crew_names, 1):
        print(f"  {i} = {nm}")
    choice = ask("Who goes on the spacewalk? (1-5)", valid=["1","2","3","4","5"])
    walker = crew_names[int(choice) - 1]
    print(f"  {walker} suits up and heads outside.")
    time.sleep(1)

    input("  Press Enter to start the spacewalk timer...")
    t0  = time.time()
    bad = 0

    dir_map    = {"left": "1", "stay": "2", "right": "3"}
    dir_prompt = "  1 = left   2 = stay   3 = right"
    n_steps    = 6 + difficulty

    def nav_phase(label):
        nonlocal bad, fuel, damage, score
        print(f"\n  --- {label} ---")
        print(dir_prompt)
        for cmd in [random.choice(list(dir_map)) for _ in range(n_steps)]:
            print(f"\n  >> Go {cmd}!")
            time.sleep(0.4)
            ans = ask("Enter (1/2/3)", valid=["1","2","3"])
            if ans == dir_map[cmd]:
                print("  [OK] Correct!")
                score += 10
            else:
                print(f"  [X]  Wrong! (correct: {dir_map[cmd]})")
                fuel   = max(0, fuel   - 2)
                damage = max(0, damage - 10)
                bad   += 1
            time.sleep(0.4)

    nav_phase("Navigate to the leak")

    task_map  = {"turn": "1", "hammer": "2", "twist": "3", "close": "4"}
    task_list = ["turn", "turn", "twist", "hammer", "twist", "close"]
    random.shuffle(task_list)
    print("\n  --- Repair the hydrogen tank ---")
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
            print(f"  [X]  Wrong! (correct: {task_map[cmd]})")
            fuel   = max(0, fuel   - 2)
            damage = max(0, damage - 12)
            bad   += 1
        time.sleep(0.4)

    nav_phase("Head back to the airlock")

    input("\n  Press Enter once safely back inside...")
    time_convert(time.time() - t0)
    print(f"\n  Spacewalk complete! Mistakes: {bad}")
    time.sleep(2)
    return fuel, damage, score, bad


# ── 3. Engine Calibration ────────────────────────────────────────────────────
def engine_calibration(fuel, damage, score, difficulty, max_fuel, max_hull):
    """Simon-says number sequence memory game."""
    divider("=")
    print("  *** ENGINE CALIBRATION ***")
    print("  Memorise the number sequence, then repeat it exactly.")
    divider("=")
    time.sleep(1)

    n        = 4 + difficulty
    sequence = [random.randint(1, 9) for _ in range(n)]
    print(f"\n  Sequence: {' - '.join(str(x) for x in sequence)}")
    secs = 3 + difficulty
    print(f"  You have {secs} seconds...")
    time.sleep(secs)
    print("\n" * 2 + "  (sequence hidden -- enter from memory, space-separated)")

    raw = input("  > ").strip().split()
    try:
        entered = [int(x) for x in raw]
    except ValueError:
        entered = []

    correct = sum(a == b for a, b in zip(entered, sequence))
    if entered == sequence:
        print(f"  [OK] PERFECT! All {n} correct. Engines calibrated!")
        score += 60
    else:
        wrong = n - correct
        print(f"  [X]  {correct}/{n} correct. Engines running rough.")
        fuel   = max(0, fuel   - wrong * 4)
        damage = max(0, damage - wrong * 5)
    print(f"  (Correct answer was: {' - '.join(str(x) for x in sequence)})")
    divider()
    time.sleep(2)
    return fuel, damage, score


# ── 4. Docking Sequence ──────────────────────────────────────────────────────
def docking_minigame(fuel, damage, score, difficulty, max_fuel, max_hull):
    """Move ship along a 9-position line to reach the target dock port."""
    divider("=")
    print("  *** DOCKING SEQUENCE ***")
    print("  Maneuver your ship to align with the supply port.")
    print("  L = Left   R = Right   D = Dock")
    divider("=")
    time.sleep(1)

    width     = 9
    ship_pos  = random.randint(1, 3)
    target    = random.randint(7, 9)
    max_moves = 14 - difficulty * 2
    moves     = 0
    docked    = False

    def draw():
        row = ["."] * width
        row[target   - 1] = "O"
        row[ship_pos - 1] = "X"
        print("  Port : [" + "][".join(row) + "]")
        print(f"  Ship @ pos {ship_pos}  |  Port @ pos {target}  |  Moves left: {max_moves - moves}")

    while moves < max_moves:
        print()
        draw()
        mv = ask("Move (L/R/D)", valid=["l","r","d","left","right","dock"])[0]
        if mv == "d":
            if ship_pos == target:
                print("  [OK] DOCKED! Perfect alignment!")
                score += 80
                docked = True
            else:
                print(f"  [CRASH] Off by {abs(ship_pos - target)} -- collision!")
                damage = max(0, damage - 20)
                score -= 20
            break
        elif mv == "l": ship_pos = max(1, ship_pos - 1)
        elif mv == "r": ship_pos = min(width, ship_pos + 1)
        moves += 1

    if not docked and moves == max_moves:
        print("  Time up! Auto-abort triggered. Fuel expended.")
        fuel = max(0, fuel - 10)
    divider()
    time.sleep(2)
    return fuel, damage, score


# ── 5. Navigation Challenge ──────────────────────────────────────────────────
def navigation_challenge(fuel, damage, score, difficulty, max_fuel, max_hull):
    """Quick-fire maths problems to plot course corrections."""
    divider("=")
    print("  *** NAVIGATION CHALLENGE ***")
    print("  Solve these equations to plot your course corrections.")
    divider("=")
    time.sleep(1)

    n_problems = 4 + difficulty
    correct    = 0

    for i in range(n_problems):
        op = random.choice(["+", "-", "*"])
        if op == "+":
            a, b   = random.randint(20, 250), random.randint(20, 250)
            answer = a + b
        elif op == "-":
            a, b   = random.randint(100, 500), random.randint(10, 99)
            answer = a - b
        else:
            a, b   = random.randint(2, 12), random.randint(2, 12)
            answer = a * b

        print(f"\n  Problem {i+1}/{n_problems}:  {a} {op} {b} = ?")
        try:
            if int(input("  > ").strip()) == answer:
                print("  [OK] Correct!")
                correct += 1
                score   += 15
            else:
                print(f"  [X]  Wrong -- answer was {answer}.")
                fuel = max(0, fuel - 3)
        except ValueError:
            print(f"  [X]  Invalid -- answer was {answer}.")
            fuel = max(0, fuel - 3)

    print(f"\n  Navigation score: {correct}/{n_problems}")
    if correct == n_problems:
        print("  Perfect navigation! +30 bonus!")
        score += 30
    divider()
    time.sleep(2)
    return fuel, damage, score


# ── 6. Solar Panel Repair ────────────────────────────────────────────────────
def solar_panel_repair(fuel, damage, score, difficulty, max_fuel, max_hull):
    """Memorise and repeat wire colour order to restore panel power."""
    divider("=")
    print("  *** SOLAR PANEL REPAIR ***")
    print("  A panel array is offline. Reconnect the power grid.")
    print("  Memorise the correct wire order, then repeat it.")
    divider("=")
    time.sleep(1)

    colours  = ["RED", "BLUE", "GREEN", "YELLOW", "WHITE", "ORANGE"]
    n_wires  = 4 + (difficulty > 0)
    wire_set = colours[:n_wires]
    correct  = random.sample(wire_set, n_wires)

    print(f"\n  Correct order: {' -> '.join(correct)}")
    secs = 4 + difficulty
    print(f"  You have {secs} seconds to memorise it...")
    time.sleep(secs)
    print("\n" * 2)
    print(f"  Available wires: {', '.join(wire_set)}")
    print("  Enter the correct order (space-separated):")
    entered = input("  > ").strip().upper().split()

    hits = sum(a == b for a, b in zip(entered, correct))
    if hits == n_wires and len(entered) == n_wires:
        print("  [OK] PERFECT! All panels restored! Bonus fuel from full output.")
        score += 70
        fuel   = min(max_fuel, fuel + 5)
    else:
        wrong = n_wires - hits
        print(f"  [X]  {hits}/{n_wires} correct. Partial power only.")
        damage = max(0, damage - wrong * 8)
    print(f"  (Correct answer was: {' -> '.join(correct)})")
    divider()
    time.sleep(2)
    return fuel, damage, score


# ── 7. Oxygen Management ─────────────────────────────────────────────────────
def oxygen_management(fuel, damage, score, difficulty, max_fuel, max_hull):
    """Distribute oxygen across modules; all minimums must be met exactly."""
    divider("=")
    print("  *** OXYGEN MANAGEMENT ***")
    print("  O2 recycler damaged! Allocate the reserve supply.")
    print("  All modules must meet their minimum. Total must be exact.")
    divider("=")
    time.sleep(1)

    n_mods = 3 + difficulty
    names  = ["Bridge", "Science Lab", "Crew Quarters", "Engine Room"][:n_mods]
    mins   = [random.randint(15, 30) for _ in range(n_mods)]
    total  = sum(mins) + random.randint(5, 18)

    print(f"\n  Available: {total} units   (must allocate exactly {total})")
    print("  Minimum requirements:")
    for nm, mn in zip(names, mins):
        print(f"    {nm:<18}: at least {mn}")
    print()

    allocs = []
    for i, (nm, mn) in enumerate(zip(names, mins)):
        future_min  = sum(mins[i+1:])
        max_allowed = total - sum(allocs) - future_min
        while True:
            try:
                val = int(input(f"  Allocate to {nm} (min {mn}, max {max_allowed}): ").strip())
                if val < mn:
                    print(f"  [!] Must be at least {mn}.")
                elif val > max_allowed:
                    print(f"  [!] Cannot exceed {max_allowed} -- too little left for the rest.")
                else:
                    allocs.append(val)
                    break
            except ValueError:
                print("  [!] Enter a whole number.")

    if sum(allocs) == total:
        print("  [OK] Perfect allocation! O2 levels fully stabilised!")
        score += 90
    else:
        diff = abs(sum(allocs) - total)
        print(f"  [X]  Off by {diff}. Partial stabilisation only.")
        damage = max(0, damage - 12)
    divider()
    time.sleep(2)
    return fuel, damage, score


# ── 8. Mars Rover Drive ──────────────────────────────────────────────────────
def mars_rover_drive(fuel, damage, score, difficulty, max_fuel, max_hull):
    """Navigate a rover on a 7x7 grid to reach the sample site."""
    divider("=")
    print("  *** MARS ROVER DRIVE ***")
    print("  Drive the rover to the sample site!")
    print("  W = up   S = down   A = left   D = right   Q = abort")
    divider("=")
    time.sleep(1)

    size      = 7
    rover     = [0, 0]
    target    = [size - 1, size - 1]
    n_rocks   = 5 + difficulty * 3
    rocks     = set()
    while len(rocks) < n_rocks:
        r, c = random.randint(0, size - 1), random.randint(0, size - 1)
        if [r, c] != rover and [r, c] != target:
            rocks.add((r, c))

    max_moves = 22 - difficulty * 2
    moves     = 0
    reached   = False

    def draw():
        print()
        for r in range(size):
            row = "  "
            for c in range(size):
                if   [r, c] == rover:  row += "[R]"
                elif [r, c] == target: row += "[*]"
                elif (r, c) in rocks:  row += "[X]"
                else:                  row += "[ ]"
            print(row)
        print(f"  R=rover  *=sample site  X=rock  | Moves left: {max_moves - moves}")

    while moves < max_moves:
        draw()
        mv = ask("Move (W/S/A/D/Q)", valid=["w","s","a","d","q"])
        if mv == "q":
            break
        dr = -1 if mv == "w" else 1 if mv == "s" else 0
        dc = -1 if mv == "a" else 1 if mv == "d" else 0
        nr = max(0, min(size - 1, rover[0] + dr))
        nc = max(0, min(size - 1, rover[1] + dc))

        if (nr, nc) in rocks:
            print("  [CRASH] Rock obstacle hit! Hull stress.")
            damage = max(0, damage - 15)
            score -= 10
        else:
            rover = [nr, nc]
            if rover == target:
                draw()
                print("  [OK] Sample site reached! Samples collected!")
                score += 100
                fuel   = min(max_fuel, fuel + 3)
                reached = True
                break
        moves += 1

    if not reached:
        print("  Rover recalled without reaching the sample site.")
        damage = max(0, damage - 5)
    divider()
    time.sleep(2)
    return fuel, damage, score


# ── 9. Re-entry Angle Challenge ──────────────────────────────────────────────
def reentry_angle_challenge(fuel, damage, score, difficulty, max_fuel, max_hull):
    """Enter the correct angle to survive re-entry."""
    divider("=")
    print("  *** RE-ENTRY ANGLE CHALLENGE ***")
    print("  Too steep -- you burn up.  Too shallow -- you skip into space.")
    divider("=")
    time.sleep(2)

    safe_min = random.randint(5, 8)
    safe_max = safe_min + random.randint(3, 5)
    attempts = 3 - difficulty

    print(f"\n  Safe corridor: {safe_min} degrees to {safe_max} degrees below horizontal.")
    print(f"  You have {attempts} attempt(s).\n")

    success = False
    for attempt in range(1, attempts + 1):
        try:
            angle = float(input(f"  > Attempt {attempt}: Enter angle in degrees: ").strip())
            if safe_min <= angle <= safe_max:
                print(f"  [OK] Angle {angle} degrees -- LOCKED IN!")
                score  += 80
                success = True
                break
            elif angle < safe_min:
                print(f"  [X]  Too shallow -- atmosphere skip risk!")
                damage = max(0, damage - 15)
            else:
                print(f"  [X]  Too steep -- heat shield overstressed!")
                damage = max(0, damage - 20)
                fuel   = max(0, fuel   - 5)
        except ValueError:
            print("  [!] Enter a number.")

    if not success:
        print(f"  Auto-systems corrected to {safe_min + 1} degrees. Heavy heat-shield stress.")
        damage = max(0, damage - 25)
    divider()
    time.sleep(2)
    return fuel, damage, score


# ===============================================================================
#  MAIN GAME
# ===============================================================================

def main():

    # -- Intro ----------------------------------------------------------------
    print(AEROFORGE_LOGO)
    time.sleep(2)
    print(TITLE_ART)
    time.sleep(2)
    print("  Note: the game looks best in a fullscreen terminal.")
    input("  Press Enter to start your flight...")
    time.sleep(1)

    # -- Difficulty -----------------------------------------------------------
    print()
    divider()
    print("  Select difficulty:")
    print("  1 = Easy   2 = Normal   3 = Hard")
    difficulty = int(ask("Difficulty (1/2/3)", valid=["1","2","3"])) - 1
    diff_name  = {0:"Easy", 1:"Normal", 2:"Hard"}[difficulty]
    print(f"  Difficulty: {diff_name}")
    time.sleep(1)

    # -- Ship class -----------------------------------------------------------
    print()
    divider()
    print("  Choose your ship:")
    for k, s in SHIP_CLASSES.items():
        print(f"  {k}. {s['name']}")
        print(f"     {s['desc']}")
        print(f"     Fuel: {s['fuel']}  Hull: {s['hull']}  "
              f"Travel time bonus: {s['day_bonus']:+d} days")
        print()
    ship_key   = ask("Ship (1/2/3)", valid=["1","2","3"])
    ship_class = SHIP_CLASSES[ship_key]
    print(f"\n  You are flying the {ship_class['name']}.")
    time.sleep(1)

    # -- Mission assignment (random) -----------------------------------------
    mission = random.choice(MISSION_TYPES)
    print()
    divider("=")
    print(f"  *** MISSION ASSIGNED: {mission['name'].upper()} ***")
    print(f"  {mission['briefing']}")
    divider("=")
    if mission["day_limit"]:
        print(f"  [WARNING] Time limit: complete mission by day {mission['day_limit']}!")
    time.sleep(3)

    # -- Starting resources --------------------------------------------------
    max_fuel  = ship_class["fuel"]
    max_hull  = ship_class["hull"]
    fuel      = max_fuel
    damage    = max_hull
    day       = 375 + ship_class["day_bonus"]
    score     = 0
    bad       = 0

    if difficulty == 0:   # easy bonus
        fuel   = min(max_fuel, fuel + 10)
    elif difficulty == 2: # hard penalty
        fuel   = max(10, fuel   - 10)
        damage = max(10, damage - 15)

    # -- Crew setup ----------------------------------------------------------
    print()
    print("  Building spacecraft...")
    time.sleep(1)
    space_fact()
    print("  Gathering samples...")
    time.sleep(1)
    print("  Training crew...")
    time.sleep(1)

    name  = input("  Mission Commander's name: ").strip() or "Commander"
    n     = input("  Mars Module Pilot's name: ").strip()  or "Pilot"
    n1    = input("  Command Pilot's name: ").strip()       or "Co-Pilot"
    n2    = input("  Engineer's name: ").strip()            or "Engineer"
    n3    = input("  Civilian's name: ").strip()            or "Civilian"

    cap        = f"Mission Commander {name}"
    name2      = f"Mars Module Pilot {n}"
    name3      = f"Command Pilot {n1}"
    name4      = f"Engineer {n2}"
    name5      = f"Civilian {n3}"
    crew_names = [cap, name2, name3, name4, name5]

    print(f"\n  Your mission starts now, {cap}!")
    time.sleep(1)

    flight    = input("  Name your space mission: ").strip() or "Apollo X"
    ship_name = input("  Name your recovery ship: ").strip() or "USS Recovery"
    time.sleep(1)

    # -- Mission map (outbound) ----------------------------------------------
    show_map(flight, "earth")
    time.sleep(3)

    # -- Go / No-Go ----------------------------------------------------------
    go_no_go(flight)

    # -- Launch code ---------------------------------------------------------
    launch_code = input("  Set your personal launch code: ").strip()
    while not launch_code:
        print("  [!] Launch code cannot be empty.")
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
    fuel = max(0, fuel - 9)
    time.sleep(1)
    print(f"  And we have liftoff of the {flight} mission!")
    space_fact()
    time.sleep(2)
    print("  Pressure looks stable.")
    time.sleep(2)
    print(f"  Houston to {flight}: you are exiting Earth's atmosphere.")
    time.sleep(2)

    # -- Fuel boost decision -------------------------------------------------
    print("  Do you want to burn extra fuel to accelerate?")
    if ask("yes or no", valid=["yes","no","y","n"]) in ["yes", "y"]:
        fuel  = max(0, fuel - 5)
        day  -= 5
        print("  Fuel burned -- you will arrive 5 days sooner.")
    else:
        print("  Conserving fuel -- journey will take a little longer.")
        day += 3
    time.sleep(2)

    # -- Radio contact -------------------------------------------------------
    print(f"\n  Houston to {flight}: please copy.")
    msg = input("  What do you want to say? ").strip()
    print(f"  {flight} to Houston: {msg}")
    time.sleep(1)
    print(f"  Houston to {flight}: thank you for advising.")
    time.sleep(2)

    # -- Stop option (random station name each run) --------------------------
    stop_name = random.choice(["the ISS", "Gateway Station", "Orbital Depot Alpha",
                               "the Lunar Gateway", "Depot Zephyr"])
    print(f"\n  Houston: do you want to stop at {stop_name} for rest and resupply?")
    if ask("yes or no", valid=["yes","no","y","n"]) in ["yes", "y"]:
        day    += 4
        damage  = min(max_hull, damage + 10)
        fuel    = min(max_fuel, fuel   + 5)
        print(f"  Docking with {stop_name}... crew rests and ship is resupplied.")
        space_fact()
        time.sleep(2)
        print("  Crew is rested. Hull systems inspected. Small resupply received.")
    else:
        print(f"  Bypassing {stop_name} -- saving time.")
    time.sleep(2)

    day  += 1
    fuel  = max(0, fuel - 3)
    show_status(fuel, damage, day, score, max_fuel, max_hull)
    check_game_over(fuel, damage, day, mission, flight, crew_names)

    # -- Build randomised mini-game pool ------------------------------------
    optional_pool = [
        engine_calibration,
        docking_minigame,
        navigation_challenge,
        solar_panel_repair,
    ]
    random.shuffle(optional_pool)
    pool_idx = 0

    # -- Outbound transit events ---------------------------------------------
    n_events = 3 + difficulty
    fuel, damage, day, score = run_event_phase(
        n_events, fuel, damage, day, score,
        flight, crew_names, max_fuel, max_hull, mission, label="Outbound")

    # -- Optional transit mini-game 1 ----------------------------------------
    print(f"\n  [Day {day}]  A systems check flags an issue requiring immediate attention...")
    time.sleep(2)
    fuel, damage, score = optional_pool[pool_idx](
        fuel, damage, score, difficulty, max_fuel, max_hull)
    pool_idx += 1
    check_game_over(fuel, damage, day, mission, flight, crew_names)
    show_status(fuel, damage, day, score, max_fuel, max_hull)

    # -- Asteroid avoidance -------------------------------------------------
    print(f"\n  Houston to {flight}: dense asteroid field detected on current heading!")
    time.sleep(2)
    fuel, damage, score = asteroid_avoidance(
        flight, fuel, damage, score, difficulty, max_fuel, max_hull)
    check_game_over(fuel, damage, day, mission, flight, crew_names)
    show_status(fuel, damage, day, score, max_fuel, max_hull)

    # -- Hydrogen leak / spacewalk ------------------------------------------
    print()
    divider("=")
    for _ in range(3):
        print("  *** WARNING ***")
        time.sleep(0.5)
    print(f"  Collision detected -- {name3} takes over!")
    time.sleep(2)
    print("  Hydrogen leak in Tank 2!  A spacewalk is required to fix it.")
    time.sleep(2)

    fuel, damage, score, bad = spacewalk_minigame(
        crew_names, fuel, damage, score, difficulty, max_fuel, max_hull)
    day += 2
    check_game_over(fuel, damage, day, mission, flight, crew_names)
    show_status(fuel, damage, day, score, max_fuel, max_hull)
    print("  Ship repaired! Continuing to Mars...")
    space_fact()
    time.sleep(3)

    # -- Mars orbit entry ----------------------------------------------------
    print("  You are now entering Mars orbit.")
    time.sleep(2)
    print(f"  {cap} takes charge.")
    time.sleep(2)
    print("  Beginning the Seven Minutes of Terror...")
    input("  Press Enter to begin Mars entry...")

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

    # -- Surface event (random from 10) -------------------------------------
    surf = random.choice(SURFACE_EVENTS)
    divider()
    print("  *** SURFACE REPORT ***")
    print(f"  {surf['text']}")
    space_fact()
    print(f"  {surf['detail']}")
    fuel   = max(0, min(max_fuel,  fuel   + surf["fuel"]))
    damage = max(0, min(max_hull,  damage + surf["damage"]))
    day   += surf["day"]
    score += surf["score"]
    if surf["score"] > 0:
        print(f"  Scientific discovery bonus: +{surf['score']} points")
    divider()
    time.sleep(2)
    check_game_over(fuel, damage, day, mission, flight, crew_names)

    # -- Surface mini-game (rover OR oxygen, randomly chosen) ---------------
    surface_game = random.choice([mars_rover_drive, oxygen_management])
    game_label   = "Surface exploration operations" if surface_game == mars_rover_drive \
                   else "Life support maintenance"
    print(f"\n  [{game_label}]  {cap} begins surface activities...")
    time.sleep(2)
    fuel, damage, score = surface_game(
        fuel, damage, score, difficulty, max_fuel, max_hull)
    check_game_over(fuel, damage, day, mission, flight, crew_names)
    show_status(fuel, damage, day, score, max_fuel, max_hull)

    # -- Mars comms and flag ------------------------------------------------
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
    print(f"  {name4} reports status:")
    show_status(fuel, damage, day, score, max_fuel, max_hull)

    # -- Mars launch --------------------------------------------------------
    input("  Press Enter to launch from Mars...")
    print("  Houston, we are go for Mars launch in T-minus...")
    time.sleep(1)
    countdown()
    fuel = max(0, fuel - 10)
    time.sleep(1)
    print(f"  The {flight} is leaving Mars and heading home!")
    space_fact()
    time.sleep(3)

    # -- Return journey events ----------------------------------------------
    day  += 175
    fuel  = max(0, fuel - 22)
    check_game_over(fuel, damage, day, mission, flight, crew_names)
    print(f"\n  [Return journey -- Day {day}]")
    time.sleep(1)

    n_return = 2 + (difficulty // 2)
    fuel, damage, day, score = run_event_phase(
        n_return, fuel, damage, day, score,
        flight, crew_names, max_fuel, max_hull, mission, label="Return")

    # -- Return mini-game (next from pool) ----------------------------------
    if pool_idx < len(optional_pool):
        print(f"\n  [Day {day}]  A systems alert requires attention on the return leg...")
        time.sleep(2)
        fuel, damage, score = optional_pool[pool_idx](
            fuel, damage, score, difficulty, max_fuel, max_hull)
        pool_idx += 1
        check_game_over(fuel, damage, day, mission, flight, crew_names)
        show_status(fuel, damage, day, score, max_fuel, max_hull)

    # -- Earth re-entry ----------------------------------------------------
    print(f"\n  You are approaching Earth.")
    print(f"  {name5} takes over.")
    time.sleep(1)
    print("  Approaching the blackout zone...")
    time.sleep(1)
    print("  We expect -------------------------------------------")
    for _ in range(5):
        print("  ----------------------------------------------------")
        time.sleep(0.3)
    print("  All comms cut. You are on your own.")
    time.sleep(2)

    fuel, damage, score = reentry_angle_challenge(
        fuel, damage, score, difficulty, max_fuel, max_hull)
    check_game_over(fuel, damage, day, mission, flight, crew_names)

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
    print(f"  The {ship_name} has recovered all five astronauts.")
    time.sleep(3)

    # -- Final summary -------------------------------------------------------
    if bad == 0:
        score += 200
        print("  PERFECT spacewalk -- no mistakes! +200 points!")
    elif bad <= 3:
        score += 100
    score += mission["bonus"]

    divider("=")
    print(f"  *** MISSION COMPLETE -- {flight} ({mission['name']}) ***")
    print()
    print(f"  Crew  : {cap}, {name2}, {name3}, {name4}, and {name5}")
    print(f"  Ship  : {ship_class['name']}  |  Recovery: {ship_name}")
    print()
    print(f"  Mission type     : {mission['name']}")
    print(f"  Difficulty       : {diff_name}")
    print(f"  Mission duration : {day} days")
    print(f"  Fuel remaining   : {fuel}/{max_fuel}")
    print(f"  Hull integrity   : {damage}/{max_hull}")
    print(f"  Spacewalk errors : {bad}")
    print(f"  Final score      : {score}")
    print()

    if   score >= 800: rating = "S  -- Legendary Mission!"
    elif score >= 600: rating = "A  -- Outstanding Mission"
    elif score >= 400: rating = "B  -- Excellent Mission"
    elif score >= 250: rating = "C  -- Good Mission"
    elif score >= 100: rating = "D  -- Mission Accomplished"
    else:              rating = "F  -- Rough Mission"
    print(f"  Rating: {rating}")
    divider("=")

    time.sleep(3)
    print(f"\n  Breaking news: All five astronauts safe after the {flight} mission!")
    time.sleep(3)
    credits_screen()


if __name__ == "__main__":
    main()
