.PHONY: _all all clean

_all: clean all

all: mountfstab.deb

clean:
	rm *.deb || echo -n

mountfstab.deb:
	dpkg -b deb mountfstab.deb 


