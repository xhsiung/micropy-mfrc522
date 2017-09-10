AMPY=ampy
SERIAL=/dev/ttyUSB0

MPYFILES := \
	boot.py \
	axapp.py \
	axreadmfrc522.py \
	mfrc522.py \
	urequests.py \
	main.py 


install: $(MPYFILES) 
	for f in $^ ; \
	do \
	    echo installing $$f ;\
	    $(AMPY) -p $(SERIAL) put $$f ;\
	done;


clean: $(MPYFILES)
	$(AMPY) -p $(SERIAL) rm config.json
	for f in $^ ; \
	do \
	    echo delete $$f ;\
	    $(AMPY) -p $(SERIAL) rm $$f ;\
	done;


ls:
	$(AMPY) -p $(SERIAL) ls

login:
	picocom -b 115200 $(SERIAL)