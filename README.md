# hash-util
<img src="https://raw.githubusercontent.com/Proactive-Development/Logos/main/hash-util/hash-util.png" width=100>
Work with file hashes easier than ever

## Dependencies
- python 3.7+

## Auto Installation (For linux)
``` curl -fsSL https://raw.githubusercontent.com/Proactive-Development/hash-util/main/scripts/install.sh | bash - ```

## Commands
```
-ls               List the directory and show the hashes of each file
-f  <Hash>        Find a file with a given hash
-v  <File> <Hash> Verify a file with a hash
-t                Same as -ls but with files in subdirectory's

--help            Displays a help message
--version         Displays the version
--verbose         Activates verbose mode
--quiet           Activates quiet mode
```

### List Directory -ls
This command lists the directory and show the hashes of each file.

for example:
`hash-util -ls`

will output:
```
File: README.md
MD5:    e2cf67ded752eaeec784e62fbf76d5c6
SHA224: 7782b31e5c33ca07fde01662c63657547806faaecbadf2196035dbf2
SHA256: 7ec39b57403ff41f418b00cbfc117067e5d54c6ba389bb210c993099cc9c958f
SHA384: fe393e9e66e9eb177172170aa957751136e152212a6cee64cb2c5e8c9ec032c8cad575cdb294b39ec55597db2b6e1386
```

### Find -f
This command can be used to find a file with a given hash.
for example if you want to find a file with a hash of `6c4e0639985cc7dcc7c11d385b341e3f` you can use the following command:

`hash-util -f 6c4e0639985cc7dcc7c11d385b341e3f`

hash-util will then search for the file with the hash `6c4e0639985cc7dcc7c11d385b341e3f` and if it finds it it will print the path of the file.

`['/home/pi/coding/proactive/hash-util/README.md']`

You can also use different hash algorithms like sha224, sha256, sha384 using the `--hash=`
flag.

example:
`hash-util -f --hash=sha224 7782b31e5c33ca07fde01662c63657547806faaecbadf2196035dbf2`

`hash-util -f --hash=sha256 7ec39b57403ff41f418b00cbfc117067e5d54c6ba389bb210c993099cc9c958f`

`hash-util -f --hash=sha384 fe393e9e66e9eb177172170aa957751136e152212a6cee64cb2c5e8c9ec032c8cad575cdb294b39ec55597db2b6e1386`

### Verify -v
This command can be used to verify a file with a given hash.
for example if you want to verify a file with a hash of `6c4e0639985cc7dcc7c11d385b341e3f` you can use the following command:
`hash-util -v README.md 6c4e0639985cc7dcc7c11d385b341e3f`

If the file has the same hash as the given hash it will say `[PASS] File has the same hash as the given hash: 6c4e0639985cc7dcc7c11d385b341e3f`

If the file has not got the same hash as the given hash it will say `[FAIL] File has not got the same hash as the given hash: 6c4e0639985cc7dcc7c11d385b341e3f`

### List Subdirectories -t
This command lists the directory and show the hashes of each file.

# Known bugs
- Hash must be last argument to work properly
