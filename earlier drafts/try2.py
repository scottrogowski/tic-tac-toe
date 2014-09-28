a = range(1,6)

def cycle(x):
	for i in range(len(x)):
		print a.pop(i)

	if type(x) == list:
		for i in x:
			cycle(i)
	else:
		print x

def cycle(x):
	for i in x:
		pass
		#print i
hx = []

for i in a:
	hx.append(a.pop())
	cycle(a)

	print a

	if len(a) == 0:
		a = hx

#cycle(a)

# check_win() -> 0,1, or -1
# push moves onto stack
# find length of that stack, to find out shortest path to victory, then choose that

# do move, push it onto stack
# is_full(), check_win()

def crawl(seed):
	"""Recursion example from web scraping."""
    crawled = set()
    def crawl_recursively(link):
        if link in crawled:
            return
        newLinks = getAllLinksOnPage(link)
        crawled.add(seed)
        for link in newLinks:
            crawl_recursively(link)
    crawl_recursively(seed)
    return sorted(crawled)