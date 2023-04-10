const width_start = $(window).width();
const height_start = $(window).height();
let mobile_start = height_start > width_start;

function orientation() {
    const width = $(window).width();
    const height = $(window).height();
    let mobile = height > width;
    if (mobile_start !== mobile) {
        mobile_start = mobile;
        orientation_update()
    }
}


function orientation_update() {
    var header_height = document.getElementById('header').offsetHeight;
    document.getElementById('container').style.marginTop=header_height+"px";

    var footer_height = document.getElementById('footer').offsetHeight;
    document.getElementById('widgets').style.marginBottom=footer_height*1.5+"px";

    var navigation_desktop_width = document.getElementById('navigation__desktop').offsetWidth;
    document.getElementById('widgets').style.marginLeft=navigation_desktop_width+"px";
}

$(window).resize(orientation);
$(window).onload = setTimeout(orientation_update, 1);
$(window).onload = orientation_update();