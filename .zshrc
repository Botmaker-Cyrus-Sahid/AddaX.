#LOCK_START
clear
echo -e '\033[1;32m'
echo '  System check...'
sleep 0.2
echo '  Encrypted link established.'
sleep 0.2
clear
attempt=1
while [ $attempt -le 3 ]; do
    echo -e "\n\033[1;96m╔══════════════════════════════════════╗"
    echo -e "║        \033[1;31mSECURE SHELL ACCESS           \033[1;96m║"
    echo -e "╚══════════════════════════════════════╝\033[0m"
    echo -ne "\033[1;93m [Attempt $attempt/3] Enter Key: \033[0m"
    read -s pass_input
    echo
    if [ "$pass_input" = "00" ]; then
        echo -e "\033[1;32m ACCESS GRANTED.\033[0m"
        sleep 1
        clear
        break
    else
        echo -e "\033[1;31m DENIED.\033[0m"
        if [ $attempt -eq 3 ]; then
            exit
        fi
        attempt=$((attempt + 1))
    fi
done
#LOCK_END

ZSH_THEME="h4Ck3r"
export ZSH=$HOME/.oh-my-zsh
plugins=(git)

source $HOME/.oh-my-zsh/oh-my-zsh.sh
[[ -f /data/data/com.termux/files/home/.oh-my-zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh ]] && source /data/data/com.termux/files/home/.oh-my-zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
[[ -f /data/data/com.termux/files/home/.oh-my-zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh ]] && source /data/data/com.termux/files/home/.oh-my-zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

clear
echo -e "\033[1;32m[*] BOOTING TERMUX-OS v3..."
echo -ne "\033[1;36m[LOADING MODULES] \033[1;32m"
for i in {1..25}; do
    echo -ne "█"
    sleep 0.02
done
echo -e "\033[0m"
sleep 0.4
clear


draw_banner() {
    local BOX_WIDTH=56
    local cyan='\033[0;36m'
    local reset='\033[0m'
    
    print_center() {
        local text="$1"
        local len=${#text}
        local space_len=$(( (BOX_WIDTH - 2 - len) / 2 ))
        printf "${cyan} ║%*s${reset}%s${cyan}%*s║${reset}\n" $space_len "" "$text" $(( BOX_WIDTH - 2 - len - space_len )) ""
    }

    draw_line() {
        local char=$1
        local end=$2
        printf "${cyan} %s" "$char"
        for ((i=0; i<BOX_WIDTH-2; i++)); do printf "═"; done
        printf "%s${reset}\n" "$end"
    }

    draw_line "╔" "╗"
    print_center ""
    
    # FIGLET CENTERED WITHIN BOX WIDTH
    figlet -c -f ASCII-Shadow -w $BOX_WIDTH "\AS S4H1D" | lolcat
    
    print_center ""
    print_center "SYSTEM: ONLINE  |  USER: ROOT"
    print_center "OS : Termux-OS v3"
    print_center "SECURE CONNECTION ESTABLISHED"
    print_center ""
    draw_line "╚" "╝"
}

draw_banner
