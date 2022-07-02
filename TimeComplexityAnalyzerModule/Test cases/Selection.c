\		#include<stdio.h>   //for using functions like printf

		int main()
		{
			int a[20],i,j,min,temp,n;     //declaration of variables
			printf("Enter the size of an array");
			scanf("%d",&n);   //taking the inputs from user of array size
			for(i=0;i<n;i++)        
			{
				printf("Enter the elements one by one");
				scanf("%d",&a[i]);     //accepting the values one by one
			}
			for(i=0;i<n;i++)
			{
				min=i;			//considering the minimum value
				for(j=i+1;j<n;j++)
				{
					if(a[min]>a[j])
					{
						min=j;	//actual minimum value found
					}
				}
				temp=a[i];
				a[i]=a[min];
				a[min]=temp;				//Swapping
			}
			printf("Sorted Array\n");
			for(i=0;i<n;i++)
			{
				printf("%d\n",a[i]);		//finally printing the 										//sorted array
			}
		}

			
				
			
