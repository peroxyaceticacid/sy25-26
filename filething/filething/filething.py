import glob 

files = glob.glob("server_dump/*.txt")

def scan_files(path):
    with open(path) as f: contents = f.read()

    warn = contents.count("WARN")
    error = contents.count("ERROR")
    ok = contents.count("OK")
    print(f"{path}: WARN={warn}, ERROR={error}, OK={ok}")

for path in files: scan_files(path)