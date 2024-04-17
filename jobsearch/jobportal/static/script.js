var a = document.getElementsByClassName('save-btn');

for (var i = 0; i < a.length; i++) {
    a[i].addEventListener('click', function() {
        // alert('Job Saved');
        Swal.fire({
            position: "top-end",
            icon: "success",
            title: "Your work has been saved",
            showConfirmButton: false,
            timer: 1500
          });
    });
}