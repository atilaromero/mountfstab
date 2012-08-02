MKFSTAB=/usr/bin/mkfstab.py
MOUNTFSTAB=/usr/bin/mountfstab.py
DEFAULTDDOPTIONS=ro,iocharset=utf8,umask=0227
DEFAULTSQUASHOPTIONS=ro,umask=227,_netdev,noexec,uid=root,gid=root,loop
DDEXTREGEXPR='\.dd$$\|\.img$$\|\.001$$\|\.iso$$\|\.tao$$'
#DEFAULTMNT='eqXX/itemXX-type(HD,pendrive)-NumMat/'
DEFAULTMNT='XXX/itemXX-XX-MXXXX/'

PHONY := _all
_all: mountfstab.config checkop all

PHONY += importconfig
importconfig:
include mountfstab.config

mountfstab.config:
	echo 'SUBDIRS=' >> mountfstab.config ;\
        echo 'GROUP=' >> mountfstab.config ;\
	echo 'all: subdirs squash dd' >> mountfstab.config
	chmod o-r mountfstab.config

PHONY += checkop
checkop:
ifeq ($(strip $(GROUP)), )
	@echo Please, fill GROUP in the mountfstab.config file.
	exit 1
endif

PHONY += subdirs $(SUBDIRS)
subdirs: $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -f $@/Makefile

PHONY += dd
dd: squash dd.fstab
	$(MOUNTFSTAB) --mkdir -v dd.fstab

dd.fstab: dd.list
	sed -e '/^ *$$/d' dd.list | while read ddfile ddmnt ;\
	do mkdir -p $$ddmnt ;\
	$(MKFSTAB) $$ddfile --basemountdir=$$ddmnt \
	  --appendoptions=$(DEFAULTDDOPTIONS),gid=$(GROUP) ;\
	done > dd.fstab
	chmod 600 dd.fstab

dd.list:
	$(MAKE) dd.list.example
	@echo Missing file: dd.list
	exit 1

dd.list.example:
	sed -e '/^ *$$/d' squash.list | while read squashfile squashmnt ;\
	do find $$squashmnt -type f | grep $(DDEXTREGEXPR) | \
	  awk '{print $$1" $(DEFAULTMNT)" }' ; \
	done > dd.list.example
	chmod 600 dd.list.example

PHONY += squash
squash: squash.fstab
	$(MOUNTFSTAB) --mkdir -v squash.fstab

squash.fstab: squash.list
	sed -e '/^ *$$/d' squash.list | while read squashfile squashmnt ;\
	do mkdir -p -m 500 $$squashmnt ;\
	echo $$squashfile $$squashmnt auto $(DEFAULTSQUASHOPTIONS) ;\
	done > squash.fstab
	chmod 600 squash.fstab

squash.list:
	ls *.squash | while read i;\
	do echo $$i $$i.dir ;\
	done > squash.list
	chmod 600 squash.list

umount: umountsubdirs umountsquash

PHONY += umountsubdirs
umountsubdirs: 
	for i in $(SUBDIRS); do \
		$(MAKE) -f "$$i"/Makefile umount; \
	done

PHONY += umountsquash
umountsquash: umountdd
	$(MOUNTFSTAB) --umount -v squash.fstab

PHONY += umountdd
umountdd:
	$(MOUNTFSTAB) --umount -v dd.fstab

.PHONY: $(PHONY)
