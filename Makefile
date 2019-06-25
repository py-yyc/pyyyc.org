test:
	@echo 'Please visit http://localhost:5728/'
	docker run --rm -p 5728:80 -v "$PWD":/usr/share/nginx/html:ro nginx
