windowsServer = []
unix = []
linux = []
netware = []
mac = []
outro = []
cont = 0

x = int(input("Urnas em operação: "))

for i in range(0, x):
    print(f"Urna {i+1}")
    while True:
        num = int(input("1- Windows Server\n"
                        "2- Unix\n"
                        "3- Linux\n"
                        "4- Netware\n"
                        "5- Mac OS\n"
                        "6- Outro\n"
                        "0- Sair\n"
                        "Digite um número: "))

        if num == 1:
            windowsServer.append(num)
            cont += 1
        elif num == 2:
            unix.append(num)
            cont += 1
        elif num == 3:
            linux.append(num)
            cont += 1
        elif num == 4:
            netware.append(num)
            cont += 1
        elif num == 5:
            mac.append(num)
            cont += 1
        elif num == 6:
            outro.append(num)
            cont += 1
        elif num == 0:
            break
        else:
            print("Número invalido!")
            continue



print(f"Sistema Operacional     Votos   %\n"
        f"-------------------     -----   ---\n"
        f"Windows Server            {len(windowsServer)}    {len(windowsServer) + len(windowsServer) * cont / cont}%\n"
        f"Unix                      {len(unix)}     {len(unix) + len(unix) * cont / cont}%\n"
        f"Linux                     {len(linux)}        {len(linux) + len(linux) * cont / cont}%\n"
        f"Netware                   {len(netware)}      {len(netware) + len(netware) * cont / cont}%\n"
        f"Mac OS                    {len(mac)}      {len(mac) + len(mac) * cont / cont}%\n"
        f"Outro                     {len(outro)}        {len(outro) + len(outro) * cont / cont}%\n")