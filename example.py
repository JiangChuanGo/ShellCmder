cmder = ShellCmder("./bin")

# ./bin/sum is a python script file which calculates the sum of all args.
# get the same result as type these in shell:
# ./bin/sum 1 2 3
ret = cmder.sum('1','2','3')
cmder.show(ret)

# result as
# 6
