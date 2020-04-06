# !/usr/bin/env python3
# Copyright cfergojr 2020 CJF https://www.chrisfergojr.com


def main():
    infile = open('img.jpg', 'rb')
    outfile = open('img-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
