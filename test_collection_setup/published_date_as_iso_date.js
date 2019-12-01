use fixdates 
db.t1.updateOne( { "text" : "third blog post" }, { "$currentDate" : { "published_date" : true } } )

