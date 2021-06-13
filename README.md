# Death Row in the State of Texas

The objective of this project is to understand gain a general understanding of death row in the state of Texas. Fortunately, a ton of rich data on this subject is publicly available here:
https://www.tdcj.texas.gov/index.html 

This repository will contain code for scraping and collecting the relevant data for the analysis, as well as the analysis itself. The repo will also contain all the data collected, and hopefully some visualizations.

-  **`Table of contents`:**
	- [Example Usage of Scraper](#example-usage-of-scraper)
	- [Schedule Daily Data Update](#schedule-daily-data-update)
	  - [Cron Format](#cron-format)	

## Example Usage of Scraper
```bash
$ git clone https://github.com/nissichima/texas_criminal_justice.git
```

```bash
$ cd /path/to/texas_criminal_justice
```

```bash
$ python code/deathrow.py --filepath /path/to/save/data/file_name.csv
```
Done! Your data should be in the specificed location, saved as a comma-separated file.

## Schedule Daily Data Update
Crontab comes in handy when trying to automate tasks and you can do it for this as well!

### Quick start!
List all your cron jobs.
```bash
$ crontab -l
```
Delete the current cron job.
```bash
$ crontab -r
```
For more details on crontab:
```bash
$ man crontab
```
Open editor to add scheduling command:
```bash
$ crontab -e
```
### Cron Format
```bash
[* * * * *] command_to_execute
```
To learn more about cron format visit:[https://en.wikipedia.org/wiki/Cron]

### Example usage
Schedule the scraper to collect and update data from the website everyday at midnight.
```bash
$ crontab -e
```
Enter the following into editor:
```text
0 0 * * * bash /path/to/your/bash_file
```
Save the file by executing ```:wq ```

Done!

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
ⴀ
