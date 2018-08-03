function show() {
    document.getElementById('waa').style.height='';
    document.getElementById('hidden').style.display='';
    document.getElementById('show').style.display='none';
}
function hid() {
    document.getElementById('waa').style.height='72px';
    document.getElementById('hidden').style.display='none';
    document.getElementById('show').style.display='';
}
// 加入书架
function addshelf(book_id) {
    $.ajax({
        url: "/bookshelf/add_to_bookshelf/",
        type: 'GET',
        data: {
            book_id: book_id,
            group_id : 1
        },
        cache: false,
        success: function (data) {
            if (data['status'] == 'SUCCESS') {
                $("#addShelf").text(data['num']);
                alert(data['message']);
            } else {
                alert(data['message']);
            }
        }
    });
}
// 投票
function bookvote(book_id) {
    $.ajax({
        url: "/bookvote/get_book_vote/",
        type: 'GET',
        data: {
            book_id: book_id,
        },
        cache: false,
        success: function (data) {
            if (data['status'] == 'SUCCESS') {
                $("#toupiaonum").text(data['num']);
                alert(data['message']);
            } else {
                alert(data['message']);
            }
        }
    });
}
// 违禁举报
function reporterror(book_id) {
    $.ajax({
        url: '/reporterror/to_novel_error/',
        type: 'GET',
        cache: false,
        success: function (data) {
            if (data['code'] == 4002) {
                alert(data['message']);
                window.location.href = "/reporterror/delete_report/"
            } else if (data['code'] == 4001) {
                alert(data['message']);
            } else {
                window.location.href = "/reporterror/report_error_form/" + book_id + "," + 0
            }
        }
    });
}