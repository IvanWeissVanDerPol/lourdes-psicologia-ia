// Multi-language support configuration
export const languages = {
  en: {
    id: 'en',
    name: 'English',
    nativeName: 'English',
    flag: '🇺🇸',
    rtl: false,
    default: true
  },
  es: {
    id: 'es',
    name: 'Spanish',
    nativeName: 'Español',
    flag: '🇪🇸',
    rtl: false,
    default: false
  }
};

// Translation utilities
export const i18nUtils = {
  // Get language by ID
  getLanguage: (langId) => languages[langId] || languages.en,
  
  // Get all available languages
  getAllLanguages: () => Object.values(languages),
  
  // Get stored language preference
  getStoredLanguage: () => {
    const stored = localStorage.getItem('preferred-language');
    if (stored && languages[stored]) {
      return stored;
    }
    
    // Try to detect browser language
    const browserLang = navigator.language.split('-')[0];
    if (languages[browserLang]) {
      return browserLang;
    }
    
    return 'en'; // Default fallback
  },
  
  // Store language preference
  setStoredLanguage: (langId) => {
    localStorage.setItem('preferred-language', langId);
  },
  
  // Initialize language system
  initializeLanguage: () => {
    const storedLang = i18nUtils.getStoredLanguage();
    return storedLang;
  }
};

// Translation function factory
export function createTranslator(translations, currentLang = 'en') {
  return function t(key, params = {}) {
    // Get translation from current language or fallback to English
    const translation = translations[currentLang]?.[key] || translations.en?.[key] || key;
    
    // Replace parameters in translation
    return Object.entries(params).reduce((str, [param, value]) => {
      return str.replace(new RegExp(`{{${param}}}`, 'g'), value);
    }, translation);
  };
}

// Default export
export default languages; 