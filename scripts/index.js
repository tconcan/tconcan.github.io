let mode = "HI";

function changeMode(newMode) {

    const about = document.getElementById('about');
    const purdue = document.getElementById('purdue');
    const intern = document.getElementById('intern');
    const project = document.getElementById('project');

    about.style.display = 'none';
    purdue.style.display = 'none';
    intern.style.display = 'none';
    project.style.display = 'none';

    if(newMode === "about") {
        about.style.display = 'block';
    } else if(newMode === "purdue") {
        purdue.style.display = 'block';
    } else if(newMode === "intern") { 
        intern.style.display = 'block';
    } else if(newMode === "project") {
        project.style.display = 'block';
    }
}

window.onload = function() {
    changeMode("about");
}