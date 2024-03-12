document.addEventListener('DOMContentLoaded', function() {
    // Add 'document-row' class to each row
    const rows = document.querySelectorAll('table tr');
    rows.forEach(row => {
        row.classList.add('document-row');
    });

    // Apply status color to status cells
    const statusCells = document.querySelectorAll('.status-cell');
    statusCells.forEach(cell => {
        const statusColor = cell.getAttribute('data-status-color');
        if (statusColor) {
            cell.style.color = statusColor;
        }
    });
});