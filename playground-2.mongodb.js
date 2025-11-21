// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("AutoInsuranceDataProject");

// Find a document in a collection.
db.getCollection("Auto_Insurance_Data").findOne({

});

// db.getCollection("Auto_Insurance_Data").find({claimcst0:{$gt:0}}).count();
// db.getCollection("Auto_Insurance_Data").find({claimcst0:0}).count();
db.getCollection("Auto_Insurance_Data").find({claimcst0:{$gt:0}}).limit(5);
