with open('/Users/chanten/Desktop/PFDL/PFDL/main_app/static/content/proverbs.csv') as f:
	reader = csv.reader(f, delimiter = ',')
	next(reader, None)
	for row in reader:
		_, created = Proverb.objects.get_or_create(
			date=row[0],
			proverb=row[1],
		)
