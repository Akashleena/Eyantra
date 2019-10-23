/********************************************************************************/
/*
* Team Id: 2457
* Author List: Rudra Narayan Pandey
* Filename: treeloop.h 
* Theme: Harvester Bot
* Functions:loop(),looptree()
* Global Variables:nom
*/
#include<stdio.h>

int nom=13;
int loop(int lo[],int flag,int num)
{
int i=1,l;
while(i<=num)
{
if(i%3==2)
{
    if(flag==0)
    lo[i]=2;
    else
        lo[i]=1;
}
else
{
    if(i==1)
    {
        lo[i]=0;
    }
else{
        if(flag==0)
            lo[i]=1;
else
    lo[i]=2;
}
}

i++;
}


return i;
}

int looptree(int a[],int j,int lo[])
{ int num_node;
  if(a[j-1]>a[j-2])
{
    if((a[j-1]-a[j-2])==row)
    {
    num_node=loop(lo,0,nom-2);
    lo[11]=1;

    }
    else
    num_node=loop(lo,0,nom);
}
else{
    if((a[j-1]-a[j-2])==-row)
    {num_node=loop(lo,0,nom-2);
    lo[11]=2;
    }
    else
        num_node=loop(lo,1,nom);

}
return num_node;
}
