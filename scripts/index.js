function changeMode(newMode) {

    const about = document.getElementById('about');
    const purdue = document.getElementById('purdue');
    const intern = document.getElementById('intern');
    const project = document.getElementById('project');
    const about_btn = document.getElementById('about_btn');
    const purdue_btn = document.getElementById('purdue_btn');
    const intern_btn = document.getElementById('intern_btn');
    const project_btn = document.getElementById('project_btn');

    [about_btn, purdue_btn, intern_btn, project_btn].forEach(section => {
        section.classList.remove('disabled');
    });

    if (newMode === "about") {
        about_btn.classList.add('disabled');
    } else if (newMode === "purdue") {
        purdue_btn.classList.add('disabled');
    } else if (newMode === "intern") { 
        intern_btn.classList.add('disabled');
    } else if (newMode === "project") {
        project_btn.classList.add('disabled');
    }

    [about, purdue, intern, project].forEach(section => {
        section.classList.remove('show');
        setTimeout(() => {
            section.style.display = 'none';
        }, 500);
    });

    setTimeout(() => {
        let sectionToShow;
        if (newMode === "about") {
            sectionToShow = about;
        } else if (newMode === "purdue") {
            sectionToShow = purdue;
        } else if (newMode === "intern") { 
            sectionToShow = intern;
        } else if (newMode === "project") {
            sectionToShow = project;
        }

        if (sectionToShow) {
            sectionToShow.style.display = 'block';
            setTimeout(() => {
                sectionToShow.classList.add('show');
            }, 50);
        }
    }, 500);
}

function fadeIn(id, time) {
    const card = document.getElementById(id);
    setTimeout(() => {
        card.style.display = 'block';
        setTimeout(() => {
            card.classList.add('show');
        }, 10);
    }, 300 * time);
}

window.onload = function() {
    fadeIn('about_card', 1);
    fadeIn('purdue_card', 1.5);
    fadeIn('intern_card', 2);
    fadeIn('project_card', 2.5);
    changeMode('about', 50);
}