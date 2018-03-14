def bin2ipv4(binary):
    ipv4 = []
    for i in range(0, 29, 8):
        #print binary[i:i+8]
        ipv4.append(int(binary[i:i+8], 2))
    #print ipv4
    return ".".join(map(str, ipv4))

while True:
    try:
        entry = raw_input().split()
        if len(entry) == 1:
            partial_ip, number_of_ones = entry[0].split("/")
            ones = int(number_of_ones)
            mask = "1"*ones + "0"*(32-ones)
            separated_ip = partial_ip.split(".")
        else:
            separated_mask = entry[1].split(".")
            separated_ip = entry[0].split(".")
            mask = ''
            for part in separated_mask:
                mask += (format(int(part), '08b'))
        ip = ''
        for part in separated_ip:
            ip += (format(int(part), '08b'))
        zeros = mask.count('0')
        machines = (2**zeros)-2
        network_ip_bin = "".join([bin(int(a) & int(b))[-1] for a,b in zip(mask,ip)])
        broadcast_ip_bin = ''
        for ch in network_ip_bin[:-zeros]:
            broadcast_ip_bin += ch
        broadcast_ip_bin += "1"*zeros
        network_ip = bin2ipv4(network_ip_bin)
        broadcast_ip= bin2ipv4(broadcast_ip_bin)
        print 'Endereco de rede: %s' % network_ip
        print 'Endereco de broadcast: %s' % broadcast_ip
        print 'Numero de maquinas: %d\n' % machines
        

    except EOFError:
        break