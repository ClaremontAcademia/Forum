$(function() {
    $(".dropdown-menu li a").draggable({
        appendTo: "body",
        helper: "clone",
        zIndex: 10000
    });
    $(".favorites").droppable({
        activeClass: "ui-state-default",
        hoverClass: "ui-state-hover",
        accept: ":not(.ui-sortable-helper)",
        drop: function(event, ui) {
            $(this).attr("href", ui.draggable.attr("href"));
            $(this).find(".favorites").remove();
            $(this).text(ui.draggable.text()).appendTo(this);
        }
    });
});