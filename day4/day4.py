import re

def load_passport(generator):
    """
    Takes a generator of strings and extracts a single passport.
    Returns the passport or None if no passport detected.
    Generator is moved to start of next passport (or end).
    """
    lines = []
    for line in generator:
        if len(line.strip()):
            lines.append(line)
        else:
            break
    if len(lines):
        return {x.split(":")[0] : x.split(":")[1] for x in (' ').join(lines).split()}
    else: lines = None
    return lines

def validate_passport_lax(passport):
    """
    Takes a passport and returns if passport passes law validation."
    """
    REQ_FIELDS= ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    missing_fields = set(REQ_FIELDS) - set(passport.keys())
    return (len(missing_fields) == 0)

def validate_passport_strict(passport):
    """
    Takes a passport and returns if passport passes strict validation."
    """
    valid = validate_passport_law(passport)
    if valid:
        VALIDATORS = {
                "byr" : lambda x: 1920 <= int(x) <= 2002,
                "iyr" : lambda x: 2010 <= int(x) <= 2020,
                "eyr" : lambda x: 2020 <= int(x) <= 2030,
                "hgt" : lambda x: (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76),
                "hcl" : lambda x: re.match("^#[a-f0-9]{6}$",x) != None,
                "ecl" : lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                "pid" : lambda x: re.match("^[0-9]{9}$", x) != None
        }
        for x in VALIDATORS:
            valid &= VALIDATORS[x](passport[x])
    return valid

def validate(filename, validator):
    """
    Counts how many of the passports in a file pass the given validation func
    """
    with open("input.txt") as fd:
        passport = 1
        good = 0
        while passport:
            passport = load_passport(fd)
            if passport:
                good += validator(passport)
    return good


if __name__ == "__main__":
    print(validate("input.txt",validate_passport_lax))
    print(validate("input.txt",validate_passport_strict))

