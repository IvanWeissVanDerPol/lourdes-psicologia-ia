// UI Module - Modern TypeScript replacement for jQuery dependencies
// Handles theme switching, language switching, navigation, and scroll effects

// Theme Definitions - Single source of truth
export const THEMES = {
  midnight: {
    '--bg-primary': '#000000',
    '--bg-secondary': '#111111',
    '--bg-tertiary': '#222222',
    '--bg-glass': 'rgba(0, 0, 0, 0.8)',
    '--bg-card': 'rgba(17, 17, 17, 0.9)',
    '--text-primary': '#f8fafc',
    '--text-secondary': '#cbd5e1',
    '--text-muted': '#94a3b8',
    '--text-heading': '#ffffff',
    '--text-accent': '#60a5fa',
    '--color-primary': '#3b82f6',
    '--color-secondary': '#8b5cf6',
    '--color-accent': '#06b6d4',
    '--border-primary': 'rgba(59, 130, 246, 0.3)',
    '--border-light': 'rgba(248, 250, 252, 0.1)',
    '--gradient-primary': 'linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%)',
    '--gradient-hero': 'linear-gradient(135deg, #3b82f6 0%, #8b5cf6 50%, #06b6d4 100%)'
  },
  cosmic: {
    '--bg-primary': '#000000',
    '--bg-secondary': '#111111',
    '--bg-tertiary': '#222222',
    '--bg-glass': 'rgba(0, 0, 0, 0.8)',
    '--bg-card': 'rgba(17, 17, 17, 0.9)',
    '--text-primary': '#f3f0ff',
    '--text-secondary': '#d1c7e8',
    '--text-muted': '#a78bfa',
    '--text-heading': '#ffffff',
    '--text-accent': '#c084fc',
    '--color-primary': '#8b5cf6',
    '--color-secondary': '#ec4899',
    '--color-accent': '#f472b6',
    '--border-primary': 'rgba(139, 92, 246, 0.3)',
    '--border-light': 'rgba(243, 240, 255, 0.1)',
    '--gradient-primary': 'linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%)',
    '--gradient-hero': 'linear-gradient(135deg, #8b5cf6 0%, #ec4899 50%, #f472b6 100%)'
  },
  forest: {
    '--bg-primary': '#000000',
    '--bg-secondary': '#111111',
    '--bg-tertiary': '#222222',
    '--bg-glass': 'rgba(0, 0, 0, 0.8)',
    '--bg-card': 'rgba(17, 17, 17, 0.9)',
    '--text-primary': '#f0fdf4',
    '--text-secondary': '#bbf7d0',
    '--text-muted': '#86efac',
    '--text-heading': '#ffffff',
    '--text-accent': '#34d399',
    '--color-primary': '#10b981',
    '--color-secondary': '#059669',
    '--color-accent': '#34d399',
    '--border-primary': 'rgba(16, 185, 129, 0.3)',
    '--border-light': 'rgba(240, 253, 244, 0.1)',
    '--gradient-primary': 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
    '--gradient-hero': 'linear-gradient(135deg, #10b981 0%, #059669 50%, #34d399 100%)'
  },
  crimson: {
    '--bg-primary': '#000000',
    '--bg-secondary': '#111111',
    '--bg-tertiary': '#222222',
    '--bg-glass': 'rgba(0, 0, 0, 0.8)',
    '--bg-card': 'rgba(17, 17, 17, 0.9)',
    '--text-primary': '#fef2f2',
    '--text-secondary': '#fecaca',
    '--text-muted': '#f87171',
    '--text-heading': '#ffffff',
    '--text-accent': '#fb7185',
    '--color-primary': '#ef4444',
    '--color-secondary': '#f97316',
    '--color-accent': '#fb7185',
    '--border-primary': 'rgba(239, 68, 68, 0.3)',
    '--border-light': 'rgba(254, 242, 242, 0.1)',
    '--gradient-primary': 'linear-gradient(135deg, #ef4444 0%, #f97316 100%)',
    '--gradient-hero': 'linear-gradient(135deg, #ef4444 0%, #f97316 50%, #fb7185 100%)'
  },
  arctic: {
    '--bg-primary': '#000000',
    '--bg-secondary': '#111111',
    '--bg-tertiary': '#222222',
    '--bg-glass': 'rgba(0, 0, 0, 0.8)',
    '--bg-card': 'rgba(17, 17, 17, 0.9)',
    '--text-primary': '#f0f9ff',
    '--text-secondary': '#bae6fd',
    '--text-muted': '#7dd3fc',
    '--text-heading': '#ffffff',
    '--text-accent': '#38bdf8',
    '--color-primary': '#0ea5e9',
    '--color-secondary': '#06b6d4',
    '--color-accent': '#22d3ee',
    '--border-primary': 'rgba(14, 165, 233, 0.3)',
    '--border-light': 'rgba(240, 249, 255, 0.1)',
    '--gradient-primary': 'linear-gradient(135deg, #0ea5e9 0%, #06b6d4 100%)',
    '--gradient-hero': 'linear-gradient(135deg, #0ea5e9 0%, #06b6d4 50%, #22d3ee 100%)'
  }
} as const;

export type ThemeId = keyof typeof THEMES;

// Language Definitions
export const LANGUAGES = {
  en: { id: 'en', name: 'English', nativeName: 'English', flag: '🇺🇸' },
  es: { id: 'es', name: 'Spanish', nativeName: 'Español', flag: '🇪🇸' },
  pt: { id: 'pt', name: 'Portuguese', nativeName: 'Português', flag: '🇵🇹' },
  fr: { id: 'fr', name: 'French', nativeName: 'Français', flag: '🇫🇷' }
} as const;

export type LanguageId = keyof typeof LANGUAGES;

// Theme Management
export function applyTheme(themeId: ThemeId = 'midnight'): void {
  const theme = THEMES[themeId] || THEMES.midnight;
  const root = document.documentElement;

  // Apply CSS custom properties
  Object.entries(theme).forEach(([property, value]) => {
    root.style.setProperty(property, value);
  });

  // Update theme class on html element (not body)
  root.className = root.className.replace(/theme-\w+/g, '');
  root.classList.add(`theme-${themeId}`);

  // Store preference
  localStorage.setItem('preferred-theme', themeId);

  // Dispatch custom event for theme change
  window.dispatchEvent(new CustomEvent('themechange', { 
    detail: { themeId, theme } 
  }));
}

export function getStoredTheme(): ThemeId {
  const stored = localStorage.getItem('preferred-theme') as ThemeId;
  return stored && stored in THEMES ? stored : 'midnight';
}

export function initializeTheme(): void {
  const storedTheme = getStoredTheme();
  applyTheme(storedTheme);
  
  // Set immediate background to prevent FOUC
  document.documentElement.style.backgroundColor = '#000000';
}

// Theme Picker Component Logic
export function initThemePicker(): void {
  const themeToggle = document.querySelector('[data-theme-toggle]') as HTMLButtonElement;
  const themeDropdown = document.querySelector('[data-theme-dropdown]') as HTMLElement;
  const themeOptions = document.querySelectorAll('[data-theme-option]') as NodeListOf<HTMLButtonElement>;

  if (!themeToggle || !themeDropdown || !themeOptions.length) {
    // Only warn in development
    if (import.meta.env.DEV) {
      console.warn('Theme picker elements not found');
    }
    return;
  }

  // Toggle dropdown
  themeToggle.addEventListener('click', (e) => {
    e.stopPropagation();
    themeDropdown.classList.toggle('active');
    themeToggle.setAttribute('aria-expanded', 
      themeDropdown.classList.contains('active').toString()
    );
  });

  // Handle theme selection
  themeOptions.forEach(option => {
    const themeId = option.getAttribute('data-theme-option') as ThemeId;
    
    option.addEventListener('click', (e) => {
      e.stopPropagation();
      applyTheme(themeId);
      themeDropdown.classList.remove('active');
      themeToggle.setAttribute('aria-expanded', 'false');
      
      // Update active state
      themeOptions.forEach(opt => opt.classList.remove('active'));
      option.classList.add('active');
    });

    // Set initial active state
    if (themeId === getStoredTheme()) {
      option.classList.add('active');
    }
  });

  // Close dropdown when clicking outside
  document.addEventListener('click', (e) => {
    if (!themeToggle.contains(e.target as Node) && !themeDropdown.contains(e.target as Node)) {
      themeDropdown.classList.remove('active');
      themeToggle.setAttribute('aria-expanded', 'false');
    }
  });

  // Keyboard navigation
  themeToggle.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      themeToggle.click();
    }
  });
}

// Language Management
export function setLanguage(languageId: LanguageId): void {
  localStorage.setItem('preferred-language', languageId);
  
  // Dispatch custom event for language change
  window.dispatchEvent(new CustomEvent('languagechange', { 
    detail: { languageId, language: LANGUAGES[languageId] } 
  }));
  
  // Reload page to apply translations
  window.location.reload();
}

export function getStoredLanguage(): LanguageId {
  const stored = localStorage.getItem('preferred-language') as LanguageId;
  return stored && stored in LANGUAGES ? stored : 'en';
}

// Language Picker Component Logic
export function initLanguagePicker(): void {
  const languageToggle = document.querySelector('[data-language-toggle]') as HTMLButtonElement;
  const languageDropdown = document.querySelector('[data-language-dropdown]') as HTMLElement;
  const languageOptions = document.querySelectorAll('[data-language-option]') as NodeListOf<HTMLButtonElement>;
  const currentFlag = document.querySelector('[data-current-flag]') as HTMLElement;
  const currentLanguage = document.querySelector('[data-current-language]') as HTMLElement;

  if (!languageToggle || !languageDropdown || !languageOptions.length) {
    // Only warn in development
    if (import.meta.env.DEV) {
      console.warn('Language picker elements not found');
    }
    return;
  }

  // Set initial language display
  const currentLang = getStoredLanguage();
  if (currentFlag && currentLanguage) {
    currentFlag.textContent = LANGUAGES[currentLang].flag;
    currentLanguage.textContent = LANGUAGES[currentLang].name;
  }

  // Toggle dropdown
  languageToggle.addEventListener('click', (e) => {
    e.stopPropagation();
    languageDropdown.classList.toggle('active');
    languageToggle.setAttribute('aria-expanded', 
      languageDropdown.classList.contains('active').toString()
    );
  });

  // Handle language selection
  languageOptions.forEach(option => {
    const languageId = option.getAttribute('data-language-option') as LanguageId;
    
    option.addEventListener('click', (e) => {
      e.stopPropagation();
      setLanguage(languageId);
    });

    // Set initial active state
    if (languageId === currentLang) {
      option.classList.add('active');
    }
  });

  // Close dropdown when clicking outside
  document.addEventListener('click', (e) => {
    if (!languageToggle.contains(e.target as Node) && !languageDropdown.contains(e.target as Node)) {
      languageDropdown.classList.remove('active');
      languageToggle.setAttribute('aria-expanded', 'false');
    }
  });

  // Keyboard navigation
  languageToggle.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      languageToggle.click();
    }
  });
}

// Mobile Navigation - Replace jQuery mobile menu
export function initMobileNavigation(): void {
  const mobileToggle = document.querySelector('[data-mobile-toggle]') as HTMLButtonElement;
  const mobileMenu = document.querySelector('[data-mobile-menu]') as HTMLElement;
  const mobileNavLinks = document.querySelectorAll('[data-mobile-nav-link]') as NodeListOf<HTMLAnchorElement>;

  if (!mobileToggle || !mobileMenu) {
    // Only warn in development
    if (import.meta.env.DEV) {
      console.warn('Mobile navigation elements not found');
    }
    return;
  }

  // Toggle mobile menu
  mobileToggle.addEventListener('click', () => {
    const isActive = mobileMenu.classList.contains('active');
    
    if (isActive) {
      mobileMenu.classList.remove('active');
      mobileToggle.classList.remove('active');
      mobileToggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    } else {
      mobileMenu.classList.add('active');
      mobileToggle.classList.add('active');
      mobileToggle.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
    }
  });

  // Close mobile menu when clicking nav links
  mobileNavLinks.forEach(link => {
    link.addEventListener('click', () => {
      mobileMenu.classList.remove('active');
      mobileToggle.classList.remove('active');
      mobileToggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    });
  });

  // Keyboard navigation for mobile toggle
  mobileToggle.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      mobileToggle.click();
    }
  });
}

// Modern Scroll Effects - Replace jQuery scrollex/scrolly
export function initScrollEffects(): void {
  // Navigation scroll effect
  const navigation = document.querySelector('[data-main-navigation]') as HTMLElement;
  
  if (navigation) {
    const scrollThreshold = 100;
    let ticking = false;

    const updateNavigation = () => {
      if (window.scrollY > scrollThreshold) {
        navigation.classList.add('scrolled');
      } else {
        navigation.classList.remove('scrolled');
      }
      ticking = false;
    };

    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(updateNavigation);
        ticking = true;
      }
    }, { passive: true });
  }

  // Smooth scroll for anchor links - Native CSS behavior
  document.documentElement.style.scrollBehavior = 'smooth';

  // Intersection Observer for reveal animations - Replace scrollex
  const observerOptions: IntersectionObserverInit = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        // Stop observing once revealed for performance
        revealObserver.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Observe elements with reveal animation
  const revealElements = document.querySelectorAll('[data-reveal]');
  revealElements.forEach(element => {
    revealObserver.observe(element);
  });
}

// Modern Breakpoint Detection - Replace breakpoints.min.js
export function initResponsiveBreakpoints(): void {
  const breakpoints = {
    xlarge: '(max-width: 1680px)',
    large: '(max-width: 1280px)', 
    medium: '(max-width: 980px)',
    small: '(max-width: 736px)',
    xsmall: '(max-width: 480px)'
  };

  Object.entries(breakpoints).forEach(([name, query]) => {
    const mediaQuery = window.matchMedia(query);
    
    const updateBreakpoint = (mq: MediaQueryListEvent | MediaQueryList) => {
      document.documentElement.classList.toggle(`breakpoint-${name}`, mq.matches);
    };

    // Initial check
    updateBreakpoint(mediaQuery);
    
    // Listen for changes
    mediaQuery.addEventListener('change', updateBreakpoint);
  });
}

// Initialize all UI components
export function initializeUI(): void {
  // Wait for DOM to be ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      initializeTheme();
      initThemePicker();
      initLanguagePicker();
      initMobileNavigation();
      initScrollEffects();
      initResponsiveBreakpoints();
    });
  } else {
    initializeTheme();
    initThemePicker();
    initLanguagePicker();
    initMobileNavigation();
    initScrollEffects();
    initResponsiveBreakpoints();
  }
}

// Global API for backward compatibility
declare global {
  interface Window {
    applyTheme: typeof applyTheme;
    setLanguage: typeof setLanguage;
    UI: {
      themes: typeof THEMES;
      languages: typeof LANGUAGES;
      applyTheme: typeof applyTheme;
      setLanguage: typeof setLanguage;
    };
  }
}

// Expose global API
window.applyTheme = applyTheme;
window.setLanguage = setLanguage;
window.UI = {
  themes: THEMES,
  languages: LANGUAGES,
  applyTheme,
  setLanguage
}; 