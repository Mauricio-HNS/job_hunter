const cvInput = document.getElementById('cvInput');
const cvName = document.getElementById('cvName');
const deleteCV = document.getElementById('deleteCV');
const compatSlider = document.getElementById('compatSlider');
const compatValue = document.getElementById('compatValue');
const startScan = document.getElementById('startScan');
const progress = document.getElementById('progress');
const jobsTable = document.getElementById('jobsTable');

// Modal
const jobModal = document.getElementById('jobModal');
const modalTitle = document.getElementById('modalTitle');
const modalCompany = document.getElementById('modalCompany');
const modalLocation = document.getElementById('modalLocation');
const modalCompat = document.getElementById('modalCompat');
const modalDescription = document.getElementById('modalDescription');
const modalApply = document.getElementById('modalApply');
const modalClose = document.querySelector('.close');

let selectedCV = null;
let currentJob = null;

cvInput.addEventListener('change', (e) => {
    selectedCV = e.target.files[0];
    cvName.textContent = selectedCV ? selectedCV.name : 'Nenhum CV selecionado';
});

deleteCV.addEventListener('click', () => {
    selectedCV = null;
    cvInput.value = '';
    cvName.textContent = 'Nenhum CV selecionado';
});

compatSlider.addEventListener('input', () => {
    compatValue.textContent = `${compatSlider.value}%`;
});

startScan.addEventListener('click', () => {
    if (!selectedCV) { alert("Selecione um CV antes de buscar vagas!"); return; }
    progress.style.width = "0%";
    jobsTable.innerHTML = '';

    let i = 0;
    const interval = setInterval(() => {
        if (i >= 100) { clearInterval(interval); populateJobs(); return; }
        i += 10;
        progress.style.width = i + '%';
    }, 100);
});

function populateJobs() {
    const dummyJobs = [
        {title: 'Software Architect', company:'Google', location:'Berlin', compat: 70, description:'Desenvolvimento de soluções escaláveis e arquitetura full stack.'},
        {title: 'Backend Developer', company:'Amazon', location:'Madrid', compat: 65, description:'APIs, microservices e integração cloud.'},
        {title: 'Fullstack Engineer', company:'Microsoft', location:'Lisbon', compat: 55, description:'Front e backend com .NET, React e Flutter.'}
    ];

    dummyJobs.forEach((job,index)=>{
        if(job.compat >= parseInt(compatSlider.value)){
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${index+1}</td>
                <td>${job.title}</td>
                <td>${job.company}</td>
                <td>${job.location}</td>
                <td>${job.compat}%</td>
                <td><button class="viewBtn">Ver Descritivo</button></td>
                <td><button class="applyBtn">Aplicar</button></td>
            `;
            row.querySelector('.viewBtn').addEventListener('click', ()=>openJobModal(job));
            row.querySelector('.applyBtn').addEventListener('click', (e)=>applyToJob(job, e.target));
            jobsTable.appendChild(row);
        }
    });
}

function openJobModal(job){
    currentJob = job;
    modalTitle.textContent = job.title;
    modalCompany.textContent = job.company;
    modalLocation.textContent = `Local: ${job.location}`;
    modalCompat.textContent = `Compatibilidade: ${job.compat}%`;
    modalDescription.textContent = job.description;

    // Reset do botão modal se já aplicado
    modalApply.textContent = "Aplicar";
    modalApply.classList.remove('applied');
    modalApply.disabled = false;

    jobModal.style.display = 'block';
}

modalClose.onclick = () => { jobModal.style.display = 'none'; }
window.onclick = (e) => { if(e.target == jobModal) jobModal.style.display = 'none'; }

modalApply.onclick = () => { 
    applyToJob(currentJob);
    modalApply.textContent = "Aplicado";
    modalApply.classList.add('applied');
    modalApply.disabled = true;
}

function applyToJob(job, button=null){
    alert(`Aplicando para ${job.title} na empresa ${job.company}`);
    
    if(button){
        button.textContent = "Aplicado";
        button.classList.add('applied');
        button.disabled = true;
    }
}
