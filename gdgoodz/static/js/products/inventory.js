$(document).ready(function() {

    // Edit button click event
    $('.edit-btn').on('click', function() {
        window.location.href = 'http://127.0.0.1:5000/products/edit/' + $(this).val();
    });

    // Delete button click event
    $('.delete-btn').on('click', function() {
        window.location.href = 'http://127.0.0.1:5000/products/delete/' + $(this).val();
    });
});