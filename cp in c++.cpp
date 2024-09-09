/* A few of my C++ codes from competitive programming problems.

#include<bits/stdc++.h>
using namespace std;
main()
{
	int t,i,a,b,n;
	cin>>t;
	for(i=1; i<=t; i++)
	{
		cin>>n>>a>>b;
		for(int j=0; j<n; j++)
		{
			cout<<char('a'+ j%b);
		}
		cout<<endl;
	}
}

#include<bits/stdc++.h>
using namespace std;
main()
{
	int t,i,n;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		if(n%4!=0)
		{
			cout<<"NO"<<endl;
		}
		else
		{
			cout<<"YES"<<endl;
			for(int j=1; j<=n; j++)
			{
				if(j%2==0) cout<<j<<" ";
			}
			for(int j=1; j<=n-2; j++)
			{
				if(j%2!=0) cout<<j<<" ";
			}
			cout<<6*(n/4)-1<<endl;
		}
	}
}

#include<bits/stdc++.h>
using namespace std;
main()
{
	int r,c,n,s,q,a,b;
	for(r=1; r<=5; r++)
	{
		for(c=1; c<=5; c++)
		{
			cin>>n;
			if(n==1)
			{
				a=abs(3-r)+abs(3-c);
			}
		}
	}
	cout<<a<<endl;
}

#include<bits/stdc++.h>
using namespace std;
main()
{
	int n,k,a[60],l=0;
	cin>>n>>k;
	for(int i=0; i<n; i++)
	{
		cin>>a[i];
	}
	for(int i=0; i<n; i++)
	{
		if(a[i]>=a[k-1] && a[i]>>0)
		{
			l++;
		}
	}
	cout<<l<<endl;
}

#include<bits/stdc++.h>
using namespace std;
main()
{
	int t,l;
	cin>>t;
	while(t--)
	{
	    char s[150];
		cin>>s;
		l=strlen(s);
		if(l<=10)
		{
			cout<<s<<endl;
		}
		else
		{
			cout<<s[0]<<l-2<<s[l-1]<<endl;
		}
	}
}

#include<bits/stdc++.h>
using namespace std;
main()
{
	int t,a,b,k;
	cin>>t;
	while(t--)
	{
		cin>>a>>b;
		if(a==0 && b==0)
		{
			cout<<"0"<<endl;
		}
		else
		{
		k=(a*a + b*b);
		float j=sqrt(k);
		int l=j/1;
		if(l==j)
		{
			cout<<"1"<<endl;
		}
		else
		{
			cout<<"2"<<endl;
		}
	}
	}
}

#include<bits/stdc++.h>
using namespace std;
main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int l1, l2, l3;
		cin>>l1>>l2>>l3;
		int s=l1+l2+l3;
		int a=abs(l3-l1);
		int b=abs(l2-l1);
		int c=abs(l2-l3);
		if(s%2!=0)
		{
			cout<<"NO"<<endl;
		}
		else
		{
			if(l1==l2 || l2==l3 || l1==l3)
			{
				cout<<"YES"<<endl;
			}
			else if(l2==a || l3==b || l1==c)
			{
				cout<<"YES"<<endl;
			}
			else
			{
				cout<<"NO"<<endl;
			}
		}
	}
}

#include<bits/stdc++.h>
using namespace std;
main()
{
	int t,i,p=0,a[100];
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		for(i=1; i<=n; i++)
		{
			cin>>a[i];
	 }
	 int l=1, r=n;
	 while(a[l+1]==1) l++;
	 while(a[r-1]==1) r--;
	 if(l>r)
	 {
	 	cout<<0<<endl;
	 }
	 else
	 {
	 	cout<<r-l<<endl;
	 }
	}
}

#include<bits/stdc++.h>
using namespace std;
main()
{
	int t,x,sum=0;
	cin>>t;
	while(t--)
	{
		sum=0;
		int n;
		cin>>n;
		for(int i=1; i<=n; i++)
	{   cin>>x;
		sum=sum+x;
	}
			if(sum%n==0)
			{
				cout<<"0"<<endl;
			}
			else
			{
				cout<<"1"<<endl;
			}
	}
}

#include<bits/stdc++.h>
using namespace std;
main()
{
	int t,n,k;
	cin>>t;
	while(t--)
	{
		cin>>n>>k;
		string s(n,'a');
		int p=2;
		while(k>p-1)
		{
			k=k-(p-1);
			p++;
		}
		s[n-p]='b';
		s[n-k]='b';
		cout<<s<<endl;
	}
		
}
*/

