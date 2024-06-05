#!/usr/bin/python3
import sys

def say_something(name,greeting):
    print(f"{greeting} {name}")

        
if __name__ == "__main__":
    if "--help" in sys.argv:
        print(f"Usage: {sys.argv[0]} --name <NAME> --greeting <ARGUMENT>")
        sys.exit()
    if "--name" in sys.argv:
        name_index = sys.argv.index("--name") + 1
        if name_index < len(sys.argv):
            name = sys.argv[name_index]
    if "--greeting" in sys.argv:
        g_index = sys.argv.index("--greeting") + 1 
        if g_index < len(sys.argv):
            greeting = sys.argv[g_index]
    say_something(name,greeting)        
    
