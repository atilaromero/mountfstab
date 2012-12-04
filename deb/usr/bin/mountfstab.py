#!/usr/bin/python
import os
import sys
import optparse
import pyparsing as pp
import subprocess

def main():
    p=optparse.OptionParser(usage="usage: %prog [options] <fstabfile>")
    p.add_option('--mkdir', action='store_true',default=False)
    p.add_option('--checkfirst', '-c',action='store_true',default=True)
    p.add_option('--umount', '-u',action='store_true',default=False)
    p.add_option('--listmnt', action='store_true',default=False)
    p.add_option('--norun', '-n',action='store_true',default=False)
    p.add_option('--verbose', '-v',action='store_true',default=False,
                 help="print commands to stderr")
    options, arguments = p.parse_args()
    if len(arguments)<1:
        p.error('fstab filepath is not optional')
    ret=0
    for path in arguments:
        ret+=mount(path,
                   verbose=options.verbose,
                   norun=options.norun,
                   umount=options.umount,
                   mkdir=options.mkdir,
                   checkfirst=options.checkfirst,
                   listmnt=options.listmnt)
    return ret

def mountpointmounted(mountpoint):
    realpath=os.path.realpath
    with open('/proc/mounts','r') as f:
        for line in f:
            a=line.strip().split(" ")
            if a and len(a)>2:
                if realpath(a[1])==realpath(mountpoint):
                    return True
    return False

def mount(fstabpath,verbose=False,norun=False,umount=False,mkdir=False,checkfirst=True,listmnt=False):
    content=pp.OneOrMore(pp.QuotedString('"',escChar='\\') | 
                         pp.QuotedString("'",escChar='\\') | 
                         pp.Word(pp.printables.replace('#','')))
    ret=1
    with open(fstabpath) as f:
        indent=0
        ret=0
        for line in f:
            if (len(line.strip())>0) and not line.strip().startswith('#'):
                lineindent=len(line)-len(line.lstrip(' \t'))
                tokens=content.parseString(line)
                if len(tokens)>0:
                    if tokens[0].startswith('!include'):
                        ret=mount(tokens[1],verbose,norun)
                    else:
                        src,dst,typ,ops=tokens[:4]
                        if umount:
                            if checkfirst and not mountpointmounted(dst):
                                pass
                            else:
                                ret+=cmd(['umount',dst],verbose,norun)
                        elif listmnt:
                            print os.path.realpath(dst)
                        else:
                            if mkdir:
                                cmd(['mkdir','-p',dst])
                            if checkfirst and mountpointmounted(dst):
                                pass
                            else:
                                ret+=cmd(['mount',src,dst,'-t',typ,'-o',ops],verbose,norun)
    return ret
                            
            
def cmd(args,verbose=False,norun=False):
    if verbose:
        print ' '.join(args)
    if not norun:
        return subprocess.call(args)
    return 0

if __name__=="__main__":
    ret=main()
    sys.exit(ret)

