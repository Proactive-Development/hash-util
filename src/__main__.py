import hashlib
import sys
import os
import hashlib
helpmsg ="""
-ls               List the directory and show the hashes of each file
-f  <Hash>        Find a file with a given hash
-v  <File> <Hash> Verify a file with a hash
-t                Same as -ls but with files in subdirectory's

--help            Displays a help message
--version         Displays the version
--verbose         Activates verbose mode
--quiet           Activates quiet mode
"""
if __name__ == "__main__":
    verbose = False
    quiet = False
    version = "0.0.1"
    for arg in sys.argv:
        if arg == "--help":
            print(helpmsg)
            exit()
        if arg == "--version":
            print("hash-util version: " + version)
            exit()
        if arg == "--verbose":
            verbose = True
            continue
        if arg == "--quiet":
            quiet = True
            continue
    for arg in sys.argv:
        if arg == "-ls":
            for file in os.listdir():
                if os.path.isfile(file):
                    print("File: "+file)
                    print("MD5:    "+hashlib.md5(open(file, 'rb').read()).hexdigest())
                    print("SHA224: "+hashlib.sha224(open(file, 'rb').read()).hexdigest())
                    print("SHA256: "+hashlib.sha256(open(file, 'rb').read()).hexdigest())
                    print("SHA384: "+hashlib.sha384(open(file, 'rb').read()).hexdigest())
                    print("\n")   
            exit()
        if arg == "-t":
            for root, dirs, files in os.walk(os.getcwd()):
                for file in files:
                    print("File: "+root+"/"+file)
                    print("MD5:    "+hashlib.md5(open(root+"/"+file, 'rb').read()).hexdigest())
                    print("SHA224: "+hashlib.sha224(open(root+"/"+file, 'rb').read()).hexdigest())
                    print("SHA256: "+hashlib.sha256(open(root+"/"+file, 'rb').read()).hexdigest())
                    print("SHA384: "+hashlib.sha384(open(root+"/"+file, 'rb').read()).hexdigest())
                    print("\n")   
            exit()
        if arg == "-f":
            method = "MD5"
            for arg in sys.argv:
                if "--hash=" in arg:
                    if arg.replace("--hash=","").upper() == "MD5":
                        method = "MD5"
                    if arg.replace("--hash=","").upper() == "SHA224":
                        method = "SHA224"
                    if arg.replace("--hash=","").upper() == "SHA256":
                        method = "SHA256"
                    if arg.replace("--hash=","").upper() == "SHA384":
                        method = "SHA384"
                    if arg.replace("--hash=","").upper() == "SHA512":
                        method = "SHA384"
            hash = sys.argv[len(sys.argv) - 1]
            foundfiles = []
            for root, dirs, files in os.walk(os.getcwd()):
                for file in files:
                    if method == "MD5":
                        if hash == str(hashlib.md5(open(root+"/"+file, 'rb').read()).hexdigest()):
                            foundfiles.append(root+"/"+file)
                    if method == "SHA224":
                        if hash == str(hashlib.sha224(open(root+"/"+file, 'rb').read()).hexdigest()):
                            foundfiles.append(root+"/"+file)
                    if method == "SHA256":
                        if hash == str(hashlib.sha256(open(root+"/"+file, 'rb').read()).hexdigest()):
                            foundfiles.append(root+"/"+file)
                    if method == "SHA384":
                        if hash == str(hashlib.sha384(open(root+"/"+file, 'rb').read()).hexdigest()):
                            foundfiles.append(root+"/"+file)
            print(foundfiles)
            exit()

        if arg == "-v":
            method = "MD5"
            for arg in sys.argv:
                if "--hash=" in arg:
                    if arg.replace("--hash=","").upper() == "MD5":
                        method = "MD5"
                    if arg.replace("--hash=","").upper() == "SHA224":
                        method = "SHA224"
                    if arg.replace("--hash=","").upper() == "SHA256":
                        method = "SHA256"
                    if arg.replace("--hash=","").upper() == "SHA384":
                        method = "SHA384"
                    if arg.replace("--hash=","").upper() == "SHA512":
                        method = "SHA384"

            hash = sys.argv[len(sys.argv) - 1]
            file = sys.argv[len(sys.argv) - 2]
            
            if method == "MD5":
                file_hash = str(hashlib.md5(open(file, 'rb').read()).hexdigest())
                if file_hash == hash:
                    print("[PASS] File has the same hash as the given hash:"+hash)
                else:
                    print("[FAIL] File has a different hash than the given hash:"+hash)
            if method == "SHA224":
                file_hash = str(hashlib.sha224(open(file, 'rb').read()).hexdigest())
                if file_hash == hash:
                    print("[PASS] File has the same hash as the given hash:"+hash)
                else:
                    print("[FAIL] File has a different hash than the given hash:"+hash)
            if method == "SHA256":
                file_hash = str(hashlib.sha256(open(file, 'rb').read()).hexdigest())
                if file_hash == hash:
                    print("[PASS] File has the same hash as the given hash:"+hash)
                else:
                    print("[FAIL] File has a different hash than the given hash:"+hash)
            if method == "SHA384":
                file_hash = str(hashlib.sha384(open(file, 'rb').read()).hexdigest())
                if file_hash == hash:
                    print("[PASS] File has the same hash as the given hash:"+hash)
                else:
                    print("[FAIL] File has a different hash than the given hash:"+hash)
            exit()
    print("Usage: hash-util -ls -f <hash> -v <file> <hash> --help --verbose --quiet")