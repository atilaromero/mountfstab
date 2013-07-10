This tiny application mounts dd images.

It also install Upstart services to mount and umount these images.

INSTALL
=======

Ubuntu
-------------
- Create a .deb:

    dpkg -b deb/ mountfstab.deb

- Install mountfstab.dev:

    sudo dpkg -i mountfstab.deb

- Link the Makefile to your images directory:

    ln -s /etc/mountfstab/Makefile ~/mydir/

Usage
=====
Suppose your directory has these files:
(Makefile is a link to /etc/mountfstab/Makefile)

    image.dd
    Makefile

Run mkfstab.py:

    mkfstab.py image.dd > 01.fstab

It will create a file named 01.fstab using the usual fstab format.

Edit it if you wish. This step is actually optional, you can just
create your fstabs by hand.

Run make:

    make

All files ending in .fstab in that directory will be readed, in alphabetical order, mounting the partitions described in them.

Umount
======

Run:

    make umount

