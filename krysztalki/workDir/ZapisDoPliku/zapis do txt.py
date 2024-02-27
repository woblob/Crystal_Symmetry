def zapis_zredukowany():
    with open("output of symmetries 2019_09_28_13_06_50.txt", "r") as f:
        myset = set()
        for line in f:
            chs = line.split("\t")[-1]
            myset.add(chs)
    plik = list(myset)

    with open("plik2.txt", "w") as f:
        # for l in plik:
        for l in sorted(plik, key=lambda x: len(x), reverse=True):
            # print(len(l), l )
            f.write(l)


def back2normal(output, size):
    mylist = []
    for el0, el1 in sorted(output, key=lambda x: len(x[1]), reverse=True):
        # if el1 != []:
        vacs = ((el0 + 1) * (size / 2)).tolist()
        myvar = ""
        for vac in vacs:
            myvar += str(vac) + ";\t"
        mylist.append(myvar + str(el1) + "\n")
    # else:
    #   break
    return mylist


def saveOutput2(OUTPUT, size, filename):
    from datetime import datetime as dt

    # raise "zmienic na datetime.now.strftime as time_format"
    modOUTPUT = back2normal(OUTPUT, size)
    filename = filename + " " + dt.now().strftime("%Y_%m_%d_%H_%M_%S") + ".txt"
    with open(filename, "w") as f:
        for line in modOUTPUT:
            f.write(str(line))
