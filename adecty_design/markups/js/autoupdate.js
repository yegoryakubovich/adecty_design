const width_start = $(window).width();
const height_start = $(window).height();
mobile_start = height_start > width_start;


$(window).resize(function(){
    const width = $(window).width();
    const height = $(window).height();
    let mobile = height > width;
    if (mobile_start !== mobile) {
        location.reload();
    }
});