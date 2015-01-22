Running via heroku now

pip install tornado
pip install python-cloudfiles

GET /cards/[CARD TITLE].jpg

See if it is in cloud files

If not:
    GET http://imperialassembly.com/oracle/?quicksearch=&search_13=[CARD TITLE]

    POST http://imperialassembly.com/oracle/dosearch
        search_13=[CARD TITLE]

    POST http://imperialassembly.com/docard",
        cardid: "3067"
        hashid: "300ce4a4924d586bbc8261515e90904d"

    Save image in cloud files

get image from cloud files

return image
