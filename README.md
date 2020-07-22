# README #

### Papertrail-ai? ###

Papertrail-ai is an enterprise grade set of tools and marketplace for automating financial processes.

Papertrail-ai includes an API wrapper specifically for financial systems (invoicing, accounting, payroll, and ERP systems). Connect data between organizations, processes and automate functions across financial systems. Current integrations include Xero, Sage, Zoho, FreshBooks, FreeAgent, QuickBooks, Wave and Syspro. 

The Papertrail-ai tools allow for implementation of robotic process automation, machine learning applications and algorithms into these financial applications.

### About papertrail-ai ###

Project modules: 

- Excel / Google Sheets
- Annual Financial Statements
- Bank
- Consolidations
- Credit Providers
- Ratio Analysis
- Customers
- Vendors 
- Inventory
- General Ledger
- Tax
- Fraud
- Leases
- Forecasting
- Valuations
- Data Visualization

### The API ###

The API is based on the Oauth2 protocal.    
Drop me a mail with your redirect URI and client id and I will send you a API test key.  
    
Making requests:

1) Get authorization

    Make a post request to the following page to get authorization.
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
	
	System
    ```
    freeagent  
    freshbooks  
    quickbooks  
    sage_sa  
    sage_uk  
    xero  
	zoho
	```

	Query

	- `bank : api_bank.php`  
		`bank_list`				(List of bank transactions)  
	    `bank_accounts_list`	(List of bank accounts)  

	- `customers : api_customers.php`  
		`list_customers`		(Lists customers)  
		`list_invoices`			(List of customer invoices)  
		`invoice_detail`		(Provides detailed single invoice)  
		`create_customer`		(Creates a new customer account)  
		`create_invoice`		(Creates a sales invoice)  
		`create_credit_note`	(Creates a sales credit note)  

	- `vendors : api_vendors.php`   
		`list_vendors`			(Lists vendors)  
		`list_invoices`			(List of vendor invoices)  
		`create_vendor`			(Creates a new vendor account)  
		`create_invoice`		(Creates a purchase invoice)  	

	- `gl : api_gl.php`   
		`list_gl_transaction`	(Provides a list of general ledger transactions Sales, Expenses, Profit, Assets and Liabilities)  
		`list_gl_accounts`		(Provides a list of general ledger accounts. Sales, Expenses, Profit, Assets and Liabilities)  

	- `accounts : api_accounts.php`   
		`account_create`		(Creates a general ledger account)   
		`account_update`		(Updates a general ledger account)   
		`account_delete`		(Delete a general ledger account)   

	- `reports : api_reports.php`   
		`trial_balance`			(Generates a trial balance)   
		`income_statement`		(Generates a income statement)  
		`balance_sheet`			(Generates a balance sheet)   
		`cash_flow`				(Generates a cash flow)   
 
	- `company : api_company.php`    
		`co_details`			(Provides company name, physical address, phone)  
		`users`					(Provides user details)  

### Contribution guidelines ###

Contributors Wanted: Inquire within. Licence fees from Marketplace will be shared with contributors.

Join our communities on the following channels:    
http://papertrail-ai.slack.com     
https://gitter.im/papertrailai/    

[![Join the chat at https://gitter.im/papertrailai/community](https://badges.gitter.im/papertrailai/community.svg)](https://gitter.im/papertrailai/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

### Who do I talk to? ###

Contact me on patrykg@papertrail-ai.com