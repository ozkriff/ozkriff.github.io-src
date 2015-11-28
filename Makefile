INPUTDIR=content
OUTPUTDIR=output
CONFFILE=pelicanconf.py
PUBLISHCONF=publishconf.py

all: html

html: clean $(OUTPUTDIR)/index.html

$(OUTPUTDIR)/%.html:
	pelican $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE)

publish:
	pelican $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF)

start_devserver:
	./develop_server.sh start

stop_devserver:
	./develop_server.sh stop

restart_devserver:
	./develop_server.sh restart

clean:
	rm -rf $(OUTPUTDIR)

.PHONY: html publish start_devserver stop_devserver restart_devserver clean
