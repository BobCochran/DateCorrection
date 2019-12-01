use fixdates 
db.t1.updateOne( { "text" : "second blog post" }, { "$set" : { "published_date" : NumberLong(-12488169600000) } } )

