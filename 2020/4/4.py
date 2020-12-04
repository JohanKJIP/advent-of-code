import re

def count_valid_passports(validation: [], passports: [], validate_values=False) -> int:
    valid = 0
    for passport in passports:
        if (all (field in passport for field in validation.keys())):
            if validate_values:
                # validate values
                valid_values = True
                for field in validation.keys():
                    pattern = validation[field]
                    result = re.match(pattern, passport[field])
                    if not result:
                        valid_values = False
                        break
                if valid_values:
                    valid += 1
            else:
                valid += 1
    return valid


if __name__ == "__main__":
    # parse file
    passports = []
    with open('input.in', 'r') as passport_file:
        passport = {} 
        for line in passport_file:
            if line == '\n':
                passports.append(passport)
                passport = {}
                continue

            line = line.replace('\n', '').split(' ')
            for field in line:
                key, value = field.split(':')
                passport[key] = value
        # add last password
        passports.append(passport)

    # Required fields and their data validation
    validation = {
        'byr': '^19[2-9][0-9]|200[0-2]$',
        'iyr': '^201[0-9]|2020$', 
        'eyr': '^202[0-9]|2030$', 
        'hgt': '^1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in$', 
        'hcl': '^#([0-9]|[a-f]){6}$', 
        'ecl': '^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$', 
        'pid': '^[0-9]{9}$'}
    valid = count_valid_passports(validation, passports)
    print(len(passports))
    print(valid)
    print(count_valid_passports(validation, passports, validate_values=True))
