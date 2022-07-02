# Collecting coding styles metrics using SonarQube API

## Description
This project uses SonarQube API to collect data about coding styles from various open source projects online. It saves the data in the form of a JSON file. Some of the metrics collected are:
 - Bugs
 - New bugs
 - Vulnerabilities
 - Security hotspots
 - Code smells


## Algorithm

- The script [scraper.py](src/sraper.py) collects a set of project keys that can be used later to collect the code styles metrics form SonarQube API.
- The script [filter.py](src/filter.py) handles sample repetitions (duplicates) and saves the clean version of the data to another file.
- The script [collector.py](src/collector.py) sends the requests to the API and saves the results in JSON format.

## Tech
Python Selenium and BeautifulSoup packages were used to scrape the [SonarQube projects explorer](https://sonarcloud.io/explore/projects). Every time the page loads, it shows only 6 projects at a time so the scraper scrolls and clicks the "Show More" button.
But the SonarQube project explorer saves 10,000 projects, so the script can be run periodically with enough time breaks to get more data.

## Usage

You can run the project using the following command:
```sh
sudo ./analyze.sh
```

## License

MIT