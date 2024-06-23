// simple script that saves in the window the mouse position
// and the mouse button state

window.mouse = {
    x: 0,
    y: 0,
    left: false,
    right: false
};

document.addEventListener('mousemove', function(e) {
    window.mouse.x = e.clientX;
    window.mouse.y = e.clientY;
})

document.addEventListener('mousedown', function(e) {
    if (e.button === 0) {
        window.mouse.left = true;
    } else if (e.button === 2) {
        window.mouse.right = true;
    }
})

document.addEventListener('mouseup', function(e) {
    if (e.button === 0) {
        window.mouse.left = false;
    } else if (e.button === 2) {
        window.mouse.right = false;
    }
})

