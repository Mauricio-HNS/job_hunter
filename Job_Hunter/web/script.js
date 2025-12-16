// Contador de jobs enviados
let sentCount = 0;

// Atualiza o contador na tela
function updateCounter() {
    document.getElementById('counter').textContent = `Jobs enviados: ${sentCount}`;
}

// Pega todos os links
const links = document.querySelectorAll('ul li a');

links.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault(); // evita abrir a página imediatamente
        if (!link.classList.contains('sent')) {
            link.classList.add('sent'); // marca como enviado
            sentCount++;
            updateCounter();
        }
        window.open(link.href, '_blank'); // abre em nova aba
    });
});

// Inicializa contador
updateCounter();
