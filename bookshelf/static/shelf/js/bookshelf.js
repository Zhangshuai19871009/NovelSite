function remove(shelf_id) {
    var id = $("#group_id").val();
    if (confirm('确实要将本书移出书架么？')) {
        window.location.href = "delete_one_book?shelf_id=" + shelf_id + '&group_id=' + id;
    }
}