/********************************************************************************/
/*
* Team Id: 2457
* Author List: Rudra Narayan Pandey 
* Filename: pidmotion.h
* Theme: Harvester Bot
* Functions:pidmotion(float)
* Global Variables:setpoint,kp,kd,ki,integral,basespeed,maxspeed,lasterror,motorspeed
*/
/*
*Function Name:		pidmotion
*Input:				check_line->float value which gives the idea about where is the bot on the line,
*					this value is calculated by using the values obtained by all the three whiteline sensor 
*Output:			according to the value of check_line it set the velocity of the bot and make the bot follow the line
*Logic:				according to the value of check_line, error(difference between check_line and setpoint) is being calculated
*					and depending upon the error the speeds of the wheel is varied by using pid technique 
*/
int setpoint=100;
unsigned int kp=1.41;
unsigned int kd=1.45;
unsigned int ki=0;
int integral=0;
unsigned int basespeed=190;    //210
unsigned int maxspeed=255;
float lasterror=0;
int motorspeed;
void pidmotion(float check_line)
{
	int error=check_line-setpoint;
	integral=integral+error;
	motorspeed=kp*error+kd*(error-lasterror)+ki*integral;
	lasterror=error;
	int rightmotorspeed=basespeed+motorspeed;
	int leftmotorspeed=basespeed-motorspeed;
	if(rightmotorspeed>maxspeed)
	{
		rightmotorspeed=maxspeed;
	}
	if(leftmotorspeed>maxspeed)
	{
		leftmotorspeed=maxspeed;
	}
	if(rightmotorspeed<0)
	{
		rightmotorspeed=0;
	}
	if(leftmotorspeed<0)
	{
		leftmotorspeed=0;
	}

	forward();
	velocity(leftmotorspeed,rightmotorspeed);
}

/********************************************************************************/