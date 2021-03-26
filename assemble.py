import glob


def get_blacklist():
    blacklist = {}
    for fname in glob.glob('*.txt'):
        allipdata = open(fname).readlines()
        for ipdata in allipdata:
            num, ip = ipdata.strip().split()
            num = int(num)
            if not ip in blacklist:
                blacklist[ip] = 0
            blacklist[ip] += num
    return blacklist


def assemble_blacklist():
    blacklist = get_blacklist()
    blackf = open('blacklist', 'w')
    hostsdenyf = open('hosts.deny', 'w')
    hostsdenyf.write(open('hosts.deny.template').read())
    for ip, num in blacklist.items():
        if num > 10:
            blackf.write(ip+'\n')
            hostsdenyf.write('sshd:' + ip + '  #' + str(num) + '\n')
    print('completed!')


if __name__ == "__main__":
    assemble_blacklist()
