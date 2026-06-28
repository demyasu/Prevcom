document.addEventListener('DOMContentLoaded', function() {
    const diasEl = document.getElementById('dias-restantes');
    if (diasEl) {
        const dias = parseInt(diasEl.textContent);
        if (dias <= 7) {
            diasEl.className = 'text-danger fw-bold';
        } else if (dias <= 30) {
            diasEl.className = 'text-warning fw-bold';
        }
    }
});
