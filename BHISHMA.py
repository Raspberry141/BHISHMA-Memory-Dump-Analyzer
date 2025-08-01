from pyfiglet import figlet_format
from colorama import Fore, Style
import subprocess

print(Fore.BLUE + figlet_format("BHISHMA"))
print(Fore.RED + "[*] Created by Vizz\n" + Style.RESET_ALL)

def analyze_memory():
    print(Fore.YELLOW + "[*] Running Volatility Plugins..." + Style.RESET_ALL)
    plugins = ["pslist", "dlllist", "netscan"]
    for plugin in plugins:
        print(Fore.GREEN + f"\n[+] {plugin.upper()} Results" + Style.RESET_ALL)
        subprocess.call(['volatility', '-f', 'memdump.raw', '--profile=Win7SP1x64', plugin])

analyze_memory()