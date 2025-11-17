// Dark Mode Toggle Functionality
(function() {
    // Get theme from localStorage or default to dark (new design is dark-first)
    const currentTheme = localStorage.getItem('theme') || 'dark';
    
    // Apply theme on page load
    if (currentTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        updateDarkModeIcon(true);
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        updateDarkModeIcon(false);
    }
    
    // Dark mode toggle button
    const darkModeToggle = document.getElementById('darkModeToggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateDarkModeIcon(newTheme === 'dark');
        });
    }
    
    // Update dark mode icon
    function updateDarkModeIcon(isDark) {
        const icon = document.getElementById('darkModeIcon');
        if (icon) {
            if (isDark) {
                icon.className = 'bi bi-sun-fill';
                icon.parentElement.title = 'Switch to Light Mode';
            } else {
                icon.className = 'bi bi-moon-fill';
                icon.parentElement.title = 'Toggle Dark Mode';
            }
        }
    }
    
    // Initialize icon on page load
    updateDarkModeIcon(currentTheme === 'dark');
})();






