import random

figlet_ansi_shadow = """

████████╗██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
╚══██╔══╝██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
   ██║   ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
   ██║   ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
   ██║   ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                                                                 
"""

figlet_big = """
 _______        _     _   _               _                                 
|__   __|      | |   | \ | |             | |                                
   | | ___  ___| |__ |  \| | _____      _| |     ___   __ _  __ _  ___ _ __ 
   | |/ _ \/ __| '_ \| . ` |/ _ \ \ /\ / / |    / _ \ / _` |/ _` |/ _ \ '__|
   | |  __/ (__| | | | |\  | (_) \ V  V /| |___| (_) | (_| | (_| |  __/ |   
   |_|\___|\___|_| |_|_| \_|\___/ \_/\_/ |______\___/ \__, |\__, |\___|_|   
                                                       __/ | __/ |          
                                                      |___/ |___/    
"""

figlet_bloody = """

▄▄▄█████▓ ██▓     ▒█████    ▄████   ▄████ ▓█████  ██▀███  
▓  ██▒ ▓▒▓██▒    ▒██▒  ██▒ ██▒ ▀█▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░    ▒██░  ██▒▒██░▄▄▄░▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██░    ▒██   ██░░▓█  ██▓░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
  ▒██▒ ░ ░██████▒░ ████▓▒░░▒▓███▀▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
  ▒ ░░   ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░    ░ ░ ▒  ░  ░ ▒ ▒░   ░   ░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
  ░        ░ ░   ░ ░ ░ ▒  ░ ░   ░ ░ ░   ░    ░     ░░   ░ 
             ░  ░    ░ ░        ░       ░    ░  ░   ░     
                                                                             
"""

figlet_doom = """
 _____         _     _   _               _                                 
|_   _|       | |   | \ | |             | |                                
  | | ___  ___| |__ |  \| | _____      _| |     ___   __ _  __ _  ___ _ __ 
  | |/ _ \/ __| '_ \| . ` |/ _ \ \ /\ / / |    / _ \ / _` |/ _` |/ _ \ '__|
  | |  __/ (__| | | | |\  | (_) \ V  V /| |___| (_) | (_| | (_| |  __/ |   
  \_/\___|\___|_| |_\_| \_/\___/ \_/\_/ \_____/\___/ \__, |\__, |\___|_|   
                                                      __/ | __/ |          
                                                     |___/ |___/ 
"""

figlet_drpepper = """
 ___           _    _ _              _                            
|_ _|___  ___ | |_ | \ | ___  _ _ _ | |   ___  ___  ___  ___  _ _ 
 | |/ ._>/ | '| . ||   |/ . \| | | || |_ / . \/ . |/ . |/ ._>| '_>
 |_|\___.\_|_.|_|_||_\_|\___/|__/_/ |___|\___/\_. |\_. |\___.|_|  
                                              <___'<___'          

"""

figlet_ogre = """
 _____          _         __               __                             
/__   \___  ___| |__   /\ \ \_____      __/ /  ___   __ _  __ _  ___ _ __ 
  / /\/ _ \/ __| '_ \ /  \/ / _ \ \ /\ / / /  / _ \ / _` |/ _` |/ _ \ '__|
 / / |  __/ (__| | | / /\  / (_) \ V  V / /__| (_) | (_| | (_| |  __/ |   
 \/   \___|\___|_| |_\_\ \/ \___/ \_/\_/\____/\___/ \__, |\__, |\___|_|   
                                                    |___/ |___/           

"""

figlet_slant = """
  ______          __    _   __              __                               
 /_  __/__  _____/ /_  / | / /___ _      __/ /   ____  ____ _____ ____  _____
  / / / _ \/ ___/ __ \/  |/ / __ \ | /| / / /   / __ \/ __ `/ __ `/ _ \/ ___/
 / / /  __/ /__/ / / / /|  / /_/ / |/ |/ / /___/ /_/ / /_/ / /_/ /  __/ /    
/_/  \___/\___/_/ /_/_/ |_/\____/|__/|__/_____/\____/\__, /\__, /\___/_/     
                                                    /____//____/ 
"""

figlet_small = """
 _____       _    _  _            _                           
|_   _|__ __| |_ | \| |_____ __ _| |   ___  __ _ __ _ ___ _ _ 
  | |/ -_) _| ' \| .` / _ \ V  V / |__/ _ \/ _` / _` / -_) '_|
  |_|\___\__|_||_|_|\_\___/\_/\_/|____\___/\__, \__, \___|_|  
                                           |___/|___/         
										   
"""

figlet_smslant = """
 ______        __   _  __           __                         
/_  __/__ ____/ /  / |/ /__ _    __/ /  ___  ___ ____ ____ ____
 / / / -_) __/ _ \/    / _ \ |/|/ / /__/ _ \/ _ `/ _ `/ -_) __/
/_/  \__/\__/_//_/_/|_/\___/__,__/____/\___/\_, /\_, /\__/_/   
                                           /___//___/   
"""

figlet_standard = """
 _____         _     _   _               _                                
|_   _|__  ___| |__ | \ | | _____      _| |    ___   __ _  __ _  ___ _ __ 
  | |/ _ \/ __| '_ \|  \| |/ _ \ \ /\ / / |   / _ \ / _` |/ _` |/ _ \ '__|
  | |  __/ (__| | | | |\  | (_) \ V  V /| |__| (_) | (_| | (_| |  __/ |   
  |_|\___|\___|_| |_|_| \_|\___/ \_/\_/ |_____\___/ \__, |\__, |\___|_|   
                                                    |___/ |___/ 
"""													

def get_banner():
    return random.choice([figlet_ansi_shadow, figlet_big, figlet_doom, figlet_drpepper, figlet_ogre, figlet_slant, figlet_small, figlet_smslant, figlet_standard])