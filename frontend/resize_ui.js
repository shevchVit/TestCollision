document.addEventListener("DOMContentLoaded", () => {
    var origin_screen_width = 1920;
    var origin_screen_height = 1080;
    var ui_body = document.getElementsByTagName("body")[0];
    var html = document.getElementsByTagName("html")[0];

    const resize_window = () => {
        var current_screen_width = html.offsetWidth;
        var current_screen_height = html.offsetHeight;
        var K_origin_resolution = origin_screen_width / origin_screen_height;
        var K_current_resolution = current_screen_width / current_screen_height;
        var k_zoom = 1;
    
        if (K_current_resolution >= K_origin_resolution) {
            // по высоте
            k_zoom = current_screen_height / origin_screen_height;
        } else {
            // по ширине
            k_zoom = current_screen_width / origin_screen_width;
        }
        ui_body.style.zoom = k_zoom;
    }
    resize_window();
    setInterval(resize_window, 500);
})

