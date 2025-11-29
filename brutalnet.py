# Author: cybermad
# BrutalNET network denial-of-service through ARP Spoofing.

import os
from lib.spoof import *
from lib.scan import *

h = "\033[38;5;118m"
c = "\033[91m"
g = "\033[92m"
r = "\033[0m"
    
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{c}      ____             __        ___   ______________
     / __ )_______  __/ /_____ _/ / | / / ____/_  __/
    / __  / ___/ / / / __/ __ `/ /  |/ / __/   / /   
   / /_/ / /  / /_/ / /_/ /_/ / / /|  / /___  / /    
  /_____/_/   \__,_/\__/\__,_/_/_/ |_/_____/ /_/         
{r}    
    {g}[*]{r}      {h}ARP Attack Tool.{r}               {g}[*]{r} 
    {g}[*]{r}      {h}Version : 1.0{r}                    {g}[*]{r} 
    {g}[*]{r}      {h}Created :{c} {c}cybermad{r}               {g}[*]{r}
    {g}[*]{r}      {h}github  : github.com/cybermads{r}   {g}[*]{r}
    {g}[*]{r}      {h}youtube : youtube.com/@cybermads{r} {g}[*]{r}
            
    {c}network denial-of-service through ARP Spoofing.{r}
            
    {g}[1]{r} ARP Network denial of service
    {g}[2]{r} ARP Network device discovery
{r}
""")


def main():
    while True:
        banner()
        select = input(f"""
╔═══[{c}root{r}@{c}BrutalNET{r}]
╚══{c}>{r} """)

        if select == "1":
            arpspoof()

        elif select == "2":
            scan()

            

if __name__ == "__main__":
    main()




