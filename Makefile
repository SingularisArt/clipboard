all:
	sudo ln -sf ${PWD}/list-copied-items.py /usr/bin/list-copied-items
	touch ~/.copied.txt
install:
	sudo ln -sf ${PWD}/list-copied-items.py /usr/bin/list-copied-items
	touch ~/.copied.txt
uninstall:
	sudo rm -rf /usr/bin/list-copied-items
	rm -rf ~/.copied.txt
