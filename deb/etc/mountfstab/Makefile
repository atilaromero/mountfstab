MAKESUBDIRS=
FSTABS=
REVFSTABS=$$(for x in ${FSTABS}; do echo $$x;done | tac)
MOUNTFSTAB=/usr/bin/mountfstab.py

PHONY := _all
_all: all

all: mountfstabs postfstabs mountmakesubdirs
umount: preumount umountmakesubdirs umountfstabs

PHONY += postfstabs
postfstabs:

PHONY += preumount
preumount:

PHONY += mountmakesubdirs
mountmakesubdirs:
	for i in $(MAKESUBDIRS); do \
		$(MAKE) -C "$$i" ; \
	done

PHONY += umountmakesubdirs
umountmakesubdirs: 
	for i in $(MAKESUBDIRS); do \
		$(MAKE) -C "$$i" umount; \
	done

PHONY += mountfstabs
mountfstabs:
	for i in $(FSTABS); do \
		$(MOUNTFSTAB) --mkdir -v "$$i"; \
	done

PHONY += umountfstabs
umountfstabs:
	for i in $(FSTABS); do \
		$(MOUNTFSTAB) --umount -v "$$i"; \
	done

PHONY += listmnt
listmnt:
	@for i in $(FSTABS); do \
		$(MOUNTFSTAB) --listmnt "$$i"; \
	done
	@for i in $(MAKESUBDIRS); do \
		$(MAKE) -s -C "$$i" listmnt; \
	done

.PHONY: all umount $(PHONY)
