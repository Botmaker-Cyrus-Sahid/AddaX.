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
