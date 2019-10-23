/********************************************************************************/
/*
* Team Id: 2457
* Author List: Rudra Narayan Pandey
* Filename: shortestpath.h 
* Theme: Harvester Bot
* Functions:pathfinder(),decision()
* Global Variables:row
*/
#include<stdio.h>
/*
*Function Name:		pathfinder
*Input:				start->start node value,
*					end->the node where the bot has to reach,
*					path_array->it is an array in which the shortest path between the start node and end node is given stored
*					tree->it is an array which stores the location of all the tree nodes
*Output:			returns the no. of steps it will take to traverse between start node and end node
*Logic:
*/
int row=7;
int pathfinder(int start,int end,int path_array[],int tree[])
{

    int quotient,temp_end,loop_var1,loop_var2=0,step=0,temp_step_var;
    if(end>start)
    {

    quotient=start/row;
    temp_end=abs(end-row*quotient);
    quotient=temp_end/row;
    loop_var1=quotient;
    }
    else{
        quotient=end/row;
temp_end=abs(start-row*quotient);
quotient=temp_end/row;
loop_var1=quotient;
    }

if(end>=start)
{
step=start;
path_array[loop_var2]=step;
loop_var2++;
while(loop_var2<=loop_var1)
{
 if((step==tree[0])||(step==tree[1])||(step==tree[2]))
    {int l=1;
    loop_var2--;
        while(l<=4)
        {

            if(l==1)
            step=path_array[loop_var2-1]-1;
            else if(l==4)
                step=path_array[loop_var2-1]+1;
            else
                step=path_array[loop_var2-1]+7;
            path_array[loop_var2]=step;
            loop_var2++;
            l++;
        }
    }
if(loop_var2<=loop_var1+2)
{
step=step+row;
path_array[loop_var2]=step;
loop_var2++;
}
}
}
else
{
step=start;
path_array[loop_var2]=step;
loop_var2++;
while(loop_var2<=loop_var1)
{
 if((step==tree[0])||(step==tree[1])||(step==tree[2]))
    {int l=1;
    loop_var2--;
        while(l<=4)
        {

            if(l==1)
            step=path_array[loop_var2-1]-1;
            else if(l==4)
                step=path_array[loop_var2-1]+1;
            else
                step=path_array[loop_var2-1]-7;
            path_array[loop_var2]=step;
            loop_var2++;
            l++;
        }
    }
if(loop_var2<=loop_var1+2)
{
step=step-row;
path_array[loop_var2]=step;
loop_var2++;
}
}
}
temp_step_var=step;
if(temp_step_var<=end)
{
while(step<end)
{
 if((step==tree[0])||(step==tree[1])||(step==tree[2]))
    {int l=1;
    loop_var2--;
        while(l<=4)
        {

            if(l==1)
            step=path_array[loop_var2-1]+7;
            else if(l==4)
                step=path_array[loop_var2-1]-7;
            else
                step=path_array[loop_var2-1]+1;
            path_array[loop_var2]=step;
            loop_var2++;
            l++;
        }
    }
if(step<end)
{
step=step+1;
path_array[loop_var2]=step;
loop_var2++;
}
}
}

else
{
while(step>end)
{
 if((step==tree[0])||(step==tree[1])||(step==tree[2]))
    {int l=1;
    loop_var2--;
        while(l<=4)
        {

            if(l==1)
            step=path_array[loop_var2-1]+7;
            else if(l==4)
                step=path_array[loop_var2-1]-7;
            else
                step=path_array[loop_var2-1]-1;
            path_array[loop_var2]=step;
            loop_var2++;
            l++;
        }
    }
if(step>end)
{
step=step-1;
path_array[loop_var2]=step;
loop_var2++;
}
}
}


return loop_var2;

}

/*
*Function Name:		decision
*Input:
*Output:			returns the no. of steps it will take to traverse between start node and end node
*					and returns an array which stores the direction which bot will follow while traversing the path 
*Logic:
*/
int decision(int n,int position,int flag,int sign,int path_array[],int temp_end)
{ int k;
    if(flag%2==0)
    {
        if((path_array[n]-position)*sign*temp_end==row)
            k=0;
        else if((path_array[n]-position)*sign*temp_end<0)
            k=2;
        else if((path_array[n]-position)*sign*temp_end>0&&(path_array[n]-position)*sign*temp_end!=row)
            k=1;
        else
            k=-1;
    }
    else
    {
      if((path_array[n]-position)*sign*temp_end==row)
            k=2;
      else if((path_array[n]-position)*sign*temp_end>0&&(path_array[n]-position)*sign*temp_end!=row)
        k=0;
    else if((path_array[n]-position)*sign*temp_end<0)
        k=1;
    else
        k=-1;


    }
    return k;
    }
	
/********************************************************************************/
