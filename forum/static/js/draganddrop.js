$(function() {
    $(".dropdown-menu li a").draggable({
        appendTo: "body",
        helper: "clone",
        cursor: "move",
        zIndex: 10000
    });
    $(".favorites").draggable({
        appendTo: "body",
        helper: "clone",
        cursor: "move",
        zIndex: 10000,
    });
    $(".favorites").droppable({
        activeClass: "ui-state-default",
        hoverClass: "ui-state-hover",
        accept: ":not(.ui-sortable-helper)",
        drop: function(event, ui) {
            if (ui.draggable.hasClass("favorites")) {
                var currentText = $(this).text();
                var currentHref = $(this).attr("href");
                $(this).attr("href", ui.draggable.attr("href"));
                $(this).text(ui.draggable.text()).appendTo(this);
                ui.draggable.text(currentText);
                ui.draggable.attr("href", currentHref);
            } else {
                $(this).attr("href", ui.draggable.attr("href"));
                $(this).find(".favorites").remove();
                $(this).text(ui.draggable.text()).appendTo(this);
            }
        }
    });
    $(".empty").droppable({
        activeClass: "ui-state-default",
        hoverClass: "ui-state-hover",
        accept: ":not(.favorites)",
        drop: function(event, ui) {
            var currentText = ui.draggable.text();
            var currentHref = ui.draggable.attr("href");
            $secondLast = $(this).parent().last().prev();
            $("<li><a class='favorites ui-draggable ui-draggable-handle ui-droppable' href='" + currentHref + "'>" + currentText + "</a></li>").insertAfter($secondLast);
            $('.favorites').draggable({
                appendTo: "body",
                helper: "clone",
                cursor: "move",
                zIndex: 10000,
            });
        }
    });
    $(".trash").droppable({
        activeClass: "ui-state-default",
        hoverClass: "ui-state-hover",
        accept: ":not(.dropdown-menu li a)",
        drop: function(event, ui) {
            ui.draggable.remove();
        }
    });
});

jQuery.fn.swapWith = function(to) {
    return this.each(function() {
        var copy_to = $(to).clone();
        var copy_from = $(this).clone();
        $(to).replaceWith(copy_from);
        $(this).replaceWith(copy_to);
    });
};