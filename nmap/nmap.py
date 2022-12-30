import os
import nmap

#os.system("pip3 install python-nmap")
os.system("apt-get install figlet")
os.system("clear")

sayac=0

while(1):

    os.system("figlet NMAP")
    print("""
Python ile yazilmis NMAP aracina hos geldiniz!
    """)
    print("""
1) Ping Scan (Host Discovery)
2) Tarama Yapmak (port/versiyon/servis)
3) SYN ACK Scan
4) UDP Scan
5) Birden Cok IP Adresi Taramak
6) Belirli IP Araligini Taramak
7) Isletim Sistemi Taramak
8) Cikis   
    """)

    nmap_tarayici=nmap.PortScanner()

    while(1):

        secim = input("Lutfen bir deger giriniz: ")

        if(secim=="1"):
            sub_addr=input("Lutfen bir subnet giriniz: ")
            sub = nmap_tarayici.scan(hosts=sub_addr, arguments='-n -sP')

            print(sub)
        elif (secim == "2"):
            ip_addr=input("Lutfen bir IP adres giriniz: ")
            scan_range = nmap_tarayici.scan(hosts=ip_addr)

            print(scan_range['scan'])

        elif (secim == "3"):
            ip_addr=input("Lutfen bir IP adres giriniz: ")
            port_range=input("Port araligi giriniz (ornek: 1-65535): ")
            syn_scan=nmap_tarayici.scan(ip_addr,port_range,'-v -sS')

            print(syn_scan)

        elif (secim == "4"):
            ip_addr=input("Lutfen bir IP adres giriniz: ")
            port_range=input("Port araligi giriniz (ornek: 1-65535): ")
            udp_scan=nmap_tarayici.scan(ip_addr,port_range, '-v -sU')

            print(udp_scan)

        elif (secim == "5"):
            sayi=int(input("Girmek istediginiz adres sayisini yaziniz: "))
            x = [i for i in range(sayi)]

            for i in range(sayi):
                x[i] = input("Lutfen bir IP adres giriniz: ")

            for i in range(sayi):
                print()
                scan_ip=nmap_tarayici.scan(hosts=x[i])
                print(scan_ip['scan'])
                print("--------------------------------------------------")

        elif (secim == "6"):
            ip_addr_range=input("Lutfen bir IP araligi giriniz (ornek: 192.168.149.100-150): ")
            scan_range = nmap_tarayici.scan(hosts=ip_addr_range)

            print(scan_range)

        elif (secim == "7"):
            ip_addr=input("Lutfen bir IP adres giriniz: ")
            os_info=nmap_tarayici.scan(ip_addr, arguments="-O")

            print(os_info)

        elif(secim == "8"):
            sayac=1
            break

        else:
            os.system("clear")
            print("LUTFEN GECERLI BIR DEGER GIRINIZ!\n")
            break

        while (1):

            devam_secenek = input("\nDevam etmek ister misiniz?(y/n): ")
            sayac = 0

            if (devam_secenek == "y"):
                os.system("clear")
                os.system("figlet NMAP")
                print("""
1) Ping Scan (Host Discovery)
2) Tarama Yapmak (port/versiyon/servis)
3) SYN ACK Scan
4) UDP Scan
5) Birden Cok IP Adresi Taramak
6) Belirli IP Araligini Taramak
7) Isletim Sistemi Taramak
8) Cikis   
                    """)
                break

            elif (devam_secenek == "n"):
                sayac = 1
                break
            else:
                print("Lutfen gecerli deger giriniz!")

        if (sayac == 1):
            break

    if (sayac == 1):
        break