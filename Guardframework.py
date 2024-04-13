import sys

# ASCII Art
skull_art = r"""
                  ___====-_  _-====___
            _--^^^#####//      \\#####^^^--_
         _-^##########// (    ) \\##########^-_
        -############//  |\^^/|  \\############-
      _/############//   (@::@)   \\############\_
     /#############((     \\//     ))#############\
    -###############\\    (oo)    //###############-
   -#################\\  / "" \  //#################-
  -###################\\/  ()  \//###################-
 _#/|##########/\######(   (())   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  \  ``  /  /##/\#/  \/\#/\#/\| \
`  |/  V  V `   V  \#\|   |   |   |/##/  V   '  V  V  \|  '
   `   `  `      `   / |  |   |  | \   '      '  '   '
                    (  |  |   |  |  )
                   __\ |  |   |  | /__
                    (vvv(VVV)(VVV)vvv)

 --------------------------------------------------------
"""
# Color definitions using ANSI escape codes
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def main_menu():
    print(Color.RED + skull_art + Color.END)
    print(Color.BOLD + Color.YELLOW + "Welcome to the GuardFramework!" + Color.END)
    print(Color.BLUE + "Developed by Odoi Nii Osa as a final year project at GIMPA.\n" + Color.END)
    print(Color.CYAN + "The GuardFramework is a comprehensive security scanning tool." + Color.END)
    print("Please select the scanner you want to use:")
    print(Color.GREEN + "1. Network Vulnerability Scanner (netguard)" + Color.END)
    print(Color.PURPLE + "2. Web Vulnerability Scanner (webguard)" + Color.END)
    print(Color.DARKCYAN + "3. Exit" + Color.END)

    choice = input(Color.CYAN + "Enter your choice (1/2/3): " + Color.END).strip()

    if choice == '1':
        netguard_instructions()
    elif choice == '2':
        webguard_menu()
    elif choice == '3':
        sys.exit(Color.BOLD + Color.RED + "Thank you for using the GuardFramework." + Color.END)
    else:
        print(Color.RED + "Invalid choice. Please try again." + Color.END)
        main_menu()

def netguard_instructions():
    print(Color.YELLOW + "\nYou've selected the Network Vulnerability Scanner (netguard)." + Color.END)
    print("This component of the GuardFramework scans networks for vulnerabilities.")
    print("Usage guide and options will be detailed when running the netguard component.")
    back_to_menu()

def webguard_menu():
    print(Color.YELLOW + "\nYou've selected the Web Vulnerability Scanner (webguard)." + Color.END)
    print("This component of the GuardFramework scans web addresses for vulnerabilities.")
    print("Select the functionality you want to explore:")
    print(Color.GREEN + "1. Spider a URL for directory listing" + Color.END)
    print(Color.BLUE + "2. Perform vulnerability scans (XSS, SQL Injection, HTML Injection)" + Color.END)
    print(Color.PURPLE + "3. Find subdomains of a site" + Color.END)
    print(Color.CYAN + "4. Dump all sites by IP or use a dork" + Color.END)
    print(Color.RED + "5. Encrypt a word using different hash types" + Color.END)
    print(Color.DARKCYAN + "6. Perform WordPress specific actions (Brute Force, User Enumerate)" + Color.END)
    print(Color.YELLOW + "7. More options..." + Color.END)
    print(Color.GREEN + "8. Exit to Main Menu" + Color.END)

    choice = input(Color.CYAN + "Enter your choice: " + Color.END).strip()

    if choice == '1':
        print("\nUsage: python3 Webguard.py --spider [URL]")
    elif choice == '2':
        print("\nUsage examples for vulnerability scans:")
        print('python3 Webguard.py --xss "paste url here"')
        print('python3 Webguard.py --sql "paste url here"')
        print('python3 Webguard.py --HTMLinj "paste url here"')
    elif choice == '3':
        print("\nUsage: python3 Webguard.py --subdomain [site]")
    elif choice == '4':
        print("\nUsage examples for site dumping:")
        print("python3 Webguard.py --RevIP [IP address]")
        print("python3 Webguard.py --dork [dork] --country [country code]")
    elif choice == '5':
        print("\nUsage examples for encryption:")
        print("python3 Webguard.py --word [word] --type [md5/sha1/sha256...]")
    elif choice == '6':
        print("\nUsage examples for WordPress actions:")
        print("python3 Webguard.py --wordpress [URL] --ListUsername [username list] --ListPassword [password list]")
        print("python3 Webguard.py --wordpress [URL] --enum")
    elif choice == '7':
        more_options()
    elif choice == '8':
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        webguard_menu()

def back_to_menu():
    choice = input(Color.YELLOW + "\nWould you like to go back to the main menu? (yes/no): " + Color.END).lower().strip()
    if choice == 'yes':
        main_menu()
    else:
        sys.exit(Color.BOLD + Color.RED + "Thank you for using the GuardFramework." + Color.END)

if __name__ == "__main__":
    main_menu()
