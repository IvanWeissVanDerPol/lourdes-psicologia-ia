// Multi-theme configuration - 5 Dark Themes with Black Backgrounds
export const themes = {
  // Theme 1: Midnight Blue (Default Dark)
  midnight: {
    id: 'midnight',
    name: 'Midnight Blue',
    description: 'Professional dark theme with blue accents',
    type: 'dark',
    colors: {
      // Background colors - Pure Black
      '--bg-primary': '#000000',
      '--bg-secondary': '#111111',
      '--bg-tertiary': '#222222',
      '--bg-glass': 'rgba(0, 0, 0, 0.8)',
      '--bg-card': 'rgba(17, 17, 17, 0.9)',
      '--bg-overlay': 'rgba(0, 0, 0, 0.9)',
      
      // Text colors
      '--text-primary': '#f8fafc',
      '--text-secondary': '#cbd5e1',
      '--text-muted': '#94a3b8',
      '--text-heading': '#ffffff',
      '--text-accent': '#60a5fa',
      
      // Brand colors
      '--color-primary': '#3b82f6',
      '--color-secondary': '#8b5cf6',
      '--color-accent': '#06b6d4',
      '--color-success': '#10b981',
      '--color-warning': '#f59e0b',
      '--color-danger': '#ef4444',
      
      // Border colors
      '--border-primary': 'rgba(59, 130, 246, 0.3)',
      '--border-secondary': 'rgba(139, 92, 246, 0.3)',
      '--border-light': 'rgba(248, 250, 252, 0.1)',
      '--border-medium': 'rgba(248, 250, 252, 0.2)',
      
      // Gradients
      '--gradient-primary': 'linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%)',
      '--gradient-hero': 'linear-gradient(135deg, #3b82f6 0%, #8b5cf6 50%, #06b6d4 100%)',
      '--gradient-text': 'linear-gradient(135deg, #60a5fa 0%, #a78bfa 100%)',
    }
  },

  // Theme 2: Cosmic Purple
  cosmic: {
    id: 'cosmic',
    name: 'Cosmic Purple',
    description: 'Deep space theme with purple and magenta',
    type: 'dark',
    colors: {
      '--bg-primary': '#000000',
      '--bg-secondary': '#111111',
      '--bg-tertiary': '#222222',
      '--bg-glass': 'rgba(0, 0, 0, 0.8)',
      '--bg-card': 'rgba(17, 17, 17, 0.9)',
      '--bg-overlay': 'rgba(0, 0, 0, 0.9)',
      
      '--text-primary': '#f3f0ff',
      '--text-secondary': '#d1c7e8',
      '--text-muted': '#a78bfa',
      '--text-heading': '#ffffff',
      '--text-accent': '#c084fc',
      
      '--color-primary': '#8b5cf6',
      '--color-secondary': '#ec4899',
      '--color-accent': '#f472b6',
      '--color-success': '#10b981',
      '--color-warning': '#f59e0b',
      '--color-danger': '#ef4444',
      
      '--border-primary': 'rgba(139, 92, 246, 0.3)',
      '--border-secondary': 'rgba(236, 72, 153, 0.3)',
      '--border-light': 'rgba(243, 240, 255, 0.1)',
      '--border-medium': 'rgba(243, 240, 255, 0.2)',
      
      '--gradient-primary': 'linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%)',
      '--gradient-hero': 'linear-gradient(135deg, #8b5cf6 0%, #ec4899 50%, #f472b6 100%)',
      '--gradient-text': 'linear-gradient(135deg, #c084fc 0%, #f472b6 100%)',
    }
  },

  // Theme 3: Emerald Forest
  forest: {
    id: 'forest',
    name: 'Emerald Forest',
    description: 'Natural dark theme with green accents',
    type: 'dark',
    colors: {
      '--bg-primary': '#000000',
      '--bg-secondary': '#111111',
      '--bg-tertiary': '#222222',
      '--bg-glass': 'rgba(0, 0, 0, 0.8)',
      '--bg-card': 'rgba(17, 17, 17, 0.9)',
      '--bg-overlay': 'rgba(0, 0, 0, 0.9)',
      
      '--text-primary': '#f0fdf4',
      '--text-secondary': '#bbf7d0',
      '--text-muted': '#86efac',
      '--text-heading': '#ffffff',
      '--text-accent': '#34d399',
      
      '--color-primary': '#10b981',
      '--color-secondary': '#059669',
      '--color-accent': '#34d399',
      '--color-success': '#22c55e',
      '--color-warning': '#f59e0b',
      '--color-danger': '#ef4444',
      
      '--border-primary': 'rgba(16, 185, 129, 0.3)',
      '--border-secondary': 'rgba(5, 150, 105, 0.3)',
      '--border-light': 'rgba(240, 253, 244, 0.1)',
      '--border-medium': 'rgba(240, 253, 244, 0.2)',
      
      '--gradient-primary': 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
      '--gradient-hero': 'linear-gradient(135deg, #10b981 0%, #059669 50%, #34d399 100%)',
      '--gradient-text': 'linear-gradient(135deg, #34d399 0%, #10b981 100%)',
    }
  },

  // Theme 4: Crimson Night
  crimson: {
    id: 'crimson',
    name: 'Crimson Night',
    description: 'Bold dark theme with red and orange',
    type: 'dark',
    colors: {
      '--bg-primary': '#000000',
      '--bg-secondary': '#111111',
      '--bg-tertiary': '#222222',
      '--bg-glass': 'rgba(0, 0, 0, 0.8)',
      '--bg-card': 'rgba(17, 17, 17, 0.9)',
      '--bg-overlay': 'rgba(0, 0, 0, 0.9)',
      
      '--text-primary': '#fef2f2',
      '--text-secondary': '#fecaca',
      '--text-muted': '#f87171',
      '--text-heading': '#ffffff',
      '--text-accent': '#fb7185',
      
      '--color-primary': '#ef4444',
      '--color-secondary': '#f97316',
      '--color-accent': '#fb7185',
      '--color-success': '#10b981',
      '--color-warning': '#f59e0b',
      '--color-danger': '#dc2626',
      
      '--border-primary': 'rgba(239, 68, 68, 0.3)',
      '--border-secondary': 'rgba(249, 115, 22, 0.3)',
      '--border-light': 'rgba(254, 242, 242, 0.1)',
      '--border-medium': 'rgba(254, 242, 242, 0.2)',
      
      '--gradient-primary': 'linear-gradient(135deg, #ef4444 0%, #f97316 100%)',
      '--gradient-hero': 'linear-gradient(135deg, #ef4444 0%, #f97316 50%, #fb7185 100%)',
      '--gradient-text': 'linear-gradient(135deg, #fb7185 0%, #ef4444 100%)',
    }
  },

  // Theme 5: Arctic Blue
  arctic: {
    id: 'arctic',
    name: 'Arctic Blue',
    description: 'Cool dark theme with cyan and ice blue',
    type: 'dark',
    colors: {
      '--bg-primary': '#000000',
      '--bg-secondary': '#111111',
      '--bg-tertiary': '#222222',
      '--bg-glass': 'rgba(0, 0, 0, 0.8)',
      '--bg-card': 'rgba(17, 17, 17, 0.9)',
      '--bg-overlay': 'rgba(0, 0, 0, 0.9)',
      
      '--text-primary': '#f0f9ff',
      '--text-secondary': '#bae6fd',
      '--text-muted': '#7dd3fc',
      '--text-heading': '#ffffff',
      '--text-accent': '#38bdf8',
      
      '--color-primary': '#0ea5e9',
      '--color-secondary': '#06b6d4',
      '--color-accent': '#22d3ee',
      '--color-success': '#10b981',
      '--color-warning': '#f59e0b',
      '--color-danger': '#ef4444',
      
      '--border-primary': 'rgba(14, 165, 233, 0.3)',
      '--border-secondary': 'rgba(6, 182, 212, 0.3)',
      '--border-light': 'rgba(240, 249, 255, 0.1)',
      '--border-medium': 'rgba(240, 249, 255, 0.2)',
      
      '--gradient-primary': 'linear-gradient(135deg, #0ea5e9 0%, #06b6d4 100%)',
      '--gradient-hero': 'linear-gradient(135deg, #0ea5e9 0%, #06b6d4 50%, #22d3ee 100%)',
      '--gradient-text': 'linear-gradient(135deg, #38bdf8 0%, #22d3ee 100%)',
    }
  }
};

// Theme utilities
export const themeUtils = {
  // Get theme by ID
  getTheme: (themeId) => themes[themeId] || themes.cosmic,
  
  // Get all available themes
  getAllThemes: () => Object.values(themes),
  
  // Apply theme to document
  applyTheme: (themeId) => {
    const theme = themeUtils.getTheme(themeId);
    const root = document.documentElement;
    
    // Apply all color variables
    Object.entries(theme.colors).forEach(([property, value]) => {
      root.style.setProperty(property, value);
    });
    
    // Store preference
    localStorage.setItem('preferred-theme', themeId);
    
    // Add theme class to body
    document.body.className = document.body.className.replace(/theme-\w+/g, '');
    document.body.classList.add(`theme-${themeId}`);
  },
  
  // Get stored theme preference
  getStoredTheme: () => {
    return localStorage.getItem('preferred-theme') || 'cosmic';
  },
  
  // Initialize theme system
  initializeTheme: () => {
    const storedTheme = themeUtils.getStoredTheme();
    themeUtils.applyTheme(storedTheme);
  }
};

// Default export
export default themes; 