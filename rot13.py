a = ord('a')
z = ord('z')


def rot13(msg):
    cypher = ""
    for character in msg:
        cypher += chr((((ord(character) - a) + 13) % 26) + a)
    return cypher


if __name__ == "__main__":
    while True:
        msg = input()
        valid = True

        for character in msg:
            if not (a <= ord(character) <= z):
                print("Invalid input. Just lowercase characters from the alphabet.")
                valid = False
                break

        if valid:
            cypher = rot13(msg)
            print(cypher)
