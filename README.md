technology used for this app:
Streamlit
MySQL

To execute this app follow these steps:
1. create a database in your local system called 'nunam'
2. run 'Database_Creation.py' to create the table '_cell_monitor_' which contains the last there sheets combined for both CELL IDs
3. Install the API:
	a. Execute 'pip install -e .' on your command line interface.
4. Execute 'python -m api.api' to run API service.
5. Execute 'streamlit run Dashboard.py --server.port 8080' to start the app.
