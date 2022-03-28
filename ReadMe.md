# ShellCmder
A shell wrapper for Linux.

You can intereact with executable files under a specified "bin dir" in a Pythonic way.

```python
from ShellCmder import ShellCmder

# specify a bin dir, the executable files home directory.
cmder = ShellCmder("./bin")

# ./bin/sum is a python script file which calculates the sum of all args.
# get the same result as type these in shell:
# ./bin/sum 1 2 3
ret = cmder.sum('1','2','3')
cmder.show(ret)

# result as
# 6
```
