#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
int k,lb,ub,i=0;
char *text=new char[50];
cin.getline(text,50);
cout<<text;
cin>>k>>lb>>ub;
char** word =new char *[k];
while(i<k)
{
word[i]=new char[25];
cin >>word[i];
++i;
}
for(i=0;i<k;++i)
{
	cout<<"\n"<<word[i];
}


return 0;
}
