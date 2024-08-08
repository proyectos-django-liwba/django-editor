
document.addEventListener('DOMContentLoaded', function () {
    const loading = document.getElementById('loading');
    addEventListener('py:ready', () => loading.close());
    loading.showModal();
});



