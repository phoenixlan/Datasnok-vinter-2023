import argparse
import os
import random
from secrets import choice

import jinja2

environment = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
template = environment.get_template("template.py.jinja2")

parser = argparse.ArgumentParser(description="Generates obfuscated python classes")
parser.add_argument("output", metavar="o", type=str, help="Output file")
parser.add_argument("count", metavar="c", type=int, help="Number of steps")
parser.add_argument("width", metavar="w", type=int, help="Number of steps")

args = parser.parse_args()

if not os.path.exists(args.output):
    os.makedirs(args.output)

total_generated = 0

possible_passwords = [
    "5w49",
    "l3375P33k",
    "xbg",
    "k3wL_83An5",
    "Pho3N1X",
    "1337",
    "5w4G4d3Ll1c",
    "8jaRn3",
    "xR4Y",
    "IrhAh",
    "c00l5sh",
    "p3kop3ko"
]

for r in range(0, args.count):
    for w in range(0, args.width):
        classname = "Bjarne%d" % total_generated
        total_generated += 1

        filename = os.path.join(args.output, "%s.py" % classname)

        # Class parent
        parent = None
        if r != 0:
            parent = "Bjarne%d" % (random.randrange(0, total_generated-1))

        choices = possible_passwords
        if r != 0:
            choices = choices + [
                None,
                None,
                None,
                None,
                None,
                None
            ]

        a = random.choice(choices)
        b = random.choice(choices)
        c = random.choice(choices)
        d = random.choice(choices)
        e = random.choice(choices)
        f = random.choice(choices)
        g = random.choice(choices)

        out = template.render({
            "passwords": {
                "a": a,
                "b": b,
                "c": c,
                "d": d,
                "e": e,
                "f": f,
                "g": g
            },
            "should_super": random.randrange(0, 50) != 9,
            "classname": classname,
            "class_parent": parent
        })
        with open(filename, mode="w", encoding="utf-8") as message:
            message.write(out)
            print("... wrote %s" % filename)