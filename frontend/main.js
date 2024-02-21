document.addEventListener("DOMContentLoaded", () => {
    
    const url_get_position = "http://127.0.0.1:9000/get_position";
    const url_get_blocks = "http://127.0.0.1:9000/get_blocks";

    let drone = document.getElementById("drone");

    let map_body = document.getElementById("map_body");

    let blocks = [];

    const mapping = (value, in_min, in_max, out_min, out_max) => {
        return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
    }

    const set_drone = (x, y, d) => {
        drone.style.scale = d;
        drone_half_width = drone.offsetWidth / 2;
        
        x_px = mapping(x, -10, 10, 1000, 0);
        y_px = mapping(y, -10, 10, 1000, 0);

        drone.style.top = "calc(" + y_px + "px - " + drone_half_width + "px)";
        drone.style.left = "calc(" + x_px + "px - " + drone_half_width + "px)";
    }

    const start = () => {
        fetch(url_get_blocks).then((response) => response.json().then((data) => {
            console.log(data)
            for (var i = 0; i < data.length; ++i) {
                let new_block = document.createElement("div");
                new_block.classList.add("block");

                x_px = mapping(data[i][0], -10, 10, 1000, 0);
                y_px = mapping(data[i][1], -10, 10, 1000, 0);

                new_block.style.top = "calc(" + y_px + "px - 25px)";
                new_block.style.left = "calc(" + x_px + "px - 25px)";

                map_body.appendChild(new_block);
                blocks.push(new_block);
            }
        })).then(setInterval(update_position, 50));
    }

    const update_position = () => {
        fetch(url_get_position).then((response) => response.json().then((data) => {
            // console.log(data)
            set_drone(data.x, data.y, data.d);
            var collisions = data.collisions;
            // console.log(collisions)
            for (let i = 0; i < blocks.length; ++i) {
                if (collisions.includes(i)) {
                    // console.log(i, collisions)
                    // console.log("collision", blocks[i])
                    blocks[i].style.background = "red";
                } else {
                    blocks[i].style.background = "transparent";
                }
            }
        }))
    }

    start();
})