import sys

def get_data():
    with open(sys.argv[1]) as inf:
        return inf.read()

data = get_data()
lines = data.split("\n")

valid_commands = ["cd", "ls"]

class Efile():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.type = "file"

    def get_size(self):
        return self.size

class Edir():
    def __init__(self, name):
        self.name = name
        self.children = []
        self.type = "dir"
        self.parent = self

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)

    def has_child(self, child_name):
        for child in self.children:
            if child.name == child_name:
                return True
        return False
    def get_child(self, child_name):
        for child in self.children:
            if child.name == child_name:
                return child
    
    def get_size(self):
        size = 0
        for child in self.children:
            size += child.get_size()
        return size

# GLOBAL
root = Edir("/")
current_dir = root

dir_sizes = []

def print_file_system(dir, tabs=""):
    if dir.type == "file":
        print(tabs + "- " + dir.name + " size=" + str(dir.size))

    else:
        s = dir.get_size()
        print(tabs + "- " + dir.name + " size=" + str(s))
        dir_sizes.append(s)
        if dir.children:
            for child in dir.children:
                print_file_system(child, tabs + "   ")

def try_command(cmd, args, expected_output = ""):
    print(cmd, args, expected_output)
    global root
    global current_dir
    if cmd == "cd":
        #print("cd")
        to_dir = args[0] 
        if to_dir == "/":
            current_dir = root
            return True
        elif to_dir == "..":
            current_dir = current_dir.parent
            return True
        else:
            if not current_dir.has_child(to_dir):
                #print("No child: " + to_dir)
                new_dir = Edir(to_dir)
                new_dir.set_parent(current_dir)
                current_dir.add_child(new_dir)
            current_dir = current_dir.get_child(to_dir)            

    elif cmd == "ls":
        print("########## ls")
        print("current " + current_dir.name)
        print("Expected: ")
        for l in expected_output:
            print(l)
            size_, name = l.split()
            if size_ != "dir":
                print(size_)
                s = int(size_)
                f = Efile(name, s)
                current_dir.add_child(f)
        
        for child in current_dir.children:
            print(child.name)

def identify_file_system(lines):
    cmd = ""
    args = []
    expected_output = []
    for line in lines:
        print("line: " + line)

        if line.startswith("$"):
            try_command(cmd, args, expected_output) # Execute prev command

            print()
            cmd = ""
            args = []
            expected_output = []
            input = line[2:].split()
            cmd = input[0]
            if len(input) > 1:
                args = input[1:]

        else:
            expected_output.append(line)

    try_command(cmd, args, expected_output) # Execute prev command


identify_file_system(lines)
print_file_system(root)

p1 = 0
p2 = 0

got_p2 = False

root_size = root.get_size()
dir_sizes.sort()
for size in dir_sizes:
    #size = dir_sizes[dir]
    if size <= 100000:
        p1 += size
    if 70000000 - (root_size - size) > 30000000 and not got_p2:
        p2 = size
        got_p2 = True
        
print(p1)
print(p2)