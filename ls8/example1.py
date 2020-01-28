import sys

# python3 file.py filename

if len(sys.argv) != 2:
    print("Usage: file.py filename", file=sys.stderr)
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        commands = []
        for line in f:
            # Ignore comments
            comment_split = line.split('#')
            val = comment_split[0]
            x = (val, 2)
            print(f'{x:08b}:{x:d}')
            commands.append(x)
        # print(commands)
        
except FileNotFoundError:
    print(f'{sys.argv[0]} : {sys.argv[1]} Not found')
    sys.exit(2)