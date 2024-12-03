#lib de defs 
strip= input('informe o IP')

def ip2bin(strip):
    octetos  = list(map (int, strip.split(".")))
    if len(octetos) != 4 or not all(0 <= o <= 255 for o in octetos):
        return (strip,octetos)

print (ip2bin)