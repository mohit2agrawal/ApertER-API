var express     = require("express"),
    app         = express();

app.set("view engine", "ejs");
app.use(express.static(__dirname + '/public'));

app.get("/er", function(req, res){
    res.render("er");
});

app.get("*", function(req,res) {
    res.redirect("er");
});

app.listen(8888, function() {
    console.log("SERVER IS UP at http://localhost:8888/");
} );