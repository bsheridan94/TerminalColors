class TerminalColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print TerminalColors.HEADER + "Fuck Yeah" + TerminalColors.ENDC
print TerminalColors.BLUE + "Fuck Yeah" + TerminalColors.ENDC
print TerminalColors.GREEN + "Fuck Yeah" + TerminalColors.ENDC
print TerminalColors.WARNING + "Fuck Yeah" + TerminalColors.ENDC
print TerminalColors.FAIL + "Fuck Yeah" + TerminalColors.ENDC
print TerminalColors.BOLD + "Fuck Yeah" + TerminalColors.ENDC
print TerminalColors.UNDERLINE + "Fuck Yeah" + TerminalColors.ENDC
