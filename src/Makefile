DICTDIR = /usr/share/myspell/dicts
FILES = shs_CA.aff shs_CA.dic shs-CA.aff shs-CA.dic

all: shs-CA.aff shs-CA.dic
shs-CA.aff:
	ln -s shs_CA.aff shs-CA.aff 
shs-CA.dic:
	ln -s shs_CA.dic shs-CA.dic
clean:
	rm -f shs-CA.*

install: shs_CA.aff shs_CA.dic shs-CA.aff shs-CA.dic
	cp -a shs_CA.aff shs_CA.dic shs-CA.aff shs-CA.dic $(DICTDIR)

uninstall: $(FILES)
	rm -f $(DICTDIR)/shs*.*

