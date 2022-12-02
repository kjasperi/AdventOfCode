import sys


def get_lines_from_file():
    input_file = sys.argv[1]

    input_lines = []

    with open(input_file) as inf:
        for line in inf:
            input_lines.append(line.strip('\n'))
    return input_lines


class Passport:
    def __init__(self):
        # byr (Birth Year)
        self.byr = None
        # iyr (Issue Year)
        self.iyr = None
        # eyr (Expiration Year)
        self.eyr = None
        # hgt (Height)
        self.hgt = None
        # hcl (Hair Color)
        self.hcl = None
        # ecl (Eye Color)
        self.ecl = None
        # pid (Passport ID)
        self.pid = None
        # cid (Country ID)
        self.cid = None

    def is_valid(self):
        return self.is_byr_valid() and self.is_iyr_valid() and \
            self.is_eyr_valid() and self.is_hgt_valid() and \
            self.is_hcl_valid() and self.is_ecl_valid() and \
            self.is_pid_valid()

    def is_byr_valid(self):
        if self.byr:
            byr = int(self.byr)
            if byr < 1920:
                return False
            if byr > 2002:
                return False
            return True

        return False

    def is_iyr_valid(self):
        if self.iyr:
            iyr = int(self.iyr)
            if iyr < 2010:
                return False
            if iyr > 2020:
                return False
            return True

        return False

    def is_eyr_valid(self):
        if self.eyr:
            eyr = int(self.eyr)
            if eyr < 2020:
                return False
            if eyr > 2030:
                return False
            return True

        return False

    def is_hgt_valid(self):
        if self.hgt:
            l = len(self.hgt) - 2

            value = int(self.hgt[:l])
            unit = self.hgt[l:]

            if unit == 'cm':
                if value < 150:
                    return False
                if value > 193:
                    return False
                return True
            elif unit == 'in':
                if value < 59:
                    return False
                if value > 76:
                    return False
                return True
            return False

        return False

    def is_hcl_valid(self):
        if self.hcl:
            num_char = len(self.hcl)
            if num_char != 7:
                return False

            if self.hcl[0] != '#':
                return False

            valid_alphas = ['a', 'b', 'c', 'd', 'e', 'f']

            for ch in self.hcl[1:]:
                
                if not(ch.isdigit() or (ch in valid_alphas)):
                    return False
            return True
        return False

    def is_ecl_valid(self):
        if self.ecl:
            valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

            return self.ecl in valid_ecl
        return False

    def is_pid_valid(self):
        if self.pid:
            if len(self.pid) != 9:
                return False

            return self.pid.isnumeric()
        return False

    def add_fields(self, passport_fields):
        for field in passport_fields:
            self.add_field(field)

    def add_field(self, field):
        (key, value) = field.split(':')
        if key == 'byr':
            self.byr = value
        elif key == 'iyr':
            self.iyr = value
        elif key == 'eyr':
            self.eyr = value
        elif key == 'hgt':
            self.hgt = value
        elif key == 'hcl':
            self.hcl = value
        elif key == 'ecl':
            self.ecl = value
        elif key == 'pid':
            self.pid = value
        elif key == 'cid':
            self.cid = value


def read_passports():
    inputlines = get_lines_from_file()
    all_passports = []
    passport = Passport()

    for line in inputlines:
        split_line = line.split()
        passport.add_fields(split_line)
        if line == "":
            all_passports.append(passport)
            passport = Passport()
    all_passports.append(passport)

    return all_passports


all_passports = read_passports()

num_valid = 0
for passport in all_passports:
    if passport.is_valid():
        num_valid += 1

print(num_valid)
