linux install

python venv commands:
python3 -m venv venv 
source venv/bin/activate

install these packages:
pip install selenium
pip install selenium webdriver-manager 
pip install python-telegram-bot
pip install bs4
pip install packaging
maybe something else ;)

sudo apt install google-chrome-stable

add to crontab (sudo crontab -e) like this line
*/10 * * * * /path/to/venv/bin/python3 /path/to/main.py >/dev/null 2>&1

