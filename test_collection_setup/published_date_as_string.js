use fixdates
db.t1.updateOne( { "text" : "first blog post" }, { "$set" : { "published_date" : "2017-09-17 15:00:00.000Z" } } )

