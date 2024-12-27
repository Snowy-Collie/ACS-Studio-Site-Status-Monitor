# ACS Studio Site Status Monitor

This project provides a site status monitoring tool that checks the availability of multiple websites every hour. It is built using Python for backend processing and HTML, CSS, and JavaScript for the frontend display. The status of each monitored website is stored in JSON files and can be displayed in a user-friendly format.

## Features
- Monitor the status of multiple websites.
- Automatically updates the status every hour.
- Displays the current status of each site in real-time using HTML and JavaScript.
- Configurable to add or remove websites for monitoring.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Snowy-Collie/ACS-Studio-Site-Status-Monitor.git
   cd ACS-Studio-Site-Status-Monitor
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the websites you want to monitor by editing the `getstatus.py` file:
   - Change the `file_path` to specify the path for the JSON status file.
   - Update the `link` with the URL of the website you want to monitor.
   - For example:
     ```python
     file_path = "./status_data_site.json"
     link = "https://acsstudio.site"
     update_status_file(file_path, link)
     ```

4. Run the Python script to update the status:
   ```bash
   python getstatus.py
   ```

## Frontend Configuration

After running the Python script, update the `index.html` file to display the status of the websites:

1. Modify the `site-container` module in the `index.html` file to reflect the corresponding website status.

2. Update the JavaScript section at the bottom of the `index.html` to point to the correct JSON files:
   ```javascript
   fetchStatusData('./status_data_site.json', 'current-status-site', 'status-container-site');
   fetchStatusData('./status_data_status.json', 'current-status-status', 'status-container-status');
   fetchStatusData('./status_data_survey.json', 'current-status-survey', 'status-container-survey');
   ```

## Example Configuration

In `getstatus.py`, you can add multiple sites by changing the file paths and links:

```python
file_path = "./status_data_site.json"
link = "https://acsstudio.site"
update_status_file(file_path, link)

file_path = "./status_data_status.json"
link = "https://status.acsstudio.site"
update_status_file(file_path, link)

file_path = "./status_data_survey.json"
link = "https://survey.acsstudio.site"
update_status_file(file_path, link)
```

In `index.html`, the status data is fetched from the corresponding JSON files:

```javascript
fetchStatusData('./status_data_site.json', 'current-status-site', 'status-container-site');
fetchStatusData('./status_data_status.json', 'current-status-status', 'status-container-status');
fetchStatusData('./status_data_survey.json', 'current-status-survey', 'status-container-survey');
```

## License

This project is open-source and licensed under the MIT License.

## Acknowledgements

- [ACS Studio](https://acsstudio.site) for providing the platform.
- [Python](https://www.python.org/) for the backend.
- [HTML/CSS/JavaScript](https://www.w3.org/) for the frontend.
