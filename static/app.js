const roleSelect = document.getElementById("roleSelect");

const careerContent = document.getElementById("careerContent");
const emptyState = document.getElementById("emptyState");
const errorMessage = document.getElementById("errorMessage");

const roleName = document.getElementById("roleName");
const roleDescription = document.getElementById("roleDescription");

const skillsContainer = document.getElementById("skillsContainer");
const technologyContainer = document.getElementById("technologyContainer");
const projectContainer = document.getElementById("projectContainer");

const skillCount = document.getElementById("skillCount");


async function fetchJSON(url) {
    const response = await fetch(url);

    if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
    }

    return await response.json();
}

async function loadCareerGraph(role) {
    const encodedRole = encodeURIComponent(role);

    return await fetchJSON(
        `/api/roles/${encodedRole}/graph`
    );
}

async function loadRoles() {
    try {
        const roles = await fetchJSON("/api/roles");

        roleSelect.innerHTML = `
            <option value="">
                Select a career role...
            </option>
        `;

        roles.forEach((role) => {
            const option = document.createElement("option");

            option.value = role.name;
            option.textContent = role.name;

            roleSelect.appendChild(option);
        });

    } catch (error) {
        roleSelect.innerHTML = `
            <option value="">
                Unable to load careers
            </option>
        `;

        showError(
            "Unable to connect to CareerGraph. Please try again later."
        );
    }
}


async function loadCareer(role) {

    hideError();

    careerContent.classList.add("hidden");
    emptyState.classList.add("hidden");

    try {

        const encodedRole = encodeURIComponent(role);

        const [
            roles,
            skills,
            technologies,
            projects,
            graph
        ] = await Promise.all([

            fetchJSON("/api/roles"),

            fetchJSON(
                `/api/roles/${encodedRole}/skills`
            ),

            fetchJSON(
                `/api/roles/${encodedRole}/technologies`
            ),

            fetchJSON(
                `/api/roles/${encodedRole}/projects`
            ),

            fetchJSON(
                `/api/roles/${encodedRole}/graph`
            )
        ]);


        const selectedRole = roles.find(
            (item) => item.name === role
        );


        if (!selectedRole) {
            throw new Error("Career role not found.");
        }


        // -------------------------
        // Role
        // -------------------------

        roleName.textContent =
            selectedRole.name;

        roleDescription.textContent =
            selectedRole.description;


        // -------------------------
        // Sections
        // -------------------------

        renderSkills(skills);

        renderTechnologies(technologies);

        renderProjects(projects);


        // -------------------------
        // Graph
        // -------------------------

        renderCareerGraph(graph);


        careerContent.classList.remove("hidden");

    } catch (error) {

        console.error(
            "Career loading error:",
            error
        );

        showError(
            "We couldn't load this career information. Please try again."
        );

        emptyState.classList.remove("hidden");
    }
}


function renderSkills(skills) {

    skillsContainer.innerHTML = "";

    skillCount.textContent =
        `${skills.length} skills`;


    skills.forEach((skill) => {

        const tag = document.createElement("div");

        tag.className = "skill-tag";

        tag.innerHTML = `
            <span>${skill.name}</span>
            <small>${skill.category}</small>
        `;

        skillsContainer.appendChild(tag);
    });
}


function renderTechnologies(technologies) {

    technologyContainer.innerHTML = "";


    technologies.forEach((technology) => {

        const card = document.createElement("div");

        card.className = "technology-card";

        card.innerHTML = `
            <div class="technology-icon">
                ${technology.name.charAt(0)}
            </div>

            <div>
                <strong>${technology.name}</strong>
                <span>${technology.type}</span>
            </div>
        `;

        technologyContainer.appendChild(card);
    });
}


function renderProjects(projects) {

    projectContainer.innerHTML = "";


    projects.forEach((project) => {

        const card = document.createElement("article");

        card.className = "project-card";


        const skills = project.matching_skills
            .map(
                (skill) =>
                    `<span>${skill}</span>`
            )
            .join("");


        card.innerHTML = `
            <div class="project-card-content">

                <p class="project-label">
                    PROJECT
                </p>

                <h4>
                    ${project.name}
                </h4>

                <p>
                    ${project.description}
                </p>

                <div class="project-skills">
                    ${skills}
                </div>

            </div>
        `;

        projectContainer.appendChild(card);
    });
}

function renderCareerGraph(graph) {

    const container = document.getElementById("career-graph");

    if (!container) {
        return;
    }

    container.innerHTML = "";

    const cy = cytoscape({

        container: container,

        elements: [
            ...graph.nodes.map(node => ({
                data: node
            })),

            ...graph.edges
        ],

        style: [

            // -------------------------
            // Default node
            // -------------------------

            {
                selector: "node",

                style: {
                    "label": "data(label)",

                    "text-wrap": "wrap",
                    "text-max-width": "100px",

                    "font-size": "11px",

                    "text-valign": "center",
                    "text-halign": "center",

                    "background-color": "#eeeeff",

                    "border-width": 1,
                    "border-color": "#c7c7e8",

                    "color": "#30305f",

                    "width": 65,
                    "height": 65
                }
            },


            // -------------------------
            // Role
            // -------------------------

            {
                selector: 'node[type="role"]',

                style: {
                    "background-color": "#5b5bd6",

                    "color": "#ffffff",

                    "width": 110,
                    "height": 110,

                    "font-size": 14,

                    "font-weight": "bold",

                    "border-width": 2,
                    "border-color": "#4545b8"
                }
            },


            // -------------------------
            // Skill
            // -------------------------

            {
                selector: 'node[type="skill"]',

                style: {
                    "background-color": "#eeeeff",

                    "border-color": "#c7c7e8",

                    "color": "#30305f"
                }
            },


            // -------------------------
            // Technology
            // -------------------------

            {
                selector: 'node[type="technology"]',

                style: {
                    "background-color": "#ecfdf5",

                    "border-color": "#a7e3cd",

                    "color": "#047857"
                }
            },


            // -------------------------
            // Project
            // -------------------------

            {
                selector: 'node[type="project"]',

                style: {
                    "background-color": "#fff7ed",

                    "border-color": "#fed7aa",

                    "color": "#9a3412",

                    "width": 85,
                    "height": 85
                }
            },


            // -------------------------
            // Edges
            // -------------------------

            {
                selector: "edge",

                style: {
                    "width": 1.5,

                    "line-color": "#cbd5e1",

                    "target-arrow-color": "#cbd5e1",

                    "target-arrow-shape": "triangle",

                    "curve-style": "bezier",

                    "label": "data(label)",

                    "font-size": 8,

                    "color": "#6b7280",

                    "text-background-color": "#ffffff",

                    "text-background-opacity": 1,

                    "text-background-padding": "3px"
                }
            }
        ],


        // -------------------------
        // Layout
        // -------------------------

        layout: {
            name: "cose",

            animate: true,

            animationDuration: 800,

            padding: 50,

            nodeRepulsion: 7000,

            idealEdgeLength: 150,

            edgeElasticity: 100
        },


        // -------------------------
        // Graph controls
        // -------------------------

        zoomingEnabled: true,

        userZoomingEnabled: true,

        panningEnabled: true,

        userPanningEnabled: true,

        boxSelectionEnabled: false,

        minZoom: 0.4,

        maxZoom: 2.5
    });


    // -------------------------
    // Node click
    // -------------------------

    cy.on("tap", "node", function (event) {

        const node = event.target;

        console.log(
            "Selected node:",
            node.data()
        );

    });


    return cy;
}

function showError(message) {

    errorMessage.textContent = message;

    errorMessage.classList.remove("hidden");
}


function hideError() {

    errorMessage.classList.add("hidden");
}


roleSelect.addEventListener(
    "change",
    (event) => {

        const role = event.target.value;

        if (!role) {

            careerContent.classList.add("hidden");

            emptyState.classList.remove("hidden");

            return;
        }

        loadCareer(role);
    }
);


loadRoles();