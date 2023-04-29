### Running Virtual Environment
    virtualenv venv
    source venv/bin/activate


### Installation of Libraries
    pip install -r requirements.txt

### Run Fast-API
    uvicorn main:app --reload --port=[port]

### Fast-API Documentation
    http://localhost:8000/docs


----
## Connecting Ethereum and FastAPI

1. Run FastAPI app

2. Run Ethereum Test Net
	- open it in a separate terminal without closing the entire testing using the same set of wallet addresses

	        ganache-cli

3. Connect Remix Ethreum and connect to ***Custom - External Http Provider***
	- use the ganahce-cli address runing in wsl
	
	    default : http://127.0.0.1:8545


4. In Fast-Api code
	- copy the ABI one line code from remix

        https://w3percentagecalculator.com/json-to-one-line-converter/

	- copy the test ethereum addess and private key from instruction 2
	- copy the contract address from remix

5. Run the FastAPI app