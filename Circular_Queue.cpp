#include<iostream>
using namespace std;
class Queue
{
	public:
	int bno[5];
	char bname[5][50];
	int front,rear;
	Queue()
	{
		front=rear=-1;
	}
	void insert();
	void delete_();
	void display();
};
void Queue::insert()
{
	if((front==0 && rear==4) || (front==rear+1))
	{
		cout<<"Queue full\n";
		return;
	}
	if(front==-1)
		front=rear=0;
	else if(rear==4)
		rear=0;
	else
		++rear;
	cout<<"enter new book number";
	cin>>bno[rear];
	cout<<"enter new book name";
	cin>>bname[rear];
	cout<<"Element added\n";
}
void Queue::delete_()
{
	if(front==-1)
	{
		cout<<"No element to delete\n";
		return;
	}
	cout<<"Element to delete:"<<bno[front]<<"\t"<<bname[front]<<endl;
	if(front==rear)
		front=rear=-1;
	else if(front==4)
		front=0;
	else
		++front;
	cout<<"Element deleted\n";
}
void Queue::display()
{
	if(front==-1)
	{
		cout<<"No element to display\n";
		return;
	}
	for(int i=front; i!=rear; ++i)
	{
		cout<<"Book number:"<<bno[i]<<endl;
		cout<<"Book name:"<<bname[i]<<endl;
		if(i==4)
			i=-1;
	}
	cout<<"Book number:"<<bno[rear]<<endl;
	cout<<"Book name:"<<bname[rear]<<endl;
}
int main()
{
	Queue Q;
	int ch=0;
	while(ch>=0)
	{
		cout<<"1. Insert"<<endl;
		cout<<"2. Delete"<<endl;
		cout<<"3. Display"<<endl;
		cout<<"Enter choice";
		cin>>ch;
		switch(ch)
		{
			case 1: Q.insert();
			    break;
			case 2: Q.delete_();
				break;
			case 3: Q.display();
				break;
			default: cout<<"Wrong choice.\n";	
		}
	}
	return 0;
}
