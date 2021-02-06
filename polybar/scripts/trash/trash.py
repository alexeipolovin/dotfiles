import os
PATH = '/home/rob/.local/share/Trash/files'
def main():
    total_size = 0
    for dirpath,dirnames,filenames in os.walk(PATH):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    print("%0.f MB" % (total_size/1000000))

if __name__ == '__main__':
    main()
