# README #

### Papertrail-ai? ###

An API wrapper specifically for financial systems (invoicing, accounting, payroll, and ERP systems). Connect data between organizations, processes and automate functions across financial systems. Current integrations include Xero, Sage, Zoho, FreshBooks, FreeAgent, QuickBooks. The wrapper also allows for implementation of robotic process automation and machine learning applications and algorithms into these financial applications.

### About papertrail-ai? ###

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

The API is based on the Oauth2 protocal.    
Drop me a mail with your redirect URI and client id and I will send you a API test key.  
    
Making requests:

1) Grant authorization

    Make a post request to the following page to grant authoization.
    https://www.papertrail-ai.com/api/authorize.php

    Parameters:  
	redirect uri  
    response_type = code  
    state 

2) Get code

	Once authorization is granted. A code is submitted back to your redirect uri.

3) Get access token 

	To obtain a token make a post request to the following page:  
	https://www.papertrail-ai.com/api/token.php

	The following parameters are required:
	```  
	grant_type: authorization_code  
    client_secret:  
    code:  
    client_id:  
    redirect_uri:  
    ```  

4) Make Api request

	Current API requests can be made to the following URI's. Query must be made with system and query name parameter. 

	Parameters:
	System and query parameters:
	
	system
    ```
    freeagent  
    freshbooks  
    quickbooks  
    sage_sa  
    sage_uk  
    xero  
	zoho
	```

	- `bank : api_bank.php`  
		`bank_list`				(Provides a list of bank transactions)  
	    `bank_accounts_list`	(Provides a list of bank accounts)  

	- `customers : api_customers.php`  
		`list_customers`		(Provides a list of customers)  
		`list_invoices`			(Provides a list of invoices)  
		`invoice_detail`		(Provides detailed single invoice)  
		`create_customer`		(Creates a new customer account)  
		`create_invoice`		(Creates a sales invoice)  
		`create_credit_note`	(Creates a sales credit note)  

	- `vendors : api_vendors.php`   
		`list_vendors`			(Provides a list of vendors)  
		`list_invoices`			(Provides a list of invoices)  
		`create_vendor`			(Creates a new vendor account)  
		`create_invoice`		(Creates a purchase invoice)  	

	- `gl : api_gl.php`  
		`list_gl_transaction`	(Provides a list of general ledger transactions)  
		`list_gl_accounts`		(Provides a list of general ledger accounts)  

### Contribution guidelines ###

Contributors Wanted: Inquire Within. Licence fees from Marketplace will be shared with contributors.

### Who do I talk to? ###

Contact me on patrykg@papertrail-ai.com