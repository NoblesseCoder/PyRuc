run: 
	python3 parser.py
	python3 ICO.py

icg:
	cat icg.txt

oic:
	cat oic.txt	

clean:
	rm -rf __pycache__
	rm -f oic.txt
	rm -f parselog.txt
	rm -f parser.out
	rm -f parsetab.py
	rm -f icg.txt
	