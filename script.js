/*document.addEventListener("DOMContentLoaded", function() {
    window.addEventListener("scroll", function() {
        var farm = document.querySelector(".farm");
        var tree = document.querySelector(".tree");

        var scrollPosition = window.pageYOffset;

        // Adjust farm and tree positions based on scroll position
        farm.style.top = -scrollPosition + "px";
        tree.style.bottom = -scrollPosition + "px";
    });
});

window.onscroll = function() {
    startAnimations();
};

// Function to start animations when user scrolls down
function startAnimations() {
    // Calculate the scroll position
    var scrollPosition = window.scrollY;

    // Define the point on the page where animations should start
    var triggerPoint = 500; // Adjust as needed

    // Check if the user has scrolled past the trigger point
    if (scrollPosition > triggerPoint) {
        // Start animations
        document.getElementById('farm-drop').classList.add('animate-farm-drop');
        document.getElementById('tree-left').classList.add('animate-tree-left');
        document.getElementById('tree-right').classList.add('animate-tree-right');
    }
}
*/
 // Function to handle scroll event
 window.onscroll = function() {
    startAnimations();
};

// Function to start animations when user scrolls down
function startAnimations() {
    // Calculate the scroll position
    var scrollPosition = window.scrollY;

    // Define the point on the page where animations should start
    var triggerPoint = 500; // Adjust as needed

    // Check if the user has scrolled past the trigger point
    if (scrollPosition > triggerPoint) {
        // Start animations by adding 'visible' class
        document.getElementById('farm-drop').classList.add('visible');
        document.querySelectorAll('.tree').forEach(function(tree) {
            tree.classList.add('visible');
        });
    }
}