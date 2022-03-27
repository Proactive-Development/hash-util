all: build
build:
	zip -r app_build.zip *
	echo '#!/usr/bin/env python3' | cat - app_build.zip > hash-util
	chmod +x hash-util
install:
	sudo install ./hash-util /usr/bin/
uninstall:
	sudo rm /usr/bin/hash-util
clean:
	rm app_build.zip
	rm hash-util