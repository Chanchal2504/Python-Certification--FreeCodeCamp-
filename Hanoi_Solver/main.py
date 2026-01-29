def hanoi_solver(disks):
    src=[x for x in range(disks,0,-1)]
    aux=[]
    dest=[]
    out = [f"{src} {aux} {dest}"]
    def tower(disks,fromrod,helperrod,torod):
        if disks==1:
            torod.append(fromrod.pop())
            out.append(f"{src} {aux} {dest}")
            return
        tower(disks-1,fromrod,torod,helperrod)
        torod.append(fromrod.pop())
        out.append(f"{src} {aux} {dest}")
        tower(disks-1,helperrod,fromrod,torod)
    tower(disks,src,aux,dest)
    return '\n'.join(out)
print(hanoi_solver(3))