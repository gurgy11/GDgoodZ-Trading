$(document).ready(function() {

    $('.edit-btn').on('click', function() {
        window.location.href = 'http://127.0.0.1:5000/suppliers/edit/' + $(this).val();
    });

    $('.delete-btn').on('click', function() {
        window.location.href = 'http://127.0.0.1:5000/suppliers/delete/' + $(this).val();
    });
});