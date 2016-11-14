# My SMT Projects using Z3

# A Simple CTF challenge
Solving a challenge which i encountered in a CTF, i don't remembers exactly which.

The function which determined whether the input was valid or not.<br>

'''c
int check_val(char *input)
{
	int len = strlen(input);
	int i,ans;
	ans = 0xdeadbeef;
	for(i=0;i<len;i++)
	{
		ans = (int)input[i] + ans*0x8;
	}
	if(ans == 0xcafebabe)
	{
		return 1;
	}
	return 0; 
}
'''
<br>
<br>

Output:<br>
<pre>
Len:  9 GVF@bBQH>
Len: 10 T[y/9[@!@~
Len: 11 R_Dg}H`RR@>
Len: 12 BICbxz$@T@H~
Len: 13 BBSXBA,TBBR9v
Len: 14 BBBSQyH9(\rN`>
Len: 15 BPBBRY~"*'*BPS&
Len: 16 BBBBBJ]WR_xd4D2.
Len: 17 BBDBBBPS*B'@"H!@~
Len: 18 BDBHBBBQGByg|>cJ@>
Len: 19 BBBBBBBDSXC6H2RD@S&
</pre>
