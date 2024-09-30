import os
from colorama import Fore, Style

# Get the NAME environment variable, default to "World" if not set
name = os.environ.get('NAME', 'World')

# Print the colorful greeting
print(f"{Fore.GREEN}Hello {Fore.BLUE}{name}{Fore.GREEN}!{Style.RESET_ALL}")

