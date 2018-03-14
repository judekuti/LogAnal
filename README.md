# LogAnal

---

### Project Summary
This project created a basic CLI analytic program that examines data in a PostgreSQL database and prints out reports in plain-text format using python3. Over 2 million data was anaalysed based on log entries in the database. 

### Generated Report
This Program generated report on the following descriptive statistics:
1. The most popular three articles of all time
2. The most popular article authors of all time
3. Days with more than 1% of error requests

---

## Quick start
#### Requirements
- Python 3
- PostgreSQL
- newsdata.sql
- 'vagrant' 
- 'VirtualBox'


#### Environment Set-Up
- Installation set-up require Unix-Style Terminal or Git Bash Terminal for windows
- Download VirtualBox [virtualbox.org](here)
- Install Vagrant [vagrantup.com](here)
    > Note to make a firewall exception or allow permissions for these downloads
- Check for successful download with `vagrant --version`
- Navigate into the 'vagrant' directory, run ```vagrant up```.
- SSH to the virtual machine with ```vagrant ssh```.

#### Test run the 'news' database
1. Navigate to the vagrant directory `cd /vagrant`
2. Use the command `psql -d news -f newsdata.sql`
3. Connect to your database using `psql -d news`
4. Explore the tables using the `\dt` and `\d` table commands and `select` statements.
5. Exit the database with `\q`

#### Run the program
1. Ensure the `newsSurvey.py` and `newsdata.sql` files are in the vagrant directory
2. Launch the VM:
    a. `vagrant up`
    b. `vagrant ssh`
3. Within the VM, navigate to `cd /vagrant`
4. Execute the file `newsSurvey.py`
5. If the execution fails then execute with `python3 newsSurvey.py`
6. The `NewsOutput.txt` is the output of the program
---

## References
- [https://www.python-course.eu](https://www.python-course.eu/index.php)
- [https://www.postgresql.org](https://www.postgresql.org/docs/9.6/static/index.html)
- [https://blog.ghost.org](https://blog.ghost.org/markdown/)
