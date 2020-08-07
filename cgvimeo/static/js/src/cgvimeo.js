/* Javascript for CGVimeoXBlock. */
function CGVimeoXBlock(runtime, element) {

    function updateUI(result) {
        console.log(result)
    }

    var handlerUrl = runtime.handlerUrl(element, 'get_vimeo_id');

    $('p', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            success: updateUI
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
