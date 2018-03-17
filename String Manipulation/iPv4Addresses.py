"""
You are given a String containing at least 4 numbers that represented an IPv4 Address, but the separator data - i.e. the dots that separate each Byte in a 4 Byte Ipv4 address, has been lost. Write a method - generate_ip_address that takes in this String and returns a List of strings containing all possible IPv4 Addresses that can be generated from the given sequence of decimal integers.


Note:

- The IP Addresses for this problem are written in the decimal dot notation.
 - You must use all the digits in the input String
 - The order in which the IP Addresses are returned does not matter
 - 0.0.0.1 and 0.0.0.01 may be considered 2 distinct possibilities. i.e. do not ignore leading or trailing 0s.

Examples:

generate_ip_address("0001") ==> ["0.0.0.1"]

generate_ip_address("0010") ==> ["0.0.1.0"]

generate_ip_address("25525511135") ==> ["255.255.11.135", "255.255.111.35"]
"""


# Collections module has already been imported.
def generate_ip_address(input):
    if len(input) < 4:
        return []

    # create return list
    ret = list()
    deque = []
    # push the first 3 node to deque
    addChildrenToDeque("", input, 0, deque)

    while deque:
        current = deque.pop()
        if current.level == 4 and current.successor == "":
            ret.append(current.predecessor)

        if current.level >= 4:
            continue
        # push next 3 children to deque
        addChildrenToDeque(current.predecessor, current.successor, current.level, deque)

    return ret


def isValidIP(iP):
    return 0 <= int(iP) <= 255


def addChildrenToDeque(predecessor, successor, level, deque):
    i = 1
    while i <= 3:
        if len(successor) < i:
            break
        ip_to_append = successor[0:i]
        if isValidIP(ip_to_append):
            if level > 0:
                deque.append(IpLevelNode(predecessor + "." + ip_to_append, level + 1, successor[i:]))
            else:
                deque.append(IpLevelNode(ip_to_append, level + 1, successor[i:]))
        i += 1


class IpLevelNode:
    def __init__(self, predecessor, level, successor):
        self.predecessor = predecessor
        self.level = level
        self.successor = successor