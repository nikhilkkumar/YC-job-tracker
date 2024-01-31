import gspread

keys = 'yc-job-scraper-027dfd285b0d.json'
gc = gspread.service_account(keys)

sh = gc.open("YC Startups and roles")

print(sh.sheet1.get('A1'))