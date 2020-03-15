init:
	pip3 install -r requirements.txt

download:
	python3 download_steps.py

test:
	python3 -m behave

upload:
	python3 upload_results.py