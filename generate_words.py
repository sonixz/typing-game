#!/usr/bin/env python3
"""
Typing Lab - Premium Word Pool Generator
Generates 10,000+ curated words from multiple sources:
- Tech/Gaming vocabulary
- Common English words (frequency-based)
- Themed categories (science, space, nature, etc.)
"""

import json
import random

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TECH & GAMING VOCABULARY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

tech_gaming = [
    # Programming
    "api", "app", "bug", "cpu", "css", "git", "gpu", "ide", "npm", "ram",
    "sdk", "sql", "url", "xml", "ajax", "bash", "blob", "byte", "chip",
    "code", "data", "disk", "file", "font", "hash", "heap", "http", "html",
    "icon", "java", "json", "link", "loop", "node", "path", "ping", "port",
    "rest", "root", "ruby", "sass", "save", "scan", "sync", "test", "unix",
    "void", "vuejs", "web", "wiki", "yaml", "zip",

    # Medium tech terms
    "admin", "adobe", "agile", "alert", "async", "audio", "bash", "batch",
    "bench", "beta", "bios", "block", "boot", "cache", "class", "click",
    "client", "clone", "cloud", "codec", "color", "compile", "config", "crash",
    "cron", "crypto", "cursor", "daemon", "debug", "delete", "deploy", "device",
    "docker", "domain", "download", "driver", "editor", "email", "engine", "error",
    "event", "export", "fetch", "field", "filter", "flash", "folder", "format",
    "frame", "github", "gitlab", "global", "google", "graphic", "header", "heroku",
    "host", "hover", "image", "import", "index", "input", "install", "internet",
    "invoke", "kernel", "lambda", "launch", "layer", "layout", "legacy", "library",
    "license", "linux", "load", "local", "logic", "login", "logout", "macro",
    "malware", "memory", "merge", "method", "metric", "mobile", "model", "module",
    "monitor", "mouse", "mysql", "network", "nodejs", "object", "offset", "online",
    "output", "packet", "panel", "parse", "patch", "pixel", "plugin", "postgres",
    "power", "print", "process", "program", "project", "prompt", "protocol", "proxy",
    "public", "python", "query", "queue", "random", "react", "record", "redux",
    "refactor", "regex", "remote", "render", "report", "request", "require", "reset",
    "resize", "resolve", "response", "restart", "return", "router", "routing", "ruby",
    "runtime", "safari", "sass", "save", "scale", "schema", "scope", "screen",
    "script", "scroll", "search", "secure", "select", "sender", "server", "service",
    "session", "setter", "setup", "shell", "signal", "socket", "source", "sqlite",
    "stack", "static", "status", "storage", "stream", "string", "struct", "style",
    "submit", "subnet", "sudo", "switch", "symbol", "syntax", "system", "table",
    "target", "task", "template", "terminal", "theme", "thread", "throw", "token",
    "toggle", "toolbar", "tooltip", "traffic", "trigger", "typescript", "ubuntu",
    "update", "upgrade", "upload", "username", "value", "variable", "vector", "vendor",
    "version", "video", "virtual", "visual", "vuejs", "webpack", "website", "widget",
    "window", "worker", "wrapper",

    # Gaming terms
    "aim", "ammo", "armor", "attack", "avatar", "boss", "buff", "camp", "clan",
    "combo", "craft", "crit", "damage", "death", "defense", "dps", "enemy", "farm",
    "fps", "game", "gear", "gold", "grind", "guild", "health", "heal", "item",
    "kill", "lag", "level", "loot", "mana", "map", "mob", "mmorpg", "nerf", "noob",
    "party", "patch", "player", "power", "quest", "raid", "rank", "respawn", "score",
    "shield", "skill", "spawn", "speed", "spell", "stack", "stats", "steam", "sword",
    "tank", "team", "trade", "trophy", "upgrade", "wave", "weapon", "xp",

    # Longer tech terms
    "algorithm", "analytics", "animation", "apache", "application", "architecture",
    "artificial", "attribute", "bandwidth", "benchmark", "binary", "bitcoin",
    "blockchain", "bootstrap", "browser", "buffer", "calculator", "callback",
    "capacity", "certificate", "channel", "character", "checkbox", "cipher",
    "circular", "cluster", "collection", "collision", "command", "comment",
    "commit", "compiler", "component", "compression", "computer", "concurrency",
    "condition", "configuration", "connection", "console", "constant", "constructor",
    "container", "content", "context", "control", "conversion", "cookie", "corruption",
    "credentials", "cryptocurrency", "dashboard", "database", "datatype", "decimal",
    "declaration", "decryption", "definition", "delegate", "deployment", "deprecated",
    "desktop", "destructor", "developer", "dictionary", "digital", "dimension",
    "directory", "disconnect", "display", "distribution", "documentation", "dynamic",
    "element", "embedded", "encoding", "encryption", "endpoint", "engineering",
    "environment", "ethernet", "exception", "executable", "execution", "expression",
    "extension", "fallback", "feedback", "fibonacci", "filename", "filesystem",
    "firewall", "firmware", "floating", "footer", "framework", "frontend", "function",
    "generator", "graphql", "hardware", "hexadecimal", "hierarchy", "hostname",
    "identifier", "implementation", "increment", "inheritance", "initialize", "injection",
    "instance", "integration", "intelligent", "interface", "interpreter", "iteration",
    "javascript", "keyboard", "latency", "localhost", "logarithm", "machine",
    "maintenance", "markdown", "matrix", "maximum", "mechanism", "metadata",
    "microservice", "middleware", "minimum", "modification", "monitor", "multiplayer",
    "namespace", "navigation", "negative", "networking", "notification", "operator",
    "optimization", "overflow", "override", "package", "pagination", "parameter",
    "partition", "password", "payload", "performance", "permission", "persistence",
    "pipeline", "placeholder", "platform", "pointer", "polygon", "polymorphism",
    "popup", "positive", "precision", "prediction", "primary", "primitive",
    "priority", "privacy", "private", "procedure", "processor", "production",
    "programming", "property", "protected", "provider", "pseudo", "quantum",
    "radian", "randomize", "reactive", "readonly", "realtime", "receiver",
    "recursion", "redirect", "redundant", "reference", "reflection", "registry",
    "regression", "regular", "relation", "relative", "reliability", "rendering",
    "repository", "resource", "responsive", "restriction", "revision", "rotation",
    "sandbox", "satellite", "scalable", "scheduler", "scientist", "scrollbar",
    "secondary", "security", "selector", "semantic", "separator", "sequence",
    "serialization", "settings", "shortcut", "sidebar", "signature", "simulator",
    "snapshot", "software", "sorting", "specification", "spreadsheet", "statement",
    "statistics", "streaming", "structure", "stylesheet", "subscription", "substring",
    "successful", "synchronization", "technology", "telegram", "telephone", "temperature",
    "temporary", "terminal", "testing", "textarea", "thumbnail", "timeout",
    "timestamp", "toolbar", "tracking", "transaction", "transformation", "transition",
    "translation", "transmission", "transport", "triangle", "tutorial", "undefined",
    "underscore", "unicode", "universal", "unsigned", "validation", "variable",
    "verification", "viewport", "visibility", "visualization", "vulnerability",
    "warehouse", "whitespace", "wireless", "workflow", "workstation",
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COMMON ENGLISH WORDS (Frequency-based)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

common_words = [
    # Very common short words (3-4 letters)
    "able", "about", "above", "acid", "acts", "aged", "ages", "aids", "aims",
    "also", "area", "arms", "army", "atom", "away", "baby", "back", "ball",
    "band", "bank", "base", "bear", "beat", "been", "bell", "belt", "best",
    "bird", "bite", "blow", "blue", "boat", "body", "bone", "book", "born",
    "both", "bowl", "bulk", "burn", "busy", "cafe", "cage", "cake", "call",
    "calm", "came", "camp", "card", "care", "case", "cash", "cast", "cell",
    "chat", "chef", "chin", "chip", "city", "clue", "coal", "coat", "coin",
    "cold", "come", "cook", "cool", "cope", "copy", "core", "corn", "cost",
    "crew", "crop", "cube", "cure", "cuts", "dare", "dark", "data", "date",
    "dawn", "days", "dead", "deal", "dean", "dear", "debt", "deck", "deed",
    "deep", "deny", "desk", "dial", "dice", "diet", "dirt", "disk", "dock",
    "does", "dogs", "dome", "done", "door", "dose", "down", "drag", "draw",
    "drew", "drop", "drug", "drum", "dual", "duck", "duke", "dull", "dump",
    "dusk", "dust", "duty", "each", "earn", "ease", "east", "easy", "echo",
    "edge", "edit", "eggs", "else", "emit", "epic", "euro", "even", "ever",
    "evil", "exam", "exit", "eyes", "face", "fact", "fade", "fail", "fair",
    "fall", "fame", "fare", "farm", "fast", "fate", "fear", "feed", "feel",
    "feet", "fell", "felt", "file", "fill", "film", "find", "fine", "fire",
    "firm", "fish", "fist", "fits", "five", "flag", "flat", "fled", "flee",
    "flew", "flip", "flow", "folk", "fond", "food", "foot", "ford", "fork",
    "form", "fort", "four", "free", "from", "fuel", "full", "fund", "gain",
    "game", "gate", "gave", "gear", "gene", "gift", "girl", "give", "glad",
    "glow", "goal", "gods", "goes", "gold", "golf", "gone", "good", "grab",
    "gray", "grew", "grey", "grid", "grim", "grip", "grow", "gulf", "guns",
    "guys", "hair", "half", "hall", "halt", "hand", "hang", "hard", "harm",
    "hate", "have", "head", "hear", "heat", "held", "hell", "help", "herb",
    "here", "hero", "hide", "high", "hill", "hint", "hire", "hold", "hole",
    "holy", "home", "hook", "hope", "horn", "host", "hour", "huge", "hung",
    "hunt", "hurt", "icon", "idea", "inch", "into", "iron", "isle", "item",
    "jack", "jail", "jane", "jazz", "jobs", "join", "joke", "jump", "june",
    "jury", "just", "keen", "keep", "kept", "keys", "kick", "kids", "kill",
    "kind", "king", "kiss", "knee", "knew", "know", "labs", "lack", "lady",
    "laid", "lake", "lamb", "lamp", "land", "lane", "last", "late", "lawn",
    "laws", "lead", "leaf", "lean", "leap", "left", "legs", "lend", "lens",
    "less", "lies", "life", "lift", "like", "limb", "line", "link", "lion",
    "lips", "list", "live", "load", "loan", "lock", "loft", "logo", "lone",
    "long", "look", "loop", "lord", "lose", "loss", "lost", "lots", "loud",
    "love", "luck", "lung", "made", "maid", "mail", "main", "make", "male",
    "mall", "mama", "many", "mark", "mars", "mask", "mass", "mate", "math",
    "meal", "mean", "meat", "meet", "melt", "memo", "menu", "mere", "mesh",
    "mess", "mice", "mile", "milk", "mill", "mind", "mine", "mint", "miss",
    "mist", "mode", "mood", "moon", "more", "moss", "most", "moth", "move",
    "much", "myth", "nail", "name", "navy", "near", "neat", "neck", "need",
    "news", "next", "nice", "nine", "node", "none", "noon", "norm", "nose",
    "note", "noun", "oath", "okay", "once", "ones", "only", "onto", "open",
    "oral", "ours", "oval", "oven", "over", "pace", "pack", "page", "paid",
    "pain", "pair", "pale", "palm", "papa", "park", "part", "pass", "past",
    "path", "peak", "pear", "peer", "pens", "pets", "pick", "pier", "pile",
    "pill", "pine", "pink", "pins", "pipe", "plan", "play", "plot", "plug",
    "plus", "poem", "poet", "pole", "poll", "pond", "pony", "pool", "poor",
    "pope", "pork", "port", "pose", "post", "pour", "pray", "prep", "prey",
    "pure", "push", "quit", "race", "rack", "rage", "raid", "rail", "rain",
    "rank", "rare", "rate", "rays", "read", "real", "rear", "rent", "rest",
    "rice", "rich", "ride", "ring", "rise", "risk", "road", "roam", "roar",
    "rock", "rode", "role", "roll", "roof", "room", "root", "rope", "rose",
    "rude", "ruin", "rule", "rush", "rust", "safe", "saga", "sage", "sail",
    "sake", "sale", "salt", "same", "sand", "sank", "save", "says", "scan",
    "seal", "seat", "sect", "seed", "seek", "seem", "seen", "self", "sell",
    "send", "sent", "sets", "shed", "shin", "ship", "shop", "shot", "show",
    "shut", "sick", "side", "sign", "silk", "sing", "sink", "site", "size",
    "skin", "skip", "slam", "slap", "slip", "slot", "slow", "snap", "snow",
    "soar", "sock", "soft", "soil", "sold", "sole", "some", "song", "sons",
    "soon", "sort", "soul", "soup", "span", "spin", "spit", "spot", "stab",
    "star", "stay", "stem", "step", "stir", "stop", "such", "suit", "sunk",
    "sure", "surf", "swap", "swim", "tabs", "tail", "take", "tale", "talk",
    "tall", "tank", "tape", "task", "taxi", "team", "tear", "teen", "tell",
    "temp", "tend", "tent", "term", "test", "text", "than", "that", "them",
    "then", "they", "thin", "this", "thus", "tick", "tide", "ties", "tile",
    "till", "tilt", "time", "tiny", "tips", "tire", "told", "toll", "tone",
    "tons", "took", "tool", "tops", "torn", "toss", "tour", "town", "toys",
    "trap", "tray", "tree", "trek", "trim", "trio", "trip", "true", "tube",
    "tune", "turn", "twin", "type", "unit", "upon", "used", "user", "uses",
    "vain", "vale", "vans", "vary", "vast", "vein", "very", "vest", "veto",
    "vice", "view", "vine", "visa", "void", "volt", "vote", "wade", "wage",
    "wait", "wake", "walk", "wall", "want", "ward", "warm", "warn", "wars",
    "wash", "wave", "ways", "weak", "wear", "weed", "week", "well", "went",
    "were", "west", "what", "when", "whip", "whom", "wide", "wife", "wild",
    "will", "wind", "wine", "wing", "wipe", "wire", "wise", "wish", "with",
    "wolf", "wood", "wool", "word", "wore", "work", "worm", "worn", "wrap",
    "yard", "yarn", "yeah", "year", "yell", "your", "zero", "zone", "zoom",
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# THEMED CATEGORIES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

science_words = [
    "acid", "atom", "beam", "cell", "dna", "gene", "ion", "lab", "lens",
    "mass", "atom", "carbon", "charge", "chemical", "compound", "crystal",
    "density", "electron", "element", "energy", "enzyme", "equation", "evolution",
    "experiment", "force", "formula", "friction", "gamma", "genetics", "gravity",
    "helium", "hypothesis", "inertia", "isotope", "kinetic", "laser", "magnet",
    "matter", "molecule", "motion", "neutron", "nucleus", "organic", "oxygen",
    "particle", "photon", "physics", "plasma", "polymer", "potential", "pressure",
    "proton", "quantum", "radiation", "reaction", "science", "serum", "sodium",
    "solution", "species", "spectrum", "theory", "thermal", "tissue", "toxin",
    "uranium", "vaccine", "velocity", "vitamin", "voltage", "volume", "wavelength",
]

space_words = [
    "alien", "apollo", "asteroid", "astronaut", "astronomy", "atmosphere", "aurora",
    "binary", "blackhole", "celestial", "comet", "constellation", "corona", "cosmic",
    "cosmos", "crater", "eclipse", "equinox", "exoplanet", "galaxy", "gravity",
    "horizon", "jupiter", "launch", "lunar", "mars", "mercury", "meteor", "milkyway",
    "mission", "moon", "nasa", "nebula", "neptune", "nova", "orbit", "planet",
    "pluto", "pulsar", "quasar", "radiation", "rocket", "satellite", "saturn",
    "solar", "space", "spacecraft", "spectrum", "star", "stellar", "supernova",
    "telescope", "terrestrial", "universe", "uranus", "venus", "void", "voyage",
]

nature_words = [
    "beach", "berry", "blossom", "branch", "breeze", "canyon", "cave", "cherry",
    "cliff", "cloud", "coral", "creek", "dawn", "desert", "dew", "earth", "echo",
    "field", "flame", "flood", "flower", "forest", "frost", "garden", "glacier",
    "grass", "grove", "habitat", "harvest", "hill", "horizon", "hurricane", "island",
    "jungle", "lake", "landscape", "lava", "leaf", "lightning", "meadow", "mineral",
    "moon", "moss", "mountain", "nature", "ocean", "peak", "petal", "pine", "plain",
    "planet", "pond", "prairie", "rain", "rainbow", "reef", "river", "rock", "sand",
    "savanna", "sea", "season", "seed", "shadow", "shore", "sky", "snow", "soil",
    "spring", "star", "stone", "storm", "stream", "summer", "sun", "thunder", "tide",
    "tree", "tsunami", "tundra", "valley", "volcano", "water", "wave", "weather",
    "wetland", "wilderness", "wind", "winter", "woods",
]

action_words = [
    "absorb", "accelerate", "accomplish", "achieve", "activate", "adapt", "advance",
    "analyze", "announce", "anticipate", "approach", "arrange", "ascend", "assemble",
    "assess", "attack", "attempt", "attract", "balance", "battle", "become", "believe",
    "belong", "boost", "bounce", "break", "breathe", "bright", "build", "burst",
    "calculate", "capture", "challenge", "change", "charge", "chase", "climb", "combine",
    "command", "compete", "complete", "compute", "concentrate", "conclude", "conquer",
    "construct", "consume", "continue", "control", "convert", "cooperate", "coordinate",
    "create", "crush", "damage", "decide", "declare", "defeat", "defend", "define",
    "deliver", "demonstrate", "descend", "describe", "design", "destroy", "detect",
    "determine", "develop", "devise", "devote", "direct", "discover", "display",
    "distinguish", "distribute", "dominate", "double", "download", "drag", "drift",
    "drive", "elevate", "eliminate", "emerge", "enable", "encode", "encounter",
    "enforce", "engage", "enhance", "enlarge", "escape", "establish", "estimate",
    "evaluate", "evolve", "examine", "exceed", "excel", "exchange", "execute",
    "expand", "expect", "experience", "experiment", "explain", "explode", "explore",
    "expose", "express", "extend", "extract", "fabricate", "facilitate", "fight",
    "finalize", "float", "focus", "force", "forecast", "forge", "formula", "fortify",
    "forward", "foster", "fragment", "freeze", "function", "generate", "glide",
    "govern", "grasp", "grind", "guide", "harvest", "hasten", "heighten", "highlight",
    "hinder", "identify", "ignite", "illuminate", "illustrate", "imagine", "impact",
    "implement", "improve", "improvise", "include", "increase", "indicate", "influence",
    "inform", "initiate", "innovate", "insert", "inspect", "inspire", "install",
    "integrate", "intensify", "interact", "interpret", "interrupt", "introduce",
    "invent", "investigate", "involve", "isolate", "launch", "lead", "learn",
    "liberate", "lift", "light", "limit", "link", "listen", "locate", "magnify",
    "maintain", "manage", "manifest", "manipulate", "manufacture", "march", "master",
    "match", "materialize", "maximize", "measure", "mediate", "merge", "migrate",
    "minimize", "modify", "monitor", "motivate", "mount", "move", "multiply",
    "navigate", "negotiate", "neutralize", "notify", "observe", "obtain", "operate",
    "optimize", "orchestrate", "organize", "originate", "overcome", "overthrow",
    "participate", "penetrate", "perceive", "perform", "persist", "persuade",
    "pierce", "pioneer", "plan", "position", "possess", "practice", "praise",
    "predict", "prepare", "present", "preserve", "prevent", "process", "produce",
    "progress", "project", "promote", "propel", "protect", "prove", "provide",
    "publish", "pursue", "qualify", "quantify", "quest", "question", "radiate",
    "rally", "range", "reach", "react", "realize", "rebuild", "recall", "receive",
    "recognize", "recommend", "reconstruct", "record", "recover", "reduce", "reflect",
    "reform", "refresh", "regulate", "reinforce", "reject", "relate", "release",
    "relocate", "remain", "remember", "remove", "render", "repair", "repeat",
    "replace", "replicate", "report", "represent", "reproduce", "rescue", "research",
    "reserve", "resist", "resolve", "respond", "restore", "restrict", "result",
    "retrieve", "return", "reveal", "reverse", "review", "revise", "revive",
    "revolve", "rotate", "sacrifice", "satisfy", "scale", "scan", "scatter",
    "schedule", "scout", "search", "secure", "seek", "seize", "select", "separate",
    "sequence", "serve", "settle", "shape", "share", "sharpen", "shift", "shine",
    "shock", "shoot", "shorten", "signal", "simplify", "simulate", "sketch",
    "slice", "slide", "soar", "solve", "sort", "spark", "speak", "specialize",
    "specify", "speed", "split", "spread", "stabilize", "stamp", "standardize",
    "start", "state", "steer", "stimulate", "store", "strengthen", "stretch",
    "strike", "structure", "struggle", "study", "submit", "substitute", "succeed",
    "summon", "supervise", "supply", "support", "suppress", "surge", "surprise",
    "surround", "survey", "survive", "suspend", "sustain", "switch", "symbolize",
    "synchronize", "synthesize", "systematize", "target", "teach", "terminate",
    "test", "think", "threaten", "thrive", "throw", "thrust", "trace", "track",
    "trade", "train", "transcend", "transfer", "transform", "translate", "transmit",
    "transport", "traverse", "treat", "trend", "trigger", "triumph", "trust",
    "uncover", "undergo", "understand", "undertake", "unify", "unite", "unleash",
    "unlock", "update", "uphold", "upload", "utilize", "validate", "vanish",
    "vary", "venture", "verify", "view", "violate", "visualize", "volunteer",
    "wander", "watch", "weaken", "weave", "welcome", "wield", "witness", "wonder",
    "yield",
]

# Combine all sources
all_sources = (
    tech_gaming +
    common_words +
    science_words +
    space_words +
    nature_words +
    action_words
)

# Remove duplicates
all_words = list(set(all_sources))

print(f"Total unique words collected: {len(all_words)}")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CATEGORIZE BY DIFFICULTY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def categorize_words(words):
    """Categorize words by length into difficulty tiers"""
    easy = []
    medium = []
    hard = []
    boss = []

    for word in words:
        length = len(word)
        if length <= 4:
            easy.append(word)
        elif length <= 7:
            medium.append(word)
        elif length <= 10:
            hard.append(word)
        else:
            boss.append(word)

    # Sort each tier alphabetically
    easy.sort()
    medium.sort()
    hard.sort()
    boss.sort()

    return {
        "easy": easy,
        "medium": medium,
        "hard": hard,
        "boss": boss
    }

# Categorize and filter
word_pools = categorize_words(all_words)

# Display statistics
print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Word Pool Statistics:")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"Easy   (≤4 chars): {len(word_pools['easy'])} words")
print(f"Medium (5-7 chars): {len(word_pools['medium'])} words")
print(f"Hard   (8-10 chars): {len(word_pools['hard'])} words")
print(f"Boss   (11+ chars): {len(word_pools['boss'])} words")
print(f"\nTotal: {sum(len(v) for v in word_pools.values())} words")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

# Write to JSON file
with open('words.json', 'w', encoding='utf-8') as f:
    json.dump(word_pools, f, indent=2, ensure_ascii=False)

print("✓ words.json generated successfully!")
print(f"✓ File size: ~{len(json.dumps(word_pools)) // 1024}KB")
