gh:
	rm -rf /tmp/gh-site
	mkdir -p /tmp/gh-site
	cp -r _site/* /tmp/gh-site/
	git checkout -B gh-pages
	rm -rf *
	mv /tmp/gh-site/* .
	git add .
	git commit -am 'site'
	git push origin gh-pages --force
	git checkout master
	echo "OK"
