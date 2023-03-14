var openNewLessonForm = function () {
    $('.create-new').show(); $('#open-form').hide()
}

var closeNewLessonForm = function (e) {
    $('.create-new').hide(); $('#open-form').show()
}

const openModalWindow = function () {
    $('.modal-container').show();
}

function isHidden(el) {
    console.log(typeof(el));
    var style = window.getComputedStyle(el);
    
    return (style.display === 'none')
}

const ToggleSettingMenu = function () {
    if ( isHidden(document.getElementsByClassName('setting-menu')[0])) {
        $('.setting-menu').show();
    } else {
        $('.setting-menu').hide();
    }
}



$(document).ready(function () {
    // Listen to submit event on the <form> itself!
    // $('#new-lesson-form').submit(function (e) {
  
    //   // Prevent form submission which refreshes page
    //     e.preventDefault();
    
    //     title = document.getElementsByName("title").value;
    //     description = document.getElementsByName("description").value
    //     cost = document.getElementByName("cost").value
    //     duration = document.getElementByName("duration").value

    //   // Serialize data
    //     var formData = $(this).serialize();

    //     const formData = new FormData();
    //     //console.log(name);
    //     formData.append('title', title);
    //     formData.append('description', description);
    //     formData.append('cost', cost);
    //     formData.append('duration', duration);
    //     formData.append('csrfmiddlewaretoken', '{{ csrf_token }}');
    //     console.log(formData);
    //     fetch('{% url "contact" %}', {
    //         method: 'POST',
    //         body: formData
    //     })
    //     .then(response => response.json())
    //     .then(data => {
    //         console.log('Success:', data);
    //     })
    //     .catch(error => {
    //         console.error('Error:', error);
    //     });
    //     });
    // });


    $('#modal-form').submit(function (e) {
  
        // Prevent form submission which refreshes page
        e.preventDefault();


        $('.modal-container').hide();
    
        
    });


});