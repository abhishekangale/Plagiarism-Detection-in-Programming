		#include<stdio.h>			//for using printf function
		#include<string.h>			//for using strlen function

		int max(int a,int b)			//Finding maximum number
		{
			return (a > b)? a : b;		//Comparison	
		}

		int lcs(char *X,char *Y,int m,int n)		//Main LCS Algo
		{
			int L[m+1][n+1];						//declaring array leaving first row and column
			int i,j;
			
			for(i=0;i< =m;i++)						//initialization of outer loop for rows
			{
				for(j=0;j<= n;j++)					//initialization of inner loop for columns
				{
					if(i==0||j==0)
						L[i][j]=0;					//if either row is 0 or column is 0
					else if(X[i-1]==Y[j-1])
						L[i][j]=L[i-1][j-1]+1;		//when match found between two characters and inserting number with 1 increment
					else
						L[i][j]=max(L[i-1][j],L[i][j-1]);		//when match not found finding maximum number between previous row and column
				}
			}
			return L[m][n];							//final matrix
		}



		int main()
		{
			char X[50],Y[50];
			printf("Enter the first string\n");
			scanf("%s",X);							//accepting the first string
			printf("Enter the second string\n");
			scanf("%s",Y);							//accepting the second string
			int m=strlen(X);
			int n=strlen(Y);						//finding the length of first and second string
			printf("Length of lcs is %d\n",lcs(X,Y,m,n));		//printing the final result
			return 0;
		}

