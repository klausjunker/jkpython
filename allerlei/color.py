class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   ROUGE = '\033[91m'
   ROT = '\x1B[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   TAB = '\x09'

print(color.BOLD + 'Hello, World!' + color.END)
print(color.BOLD+color.ROUGE + 'ROUGE: Hello, \011 World!' + color.END)
print(color.BOLD+color.ROT + 'ROT: Hello, \011 World!' + color.END)
print(color.BOLD + 'Hello, '+color.TAB+' TAB:World!' + color.END)
print(color.BOLD + 'Hello1, '+color.TAB+' TAB:World!' + color.END)
print(color.BOLD + 'Hello12, '+color.TAB+' TAB:World!' + color.END)
print(color.BOLD + 'Hello123, '+color.TAB+' TAB:World!' + color.END)
print(color.BOLD+color.RED + 'ROT!' + color.END)
print(color.BOLD+color.YELLOW + 'GELB!' + color.END)
