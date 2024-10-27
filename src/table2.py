#this is my file for the table 2
class Table2:
    def test(self, pos, move_before, pos2):
        match pos2:
            case 33:
                return "raise"
            case 32:
                if move_before == "raise":
                    return "call"
                if pos == 0 and move_before == "fold":
                    return "fold"
                return "raise"
            case 22:
                if move_before == "raise":
                    return "call"
                if pos == 0:
                    return "fold"
                if pos == 2 and move_before == "fold":
                    return "raise"
                return "call"
            case 31:
                if pos == 0 or move_before == "raise":
                    return "fold"
                if move_before == "fold":
                    return "raise"
                if pos == 2 and move_before == "call":
                    return "raise"
                return "call"
            case 30:
                if pos == 0 or move_before == "raise":
                    return "fold"
                if pos == 1 and move_before == "call":
                    return "call"
                return "raise"
            case 13:
                if pos == 3:
                    if move_before == "fold":
                        return "raise"
                    if move_before == "call":
                        return "call"
                return "fold"
            case others:
                return "fold"

    def __init__(self):
        self.dictionary = {'22': 22, 'A2': 30, '33': 22, 'A3': 30, '44': 22, 'A4': 30, '55': 22, 'A5': 30, '66': 22, 'A6': 30, '77': 22,
                    'A7': 30, '88': 22, 'A8': 30, '99': 32, 'A9': 30, '1010': 32, '98': 13, '87': 13, '76': 13, '54': 13,
                    'J10': 13, 'Q10': 13, 'K10': 13, 'A10': 31, 'JJ': 32, 'QJ': 13, 'KJ': 13, 'AJ': 31, 'QQ': 33,
                    'KQ': 13, 'AQ': 31, 'KK': 33, 'AK': 33, 'AA': 33}