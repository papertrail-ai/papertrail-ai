# README #

### papertrail-ai? ###

An API wrapper specifically for financial systems (invoicing, accounting, payroll, and ERP systems). Connect data between organizations, processes and automate functions across financial systems. Current integrations include Xero, Sage, Zoho, FreshBooks, FreeAgent, QuickBooks. The wrapper also allows for implementation of robotic process automation and machine learning applications and algorithms into these financial applications.

### about papertrail-ai? ###

Project modules: 

- Annual Financial Statements
- Bank
- Consolidations
- Credit Providers
- Credit Profile
- Customers
- Vendors 
- General Ledger
- Tax
- Excel
- Robotic Process Automation
- Machine Learning

The API 

- The API is based on the Oauth2 protocal.
- Drop me a mail with your redirect URI and I will send you a API test key.
- Making requests:

1) Grant authorization

	You will be redirected where you will be required to login and grant authorization. 

	https://www.papertrail-ai.com/api/authorize.php

	Parameters:
	system - system parameters currently accepted
		freeagent
		freshbooks
		quickbooks
		sage_sa
		sage_uk
		xero
		zoho  
	redirect uri 

2) Get code

	Once authorization is granted. A code is submitted back to your redirect uri

3) Get access token 

	https://www.papertrail-ai.com/api/token.php

4) Make Api request

	Current API requests can be made to the following URI's. Query must be made with module and query name parameter. 

	Parameters:
	Module and query parameters currently accepted:
	- bank
		=>bank_list (Provides a list of bank transactions)

	- customers
		=>list_customers
		=>list_invoices	

	- vendors
		=>list_vendors
		=>list_invoices	

	- gl
		=>list_gl_transaction

### contribution guidelines ###

Contributors Wanted: Inquire Within. Licence fees from Marketpplace will be shared with contributors.

### who do I talk to? ###

Contact me on patrykg@papertrail-ai.com