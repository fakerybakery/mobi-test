from MOBI.MOBI import MOBI
data = "<p>Hello</p>";
options = {
	"title": "Local document",
  	"author": "Author name",
  	"subject": "Subject"
};

mobi = MOBI()

mobi.set_data(data)
mobi.set_options(options)

mobi.save('pyMobi.mobi');