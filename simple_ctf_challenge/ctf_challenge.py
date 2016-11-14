
from __future__ import print_function
from z3 import *

# Encountered this challenge in a ctf, i dont remembers which exactly
#
#int check_val(char *input)
#{
#	int len = strlen(input);
#	int i,ans;
#	ans = 0xdeadbeef;
#	for(i=0;i<len;i++)
#	{
#		ans = (int)input[i] + ans*0x8;
#	}
#	if(ans == 0xcafebabe)
#	{
#		return 1;
#	}
#	return 0; 
#}
#


def solve(len):
    s = Solver()
    input_str = BitVecs(['input_str_{0}'.format(i) for i in range(len)],32)

    # Only printable characters
    for v in input_str:
        s.add(v>32)
        s.add(v<127)

    ans = 0xdeadbeef
    for v in input_str:
        ans = ans * 0x8 + v

    s.add(ans == 0xcafebabe)
    if s.check() ==sat:
        m = s.model()
        print("Len: {0:2}".format(len), end=' ')

        for v in input_str:
            print(chr(m[v].as_long()), end='')
        
        print()

for i in range(1,20):
    solve(i)