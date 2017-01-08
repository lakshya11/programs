#include<iostream>
#include<cstdlib>
using namespace std;
struct Node
{
int info;
struct Node *next;

};
typedef Node *node; 

void insert(node &head,int info,int pos)
{
int k;
node nnode,p;
nnode=(struct Node*)malloc(sizeof(struct Node));
nnode->info=info;

	if(head==NULL)
	{
		nnode->next=NULL;
		head=nnode;
		
	}
	else{
		p=head;
		while(k<(pos-1)&&p->next!=NULL)
		{
			p=p->next;
			++k;
		}
		if(p->next==NULL){
		p->next=nnode;
		nnode->next=NULL;}
		else{
		nnode->next=p->next;
		p->next=nnode;}
		
	}
}

void display(node &head)
{
	node p;
	p=head;
	while(p!=NULL)
	{
		cout<<p->info<<" ";
		p=p->next;
	}
}

int main()
{
int pos,i,info;
node head=NULL;
for(i=0;i<5;++i)
{
	cout<<"enter the data and pos\n";
	cin>>info;
	cin>>pos;
	insert(head,info,pos);
	display(head);

}
return 0;
}
