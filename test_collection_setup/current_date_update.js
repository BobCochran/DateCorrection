use fixdates 
db.t1.updateOne( { "text" : "third blog post" }, { "$currentDate" : { "odt" : true } } )

