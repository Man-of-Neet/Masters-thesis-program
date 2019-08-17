import conection
import rooting
import itertools
import netlink
import random
if __name__ == '__main__':
    Core = [0,1,2,3]
    for i in itertools.product(Core, repeat=10):
        Core_Combination = i
        #print(i)
        for j in range(len(Core_Combination)):
            #print(Core_Combination[j])
            pass
    print("finish")
    #Link = netlink.link_init()
    #netlink.print_link(Link)
