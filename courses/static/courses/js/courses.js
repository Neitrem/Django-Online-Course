var openNewLessonForm = function () {
    $('.create-new').show(); $('#open-form').hide()
}

var closeNewLessonForm = function (e) {
    $('.create-new').hide(); $('#open-form').show()
}



$(document).ready(function () {
    // Listen to submit event on the <form> itself!
    $('#new-lesson-form').submit(function (e) {
  
      // Prevent form submission which refreshes page
      e.preventDefault();
  
      // Serialize data
      var formData = $(this).serialize();
    });

});