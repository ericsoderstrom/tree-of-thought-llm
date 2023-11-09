# 5-shot
standard_prompt = '''Partition the input set of 16 words into 4 non-overlapping groups of 4 related words
Input:
BUILD, GROW, SWELL, MOUNT, ACES, KEEN, NEATO, NIFTY, FOAM, FROTH, HEAD, LATHER, BUBBLE, GLOBE, MARBLE, PEARL
Output:
INCREASE : BUILD, GROW, SWELL, MOUNT
EXCELLENT, IN OLD SLANG : ACES, KEEN, NEATO, NIFTY
FINE BUBBLES : FOAM, FROTH, HEAD, LATHER
SPHERICAL THINGS : BUBBLE, GLOBE, MARBLE, PEARL

Input:
FUTURE, PAST, PERFECT, PRESENT, GOODNESS, HEAVENS, LORD, MERCY, DRUMMER, LADY, RING, SWAN, CORN, COUGH, MAPLE, SIMPLE
Output:
GRAMMAR TENSE TERMS : FUTURE, PAST, PERFECT, PRESENT
“GRACIOUS ME!” : GOODNESS, HEAVENS, LORD, MERCY
12 DAYS OF CHRISTMAS : DRUMMER, LADY, RING, SWAN
___ SYRUP : CORN, COUGH, MAPLE, SIMPLE

Input:
COLONY, HERD, PRIDE, SCHOOL, CRANNY, NICHE, NOOK, RECESS, CLASSIC, DEFINITIVE, MODEL, TEXTBOOK, BACKPACK, BIGWIG, DOWNTOWN, RAGTAG
Output:
ANIMAL GROUPS : COLONY, HERD, PRIDE, SCHOOL
SMALL OPENING : CRANNY, NICHE, NOOK, RECESS
PARADIGMATIC : CLASSIC, DEFINITIVE, MODEL, TEXTBOOK
RHYMING COMPOUND WORDS : BACKPACK, BIGWIG, DOWNTOWN, RAGTAG

Input:
FOCUS, RING, SILENT, VIBRATE, DRIVE, INSPIRE, MOTIVATE, SPUR, CONNECTION, FEELINGS, SPARK, VIBE, CANDY, COPY, KNOCKS, SELTZER
Output:
CELL PHONE MODES : FOCUS, RING, SILENT, VIBRATE
IMPEL : DRIVE, INSPIRE, MOTIVATE, SPUR
ROMANTIC BEGINNINGS : CONNECTION, FEELINGS, SPARK, VIBE
HARD ___ : CANDY, COPY, KNOCKS, SELTZER

Input:
CHILL, HANG, LOAF, LOUNGE, BANGER, BOP, GROOVE, JAM, MASH, ROAST, SCONE, TRIFLE, BIND, PICKLE, SCRAPE, SPOT
Output:
RELAX : CHILL, HANG, LOAF, LOUNGE
CATCHY SONG : BANGER, BOP, GROOVE, JAM
BRITISH CUISINE : MASH, ROAST, SCONE, TRIFLE
STICKY SITUATION : BIND, PICKLE, SCRAPE, SPOT

Input:
{input}
Output:
'''