$(document).ready(function() {
    $("#blanks form").submit(function(event) {

      var blanks = ["person1", "person2", "animal", "exclamation", "verb", "noun"];

      blanks.forEach(function(blank) {
        // debugger;
        var userInput = $("input#" + blank).val();
        $("." + blank).text(userInput).val();
      });

      $("#story").show()
      console.log("i am here")
      event.preventDefault();
    });
  });