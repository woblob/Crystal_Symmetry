# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("echo",type=int, help="echo the string")
# parser.add_argument("-v","--verbose", help="verbosity",action="store_true")

# args = parser.parse_args()

# if args.verbose:
#   print("lol")
  
def getfile(file_name):
    from crystals import Crystal
    
    """
    open cif file from local repository or download from Crystallography Open Database

    file_name can be either:
        integer: COD number
        string:  CIF file

    examples:
        file_name = 1000041 # NaCl Fm-3m
        file_name = 'path/to/file.cif'
    """
    if isinstance(file_name, int):
        func = Crystal.from_cod
    elif isinstance(file_name, str):
        func = Crystal.from_cif
    else:
        raise argparse.ArgumentTypeError(f"Wrong type of: {file_name=}\n{type(file_name)}")
    return func(file_name)


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=getfile, help="name of CIF file or COD number")
parser.add_argument("-s", "--size", type=int, help="size of supercell in every direction (xyz)")
parser.add_argument("-v", "--number_of_vacancies", metavar="V", type=int, help="amount of vacancies in a Cell")
args = parser.parse_args()

print(args)
print(f"\n{args.size=}\n{args.filename=}\n{args.number_of_vacancies=}\n")

# https://click.palletsprojects.com/en/7.x/



# def perfect_square(string):
#     value = int(string)
#     sqrt = math.sqrt(value)
#     if sqrt != int(sqrt):
#         msg = "%r is not a perfect square" % string
#         raise argparse.ArgumentTypeError(msg)
#     return value

# parser = argparse.ArgumentParser(prog='PROG')
# parser.add_argument('foo', type=perfect_square)
# parser.parse_args(['9'])
# #Namespace(foo=9)
# parser.parse_args(['7'])
# # usage: PROG [-h] foo
# # PROG: error: argument foo: '7' is not a perfect square

