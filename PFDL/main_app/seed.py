import csv
from .models import Proverbs

with open('/Users/chanten/Desktop/PFDL/content/proverbs.csv') as f:
	reader = csv.reader(f, delimiter = '<')
	for row in reader:
		_, created = Proverbs.objects.get_or_create(
			date=row[0],
			proverb=row[1],
		)
